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
			results {
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
	
Note that the last entry in the ``bundles`` list is a :ref:`display templates <display_templates>`. This query would return a result in this form:
	
.. code-block:: text
	
	{
    "ok": true,
    "data": {
        "search": {
            "table": "ca_objects",
            "search": "Drop the Dips",
            "count": 1,
            "results": [
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
			results {
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
			results {
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
			bundle: "ca_objects.idno",
			values: ["513En", "514En", "515En"]
		) {
			table,
			bundle,
			map,
			values { id, ids, value }
		}
	}

returns:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"exists": {
				"table": "ca_objects",
				"bundle": "ca_objects.idno",
				"map": "{\"513En\":\"39584\",\"514En\":\"39585\",\"515En\":\"39586\"}",
				"values": [
					{
						"value": "513En",
						"id": 39584,
						"ids": [
							39584
						]
					},
					{
						"value": "514En",
						"id": 39585,
						"ids": [
							39585
						]
					},
					{
						"value": "515En",
						"id": 39586,
						"ids": [
							39586
						]
					}
				]
			}
		}
	}
	
The ``bundle`` parameter must be a bundle on the queried table and can be specified in <table>.<bundle code> format or simply as a bundle code. In the example above, ``ca_objects.idno`` and ``idno`` are equivalent. The bundle can refer to any intrinsic, label or metadata element defined for the table. For labels, specify the bundle as ``<table>.preferred_labels`` (or simplly ``preferred_labels``) for the label display value, or ``<table>.preferred_labels.<sub field>`` to query a specific field. For example, for entities setting ``bundle`` to ``ca_entities.preferred_labels`` (or ``ca_entities.preferred_labels.displayname``) will perform matching on the ``displayname`` field. Using  ``ca_entities.preferred_labels.surname`` will operate on the ``surname`` field in the table.

The ``values`` return value contains a list of query values and the ids of records containing those values. Within each ``values`` list item the ``id`` value contains the database id value for the first matched record. The ``ids`` return value contains a list of all matches. 

The ``exists`` query will return `all` values, whether they exist in the database or not. Values without matches will return ``id`` and ``ids`` as null.

The ``map`` return value is an alternative rendering of the ``values`` list as a JSON-encoded lookup table of values and matching identifiers. Each key in the lookup tables resolves to a list of matching record ids, or null if the key value doesn't exist in the database. This table can be used by calling applications to quickly determine by values which values are in use, and which records they resolve to.


