.. _developer_api_graphql:

GraphQL API
=====================

Intro here...


URLs
----

API access in provided through several endpoints, each implementing a category of functionality. The format for GraphQL service URLs is: ``<base-url>``/service/``<endpoint-name>``, where the base URL is the root URL for your CollectiveAccess install and endpoint is name of a service described below. If your CollectiveAccess system is at https://www.mysite.com, the URL for the authentication endpoint would be ``https://www.mysite.com/service/Auth``. 

Endpoints
--------

.. toctree::
   :maxdepth: 2
   
   graphql/auth
   graphql/search
   graphql/item
   graphql/edit
   graphql/browse
   graphql/schema
   graphql/configuration
   graphql/utility