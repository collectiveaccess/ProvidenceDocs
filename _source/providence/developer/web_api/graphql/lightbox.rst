.. _developer_api_graphql_lightbox:

Lightbox/set management (endpoint name ``Lightbox``)
====================================================

The Lightbox service provides access to CollectiveAccess' back-end ``sets`` functionality, which is usually referred to as ``Lightbox`` on public-facing front-end interfaces, such as the interface provided by Pawtucket2.


Fetching a list of lightboxes
-----------------------------

To get a list of available lightboxes for the current user:

.. code-block:: text

	query {
	  list {
		id, title, count,
		author_lname, author_fname, author_email,
		type, created, content_type, content_type_singular, content_type_plural						
	  }
	}
	
The query does not take parameters and always returns results within the context of the currently authenticated user. The response includes basic information about the lightbox (identifier, title item count, owner/creator and content type). A typical response:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"list": [
				{
					"id": 862,
					"title": "Test lightbox",
					"count": 3,
					"author_lname": "Steve",
					"author_fname": "Smith",
					"author_email": "Steve@smithtown.org",
					"type": "User set",
					"created": "2023-04-10T12:00:10-04:00",
					"content_type": "ca_objects",
					"content_type_singular": "object",
					"content_type_plural": "objects"
				},
				{
					"id": 863,
					"title": "Selina Lightbox",
					"count": 5,
					"author_lname": "Selina",
					"author_fname": "M",
					"author_email": "selina@whirl-i-gig.com",
					"type": "User set",
					"created": "2023-04-11T15:08:54-04:00",
					"content_type": "ca_objects",
					"content_type_singular": "object",
					"content_type_plural": "objects"
				},
				{
					"id": 865,
					"title": "Lightbox with 1 item",
					"count": 1,
					"author_lname": "Steve",
					"author_fname": "Smith",
					"author_email": "Steve@smithtown.org"",
					"type": "User set",
					"created": "2023-04-11T15:12:58-04:00",
					"content_type": "ca_objects",
					"content_type_singular": "object",
					"content_type_plural": "objects"
				}
			]
		}
	}

Getting the contents of a lightbox
----------------------------------

To obtain detailed information about a lightbox and its contents use the ``content`` query with the ``id`` of a lightbox. The ``start`` and ``limit`` options may be set to limit the length of the returned item list and facilitate paging. The ``sort`` parameter may be set to sort lightbox item on any bundle available for the lightbox content type. ``sortDirection`` may be set to ``ASC`` or ``DESC`` to control whether items are sorted ascending or descending. 

Media attached to each lightbox item may be returned. By default only the ``small`` version is returned. Versions may be specified in a list using the ``mediaVersions`` option.

.. code-block:: text

	query {
	  content(id:862, mediaVersions: ["small", "medium", "large"])
	  {
		id, title, type, content_type, created, item_count,
		sortOptions {
			label, sort
		},
		comments {
			fname, lname, email, user_id, created, content
		},
		items {
			id, title, caption, identifier, rank, media {
				version, url, tag, width, height, mimetype
			}
		}
								
	  }
	}
	
