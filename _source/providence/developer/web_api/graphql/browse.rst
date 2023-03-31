.. _developer_api_graphql_browse:

Browsing (endpoint name ``Browse``)
====================================

The Browse service provides access to CollectiveAccess' faceted browse functionality. Facets are defined in the ``browse.conf`` file for each table. 

Service queries operate using ``browseType`` names. Each ``browseType`` is defined in ``browse.conf`` as a context for browse, incorporating a display name, table, type restrictions and display settings. 

The ``key`` parameter
---------------------

All browse service queries and mutations accept a ``key`` parameter, which is a compact representation of current browse criteria.  When beginning a new browse, they key will be empty and need not be passed in queries. As the browse is refined using filter criteria the key will change, with queries that modify browse criteria taking the current ``key`` as a parameter and returning a new ``key`` in the response.

.. note::
	
	Explain more about keys here...
	

Fetching information about facets
---------------------------------

To get a list of available facets with values:

.. code-block:: text

	query {
		  facets(browseType: "objects", key: "") {
			facets { name, labelSingular, labelPlural, description, type, values { id, value, sortableValue, contentCount, childCount} }
		  }
	}
	
Note with an empty key this query returns all available facets with selectivity on all accessible records. Setting the key will limit returned facets. Each returned facet can include display text for the facet a well as a list of available facet values and the number of records that match each value. A typical response:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"facets": {
				"facets": [
					{
						"name": "title_facet",
						"labelSingular": "object title",
						"labelPlural": "object titles",
						"description": null,
						"type": "label",
						"values": [
							{
								"id": "1",
								"value": "Object 1",
								"sortableValue": null,
								"contentCount": 1,
								"childCount": 0
							},
							{
								"id": "2",
								"value": "Object 2xx",
								"sortableValue": null,
								"contentCount": 1,
								"childCount": 0
							},
							{
								"id": "3",
								"value": "Object 3",
								"sortableValue": null,
								"contentCount": 1,
								"childCount": 0
							}
						]
					},
					{
						"name": "checkouts_facet",
						"labelSingular": "checkout",
						"labelPlural": "checkouts",
						"description": null,
						"type": "checkouts",
						"values": [
							{
								"id": "available",
								"value": "Available",
								"sortableValue": null,
								"contentCount": null,
								"childCount": null
							},
							{
								"id": "out",
								"value": "Out",
								"sortableValue": null,
								"contentCount": null,
								"childCount": null
							}
						]
					},
					{
						"name": "has_media_facet",
						"labelSingular": "has media",
						"labelPlural": "has media",
						"description": null,
						"type": "has",
						"values": [
							{
								"id": "1",
								"value": "Has media",
								"sortableValue": null,
								"contentCount": 2,
								"childCount": null
							},
							{
								"id": "0",
								"value": "Has no media",
								"sortableValue": null,
								"contentCount": 1,
								"childCount": null
							}
						]
					},
					{
						"name": "collection_facet",
						"labelSingular": "collection",
						"labelPlural": "collections",
						"description": null,
						"type": "authority",
						"values": [
							{
								"id": "1",
								"value": "xxx",
								"sortableValue": "xxx           ",
								"contentCount": 3,
								"childCount": 3
							},
							{
								"id": "2",
								"value": "yyy",
								"sortableValue": "yyy           ",
								"contentCount": 2,
								"childCount": 0
							}
						]
					},
					{
						"name": "storage_location_facet",
						"labelSingular": "storage location",
						"labelPlural": "storage locations",
						"description": null,
						"type": "authority",
						"values": [
							{
								"id": "2",
								"value": "Library A",
								"sortableValue": "Library        A             ",
								"contentCount": 2,
								"childCount": 3
							},
							{
								"id": "3",
								"value": "Library B",
								"sortableValue": "Library        B             ",
								"contentCount": 1,
								"childCount": 3
							},
							{
								"id": "4",
								"value": "Room A1",
								"sortableValue": "Room           A1            ",
								"contentCount": 1,
								"childCount": 0
							},
							{
								"id": "5",
								"value": "Room B1",
								"sortableValue": "Room           B1            ",
								"contentCount": 1,
								"childCount": 0
							}
						]
					},
					{
						"name": "type_facet",
						"labelSingular": "type",
						"labelPlural": "types",
						"description": null,
						"type": "fieldList",
						"values": [
							{
								"id": "26",
								"value": "Moving Images",
								"sortableValue": null,
								"contentCount": 1,
								"childCount": 0
							},
							{
								"id": "27",
								"value": "Physical Objects",
								"sortableValue": null,
								"contentCount": 2,
								"childCount": 0
							}
						]
					},
					{
						"name": "status_facet",
						"labelSingular": "status",
						"labelPlural": "statuses",
						"description": null,
						"type": "fieldList",
						"values": [
							{
								"id": "0",
								"value": "new",
								"sortableValue": null,
								"contentCount": 2,
								"childCount": null
							},
							{
								"id": "3",
								"value": "review in progress",
								"sortableValue": null,
								"contentCount": 1,
								"childCount": null
							}
						]
					},
					{
						"name": "access_facet",
						"labelSingular": "access status",
						"labelPlural": "access statuses",
						"description": null,
						"type": "fieldList",
						"values": [
							{
								"id": "0",
								"value": "not accessible to public",
								"sortableValue": null,
								"contentCount": 3,
								"childCount": null
							}
						]
					}
				]
			}
		}
	}
	
