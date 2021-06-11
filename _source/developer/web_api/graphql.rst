.. _developer_api_graphql:

GraphQL API
=====================

Intro here...


URLs
----

API access in provided through several endpoints, each implementing a category of functionality. The format for GraphQL service URLs is: ``<base-url>``/service/``<endpoint-name>``, where the base URL is the root URL for your CollectiveAccess install and endpoint is name of a service described below. If your CollectiveAccess system is at https://www.mysite.com, the URL for the authentication endpoint would be ``https://www.mysite.com/service/Auth``. 


Authentication (endpoint name ``Auth``)
---------------------------------------

`JSON Web Tokens <https://jwt.io>`_ (JWT) are used to maintain API sessions. All API actions require a valid JWT. For initial authentication send the ``login`` query to ``<baseurl>/service/Auth``:

.. code-block:: text

	query { 
		login(username:"my_api_login_name", password: "my_api_password") 
		{ 
			jwt, 
			refresh, 
			user { 
				id, 
				fname, 
				lname, 
				email 
			} 
		} 
	}

The response will be in the form:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"login": {
				"jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJtYXh3ZWxsLndoaXJsLWktZ2lnLmNvbSIsImF1ZCI6Im1heHdlbGwud2hpcmwtaS1naWcuY29tIiwiaWF0IjoxNjIxODkxNjI5LCJuYmYiOjE2MjE4OTE2MjksImV4cCI6MTYyMjc1NTYyOSwiaWQiOiIyIn0.Hlj1n_62Oq_xSDev6FkW8tzaU-oHKipMD2pzSHCM0gk",
				"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJtYXh3ZWxsLndoaXJsLWktZ2lnLmNvbSIsImF1ZCI6Im1heHdlbGwud2hpcmwtaS1naWcuY29tIiwiaWF0IjoxNjIxODkxNjI5LCJuYmYiOjE2MjE4OTE2MjksImV4cCI6MTYyMTk3ODAyOSwiaWQiOiIyIn0.bYuqFbfkG9gCgl5UOQ0KVEptefPQ0yUEKnwV9sa3WJA",
				"user": {
					"id": 2,
					"fname": "Api",
					"lname": "User",
					"email": "api@test.com"
				}
			}
		}
	}
	
where the ``jwt`` value is the newly created access token and ``refresh`` is a refresh token you can use to generate replacement tokens for expired JWTs. Data about the login used, including internal CollectiveAccess user_id, display name and contact email for the account can be returned in the ``user`` block.

To refresh an expired JWT access token send the ``refresh`` query to ``<baseurl>/service/Auth``:

.. code-block:: text

	query { 
		refresh(token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJtYXh3ZWxsLndoaXJsLWktZ2lnLmNvbSIsImF1ZCI6Im1heHdlbGwud2hpcmwtaS1naWcuY29tIiwiaWF0IjoxNjIxODkxNjI5LCJuYmYiOjE2MjE4OTE2MjksImV4cCI6MTYyMTk3ODAyOSwiaWQiOiIyIn0.bYuqFbfkG9gCgl5UOQ0KVEptefPQ0yUEKnwV9sa3WJA") 
		{ 
			jwt
		} 
	}
	
The response will be in the form:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"refresh": {
				"jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJtYXh3ZWxsLndoaXJsLWktZ2lnLmNvbSIsImF1ZCI6Im1heHdlbGwud2hpcmwtaS1naWcuY29tIiwiaWF0IjoxNjIxOTUwMTEzLCJuYmYiOjE2MjE5NTAxMTMsImV4cCI6MTYyMjgxNDExMywiaWQiOiIyIn0.p9aYMiu0CktcGAmYBT76wP5tLLQRdh1qSh6JTm_2RbU"
			}
		}
	}
	
where ``jwt`` is the replacement JWT access token to be used for subsequent API access.

Once a JWT is obtained it must be included in each API request, either as a `bearer token <https://en.wikipedia.org/wiki/JSON_Web_Token#Use>`_ or as a query parameter named ``jwt``.

JWT configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~

