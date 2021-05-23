.. _developer_api_simple:

Simple API
=====================

= QuickStart =

* Edit API endpoints in app/conf/services.conf, for example like this:

<pre>
template_api_endpoints = {
	testDetail = {
		type = detail,
		table = ca_objects,
		restrictToTypes = [image,dataset],
		checkAccess = [1,2],
		content = {
			object_id = ^ca_objects.object_id,
			display_label = ^ca_objects.preferred_labels
		}
	},
	testSearch = {
    		type = search,
    		table = ca_objects,
    		content = {
    			object_id = ^ca_objects.object_id,
    			display_label = ^ca_objects.preferred_labels
    		}
    	}
}
</pre>

* [[Web_Service_API#Authentication|authenticate]]
* Query either <pre>http://localhost/service.php/simple/<your_endpoint>?id=<id_or_idno>&pretty=1</pre> for detail pages or <pre>http://localhost/service.php/simple/<your_endpoint>?q=*&pretty=1</pre> for search endpoints.

= Documentation =

Contrary to the "main" [[Web_Service_API]] this simpler interface puts the payload formatting configuration for a service call in a config file on the CollectiveAccess server. This allows for much simpler client-side code and also means you can change the returned format without changing the client code (which could mean having to recompile and going through App Store approval again, etc.). The server-side configuration is done using [[Display_Templates]].

== Authentication ==

The authentication code is shared with the advanced Web Service API, so please refer to the respective section in the [[Web_Service_API#Authentication|documentation]]. '''Note that you should not use your admin or every-day user account and unencrypted HTTP basic auth to access the service API!''' It's okay to do so while developing on a local machine, which is why some of the examples below include plaintext user/pw combinations.

If you're operating remotely on a production system however, you should look into token-based authentication, a separate API user account that doesn't have permissions to do anything else, and most importantly, TLS encryption.

== Usage and configuration ==

Each service call refers to what we call an "endpoint". A system can have an arbitrary number of simple service endpoints. They are configurable in app/conf/services.conf and are called by sending a simple GET request to:

<pre>
http://localhost/service.php/simple/<your_endpoint>
</pre>

There are two different types of simple services: '''detail''' is used to get detailed information about a specific record identified by either its primary key or its idno. '''search''' can be used to run basic searches and return information about a list of records. Both have an additional mandatory GET parameter that must be passed to the endpoint:

{| class="wikitable"
! style="font-weight: bold;" | Service type
! style="font-weight: bold;" | Parameter
! style="font-weight: bold;" | Values
! style="font-weight: bold;" | Description
|-
| search
| q
| string
| Search query
|-
| detail
| id
| integer or short string
| Primary key
|-
| all
| pretty
| 0 or 1
| format returned JSON for readability ''(parameter is optional)''
|-
| all
| noCache
| 0 or 1
| If set to 1, result is always pulled from the database and not from a local cache. Can be handy when developing configurations.
|-
| search
| returnDataAsList
| 0 or 1
| If set to 1, search result data is returned as a list under the key "data", rather than as key/value pairs in the response hash. This option is useful when maintaining the order of returned results is important, as the JSON specification only guarantees maintenance of order for lists. '''Available from version 1.7'''
|}

The endpoint configuration is in the "simple_api_endpoints" array in app/conf/services.conf. You can have an arbitrary number of endpoints. Each endpoint refers to a specific kind of record (objects, entities, occurrences, etc, see [[Basic_Tables|"Basic Tables"]]), can optionally be restricted by type and also defines a list of key value pairs that are returned in the service response if that endpoint is queried. 

The settings for an endpoint are as follows:

{| class="wikitable"
! style="font-weight: bold;" | Setting
! style="font-weight: bold;" | Description
! style="font-weight: bold;" | Example
|-
| type
| Type of service endpoint. Can be "search" or "detail".
| detail
|-
| table
| What kind of record should this endpoint return information for? Should refer to one of the CollectiveAccess [[Basic_Tables]]
| ca_objects
|-
| restrictToTypes
| Optional list of type restrictions for this service. Can be useful if you want to tailor an endpoint towards a specific type of record (e.g. persons/individuals), and don't want it to be used for other records in the same class (e.g. organizations)
| [image,dataset]
|-
| checkAccess
| Optional list of access restrictions for this service. If set, records with access values not in that list won't show up, at least for the primary service "target". You can potentially still pull in non-accessible related records.
| [1,2]
|-
| content
| List of key value pairs that are part of the service response for this endpoint. Each value must be a valid [[Display_Templates|display template]] that is then run against the current record or against each record in the result set. As of version 1.7 you may optionally set the value of a key to a list of properties allowing greater control over output. Supported properties are described [[SimpleAPI#Content_key_options|below]].
| 
|}

A valid minimal example is in the quickstart section above.

If you have that configuration set up, you could run a simple query like this to get details for the object with primary key (object_id) 33:

<pre>
$ curl -XGET 'http://user:password@localhost/service.php/simple/testDetail?id=33&pretty=1'
</pre>

Note the endpoint name "testDetail". The result would be
<pre>
{
  "ok":true,
  "object_id":"1",
  "display_label":"asdf"
}
</pre>

The "ok" key is always present and indicates if there was an error while processing the request.

== Content key options ==

Normally the content block of an endpoint consists of simple key/value entries, where the key functions as a distinguishing name for a template-generated content value. In cases where more control is needed a block with additional properties may be substituted for the value template. Available properties include:

{| class="wikitable"
! style="font-weight: bold;" | Property
! style="font-weight: bold;" | Description
|-
| returnAs
| Format of return value. Options are JSON or text.
|-
| delimiter
| Delimiter to split key and content templates on when generating JSON for repeating values. Default is ";"
| 
|-
| keyTemplate
| Display template used to generate keys when generating lists of JSON-format return values. Keys generated with this template can be used to distinguish one value from another in a list of repeating values. If this is omitted no keys will be used and a simple JSON list returned.
|-
| valueTemplate
| Display template used to generate content values.
|}

For example, configuration to output Floorplan metadata elements, which include JSON-formatted text values, as decoded JSON integral to the service response might look like this:
<pre>
template_api_endpoints = {
	testDetail = {
		type = detail,
		table = ca_places,
		content = {
			place_id = ^ca_places.place_id,
			floorpans = {
				returnAs = JSON,
				delimiter = ;,
				keyTemplate = ^ca_occurrences.occurrence_id,
				valueTemplate = <unit relativeTo='ca_places_x_occurrences'>^ca_places_x_occurrences.floor_plan</unit>
			}
		}
	}
}
</pre>

[[Category:APIs]]