The ``facet`` query return details about a specific facet, given the ``facet`` parameter set to a facet ``name`` as returned in a ``facets`` query:

.. code-block:: text

	query {
		  facet(browseType: "objects", facet: "has_media_facet", key: "") {
			name, labelSingular, labelPlural, description, type, values { id, value, sortableValue, contentCount, childCount} 
		  }
	}
	
A typical response:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"facet": {
				"name": "has_media_facet",
				"labelSingular": null,
				"labelPlural": null,
				"description": null,
				"type": "has",
				"values": [
					{
						"id": "1",
						"value": "Has media",
						"sortableValue": null,
						"contentCount": 2,
						"childCount": null
					},
					{
						"id": "0",
						"value": "Has no media",
						"sortableValue": null,
						"contentCount": 1,
						"childCount": null
					}
				]
			}
		}
	}
	
Managing browse filter criteria
---------------------------------

A browse without filter criteria will match all available records. As criteria are added the browse will return fewer and fewer results. To add a filter criterion use the ``addFilterValue`` mutation:

.. code-block:: text

	mutation {
		  addFilterValue(browseType: "objects", facet: "has_media_facet", key: "", value : "yes") {
			key , created, content_type, content_type_display, item_count, items { id, title, viewerUrl, viewerClass, identifier, rank, media { version, url, width, height, mimetype } }, filters { facet, values { id, value } }
		  }
	}
	
In addition to adding the filter value, ``addFilterValue`` can also return results for the newly refined browse (``items``), as well as display media for items (``items`` >> ``media``) and a list of currently applied criteria (``filters``).

.. code-block:: text