JWTs are created using a token key. It is extremely important to set this value to a random, impossible to guess string of letters and numbers. Do not leave this value as the default value set in the ``GRAPHQL_SERVICES_JWT_TOKEN_KEY`` setting in  ``setup.php`` or ``graphql_services_jwt_token_key`` in the :ref:`app.conf <app_conf>` configuration file.

The interval for which a JWT access token is valid can be controlled using the `graphql_services_jwt_access_token_lifetime` setting in the :ref:`app.conf <app_conf>` configuration file. The interval is specified in seconds. Common practice is to expire JWT access tokens every 15 minutes (900 seconds).

The interval for which a JWT refresh token is valid can be controlled using the `graphql_services_jwt_refresh_token_lifetime` setting in the :ref:`app.conf <app_conf>` configuration file. The interval is specified in seconds. Common practice is to expire JWT refresh tokens every 1 - 7 days (86400 - 604,800 seconds).

Searching (endpoint name ``Search``)
------------------------------------

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

Item-level data access (endpoint name ``Item``)
-----------------------------------------------

The Item service returns detailed data for a single record retrieved using either an internal CollectiveAccess ID value or the ``idno`` value of the record.

To fetch a record pass the table, identifier and list of bundles to return in a ``get`` query:

.. code-block:: text

	query { 
		get(
			table: "ca_objects", 
			identifier: "test.1", 
			bundles: ["ca_objects.idno", "ca_objects.type_id", "ca_objects.preferred_labels.name", "ca_objects.nonpreferred_labels", "ca_objects.description"]
    	) { 
    		id, 
    		table, 
    		idno, 
    		bundles { 
    			name, 
    			code, 
    			dataType, 
    			values { 
    				locale, 
    				value, 
    				subvalues { 
    					code, 
    					value, 
    					dataType
    				} 
    			}
    		}
    	}
    }

The query will return:

.. code-block:: text
	
	{
		"ok": true,
		"data": {
			"get": {
				"id": 10,
				"table": "ca_objects",
				"idno": null,
				"bundles": [
					{
						"name": "Object identifier",
						"code": "ca_objects.idno",
						"dataType": "Text",
						"values": [
							{
								"locale": null,
								"value": "test.1",
								"subvalues": null
							}
						]
					},
					{
						"name": "Type",
						"code": "ca_objects.type_id",
						"dataType": "Text",
						"values": [
							{
								"locale": null,
								"value": "artifact_item",
								"subvalues": null
							}
						]
					},
					{
						"name": "Name",
						"code": "ca_objects.preferred_labels.name",
						"dataType": null,
						"values": [
							{
								"locale": "en_US",
								"value": "My first record",
								"subvalues": [
									{
										"code": "name",
										"value": "My first record",
										"dataType": "Text"
									}
								]
							}
						]
					},
					{
						"name": "Description",
						"code": "ca_objects.description",
						"dataType": "Text",
						"values": [
							{
								"locale": "en_US",
								"value": "Drop the Dips was a roller coaster in Coney Island, NY",
								"subvalues": [
									{
										"code": "description",
										"value": "Drop the Dips was a roller coaster in Coney Island, NY",
										"dataType": "Text"
									}
								]
							}
						]
					}
				]
			}
		}
	}
	
Including bundles referring to related tables will include relationship data in the item response. For example, adding `ca_entities` to the query would return:

TODO: add note about ids


Fetching relationships for an item
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``getRelationships`` query to fetch a list of relationships between an item and items in another table. You can filter the returned list to only include related items or relationships with specific types via the ``restrictToTypes`` and ``restrictToRelationshipTypes`` parameters.

.. code-block:: text

	query { 
		getRelationships(
			table: "ca_objects", 
			identifier: "test.1", 
			target:"ca_entities", 
			bundles: [
				"ca_entities.preferred_labels.displayname", "ca_entities.txt_biography"], restrictToRelationshipTypes: ["donor"]
		) { 
			id, 
			table, 
			idno, 
			relationships { 
				id, 
				table, 
				bundles { 
					name, 
					code, 
					dataType, 
					values { 
						id, 
						value_id, 
						locale, 
						value, 
						subvalues { 
							id, 
							code, 
							value, 
							dataType
						}
					}
				} 
			} 
		}
	}

