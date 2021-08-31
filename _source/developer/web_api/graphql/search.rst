.. _developer_api_graphql_search:

Searching (endpoint name ``Search``)
====================================

The search service provides both full-text and field-level search facilities using two queries. The ``search`` query accepts a :ref:`Lucene-format search expression <search_syntax>` and returns results for the specified table. The returned data will include data specified by the ``bundles`` parameter. You can list any number of bundles, and include bundles in related tables. 

A typical ``search`` query might take the form:

.. code-block:: text

	query { 
		search(
			table: "ca_objects", 
			search: "Drop the Dips", 
			bundles: ["ca_objects.idno", "ca_objects.preferred_labels.name", "ca_objects.description"],
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
	
This query would return a result in this form:
	
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
	
When importing data using the API, it is often useful to perform bulk lookups on idno values, label values, or both. The ``exists`` query provides a simple, performant method to test for existence of records by idnos and labels. Three parameters are required: the ``table`` to search on, a list of ``idnos`` to search for and/or a list of ``labels`` to search on. Both ``idnos`` and ``labels`` maybe present in a single query. At a minimum, one must be present. For example:

.. code-block:: text

	query {
        exists(
                table: "ca_objects",
                idnos: ["2011.10.01", "V2021.42.1"],
                labels: ["Frame, Picture"]
        ) {
                table,
                idnos { id, ids, value },
                labels { id, ids, value }
        }
	}

returns:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"exists": {
				"table": "ca_objects",
				"idnos": [
					{
						"id": 26246,
						"ids": [
							26246,
							26247,
							26248
						],
						"value": "2011.10.01"
					},
					{
						"id": null,
						"ids": null,
						"value": "V2021.42.1"
					}
				],
				"labels": [
					{
						"id": 22936,
						"ids": [
							22936,
							22958,
							22967,
							22972,
							23007,
							23025
						],
						"value": "Frame, Picture"
					}
				]
			}
		}
	}
	
The ``id`` return value contains the database id value for the first matched record. If a list of all matches is required, use the ``ids`` return value. The ``exists`` query will return `all` idno and label values, whether they exist in the database or not. Values without matches will return ``id`` and ``ids`` as null.
