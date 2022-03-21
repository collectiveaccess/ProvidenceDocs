Metadata import (endpoint name ``MetadataImport``)
---------------------------------------------------

Get a list of available importers:

.. code-block:: Text

	query {
		list {
			id, name, code, table, formats, source
		}
	}

Returns

.. code-block:: Text

	{
		"ok": true,
		"data": {
			"list": [
				{
					"id": 1,
					"name": "CS Artworks",
					"code": "cs_artwork_mapping",
					"table": "ca_objects",
					"formats": [
						"FMPXML"
					],
					"source": null
				},
				{
					"id": 2,
					"name": "ARSENAL Storage Locations Import Mapping",
					"code": "ARSENAL_storage_locations_import_mapping",
					"table": "ca_storage_locations",
					"formats": [
						"XLSX"
					],
					"source": "https://docs.google.com/spreadsheets/d/1KP86kQ1Et6y2YvBn9bBrXIGg3t5gIkZt/edit?usp=sharing&ouid=110406525006532822247&rtpof=true&sd=true"
				}
			]
		}
	}