.. developer_web_api:

Overview
=====================

.. toctree::
   :hidden:
   
   GraphQL <web_api/graphql>
   Simple <web_api/simple>
   JSON <web_api/json>
   IIIF <web_api/IIIF>

CollectiveAccess offers three web-based APIs for data access and manipulation, two of which are legacy and should generally be avoided for new projects:

* :ref:`GraphQL API <developer_api_graphql>` The new GraphQL-based API offered in CollectiveAccess version 1.8. This API provides a full range of services for reading and writing both catalogue data and system configuration, and is under active development. 
* :ref:`"Simple" API (Legacy) <developer_api_simple>` A read-only API that provides configurable endpoints returning pre-formatted data in flat JSON-encoded key value responses. Endpoints can be generated for search result sets or individual records referenced by ID. This API is considered legacy but will continue to be supported.
* :ref:`Legacy JSON API (Legacy) <developer_api_json>` A REST-style API returning JSON-encoded payloads for read and write operations. This API is deprecated and will be removed in a future release.

For media access an :ref:`IIIF API service <developer_api_iiif>` is provided. 