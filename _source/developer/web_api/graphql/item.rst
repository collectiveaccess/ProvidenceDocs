.. _developer_api_graphql_item:

Item-level data access (endpoint name ``Item``)
================================================

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