A typical response:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"content": {
				"id": 862,
				"title": "Test lightbox",
				"type": "user",
				"content_type": "ca_objects",
				"created": "2023-04-10T12:00:10-04:00",
				"item_count": 3,
				"sortOptions": [],
				"comments": [],
				"items": [
					{
						"id": 19308,
						"title": "BTR2016_OVS_crop_005.tif",
						"caption": "[BLANK]",
						"identifier": "2018.731",
						"rank": 122627,
						"media": [
							{
								"version": "small",
								"url": "http://test.com/admin/media/collectiveaccess/images/1/8/8/81790_ca_object_representations_media_18851_small.jpg",
								"tag": "<img src='http://test.com/admin/media/collectiveaccess/images/1/8/8/81790_ca_object_representations_media_18851_small.jpg' width='240' height='155' alt='BTR2016_OVS_crop_005.tif' />",
								"width": "240",
								"height": "155",
								"mimetype": "image/jpeg"
							},
							{
								"version": "medium",
								"url": "http://test.com/admin/media/collectiveaccess/images/1/8/8/18108_ca_object_representations_media_18851_medium.jpg",
								"tag": "<img src='http://test.com/admin/media/collectiveaccess/images/1/8/8/18108_ca_object_representations_media_18851_medium.jpg' width='400' height='259' alt='BTR2016_OVS_crop_005.tif' />",
								"width": "400",
								"height": "259",
								"mimetype": "image/jpeg"
							},
							{
								"version": "large",
								"url": "http://test.com/admin/media/collectiveaccess/images/1/8/8/96787_ca_object_representations_media_18851_large.jpg",
								"tag": "<img src='http://test.com/admin/media/collectiveaccess/images/1/8/8/96787_ca_object_representations_media_18851_large.jpg' width='700' height='453' alt='BTR2016_OVS_crop_005.tif' />",
								"width": "700",
								"height": "453",
								"mimetype": "image/jpeg"
							}
						]
					},
					{
						"id": 19262,
						"title": "BTR2016_OVS_crop_007.tif",
						"caption": "[BLANK]",
						"identifier": "2018.727",
						"rank": 122628,
						"media": [
							{
								"version": "small",
								"url": "http://test.com/admin/media/collectiveaccess/images/1/8/8/3688_ca_object_representations_media_18805_small.jpg",
								"tag": "<img src='http://test.com/admin/media/collectiveaccess/images/1/8/8/3688_ca_object_representations_media_18805_small.jpg' width='240' height='114' alt='BTR2016_OVS_crop_007.tif' />",
								"width": "240",
								"height": "114",
								"mimetype": "image/jpeg"
							},
							{
								"version": "medium",
								"url": "http://test.com/admin/media/collectiveaccess/images/1/8/8/80487_ca_object_representations_media_18805_medium.jpg",
								"tag": "<img src='http://test.com/admin/media/collectiveaccess/images/1/8/8/80487_ca_object_representations_media_18805_medium.jpg' width='400' height='190' alt='BTR2016_OVS_crop_007.tif' />",
								"width": "400",
								"height": "190",
								"mimetype": "image/jpeg"
							},
							{
								"version": "large",
								"url": "http://test.com/admin/media/collectiveaccess/images/1/8/8/4852_ca_object_representations_media_18805_large.jpg",
								"tag": "<img src='http://test.com/admin/media/collectiveaccess/images/1/8/8/4852_ca_object_representations_media_18805_large.jpg' width='700' height='332' alt='BTR2016_OVS_crop_007.tif' />",
								"width": "700",
								"height": "332",
								"mimetype": "image/jpeg"
							}
						]
					},
					{
						"id": 9539,
						"title": "Delta of Mount Whitney_Lauren Bon_2013_6.tiff",
						"caption": "[BLANK]",
						"identifier": "2018.462",
						"rank": 122629,
						"media": [
							{
								"version": "small",
								"url": "http://test.com/admin/media/collectiveaccess/images/9/7/81829_ca_object_representations_media_9722_small.jpg",
								"tag": "<img src='http://test.com/admin/media/collectiveaccess/images/9/7/81829_ca_object_representations_media_9722_small.jpg' width='169' height='240' alt='Delta of Mount Whitney_Lauren Bon_2013_6.tiff' />",
								"width": "169",
								"height": "240",
								"mimetype": "image/jpeg"
							},
							{
								"version": "medium",
								"url": "http://test.com/admin/media/collectiveaccess/images/9/7/44386_ca_object_representations_media_9722_medium.jpg",
								"tag": "<img src='http://test.com/admin/media/collectiveaccess/images/9/7/44386_ca_object_representations_media_9722_medium.jpg' width='281' height='400' alt='Delta of Mount Whitney_Lauren Bon_2013_6.tiff' />",
								"width": "281",
								"height": "400",
								"mimetype": "image/jpeg"
							},
							{
								"version": "large",
								"url": "http://test.com/admin/media/collectiveaccess/images/9/7/42370_ca_object_representations_media_9722_large.jpg",
								"tag": "<img src='http://test.com/admin/media/collectiveaccess/images/9/7/42370_ca_object_representations_media_9722_large.jpg' width='700' height='996' alt='Delta of Mount Whitney_Lauren Bon_2013_6.tiff' />",
								"width": "700",
								"height": "996",
								"mimetype": "image/jpeg"
							}
						]
					}
				]
			}
		}
	}

Creating and editing lightboxes
-------------------------------