returns:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"getRelationships": {
				"id": 10,
				"table": "ca_objects",
				"idno": "test.1",
				"relationships": [
					{
						"id": 11,
						"table": "ca_objects_x_entities",
						"bundles": [
							{
								"name": "Display name (from entities)",
								"code": "ca_entities.preferred_labels.displayname",
								"dataType": "Container",
								"values": [
									{
										"id": 52,
										"value_id": null,
										"locale": "en_US",
										"value": "Fay Abrams",
										"subvalues": [
											{
												"id": null,
												"code": "displayname",
												"value": "Fay Abrams",
												"dataType": "Container"
											}
										]
									}
								]
							},
							{
								"name": "Biography (from entities)",
								"code": "ca_entities.txt_biography",
								"dataType": "Text",
								"values": [
									{
										"id": 472,
										"value_id": 856,
										"locale": "en_US",
										"value": "Hello there!",
										"subvalues": [
											{
												"id": 856,
												"code": "txt_biography",
												"value": "Hello there!",
												"dataType": "Text"
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



Editing (endpoint name ``Edit``)
--------------------------------

The Edit service provides mutations to create new records, and modify or delete existing records.

Creating new records
~~~~~~~~~~~~~~~~~~~~

The ``add`` mutation is used to create new records. To create a record three bits of information are needed: the :ref:`table <primary_tables>` the record will reside in, the ``type`` for the new record, and an ``idno`` (a unique user-provided identifier) value. Other data elements (or "bundles") can be set by listing them in the ``bundles`` parameter of the query. For example:

.. code-block:: text

	mutation { 
		add(
			table: "ca_objects", 
			idno: "test.101", 
			type: "artifact",
			bundles: [
				{ name: "preferred_labels", value: "My first record"},
				{ name: "description", value: "This is a new record!"},
				{ name: "date", value: "April 3 1984"}
			]
		) { 
			id, 
			table, 
			identifier, 
			errors {code, message, bundle}, 
			warnings { message, bundle}
		} 
	} 
 
This mutation will create a new artifact object record with the provided values for idno, title (aka. preferred label), description and date. Note that that format for the ``idno`` value, valid values for ``type`` and available bundles are system-specific. The values used here are examples. 

The ``bundles`` parameter takes a list of bundle value specifications. Each specification requires, at a minimum, a bundle ``name`` and ``value`` to set. For bundles that repeat, specifications with the same bundle name may be set. For example, to set multiple dates on an object (assuming the schema is configured to allow repeating dates):

.. code-block:: text

	mutation { 
		add(
			table: "ca_objects", 
			idno: "test.101", 
			type: "artifact",
			bundles: [
				{ name: "preferred_labels", value: "My first record"},
				{ name: "description", value: "This is a new record!"},
				{ name: "date", value: "April 3 1984"},
				{ name: "date", value: "June 8 1984"},
				{ name: "date", value: "July 26 1984"}
			]
		) { 
			id, 
			table, 
			identifier, 
			errors {code, message, bundle}, 
			warnings { message, bundle}
		} 
	} 

If your system supports multiple cataloguing locales, the locale for each bundle value may be specified using ``locale`` and an ISO code:

.. code-block:: text

	{ name: "description", value: "Hier ist ein neuer Rekord", locale: "de_DE" },
	
If you omit the locale value for a bundle, the system default locale is used.

For container bundles – fields that contain sub-fields, set ``values`` for the bundle specifier with a list of sub-field specifiers. For example:

.. code-block:: text

	mutation { 
		add(
			table: "ca_objects", 
			idno: "test.101", 
			type: "artifact",
			bundles: [
				{ name: "preferred_labels", value: "My first record"},
				{ name: "description", value: "This is a new record!"},
				{ name: "address", values: [
					{ name: "address1", value: "1000 Surf Avenue" },
					{ name: "city", value: "Brooklyn" },
					{ name: "state", value: "NY" },
					{ name: "postal_code", value: "11224" },
					{ name: "country", value: "USA" }
				]}
			]
		) { 
			id, 
			table, 
			identifier, 
			errors {code, message, bundle}, 
			warnings { message, bundle}
		} 
	} 

Similarly, for preferred and non-preferred labels that take multiple sub-values, such as entities, ``values`` may be set on the bundle to specific sub-field values:

.. code-block:: text

	mutation { 
		add(
			table: "ca_entities", 
			idno: "E.1", 
			type: "individual",
			bundles: [
				{ name: "preferred_labels", values: [
					{ name: "forename", value: "David" },
					{ name: "surname", value: "Lowery" },
					{ name: "middlename", "Alan" },
					{ name: "prefix", value: "Mr" }
				]},
				{ name: "biography", value: "He was born in Brooklyn in 1914... etc etc"},
				{ name: "lifedates", value: "February 13, 1914 - March 6, 1981"}
			]
		) { 
			id, 
			table, 
			idno, 
			errors {code, message, bundle}, 
			warnings { message, bundle}
		} 
	} 

For non-preferred labels, which take an option label ``type`` value, you may also pass ``type`` in the bundle specification. If it is omitted the default type will be used.

Note that all bundles are assumed to be part of the table into which you are adding the record. A separate ``relationship`` mutation (not implemented yet) is used to manage relationships between records.

The ``add`` mutation can return the internal CollectiveAccess ``id`` value for the newly created record, the ``table`` of the record (always the same as the table parameter passed in the mutation), the idno value (which may be calculated using a server-side policy and differ from the passed value) and a list of errors and warnings that may have occurred during the add operation. Errors indicate failures and include a numeric error code, a descriptive message and the name of the bundle the error affects. Non-bundle-specific errors will have a bundle code of ``GENERAL``. Warnings are purely advisory and include a message and related bundle name.

Editing records
~~~~~~~~~~~~~~~~~~~~

To edit an existing record, the ``edit`` mutation is used with the target record specified by ``table`` and ``identifier`` parameters. The ``identifier`` parameter may be either an internal CollectiveAccess ID value or the ``idno`` value of a record. Note that ``idno`` values are not guaranteed to be unique (although they typically are). If more than one record matches the identifier, the first match will be edited and additional matches ignored.

Edited values are specified in the ``bundles`` parameter, similar to the format used for adding with a few additions. By default each listed bundle will be appended to the record. For bundles supporting repeating values, this means the addition of values. For fields that limited or not repeatability, edits will fail once the limit is reached. To replace a value rather than append to it, a ``replace`` value set to ``true`` may be set in the bundle specification. If a value exists it will be replaced by the new value; if no value exists yet, the new value will be added. 

To target a specific value in a bundle with multiple repeating values a value ``id`` may be set in the bundle specifier. These ``id`` values can be returned alongside their values in ``Item`` service endpoint responses (described above)

To delete a value from a record set a ``delete`` value to ``true`` in the bundle specifier. If ``id`` is also specified the specific value will be removed. If ``id`` is omitted all values will be removed.

An ``edit`` mutation that changes the ``idno``, replaces the description and removes all non-preferred labels:

.. code-block:: text

	mutation { 
		edit(
			table: "ca_objects", 
			identifier: "TEST.1", 
			bundles: [
				{name:"idno", value: "test.101"},
				{ name:"nonpreferred_labels", delete: true },
				{ name: "description", value: "This is a new description", replace: true }
			]
		) { 
			id, 
			table, 
			idno, 
			errors {code, message, bundle}, 
			warnings { message, bundle}
		} 
	} 

Note that the response format is identical to that used for ``add``.

Deleting records
~~~~~~~~~~~~~~~~~~~~

To delete a record, pass the table and an identifier (CollectiveAccess ID value or ``idno`` value):

.. code-block:: text

	mutation { 
		delete(
			table: "ca_objects", 
			identifier: "test.101"
		) { 
			id, 
			table, 
			identifier, 
			errors {code, message, bundle}, 
			warnings { message, bundle}
		}
	} 
	
The response will be in the same format as that used for ``add`` and ``edit`` mutations, but ``id`` and ``identifier`` will always be set to null.

Creating relationships
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

	mutation { 
		addRelationship(
			subject: "ca_objects", 
			target: "ca_entities", 
			subjectIdentifier: "test.1", 
			targetIdentifier:"51", 
			relationshipType: "creator"
		) { 
			id, 
			idno, 
			table, 
			errors {
				code, 
				message, 
				bundle
			}, 
			warnings { 
				message, 
				bundle
			}
		} 
	} 
	
Returns:

.. code-block:: Text

	{
		"ok": true,
		"data": {
			"addRelationship": {
				"id": 1,
				"idno": null,
				"table": "ca_objects_x_entities",
				"errors": [],
				"warnings": []
			}
		}
	}
	
Editing relationships
~~~~~~~~~~~~~~~~~~~~~~	

.. code-block:: text
	
	mutation { 
		editRelationship(
			subject: "ca_objects", 
			subjectIdentifier: "test.1", 
			target:"ca_entities",
			targetIdentifier: "55", 
			relationshipType: "creator", 
			bundles: [
				{name: "effective_date", value: "1960"}, 
				{name: "relationship_type", value: "creator"}, 
				{name: "description", value: "hello world???", replace: true}
			]) { 
				id, 
				table, 
				idno, 
				errors {
					code, 
					message, 
					bundle
				}, 
				warnings { 
					message, 
					bundle
				}
			}
		} 

Deleting relationships
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
	
	mutation { 
		deleteRelationship(
			subject: "ca_objects", 
			id: 1, 
			target:"ca_entities"
		) { 
			id, 
			table, 
			idno, 
			errors {
				code, 
				message, 
				bundle
			}, 
			warnings { 
				message, 
				bundle
			}
		}
	} 

Deleting all relationships:
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

	mutation { 
		deleteAllRelationships(
			subject: "ca_objects", 
			subjectIdentifier: "test.1", 
			target:"ca_entities", 
			relationshipType: "related"
		) { 
			id, 
			table, 
			idno, 
			errors {
				code, 
				message, 
				bundle
			}, 
			warnings { 
				message, 
				bundle
			}
		} 
	} 
	
	
Browsing (endpoint name ``Browse``)
-----------------------------------

To come

Schema information (endpoint name ``Schema``)
-------------------------------------------

To come


Configuration (endpoint name ``Config``)
----------------------------------------

To come

Utility (endpoint name ``Utility``)
----------------------------------------

The utility service offers miscellaneous queries for parsing and validating data. 

The ``splitEntityName`` service exposes CollectiveAccess' internal entity name processing system, providing conversion of text names into field-level components compatible with CA's entity record label format.

This query takes a text name and splits it into prefix, surname and forename. The ``displaynameFormat`` controls how the display text version is formatted. By default display text is the same as the input text, but can be normalized with to ``surnameCommaForename``, ``forenameCommaSurname``, ``forenameSurname``, ``forenamemiddlenamesurname``, or a :ref:`display template <display_templates>`.

.. code-block:: Text
	
	query { 
		splitEntityName(
			name: "Mr. Seth Kaufman", 
			displaynameFormat: "surnamecommaforename"
		) { 
				surname, 
				forename, 
				middlename, 
				displayname, 
				suffix, 
				prefix  
			}
		} 
	}

The ``parseDate`` query parse text dates into a numeric interval and a normalized text representation. The interval can be returned in CA's internal "historic" floating point format, or as Unix timestamps. Note that Unix timestamps can only be created for dates on or after January 1, 1970. Historic values are used by default. Set the ``format`` parameter to "unix" to return Unix timestamps. The format of the normalized text date can be controlled using the ``displayFormat`` parameter. Possible values are ``text`` (localized text), ``delimited`` (a date in the format 1/1/2020), ``iso8601``, ``yearOnly`` (only the year no matter how specific the input date is) and ymd (a date in the form 20200101). By default ``text`` is used. To set language of text sets pass the ``locale`` parameter, as in this query:
	
.. code-block:: text
	
	query { 
		parseDate(
			date: "january 1950", 
			locale: "de_DE"
		) { 
			start, 
			end, 
			text  
		} 
	} 
	
which returns 

.. code-block:: text

	{
    "ok": true,
    "data": {
        "parseDate": {
            "start": 1950.0101,
            "end": 1950.0131235959,
            "text": "Januar 1950"
        }
    }
}