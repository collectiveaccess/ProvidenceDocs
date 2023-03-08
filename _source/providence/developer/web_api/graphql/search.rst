.. _developer_api_graphql_search:

Searching (endpoint name ``Search``)
====================================

The search service provides both full-text and field-level search facilities using two queries. The ``search`` query accepts a :ref:`Lucene-format search expression <search_syntax>` and returns results for the specified table. The returned data will include data specified by the ``bundles`` parameter. You can list any number of bundles, and include bundles in related tables. You may also specify :ref:`display templates <display_templates>`.

.. tip::
	
	Display templates can be used to format arbitrarily complex data extracted from returned records, as well as directly and indirectly related records. They are evaluated relative to each returned record in the search result.

A typical ``search`` query might take the form:

.. code-block:: text

	query { 
		search(
			table: "ca_objects", 
			search: "Drop the Dips", 
			bundles: ["ca_objects.idno", "ca_objects.preferred_labels.name", "ca_objects.description", "<strong>[^ca_objects.type_id]</strong>: <unit relativeTo='ca_entities' delimiter='; '>^ca_entities.preferred_labels.surname, ^ca_entities.preferred_labels.forename</unit>"],
			start: 0,
			limit: 10
		) { 
			table, 
			search, 
			count, 
			result {
				id, 
				table, 
				idno, 
				bundles {
					name, 
					values { 
						value, 
						locale 
					}
				}
			}
		} 
	} 
	
Note that the last entry in the ``bundles`` list is a :ref:`display template <display_templates>`. This query would return a result in this form:
	
