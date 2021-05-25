.. _developer_api_graphql:

GraphQL API
=====================

Intro here...


URLs
----

API access in provided through several endpoints, each implementing a category of functionality. The format for GraphQL service URLs is: ``<base-url>``/service/``<endpoint-name>``, where the base URL is the root URL for your CollectiveAccess install and endpoint is name of a service described below. If your CollectiveAccess system is at https://www.mysite.com, the URL for the authentication endpoint would be ``http://www.mysite.com/service/Auth``. 


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

JWT configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~

JWTs are created using a token key. It is extremely important to set this value to a random, impossible to guess string of letters and numbers. Do not leave this value as the default value set in the ``GRAPHQL_SERVICES_JWT_TOKEN_KEY`` setting in  ``setup.php`` or ``graphql_services_jwt_token_key`` in the :ref:`app.conf <app_conf>` configuration file.

The interval for which a JWT access token is valid can be controlled using the `graphql_services_jwt_access_token_lifetime` setting in the :ref:`app.conf <app_conf>` configuration file. The interval is specified in seconds. Common practice is to expire JWT access tokens every 15 minutes (900 seconds).

The interval for which a JWT refresh token is valid can be controlled using the `graphql_services_jwt_refresh_token_lifetime` setting in the :ref:`app.conf <app_conf>` configuration file. The interval is specified in seconds. Common practice is to expire JWT refresh tokens every 1 - 7 days (86400 - 604,800 seconds).

Searching (endpoint name ``Search``)
------------------------------------

To come

Item-level data access (endpoint name ``Item``)
-----------------------------------------------

To come

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
	
Browsing (endpoint name ``Browse``)
-----------------------------------

To come

Schema information (endpoint name ``Schema``)
-------------------------------------------

To come


Configuration (endpoint name ``Config``)
----------------------------------------

To come
