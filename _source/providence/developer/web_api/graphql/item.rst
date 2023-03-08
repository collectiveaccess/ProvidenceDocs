.. _developer_api_graphql_item:

Item-level data access (endpoint name ``Item``)
================================================

The Item service returns detailed data for a single record retrieved using either an internal CollectiveAccess ID value or the ``idno`` value of the record.

To fetch a record pass the table, identifier and list of bundles to return in a ``get`` query. You can list any number of bundles, and include bundles in related tables. You may also specify :ref:`display templates <display_templates>`.

.. tip::
	
	Display templates can be used to format arbitrarily complex data extracted from returned records, as well as directly and indirectly related records. They are evaluated relative to the specified item.
	
.. code-block:: text

	query { 
		get(
			table: "ca_objects", 
			identifier: "test.1", 
			bundles: ["ca_objects.idno", "ca_objects.type_id", "ca_objects.preferred_labels.name", "ca_objects.nonpreferred_labels", "ca_objects.description", "<strong>[^ca_objects.type_id]</strong>: <unit relativeTo='ca_entities' delimiter='; '>^ca_entities.preferred_labels.surname, ^ca_entities.preferred_labels.forename</unit>"]
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
					},
					,
					{
						"name": "<strong>[^ca_objects.type_id]</strong>: <unit relativeTo='ca_entities' delimiter='; '>^ca_entities.preferred_labels.surname, ^ca_entities.preferred_labels.forename</unit>",
						"code": "<strong>[^ca_objects.type_id]</strong>: <unit relativeTo='ca_entities' delimiter='; '>^ca_entities.preferred_labels.surname, ^ca_entities.preferred_labels.forename</unit>",
						"dataType": "Text",
						"values": [
							{
								"locale": "en_US",
								"value": "<strong>Postcard</strong>: Tilyou, George; Dundee, Elmer; Thompson, Fred",
								"subvalues": [
									{
										"code": "description",
										"value": "<strong>Postcard</strong>: Tilyou, George; Dundee, Elmer; Thompson, Fred",
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
				relationship_typename,
				relationship_typecode,
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
						"relationship_typename": "Donor",
						"relationship_typecode": "donor",
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
	
.. tip::
	
	Value_id values are returned in the subvalues list for metadata elements. Valid_id's are unique numeric identifiers assigned automatically by CollectiveAccess for each individual metadata value attached to a record. These ids can be used to refer to a specific value for editing or deletion.
	

Fetching different relationships for an item in a single query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some applications need to fetch a variety of relationships for an item at once. Issuing a separate query for each relationship type may  impacts performance. It is possible to fetch any number of relationships for an item using the ``targets`` option. Each target may include any of the options used in a simple ``getRelationships query``. This query will return up to five objects and/or donor entities of type individual related to object 2022.001: 

.. code-block:: text

	query {
			getRelationships(
					table: "ca_objects",
					idno: "2022.001",
					targets:[
						{
							name: "related_objects",
							start: 0,
							limit: 5, 
							table: "ca_objects",
							bundles: ["ca_objects.preferred_labels.name", "ca_objects.idno"]
						},
						{
							name: "related_entities",
							start: 0,
							limit: 5, 
							table: "ca_entities",
							restrictToTypes: ["individual"],
							restrictToRelationshipTypes:["donor"],
							bundles: ["ca_entities.preferred_labels.displayname", "ca_entities.idno"]
						}
					]
				) {
					id,
					table,
					idno,
					targets { 
						name,
				
						relationships {
								relationship_typename,
								relationship_typecode,
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
				}
			
The response:


.. code-block:: text

	{
		"ok": true,
		"data": {
			"getRelationships": {
				"id": 2379,
				"table": "ca_objects",
				"idno": "2022.001",
				"targets": [
					{
						"name": "related_objects",
						"relationships": [
							{
								"relationship_typename": "is related to (forward)",
								"relationship_typecode": "related",
								"id": 59,
								"table": "ca_objects_x_objects",
								"bundles": [
									{
										"name": "Name (from art objects)",
										"code": "ca_objects.preferred_labels.name",
										"dataType": null,
										"values": [
											{
												"id": 6139,
												"value_id": null,
												"locale": "en_US",
												"value": "Madonna and Child",
												"subvalues": [
													{
														"id": null,
														"code": "name",
														"value": "Madonna and Child",
														"dataType": null
													}
												]
											}
										]
									},
									{
										"name": "Object identifier (from art objects)",
										"code": "ca_objects.idno",
										"dataType": null,
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "3349",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "3349",
														"dataType": null
													}
												]
											}
										]
									}
								]
							},
							{
								"relationship_typename": "is related to (reverse)",
								"relationship_typecode": "related",
								"id": 61,
								"table": "ca_objects_x_objects",
								"bundles": [
									{
										"name": "Name (from art objects)",
										"code": "ca_objects.preferred_labels.name",
										"dataType": "Container",
										"values": [
											{
												"id": 4941,
												"value_id": null,
												"locale": "en_US",
												"value": "The Adoration of the Magi",
												"subvalues": [
													{
														"id": null,
														"code": "name",
														"value": "The Adoration of the Magi",
														"dataType": "Container"
													}
												]
											}
										]
									},
									{
										"name": "Object identifier (from art objects)",
										"code": "ca_objects.idno",
										"dataType": "Container",
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "2047",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "2047",
														"dataType": null
													}
												]
											}
										]
									}
								]
							},
							{
								"relationship_typename": "is related to (forward)",
								"relationship_typecode": "related",
								"id": 62,
								"table": "ca_objects_x_objects",
								"bundles": [
									{
										"name": "Name (from art objects)",
										"code": "ca_objects.preferred_labels.name",
										"dataType": "Container",
										"values": [
											{
												"id": 5134,
												"value_id": null,
												"locale": "en_US",
												"value": "The Presentation in the Temple",
												"subvalues": [
													{
														"id": null,
														"code": "name",
														"value": "The Presentation in the Temple",
														"dataType": "Container"
													}
												]
											}
										]
									},
									{
										"name": "Object identifier (from art objects)",
										"code": "ca_objects.idno",
										"dataType": "Container",
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "2271",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "2271",
														"dataType": null
													}
												]
											}
										]
									}
								]
							}
						]
					},
					{
						"name": "related_entities",
						"relationships": [
							{
								"relationship_typename": "Artist",
								"relationship_typecode": "artist",
								"id": 1901,
								"table": "ca_objects_x_entities",
								"bundles": [
									{
										"name": "Display name (from name authorities)",
										"code": "ca_entities.preferred_labels.displayname",
										"dataType": "Container",
										"values": [
											{
												"id": 137,
												"value_id": null,
												"locale": "en_US",
												"value": "Bolognese 15th Century",
												"subvalues": [
													{
														"id": null,
														"code": "displayname",
														"value": "Bolognese 15th Century",
														"dataType": null
													}
												]
											}
										]
									},
									{
										"name": "Name Authority identifier (from name authorities)",
										"code": "ca_entities.idno",
										"dataType": "Container",
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "NAM0144",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "NAM0144",
														"dataType": null
													}
												]
											}
										]
									}
								]
							},
							{
								"relationship_typename": "Artist",
								"relationship_typecode": "artist",
								"id": 1902,
								"table": "ca_objects_x_entities",
								"bundles": [
									{
										"name": "Display name (from name authorities)",
										"code": "ca_entities.preferred_labels.displayname",
										"dataType": "Container",
										"values": [
											{
												"id": 138,
												"value_id": null,
												"locale": "en_US",
												"value": "Bolognese 16th Century",
												"subvalues": [
													{
														"id": null,
														"code": "displayname",
														"value": "Bolognese 16th Century",
														"dataType": "Container"
													}
												]
											}
										]
									},
									{
										"name": "Name Authority identifier (from name authorities)",
										"code": "ca_entities.idno",
										"dataType": "Container",
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "NAM0145",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "NAM0145",
														"dataType": null
													}
												]
											}
										]
									}
								]
							},
							{
								"relationship_typename": "location",
								"relationship_typecode": "location",
								"id": 1903,
								"table": "ca_objects_x_entities",
								"bundles": [
									{
										"name": "Display name (from name authorities)",
										"code": "ca_entities.preferred_labels.displayname",
										"dataType": "Container",
										"values": [
											{
												"id": 777,
												"value_id": null,
												"locale": "en_US",
												"value": "National Gallery of Art, Washington, District of Columbia",
												"subvalues": [
													{
														"id": null,
														"code": "displayname",
														"value": "National Gallery of Art, Washington, District of Columbia",
														"dataType": "Container"
													}
												]
											}
										]
									},
									{
										"name": "Name Authority identifier (from name authorities)",
										"code": "ca_entities.idno",
										"dataType": "Container",
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "NAM0858",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "NAM0858",
														"dataType": null
													}
												]
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
	

Fetching related media representations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using the ``targets`` option information about representations attached to related records may be returned setting the ``includeMedia`` option on a target. By default information for the "thumbnail", "small", "medium", "large" and "original" media versions are returned. Use the ``mediaVersions`` option on the target return other media versions. Information for attached media includes original media attributes such as representation idno, name (label), representation type, MIME type, width, height, duration and primary status. Per-version attributes include url, MIME type, width, height, duration and filesize. The previous query with media returned for related objects:


.. code-block:: text

	query {
				getRelationships(
						table: "ca_objects",
						idno: "2022.001",
						targets:[
							{
								name: "related_objects",
								start: 0,
								limit: 5, 
								table: "ca_objects",
								bundles: ["ca_objects.preferred_labels.name", "ca_objects.idno"],
								includeMedia: true,
								mediaVersions: ["tiny", "original"]
							},
							{
								name: "related_entities",
								start: 0,
								limit: 5, 
								table: "ca_entities",
								restrictToTypes: ["individual"],
								restrictToRelationshipTypes:["artist"],
								bundles: ["ca_entities.preferred_labels.displayname", "ca_entities.idno"]
							}
						]
					) {
						id,
						table,
						idno,
						targets { 
							name,
				
							relationships {
									relationship_typename,
									relationship_typecode,
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
									},
									media {
										id, idno, name, type, mimetype, isPrimary, width, height, duration, 
										versions {
											version, url, mimetype, width, height, duration, filesize
										}
									}    
								}
							}
						}
					}