.. code-block:: text
	
	{
    "ok": true,
    "data": {
        "search": {
            "table": "ca_objects",
            "search": "Drop the Dips",
            "count": 1,
            "result": [
                {
                    "id": 10,
                    "table": "ca_objects",
                    "idno": "test.1",
                    "bundles": [
                        {
                            "name": "Object identifier",
                            "values": [
                                {
                                    "value": "test.1",
                                    "locale": null
                                }
                            ]
                        },
                        {
                            "name": "Name",
                            "values": [
                                {
                                    "value": "My first record",
                                    "locale": "en_US"
                                }
                            ]
                        },
                        {
                            "name": "Description",
                            "values": [
                                {
                                    "value": "Drop the Dips was a roller coaster in Coney Island, NY",
                                    "locale": "en_US"
                                }
                            ]
                        },
                        {
                            "name": "<strong>[^ca_objects.type_id]</strong>: <unit relativeTo='ca_entities' delimiter='; '>^ca_entities.preferred_labels.surname, ^ca_entities.preferred_labels.forename</unit>",
                            "values": [
                                {
                                    "value": "<strong>Postcard</strong>: Tilyou, George; Dundee, Elmer; Thompson, Fred",
                                    "locale": "en_US"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
}

You can cap the number of records returned in a response using the ``limit`` parameter. If omitted all records will be returned. The ``start`` parameter can be used to offset the point from which results are returned. Together ``start`` and ``limit`` can be used to implement paging of search results.

Returned results can be limited to specified record types setting the ``restrictToTypes`` option to a list of type codes. Eg.

.. code-block:: text

	query { 
		search(
			table: "ca_objects", 
			search: "Drop the Dips", 
			bundles: ["ca_objects.idno", "ca_objects.preferred_labels.name", "ca_objects.description"],
			start: 0,
			limit: 10,
			restrictToTypes: ["artifact", "artwork"]
		) { 
			table, 
			search, 
			count, 
			result {
				id, 
				table, 
				idno, 
				bundles {
					name, 
					values { 
						value, 
						locale 
					}
				}
			}
		} 
	} 

Field-level searches using the ``find`` query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``find`` query offers field-specific searching. While the ``search`` query operates on a full-text index built on top of the database, ``find`` queries the underlying data directly, with minimal modification and expansion of your query.

The ``find`` query takes most of the parameters used for ``search`` (``table``, ``start``, ``limit``, ``bundles`` and ``restrictToTypes``), but uses the ``criteria`` parameter to specify field level search criteria in place of the ``search`` parameter. It returns data in the same format as ``search``.

.. code-block:: text

	query { 
		find(
			limit: 10, 
			start: 0, 
			table: "ca_objects", 
			criteria: [
				{
					name: "ca_objects.preferred_labels.name", 
					operator: LIKE, 
					value: "Lego*"
				}
			], 
			bundles: ["ca_objects.idno", "ca_objects.preferred_labels.name", "ca_objects.description"]
		) { 
			table, 
			search, 
			count, 
			result {
				id, 
				table, 
				idno, 
				bundles {
					name, 
					values { 
						value, 
						locale 
					}
				}
			}
		}
	} 

The ``criteria`` parameter is a list of field-level search criteria. Each criterion includes a bundle ``name``, an operator and a value. Operators include ``LT`` (less than), ``LTE`` (less than or equal), ``GR`` (greater than), ``GTE`` (greater than or equal), ``EQ`` (equal), ``LIKE`` (matching with wildcards), ``BETWEEN`` (between two listed ``values``), ``IN`` (present in a list of ``values``) and ``NOT_IN`` (not present in a list of ``values``). A criterion using ``IN``:

.. code-block:: text

	{
		name: "ca_objects.idno", 
		operator: IN, 
		values: ["2020.22", "2020.55"]
	}
	
Multiple searches or finds in a single query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For applications needing to launch multiple simultaneous searches (to query across several different record types, for example) issuing a separate request for each search can significantly impact performance. The API provides a method to wrap any number of searches or finds in a single GraphQL query. To execute multiple searches set the ``searches`` option with a list of searches, in this form:

.. code-block:: text

	query {
	  search(
		searches:[{
			name:"entity_search",
			table: "ca_entities",
			search:"Berlin",
			bundles: ["ca_entitiy.preferred_labels.displayname", "ca_entities.idno"],
			restrictToTypes:["individual"],
			start: 0,
			limit: 5
		}, {
			name:"object_search",
			table: "ca_objects",
			search:"Berlin",
			bundles: ["ca_objects.preferred_labels", "ca_objects.idno"],
			start: 0,
			limit: 5
		}]
	  )
	  {
		results {
			name, count, result {
		  id,
		  table,
		  idno,
		  bundles {
			code,
			name,
			dataType,
			values {
			  value,
			  locale
			}}
		  }
		}
	  }
	}

This query will search for entities of type "individual" and objects of any type containing the word "Berlin". If will return up to five matching records for each. Note that each search may be named. These names are returned with results in the query response and may be used to pain results with queries. If the ``name`` option is not set it will default to the value of the ``table`` option. A typical response would resemble:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"search": {
				"results": [
					{
						"name": "entity_search",
						"count": 5,
						"result": [
							{
								"id": 4,
								"table": "ca_entities",
								"idno": "NAM0001",
								"bundles": [
									{
										"code": "ca_entities.preferred_labels.displayname",
										"name": "Display name",
										"dataType": "Text",
										"values": [
											{
												"value": "Abate, Niccolò dell', 1509/1512-1571",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_entities.idno",
										"name": "Name Authority identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "NAM0001",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 896,
								"table": "ca_entities",
								"idno": "NAM0980",
								"bundles": [
									{
										"code": "ca_entities.preferred_labels.displayname",
										"name": "Display name",
										"dataType": "Text",
										"values": [
											{
												"value": "Pseudo Jacopino di Francesco, c. 1325-1350",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_entities.idno",
										"name": "Name Authority identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "NAM0980",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 903,
								"table": "ca_entities",
								"idno": "NAM0987",
								"bundles": [
									{
										"code": "ca_entities.preferred_labels.displayname",
										"name": "Display name",
										"dataType": "Text",
										"values": [
											{
												"value": "Quercia, Priamo della, active 1438-after 1467",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_entities.idno",
										"name": "Name Authority identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "NAM0987",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 902,
								"table": "ca_entities",
								"idno": "NAM0986",
								"bundles": [
									{
										"code": "ca_entities.preferred_labels.displayname",
										"name": "Display name",
										"dataType": "Text",
										"values": [
											{
												"value": "Quercia, Jacopo della, 1371/1374-1438",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_entities.idno",
										"name": "Name Authority identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "NAM0986",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 901,
								"table": "ca_entities",
								"idno": "NAM0985",
								"bundles": [
									{
										"code": "ca_entities.preferred_labels.displayname",
										"name": "Display name",
										"dataType": "Text",
										"values": [
											{
												"value": "Pütt, Johann Philipp von der, c. 1560/1562-1619",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_entities.idno",
										"name": "Name Authority identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "NAM0985",
												"locale": null
											}
										]
									}
								]
							}
						]
					},
					{
						"name": "object_search",
						"count": 5,
						"result": [
							{
								"id": 3227,
								"table": "ca_objects",
								"idno": "1330",
								"bundles": [
									{
										"code": "ca_objects.preferred_labels",
										"name": "Art object titles",
										"dataType": "Container",
										"values": [
											{
												"value": "Madonna and Child",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_objects.idno",
										"name": "Object identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "1330",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 3379,
								"table": "ca_objects",
								"idno": "1872",
								"bundles": [
									{
										"code": "ca_objects.preferred_labels",
										"name": "Art object titles",
										"dataType": "Container",
										"values": [
											{
												"value": "Saint Margaret",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_objects.idno",
										"name": "Object identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "1872",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 3179,
								"table": "ca_objects",
								"idno": "1798",
								"bundles": [
									{
										"code": "ca_objects.preferred_labels",
										"name": "Art object titles",
										"dataType": "Container",
										"values": [
											{
												"value": "Saint Apollonia",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_objects.idno",
										"name": "Object identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "1798",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 485,
								"table": "ca_objects",
								"idno": "2087",
								"bundles": [
									{
										"code": "ca_objects.preferred_labels",
										"name": "Art object titles",
										"dataType": "Container",
										"values": [
											{
												"value": "The Baptism of Christ",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_objects.idno",
										"name": "Object identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "2087",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 1578,
								"table": "ca_objects",
								"idno": "1223",
								"bundles": [
									{
										"code": "ca_objects.preferred_labels",
										"name": "Art object titles",
										"dataType": "Container",
										"values": [
											{
												"value": "Laocoön",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_objects.idno",
										"name": "Object identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "1223",
												"locale": null
											}
										]
									}
								]
							}
						]
					}
				]
			}
		}
	}
	
A similar construction may be used to execute several ``find`` operations in a single GraphQL query. Multiple find operations are defined in the ``finds`` option. For example to simultaneous find entity and object records: 

.. code-block:: text

	query {
	  find(
		finds:[{
			name:"entity_find",
			table: "ca_entities",
			criteria:[{name:"ca_entities.preferred_labels.displayname", operator:LIKE, value:"%berlin%"}],
			bundles: ["ca_entities.preferred_labels.displayname",
			"ca_entities.idno"],
			start: 0,
			limit: 5
		}, {
			name:"object_find",
			table: "ca_objects",
			criteria:[{name:"ca_objects.preferred_labels.name", operator:LIKE, value:"%adoration%"}],
			bundles: ["ca_objects.preferred_labels",
			"ca_objects.idno"],
			start: 0,
			limit: 5
		}]
	  )
	  {
		results {
			name, count, result {
		  id,
		  table,
		  idno,
		  bundles {
			code,
			name,
			dataType,
			values {
			  value,
			  locale
			}}
		  }
		}
	  }
	}
	
A typical response would look like:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"find": {
				"table": "ca_entities",
				"count": 2,
				"results": [
					{
						"result": [
							{
								"id": 20,
								"table": "ca_entities",
								"idno": "NAM0017",
								"bundles": [
									{
										"code": "ca_entities.preferred_labels.displayname",
										"name": "Display name",
										"dataType": "Text",
										"values": [
											{
												"value": "Allen Memorial Art Museum, Oberlin College, Oberlin, Ohio",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_entities.idno",
										"name": "Name Authority identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "NAM0017",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 1187,
								"table": "ca_entities",
								"idno": "NAM1293",
								"bundles": [
									{
										"code": "ca_entities.preferred_labels.displayname",
										"name": "Display name",
										"dataType": "Text",
										"values": [
											{
												"value": "Berlinghieri, Bonaventura, active 13th century",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_entities.idno",
										"name": "Name Authority identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "NAM1293",
												"locale": null
											}
										]
									}
								]
							}
						]
					},
					{
						"result": [
							{
								"id": 1664,
								"table": "ca_objects",
								"idno": "44",
								"bundles": [
									{
										"code": "ca_objects.preferred_labels",
										"name": "Art object titles",
										"dataType": "Container",
										"values": [
											{
												"value": "A Gentleman in Adoration before the Madonna",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_objects.idno",
										"name": "Object identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "44",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 817,
								"table": "ca_objects",
								"idno": "578",
								"bundles": [
									{
										"code": "ca_objects.preferred_labels",
										"name": "Art object titles",
										"dataType": "Container",
										"values": [
											{
												"value": "Coronation of the Virgin; Adoration of the Magi",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_objects.idno",
										"name": "Object identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "578",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 1401,
								"table": "ca_objects",
								"idno": "2038",
								"bundles": [
									{
										"code": "ca_objects.preferred_labels",
										"name": "Art object titles",
										"dataType": "Container",
										"values": [
											{
												"value": "The Adoration of the Child",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_objects.idno",
										"name": "Object identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "2038",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 1188,
								"table": "ca_objects",
								"idno": "2039",
								"bundles": [
									{
										"code": "ca_objects.preferred_labels",
										"name": "Art object titles",
										"dataType": "Container",
										"values": [
											{
												"value": "The Adoration of the Magi",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_objects.idno",
										"name": "Object identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "2039",
												"locale": null
											}
										]
									}
								]
							},
							{
								"id": 476,
								"table": "ca_objects",
								"idno": "2040",
								"bundles": [
									{
										"code": "ca_objects.preferred_labels",
										"name": "Art object titles",
										"dataType": "Container",
										"values": [
											{
												"value": "The Adoration of the Magi",
												"locale": "en_US"
											}
										]
									},
									{
										"code": "ca_objects.idno",
										"name": "Object identifier",
										"dataType": "Text",
										"values": [
											{
												"value": "2040",
												"locale": null
											}
										]
									}
								]
							}
						]
					}
				]
			}
		}
	}
	
There is no restriction on the number of operations that may be executed, and multiple operations may be executed on the same table, each individually restricted and/or limited.

	
Record lookup by value using the ``exists`` query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When importing data using the API, it is often useful to perform bulk lookups on identifiers, labels and other values. The ``exists`` query provides a simple, performant method to test for existence of records having one more values in a specific location. Three parameters are required: the ``table`` and ``bundle`` to search on, and a list of ``values``. 


.. IMPORTANT::
	Use of this GraphQL service requires authentication with an account having the ``can_access_graphql_exists_search_service`` action privilege. For performance reasons the ``exists`` query bypasses type- and item-level access control, and may return data to which the authenticated service user would not normally have access. The ``can_access_graphql_exists_search_service`` privilege provides a means to restrict access to this service to only those accounts that absolutely require it.

For example:

.. code-block:: text

	query {
		exists(
			table: "ca_objects",
			restrictToTypes: ["artifact"],
			bundle: "ca_objects.materials",
			values: ["quartz"]
		)
		{
			table,
			bundle,
			map,
			values { id, ids, idno, idnos, value }
		}
	}

returns:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"exists": {
				"table": "ca_objects",
				"bundle": "ca_objects.materials",
				"map": "{\"quartz\":[{\"idno\":\"75.1.272\",\"id\":\"15793\"},{\"idno\":\"75.47.13\",\"id\":\"16044\"},{\"idno\":\"75.47.20\",\"id\":\"16049\"}]}",
				"values": [
					{
						"id": 15793,
						"ids": [
							15793,
							16044,
							16049
						],
						"idno": "75.1.272",
						"idnos": [
							"75.1.272",
							"75.47.13",
							"75.47.20"
						],
						"value": "quartz"
					}
				]
			}
		}
	}
	
The ``bundle`` parameter must be a bundle on the queried table and can be specified in <table>.<bundle code> format or simply as a bundle code. In the example above, ``ca_objects.idno`` and ``idno`` are equivalent. The bundle can refer to any intrinsic, label (preferred or non-preferred) or metadata element defined for the table. For preferred labels, specify the bundle as ``<table>.preferred_labels`` (or simply ``preferred_labels``) for the label display value, or ``<table>.preferred_labels.<sub field>`` to query a specific field. For example, for entities setting ``bundle`` to ``ca_entities.preferred_labels`` (or ``ca_entities.preferred_labels.displayname``) will perform matching on the ``displayname`` field. Using  ``ca_entities.preferred_labels.surname`` will operate on the ``surname`` field in the table. Queries on non-preferred labels are specified similarly, using the ``nonpreferred_labels`` bundle name.

The set of records checked by an ``exists`` query can be restricted to one or more types by setting the optional ``restrictToTypes`` parameter to a list of types fot the specified ``table``. If omitted, all types will be included.

The ``values`` return value contains a list of query values and the ids and idnos (identifiers) of records containing those values. Within each ``values`` list item the ``id`` value contains the database id value for the first matched record. The ``ids`` return value contains a list of all matches. Similarly, for identifiers ``idno`` contains the identifer for the first matched record while ``idnos`` contains the complete list of matching identifiers.

The ``exists`` query will return `all` values, whether they exist in the database or not. Values without matches will return ``id`` and ``ids`` as null.

The ``map`` return value is an alternative rendering of the ``values`` list as a JSON-encoded lookup table of values and matching identifiers. Each key in the lookup tables resolves to a list of matching record ids, or null if the key value doesn't exist in the database. This table can be used by calling applications to quickly determine by values which values are in use, and which records they resolve to.

Limiting results using access values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All primary records in CollectiveAccess include an ``access`` field to control visibility in public-facing contexts such as web sites and data feeds. Data in ``search`` and ``find`` queries can be limited by one or more access values using the ``checkAccess`` parameter, set to a list of integer access codes, as defined in the ``access_statuses`` list for the CollectiveAccess installation. By convention 0 indicates a private record, 1 a public record and 2 a record available in public interfaces to users with elevated privileges. However, these values may be vary across installations and should be verified before use. 
