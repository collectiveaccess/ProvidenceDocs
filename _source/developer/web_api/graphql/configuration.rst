.. _developer_api_graphql_config:

Configuration (endpoint name ``Config``)
========================================

The configuration service provides access to configuration file settings, as well as configuration for editing user interfaces, displays, metadata elements, relationship types, locales and the data dictionary.

The ``configurationFile`` query provides access to any entry in a configuration file. The query requires the full name of the configuration file (including ``.conf`` extension) and the names of settings to be fetched in a ``keys`` list (single key values may be passed as a string in the ``key`` parameter). Return configuration values will be returned as encoded JSON along with ``type`` values indicating the structure of each value. ``ASSOC`` is used for associative array formatted values; ``LIST`` is used for lists of values, and ``SCALAR`` is returned for simple string values. A typical query to fetch values from the ``app.conf`` configuration file:

.. code-block:: Text

	  query {
		configurationFile (file:"app.conf", keys: ["wysiwyg_editor_toolbar", "ca_loans_disable"]) {
		  file, 
		  values { 
		  	key, 
		  	type, 
		  	value 
		  }
		}
	  }

would return:

.. code-block:: Text

	{
		"ok": true,
		"data": {
			"configurationFile": {
				"file": "app.conf",
				"values": [
					{
						"key": "wysiwyg_editor_toolbar",
						"type": "ASSOC",
						"value": "{\"formatting\":[\"Bold\",\"Italic\",\"Underline\",\"Strike\",\"-\",\"Subscript\",\"Superscript\",\"Font\",\"FontSize\",\"TextColor\"],\"lists\":[\"-\",\"NumberedList\",\"BulletedList\",\"Outdent\",\"Indent\",\"Blockquote\"],\"links\":[\"Link\",\"Unlink\",\"Anchor\"],\"misc\":[\"SelectAll\",\"Undo\",\"Redo\",\"-\",\"Source\",\"Maximize\",\"Image\",\"CALink\"]}"
					},
					{
						"key": "ca_loans_disable",
						"type": "SCALAR",
						"value": "\"0\""
					}
				]
			}
		}
	}

.. IMPORTANT::
   Access to configuration file values using this GraphQL service requires authentication with an account having the ``can_access_configuration_files_via_graphql`` action privilege.