The response would resemble:

.. code-block:: text

	{
		"ok": true,
		"data": {
			"getRelationships": {
				"id": 2379,
				"table": "ca_objects",
				"idno": "2022.001",
				"targets": [
					{
						"name": "related_objects",
						"relationships": [
							{
								"relationship_typename": "is related to (forward)",
								"relationship_typecode": "related",
								"id": 59,
								"table": "ca_objects_x_objects",
								"media": [
									{
										"id": "2013",
										"idno": "4026",
										"name": "[No Title]",
										"type": "front",
										"mimetype": "image/jpeg",
										"isPrimary": true,
										"width": 5201,
										"height": 6480,
										"duration": null,
										"versions": [
											{
												"version": "tiny",
												"url": "https://examplesite.com:8085/admin/media/collectiveaccess/images/2/0/70896_ca_object_representations_media_2013_tiny.jpg",
												"mimetype": "image/jpeg",
												"width": 58,
												"height": 72,
												"duration": null,
												"filesize": 19949
											},
											{
												"version": "original",
												"url": "https://examplesite.com:8085/admin/media/collectiveaccess/images/2/0/49772_ca_object_representations_media_2013_original.jpg",
												"mimetype": "image/jpeg",
												"width": 5201,
												"height": 6480,
												"duration": null,
												"filesize": 8280906
											}
										]
									},
									{
										"id": "4134",
										"idno": "8257",
										"name": "[No Title]",
										"type": "front",
										"mimetype": "video/mp4",
										"isPrimary": false,
										"width": 640,
										"height": 480,
										"duration": 71,
										"versions": [
											{
												"version": "tiny",
												"url": "https://examplesite.com:8085/admin/media/collectiveaccess/images/4/1/34644_ca_object_representations_media_4134_tiny.jpg",
												"mimetype": "image/jpeg",
												"width": 72,
												"height": 54,
												"duration": 71,
												"filesize": 722
											},
											{
												"version": "original",
												"url": "https://examplesite.com:8085/admin/media/collectiveaccess/quicktime/4/1/78104_ca_object_representations_media_4134_original.m4v",
												"mimetype": "video/mp4",
												"width": 640,
												"height": 480,
												"duration": 71,
												"filesize": 14438991
											}
										]
									}
								],
								"bundles": [
									{
										"name": "Name (from art objects)",
										"code": "ca_objects.preferred_labels.name",
										"dataType": null,
										"values": [
											{
												"id": 6139,
												"value_id": null,
												"locale": "en_US",
												"value": "Madonna and Child",
												"subvalues": [
													{
														"id": null,
														"code": "name",
														"value": "Madonna and Child",
														"dataType": null
													}
												]
											}
										]
									},
									{
										"name": "Object identifier (from art objects)",
										"code": "ca_objects.idno",
										"dataType": null,
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "3349",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "3349",
														"dataType": null
													}
												]
											}
										]
									}
								]
							},
							{
								"relationship_typename": "is related to (reverse)",
								"relationship_typecode": "related",
								"id": 61,
								"table": "ca_objects_x_objects",
								"media": [
									{
										"id": "960",
										"idno": "1920",
										"name": "[No Title]",
										"mimetype": "image/jpeg",
										"isPrimary": true,
										"width": 17698,
										"height": 27603,
										"duration": null,
										"versions": [
											{
												"version": "tiny",
												"url": "https://examplesite.com:8085/admin/media/collectiveaccess/images/9/37506_ca_object_representations_media_960_tiny.jpg",
												"mimetype": "image/jpeg",
												"width": 46,
												"height": 72,
												"duration": null,
												"filesize": 23123
											},
											{
												"version": "original",
												"url": "https://examplesite.com:8085/admin/media/collectiveaccess/images/9/27193_ca_object_representations_media_960_original.jpg",
												"mimetype": "image/jpeg",
												"width": 17698,
												"height": 27603,
												"duration": null,
												"filesize": 200100680
											}
										]
									}
								],
								"bundles": [
									{
										"name": "Name (from art objects)",
										"code": "ca_objects.preferred_labels.name",
										"dataType": "Container",
										"values": [
											{
												"id": 4941,
												"value_id": null,
												"locale": "en_US",
												"value": "The Adoration of the Magi",
												"subvalues": [
													{
														"id": null,
														"code": "name",
														"value": "The Adoration of the Magi",
														"dataType": "Container"
													}
												]
											}
										]
									},
									{
										"name": "Object identifier (from art objects)",
										"code": "ca_objects.idno",
										"dataType": "Container",
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "2047",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "2047",
														"dataType": null
													}
												]
											}
										]
									}
								]
							},
							{
								"relationship_typename": "is related to (forward)",
								"relationship_typecode": "related",
								"id": 62,
								"table": "ca_objects_x_objects",
								"media": [
									{
										"id": "1134",
										"idno": "2268",
										"name": "[No Title]",
										"mimetype": "image/jpeg",
										"isPrimary": true,
										"width": 10307,
										"height": 12448,
										"duration": null,
										"versions": [
											{
												"version": "tiny",
												"url": "https://examplesite.com:8085/admin/media/collectiveaccess/images/1/1/43558_ca_object_representations_media_1134_tiny.jpg",
												"mimetype": "image/jpeg",
												"width": 60,
												"height": 72,
												"duration": null,
												"filesize": 26858
											},
											{
												"version": "original",
												"url": "https://examplesite.com:8085/admin/media/collectiveaccess/images/1/1/7081_ca_object_representations_media_1134_original.jpg",
												"mimetype": "image/jpeg",
												"width": 10307,
												"height": 12448,
												"duration": null,
												"filesize": 42116690
											}
										]
									}
								],
								"bundles": [
									{
										"name": "Name (from art objects)",
										"code": "ca_objects.preferred_labels.name",
										"dataType": "Container",
										"values": [
											{
												"id": 5134,
												"value_id": null,
												"locale": "en_US",
												"value": "The Presentation in the Temple",
												"subvalues": [
													{
														"id": null,
														"code": "name",
														"value": "The Presentation in the Temple",
														"dataType": "Container"
													}
												]
											}
										]
									},
									{
										"name": "Object identifier (from art objects)",
										"code": "ca_objects.idno",
										"dataType": "Container",
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "2271",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "2271",
														"dataType": null
													}
												]
											}
										]
									}
								]
							}
						]
					},
					{
						"name": "related_entities",
						"relationships": [
							{
								"relationship_typename": "Artist",
								"relationship_typecode": "artist",
								"id": 1901,
								"table": "ca_objects_x_entities",
								"media": [],
								"bundles": [
									{
										"name": "Display name (from name authorities)",
										"code": "ca_entities.preferred_labels.displayname",
										"dataType": "Container",
										"values": [
											{
												"id": 137,
												"value_id": null,
												"locale": "en_US",
												"value": "Bolognese 15th Century",
												"subvalues": [
													{
														"id": null,
														"code": "displayname",
														"value": "Bolognese 15th Century",
														"dataType": null
													}
												]
											}
										]
									},
									{
										"name": "Name Authority identifier (from name authorities)",
										"code": "ca_entities.idno",
										"dataType": "Container",
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "NAM0144",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "NAM0144",
														"dataType": null
													}
												]
											}
										]
									}
								]
							},
							{
								"relationship_typename": "Artist",
								"relationship_typecode": "artist",
								"id": 1902,
								"table": "ca_objects_x_entities",
								"media": [],
								"bundles": [
									{
										"name": "Display name (from name authorities)",
										"code": "ca_entities.preferred_labels.displayname",
										"dataType": "Container",
										"values": [
											{
												"id": 138,
												"value_id": null,
												"locale": "en_US",
												"value": "Bolognese 16th Century",
												"subvalues": [
													{
														"id": null,
														"code": "displayname",
														"value": "Bolognese 16th Century",
														"dataType": "Container"
													}
												]
											}
										]
									},
									{
										"name": "Name Authority identifier (from name authorities)",
										"code": "ca_entities.idno",
										"dataType": "Container",
										"values": [
											{
												"id": 0,
												"value_id": null,
												"locale": "en_US",
												"value": "NAM0145",
												"subvalues": [
													{
														"id": null,
														"code": "0",
														"value": "NAM0145",
														"dataType": null
													}
												]
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
	
You may optionally restrict media returned type type using the optional ``restrictMediaToTypes`` option.
	
Limiting results using access values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All primary records in CollectiveAccess include an ``access`` field to control visibility in public-facing contexts such as web sites and data feeds. Data in the ``getRelationships`` query can be limited by one or more access values using the ``checkAccess`` parameter, set to a list of integer access codes, as defined in the ``access_statuses`` list for the CollectiveAccess installation. By convention 0 indicates a private record, 1 a public record and 2 a record available in public interfaces to users with elevated privileges. However, these values may be vary across installations and should be verified before use. 