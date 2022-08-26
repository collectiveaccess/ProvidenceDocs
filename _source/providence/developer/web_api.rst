.. developer_web_api:

Overview
========

CollectiveAccess offers several web-based APIs for data access and manipulation. Two are general-use APIs, providing access to much of CollectiveAccess' functionality including data access and editing, search and configuration. 

General-Use APIs
----------------

* :ref:`GraphQL API <developer_api_graphql>`: A `GraphQL <https://graphql.org>`_-based API first offered in CollectiveAccess version 1.8. This API provides a full range of services for reading and writing both catalogue data and system configuration, and is under active development. 

* :ref:`JSON API (Legacy) <developer_api_json>`: A REST-style API returning JSON-encoded payloads for read and write operations. Available since version 1.3, this API is deprecated and will be removed in a future release. We recommend avoiding use of this API for new projects.

APIs Providing More Specialized Access:
---------------------------------------

* :ref:`"Simple" API <developer_api_simple>`: A read-only API that provides configurable endpoints returning pre-formatted data (using :ref:`display templates <display_templates>`) in flat JSON-encoded key value responses. Endpoints can be generated for search result sets or individual records referenced by ID.

* :ref:`International Image Interoperability Framework (IIIF) Image service <developer_api_iiif>`: IIIF is a `standard for describing and delivering images via http <https://iiif.io>`_. The CollectiveAccess IIIF Image API returns images in response to a web request. Request URIs can specify cropping, size, rotation, quality and format of the returned image, as well as request technical information about the image. This service is often used to support advanced image viewing and presentation applications. CollectiveAccess uses this service internally to enable use of IIIF-compliant image and document viewers such as `Mirador <https://projectmirador.org>`_, `UniversalViewer <https://universalviewer.io>`_ and `DivaJS <https://ddmal.music.mcgill.ca/diva.js/>`_.

* :ref:`"Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) service <developer_api_oaipmh>`: A read-only API used to disseminate metadata to other systems in a `widely supported, standards-compliant manner <https://www.openarchives.org/pmh/>`_. CollectiveAccess can publish data in formats defined by an :ref:`export mapping <export_mappings>` for use by OAI-PMH clients.