New lightboxes for the current user may be created using the ``create`` query:

.. code-block:: text

	mutation {
	   create(content: "ca_objects", data: {name: "My new lightbox", code:"my_new_lightbox"}, items: { ids: "43;54;1003" })
	  {
	   id, name, count 
	  }						
	}

The ``content`` option specifies what kind of record the lightbox will contain using a table code (Eg. ``ca_objects`` for a lightbox containing objects). A lightbox cannot contain more than one kind of record. The ``data`` input type takes two values specifying the ``name`` and ``code`` of the new lightbox. ``name`` is required. ``code`` is an alphanumeric value uniquely identifying the lightbox. If omitted one will be automatically generated. The ``items`` input type should be a string listing numeric item ids separated by semicolons. The referenced items will be added to the new lightbox if they are accessible to the current user.

The response will indicate whether the lightbox could be created or not, and when successful will include the numeric id of the newly created lightbox as well as the name and item count. The returned item count may be less than the number of items set in the ``items`` option if some of the specified ids are not accessible or do not exist.

A typical response:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"create": {
				"id": 866,
				"name": "My new lightbox",
				"count": 3
			}
		}
	}
	
The response for all lightbox mutation follow this form.
	
To edit the name and/or code of an existing lightbox use the ``edit`` query and the numeric ``id`` of the lightbox:

.. code-block:: text

	mutation {
	   edit(id: 866, data: {name: "Another name", "code": "a_new_code"}})
	  {
	   id, name, count 
	  }						
	}

The response will be in the same form as that returned by the ``create`` mutation. 

To add or remove items from a lightbox use the ``appendItems`` and ``removeItems`` mutations. The ``appendItems`` mutation works similarly to the ``create`` mutation, with ``items`` being added to whatever items are already contained in the lightbox with the specified ``id``. It is also possible to update the lightbox ``name`` and ``code`` using the ``data`` option:

.. code-block:: text

	mutation {
	   appendItems(id: 866, data: {name: "My new lightbox", code:"my_new_lightbox"}, items: { ids: "43;54;1003" })
	  {
	   id, name, count 
	  }						
	}	

The ``removeItem`` mutation will remove items from a lightbox using a semicolon delimited list of item ids:

.. code-block:: text

	mutation {
	   removeItems(id: 866,items: { ids: "43;54;1003" })
	  {
	   id, name, count 
	  }						
	}	

A lightbox may be deleted using the ``delete`` mutation:

.. code-block:: text

	mutation {
	   delete(id: 866)
	  {
	   id, name, count 
	  }						
	}	


Managing order of items in a lightbox
-------------------------------------

By default items in a lightbox are returned in the order that they were added. This lightbox-specific ordering may be modified using the ``reorder`` mutation:

.. code-block:: text

	mutation {
	   reorder(id: 866, data { ids: "1003;43;54" })
	  {
	   id, name, count 
	  }						
	}	

Items referenced in the ``data`` option will be placed in the order specified in the semicolon-separated list of ``ids``. Ids not present in the lightbox will be ignored.

Transferring items between lightboxes
-------------------------------------

Items maybe transfered between lightboxes with the same content type using the ``transferItems`` mutation:

.. code-block:: text

	mutation {
	   transferITems(id: 866, toId: 996, items: { ids: "54;542;113" })
	  {
	   id, name, count 
	  }						
	}	

The response for this mutation will be in the same form as that returned by the ``create`` mutation. 


Sharing lightboxes
-------------------------------

Lightboxes may be shared with other users. To manage access use the ``share`` mutation:

.. code-block:: text

	mutation {
	   share(id: 866, share: { users: "steve@steveville.org;meow@kitty.com", access: 1})
	  {
	   id, name, count 
	  }						
	}	
	
The ``share`` option includes two values. ``users`` is a semicolon-separated list of user email addresses. ``access`` determines the type of access granted. Set to 1 to grant read-only access or 2 for full edit access.

Commenting on lightboxes
-------------------------

Comments may be attached to lightboxes using the ``comment`` mutation:

.. code-block:: text

	mutation {
	   comment(id: 866, comment: { content: "This is a commnent!"})
	  {
	   id, name, count 
	  }						
	}	
	
Comments are attached to lightboxes with attribution to the currently authenticated user. Removal of comments via the API is not currently supported.