A typical response:

	{
		"ok": true,
		"data": {
			"addFilterValue": {
				"key": "64b9ecffa743b70d125d7cfca65bf301",
				"created": "2023-03-31T13:39:23-04:00",
				"content_type": "ca_objects",
				"content_type_display": "objects",
				"item_count": 2,
				"items": [
					{
						"id": 1,
						"title": "Object 1",
						"viewerUrl": "http://providence/media/collectiveaccess/images/0/82831_ca_object_representations_media_20_compressed.pdf",
						"viewerClass": "document",
						"identifier": "Obj.1",
						"rank": 0,
						"media": [
							{
								"version": "small",
								"url": "http://providence/media/collectiveaccess/images/0/46727_ca_object_representations_media_20_small.jpg",
								"width": "170",
								"height": "240",
								"mimetype": "image/jpeg"
							},
							{
								"version": "medium",
								"url": "http://providence/media/collectiveaccess/images/0/5471_ca_object_representations_media_20_medium.jpg",
								"width": "283",
								"height": "400",
								"mimetype": "image/jpeg"
							},
							{
								"version": "large",
								"url": "http://providence/media/collectiveaccess/images/0/11509_ca_object_representations_media_20_large.jpg",
								"width": "700",
								"height": "991",
								"mimetype": "image/jpeg"
							},
							{
								"version": "original",
								"url": "http://providence/media/collectiveaccess/images/0/58981_ca_object_representations_media_20_original.pdf",
								"width": "595",
								"height": "842",
								"mimetype": "application/pdf"
							},
							{
								"version": "compressed",
								"url": "http://providence/media/collectiveaccess/images/0/82831_ca_object_representations_media_20_compressed.pdf",
								"width": "595",
								"height": "842",
								"mimetype": "application/pdf"
							}
						]
					},
					{
						"id": 2,
						"title": "Object 2xx",
						"viewerUrl": "/service.php/IIIF/5/info.json",
						"viewerClass": "image",
						"identifier": "Obj.2",
						"rank": 1,
						"media": [
							{
								"version": "small",
								"url": "http://providence/media/collectiveaccess/images/0/5745_ca_object_representations_media_5_small.jpg",
								"width": "240",
								"height": "180",
								"mimetype": "image/jpeg"
							},
							{
								"version": "medium",
								"url": "http://providence/media/collectiveaccess/images/0/11816_ca_object_representations_media_5_medium.jpg",
								"width": "400",
								"height": "300",
								"mimetype": "image/jpeg"
							},
							{
								"version": "large",
								"url": "http://providence/media/collectiveaccess/images/0/60506_ca_object_representations_media_5_large.jpg",
								"width": "700",
								"height": "525",
								"mimetype": "image/jpeg"
							},
							{
								"version": "original",
								"url": "http://providence/media/collectiveaccess/images/0/54655_ca_object_representations_media_5_original.jpg",
								"width": "1632",
								"height": "1224",
								"mimetype": "image/jpeg"
							}
						]
					}
				],
				"filters": [
					{
						"facet": "has_media_facet",
						"values": [
							{
								"id": "yes",
								"value": "Has media"
							}
						]
					}
				]
			}
		}
	}
	
To remove filter values use the ``removeFilterValue`` mutation:

.. code-block:: text

	mutation {
		  removeFilterValue(browseType: "objects", facet: "has_media_facet", key: "64b9ecffa743b70d125d7cfca65bf301", value : "yes") {
			key , created, content_type, content_type_display, item_count, items { id, title, viewerUrl, viewerClass, identifier, rank, media { version, url, width, height, mimetype } }, filters { facet, values { id, value } }
		  }
	}

If both ``facet`` and ``value`` are set only the criterion with the specified value will be removed. If ``value`` is omitted then all criteria for the facet are removed. The response structure is similar to that of ``removeFilterValue`` and can include and updated list of filters and items.

To remove all filter values and return the browse use the ``removeAllFilterValues`` mutation:

.. code-block:: text

	mutation {
		  removeAllFilterValues(browseType: "objects" key: "64b9ecffa743b70d125d7cfca65bf301") {
			key , created, content_type, content_type_display, item_count, items { id, title, viewerUrl, viewerClass, identifier, rank, media { version, url, width, height, mimetype } }, filters { facet, values { id, value } }
		  }
	}

All filter criteria, regardless of facet will be removed. The response structure is similar to that of ``removeFilterValue`` and can include and updated list of filters and items.

Fetching results
----------------

To reduce the number of service calls the results of a browse can be returned as part of the response for mutations that change criteria (		addFilterValue``, ``removeFilterValue`` and ``removeAllFilterValues``). The results of a browse associated with a given ``key`` may be returned at any time using the ``result`` query:

.. code-block:: text

	query {
		  result(browseType: "objects", key: "64b9ecffa743b70d125d7cfca65bf301") {
			key , created, content_type, content_type_display, item_count, items { id, title, viewerUrl, viewerClass, identifier, rank, media { version, url, width, height, mimetype } }, filters { facet, values { id, value } }
		  }
	}

The response format is the same as for the criteria mutations.