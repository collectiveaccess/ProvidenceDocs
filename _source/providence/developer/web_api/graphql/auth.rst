.. _developer_api_graphql_auth:

Authentication (endpoint name ``Auth``)
=======================================

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