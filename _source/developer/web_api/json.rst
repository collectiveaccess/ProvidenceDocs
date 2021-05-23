.. _developer_api_json:

JSON API
=====================

This article describes the REST API provided by CollectiveAccess. Short of very few HTTP GET parameters both the request parameters and the responses are encoded in [http://en.wikipedia.org/wiki/JSON JSON]. Note that most of the query examples in this article assume that you have [http://curl.haxx.se/ curl] installed. If you have never done any CollectiveAccess development you should take a few minutes and read the article [[API:Accessing_Data]] as introduction. Most of the concepts used in the web service API are explained there.

== Global parameters ==

=== Authentication ===

Access to the whole service API or to certain parts of the CollectiveAccess data may be restricted to specific users, user groups or user roles. This web service API respects those restrictions where possible, so you will probably have to authenticate to use it.

'''From v1.5''', the API has a special service endpoint for authentication that will generate a temporary token that you can use for subsequent calls. You log in using HTTP Basic authentication. This can be done either via HTTP header or directly in the URL. Odds are the HTTP request library you're using has native support for HTTP basic auth, but in case you're testing by hand in a browser, you can use the following pattern:

<pre>
http://user:password@localhost/service.php/auth/login
</pre>

Calling this service via GET will give you a JSON response that includes a 256bit authentication token. If the username/password combination is valid, that is. It should look something like this:

<pre>
{"ok":true,"authToken":"c55ccee391f972097267a4afd8da4eb6d32da0acd3311f41ea0806142169b7ca"}
</pre>

You can use that token to quickly authenticate all subsequent requests against the API, using the "authToken" GET parameter, e.g.

<pre>
http://localhost/service.php/item/ca_objects/id/1?authToken=c55ccee391f972097267a4afd8da4eb6d32da0acd3311f41ea0806142169b7ca
</pre>

The token will expire within a few hours, so you'll eventually get a 401 Access Denied HTTP response. At that point simply re-authenticate using the auth/login service.

'''Pre v1.5''' you're going to have to add HTTP Basic authentication to '''every API call'''. This is still supported in v1.5 for compatibility reasons, but strongly discouraged.

<pre>
http://user:password@localhost/service.php/<your_service_endpoint>
</pre>

Note that anyone can easily sniff the password if the transport layer is not encrypted. If you're opening up your API for remote access, you should strongly consider enabling TLS in your web server.

=== JSON pretty printing ===

Per default the API returns a JSON-encoded string without any indentation or line breaks which makes it difficult to read. You can append 

<code><pre>
?pretty=1
</pre></code>

to every request to have CollectiveAccess return the data in a more readable format. You shouldn't do this if you're processing the data programmatically because without the "pretty printing" the response will arrive faster and will be smaller.

=== Language / Locale ===

The results are returned in en_US by default. If you would like your results in a different locale add the <code>lang</code> parameter:

<code><pre>
?lang=en_AU
</pre></code>

=== Request body in non-POST HTTP requests ===

Almost all of the service endoints and methods below support adding additional parameters as JSON in the HTTP request body. While adding this request body to GET, PUT or OPTIONS requests is not strictly speaking valid HTTP 1.1 a lot of libraries and tools in various languages and environments support this notion, most famously curl.

''(From v1.5)'' If your toolchain doesn't, you can pass the request body JSON (everything in the -d argument of curl in the examples below) as GET parameter '''source''' instead. In that case, you're going to have to URL-encode the content though.

== Searching ==

A simple search interface is available through the following service endpoint:

<pre>
http://localhost/service.php/find/<table_name>?q=<your_query>
</pre>

Possible values for table_name are: "ca_objects", "ca_object_lots", "ca_entities", "ca_places", "ca_occurrences", "ca_collections", "ca_lists", "ca_list_items", "ca_object_representations", "ca_storage_locations", "ca_movements", "ca_loans", "ca_tours", "ca_tour_stops". If you don't know what those are, the [[API:Accessing_Data]] article should be a good read to get started.

The service takes the URL-encoded query string as "q" parameter and returns a simple JSON-encoded result list. Please refer to the [[Search_Syntax]] article to learn how to build queries. A simple example query that returns all objects could look like this:

<pre>
$ curl -XGET 'http://localhost/service.php/find/ca_objects?q=*&pretty=1'
</pre>

By default only the primary key, the record's idno and a label for display are included in the result list, for example:

<pre>
{
  "ok":true,
  "results":[
    {
      "object_id":1,
      "idno":"ABC-123",
      "display_label":"My new test object"
    }
  ]
}
</pre>

If you want the service to return additional data for each search hit, you can specify what should be added and in which format in the request body. The key "bundles" of the JSON you send should be a list of simple objects, keyed by the specifier of the bundle you want to get. The object is a hash of options (option-name-value pairs) for the bundle. Both the bundle specifiers and the available options are described in detail in section "Bundle specifiers" of the [[API:Accessing_Data#Bundle_specifiers]] article. An example request could look like this:

<pre>
$ curl -XGET 'http://localhost/service.php/find/ca_objects?q=*&pretty=1' -d '{
	"bundles" : {
		"access" : { "convertCodesToDisplayText" : true },
		"status" : { "convertCodesToDisplayText" : true },
		"ca_entities.entity_id" : {"returnAsArray" : true }
	}
}'
</pre>

Which would result in something like the following response:

<pre>
{
  "ok":true,
  "results":[
    {
      "object_id":1,
      "idno":"ABC-123",
      "display_label":"My new test object",
      "access":"not accessible to public",
      "status":"new",
      "ca_entities.entity_id":[
        "2",
        "1"
      ]
    }
  ]
}
</pre>

=== Sorting ===

Sorting is available through the GET parameter sort. You can list a single field or a semi-colon separated list of fields to sort the results. For example:

<pre>
curl -XGET 'http://administrator:password@localhost/service.php/find/ca_entities?pretty=1&q=*&sort=ca_entity_labels.surname;ca_entity_labels.forename'
</pre>

== Browsing ==

The following endpoint exposes our BrowseEngine through to the service API:

<pre>
http://localhost/service.php/browse/<table_name>
</pre>

Possible values for table_name are: "ca_objects", "ca_object_lots", "ca_entities", "ca_places", "ca_occurrences", "ca_collections", "ca_lists", "ca_list_items", "ca_object_representations", "ca_storage_locations", "ca_movements", "ca_loans", "ca_tours", "ca_tour_stops".

If Since REST services are by definition stateless, we have to pass the state of the browse, which basically consists of the criteria that have already been set, to each call. The endpoint supports two types of calls. The first one is a simple OPTIONS call to the endpoint and returns info about the currently available facets and their contents (i.e. the terms you can use to restrict the result set):

<pre>
curl -XOPTIONS 'http://localhost/service.php/browse/ca_objects?pretty=1'
</pre>

The second one returns the actual results for the set criteria. But before we get to that, we have to learn how to pass existing criteria (our browse state) to both services. The above call should return something like this:

<pre>
  ...
  "type_facet":{
    "type":"fieldList",
    "field":"type_id",
    "group_mode":"none",
    "order_by_label_fields":[
      "name_plural"
    ],
    "label_singular":"type",
    "label_plural":"types",
    "content":{
      "24":{
        "id":"24",
        "label":"Boxes"
      },
      "21":{
        "id":"21",
        "label":"Collections"
      }
    }
  },
  ...
</pre>

This tells us that there is a facet "type_facet" which allows us to browse object on their types and which we can restrict on either "Boxes" (ID 24) or "Collections" (ID 21). To restrict it do ID 21, we would pass on the following in the request body:

<pre>
"criteria" : {
    "type_facet" : [21]
},
</pre>

Note that the actual value is a list, which means we can restrict facets on multiple values. This is actually useless in type facets because each object can only have one type and the criteria must all be matched, but we just want to demonstrate the syntax for now:

<pre>
"criteria" : {
    "type_facet" : [21,24]
},
</pre>

We also note multiple criteria in typical JSON fashion:

<pre>
"criteria" : {
    "type_facet" : [21],
    "status_facet" : [4],
    "access_facet" : [1]
},
</pre>

To put this all together, here's an example call to the facet returning part of the service:

<pre>
curl -XOPTIONS 'http://localhost/service.php/browse/ca_objects?pretty=1' -d '{
    "criteria" : {
        "type_facet" : [21],
        "status_facet" : [4],
        "access_facet" : [1]
    }
}'
</pre>

The second part of the service (the one that returns the results) is called by sending GET requests to the same endpoint. Existing criteria are passed as described above. Note that returning results on a browse without criteria is not supported and will result in an error, so you will have to add at least one criterion. Here is an example using the same criteria as above.

<pre>
curl -XGET 'http://localhost/service.php/browse/ca_objects?pretty=1' -d '{
    "criteria" : {
        "type_facet" : [21],
        "status_facet" : [4],
        "access_facet" : [1]
    }
}'
</pre>

Similar to the simple search service we introduced in the last section, this part of the service returns only the primary key, an idno and a display label by default, like so:

<pre>
{
  "ok":true,
  "results":[
    {
      "object_id":"153",
      "idno":"123",
      "display_label":"Some object label"
    },
    ....
}
</pre>

If you want more information on the results, you can get it by adding a "bundles" definition. For more information, please refer to the section on searching. Here's an example that makes use of this feature:

<pre>
curl -XGET 'http://localhost/service.php/browse/ca_objects?pretty=1' -d '{
    "criteria" : {
        "type_facet" : [21],
        "status_facet" : [4],
        "access_facet" : [1]
    },
    "bundles" : {
        "access" : { "convertCodesToDisplayText" : true },
        "status" : { "convertCodesToDisplayText" : true },
        "ca_entities.entity_id" : {"returnAsArray" : true }
    }
}'
</pre>

== Getting item-level data ==

The generic endpoint for requesting item-level record data is

<code><pre>
http://localhost/service.php/item/<table_name>/id/<record_id>
</pre></code>
<p>
The two parameters you have to fill in are the table_name and the primary key identifier of the record. Possible values for table_name are: "ca_objects", "ca_object_lots", "ca_entities", "ca_places", "ca_occurrences", "ca_collections", "ca_lists", "ca_list_items", "ca_object_representations", "ca_storage_locations", "ca_movements", "ca_loans", "ca_tours", "ca_tour_stops". If you don't know what those are, the [[API:Accessing_Data]] article should be a good read to get started. Note that instead of using the primary key identifier you can use a record's idno for the "id" parameter. This is not recommended because technically two records could have the same idno but there might be cases where this simplifies things significantly.
</p>
<p>
You have two possibilities of querying this service: The first one is a simple GET request to the service endpoint. In this case you get a generic summary of the record data. The other variant is meant for advanced users and allows you to specify exactly what data you want and in what format it should be returned.
</p>
<p>
Also, this service endpoint has another unique parameter called "include_deleted". If set to a non-zero value, data is returned for "softly deleted" items (which have only been marked as inactive in the database but weren't really deleted) as well. This can be useful if you want to restore accidentally deleted records. Example usage:
<pre>
$ curl -XGET 'http://localhost/service.php/item/ca_entities/id/287?include_deleted=1&pretty=1'
</pre>
</p>

=== Getting a generic summary ===

If you're sending a simple HTTP GET request to the service endpoint described above, you will get a generic summary where we try to provide all necessary data for the most common tasks. The complexity of the return format can be attributed to the potential complexity of CollectiveAccess metadata (multilingual, nested containers and the like). The request

<pre>
$ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1'
</pre>

should return the summary for the object with object_id 1. If that ID doesn't exist in your installation, try an existing one. You can see the object_id of a record in the URL displayed by the browser while you're navigating the object editor for an existing record.

<div class="toccolours mw-collapsible mw-collapsed">An example response can be seen by clicking the "Expand" button to the right.
<div class="mw-collapsible-content"><github gist="3851618"/></div>
</div>

In CollectiveAccess 1.4 or later it is also possible to get a summary in a format that is closer to what the 'item' service endpoint expects for adding and editing items (see the "Creating new records" section below). To do this, add a GET parameter named 'format' to your request and set it to 'edit', like this:

<pre>
$ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1&format=edit'
</pre>

The response is not quite as verbose as the more generic one above, but it can be used to add a similar record to the database as-is:

<pre>
$ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1&format=edit' > new.json
// modify object if necessary in new.json
$ curl -XPUT http://localhost/service.php/item/ca_objects -d @new.json
</pre>

It's also a great starting point to edit an existing object:

<pre>
$ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1&format=edit' > edit.json
// edit object in edit.json
$ curl -XPUT http://localhost/service.php/item/ca_objects/id/1 -d @new.json
</pre>

For more information on the add and edit part of the service, refer to the corresponding sections in this article.

=== Building advanced requests ===

If you know what you're doing and if the generic summary doesn't include some detail or isn't formatted as you need it, you can specify exactly what should be returned by the service and in what format by adding a JSON-encoded body to your HTTP request. The key "bundles" of the json you send should be a list of simple objects, keyed by the specifier of the bundle you want to get. The object is a hash of options (option-name-value pairs) for the bundle. Both the bundle specifiers and the available options are described in detail in section "Bundle specifiers" of the [[API:Accessing_Data#Bundle_specifiers]] article. An example request could look like this:

<pre>
$ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1' -d '{
    "bundles" : {
        "ca_objects.access" : {
            "convertCodesToDisplayText" : true
        },
        "ca_objects.preferred_labels.name" : {
            "delimiter" : "; "
        },
        "ca_entities.entity_id" : {
            "returnAsArray" : true
        }
    }
}'
</pre>

The response is a json_encoded array of the return values of the underlying CA API, in the above case it looks like this:

<pre>
{
  "ok":true,
  "ca_objects.access":"not accessible to public",
  "ca_objects.preferred_labels.name":"My new test object",
  "ca_entities.entity_id":[
    "1",
    "2"
  ]
}
</pre>

== Getting model information ==

The service endpoint for getting model information like available types, available metadata elements and relationship types is 

<pre>
http://localhost/service.php/model/<table_name>
</pre>

Possible values for table_name are: "ca_objects", "ca_object_lots", "ca_entities", "ca_places", "ca_occurrences", "ca_collections", "ca_lists", "ca_list_items", "ca_object_representations", "ca_storage_locations", "ca_movements", "ca_loans", "ca_tours", "ca_tour_stops". An example request could look like this:

<pre>
$ curl -XGET 'http://localhost/service.php/model/ca_entities?pretty=1'
</pre>

If you query the service without additional request body, it will return a generic, JSON-encoded summary about the table in question, including all available types, metadata elements and relationship types. The service also allows restricting the response to a list of predefined types. Let's assume you want to get info for a single entity type with the idno "ind" (as in "individual"). You'd build that request like this:

<pre>
$ curl -XGET 'http://localhost/service.php/model/ca_entities?pretty=1' -d '{
    "types" : ["ind"]
}'
</pre>

<div class="toccolours mw-collapsible mw-collapsed">A fairly big example response for two entity types is available if you use the "Expand" button to the right.
<div class="mw-collapsible-content"><github gist="3855079"/></div>
</div>

== Creating new records ==

New records are created using the same service endpoint you know from the "Getting data" section, except this time we use HTTP PUT requests with the actual record data encoded in the request body. So for instance if you were to create brand new entity, you'd send a request like this:
<code><pre>
$ curl -XPUT http://localhost/service.php/item/ca_entities -d '{<your_record_data_here}'
</pre></code>
To get started, let's review a complete request ...
<div class="toccolours mw-collapsible mw-collapsed">This is a simple example for creating a new entity with some basic data in each category. View by clicking "Expand" on the right.
<div class="mw-collapsible-content"><github gist="3871797"/></div>
</div>
You can clone the GitHub gist above to your local filesystem to have a great starting point:
<pre>
$ git clone git://gist.github.com/3871797.git item_request
$ cd item_request/
// edit item_request.json to fit your datamodel!
$ curl -XPUT http://localhost/service.php/item/ca_entities -d @item_request.json
// now view the new record
$ curl -XGET http://localhost/service.php/item/ca_entities/id/<insert_new_id_here>?pretty=1 | less
</pre>

You can also export an existing record using the 'edit' format and use this as starting point:

<pre>
$ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1&format=edit' > new.json 
// edit new.json
$ curl -XPUT http://localhost/service.php/item/ca_objects -d @new.json
// now view the new record
$ curl -XGET http://localhost/service.php/item/ca_objects/id/<insert_new_id_here>?pretty=1 | less
</pre>

You'll note that the request body has a section for each part that defines a CollectiveAccess record: intrinsic fields, labels, metadata attributes and relationships. If you have no idea what any of this means, the [[Installation_Profile_Syntax]] guide might be a good read to get you started on the CollectiveAccess basics. The table below describes each block and how it should be formatted.

{|border="1" cellpadding="5" cellspacing="0"
||'''Block key'''||'''Description'''
|-
||intrinsic_fields||Simple list of key-value pairs. The key is the field name. If a mandatory field is missing or if a field value is invalid, you will get an appropriate error message.
|-
||preferred_labels||List of JSON objects each describing one preferred label. Note that there can only be one preferred label per locale. The "locale" key is mandatory and should contain the locale code used for this label. The other keys depend on the label fields of the table you want to insert the record in. ca_object_labels for instance only has a single "name" field while ca_entity_labels has "forename","middlename","surname","displayname" and more. 
|-
||nonpreferred_labels||Same as preferred_labels except that multiple labels per locale are allowed. Also, there is an optional "type_id" parameter that can be used to specify the type of the label.
|-
||attributes|| A list of key => list of values mappings. Depending on your configuration, elements can be repeatable and therefore take multiple values. Key is the element_code of the element you want to use to create the attributes. Each of the values can have a "locale" value (depending on the element configuration it might be mandatory). Furthermore, each pair in a single value definition consists the element_code of an element in the current set (the key) and the corresponding value. If the top element is not nested (i.e. a "Container"), there is only one element in the set (see the "notes" element in the example gist). If there are multiple elements in the set (i.e. the top element is a Container), it doesn't matter how deeply nested the structure of the element, it's all a flat namespace - which means all sub-elements can be set in a simple list as can be seen in the GitHub gist example (element "address").
|-
||related||A list of relationship instances, grouped by name of the related table. For each instance, the primary key of the related record and the type_id (which refers to the relationship type used for this relationship instance) are mandatory. "effective_date" and "source_info" are optional keys.
|}

== Editing records ==

Editing existing records is possible by sending a PUT HTTP request to the "item" service endpoint. If you haven't done so yet, read the above section about creating new records as the request body format is very similar and therefore not explained down to the last detail here. Here is how you send a request for editing:

<code><pre>
$ curl -XPUT http://localhost/service.php/item/<table_name>/id/<record_id> -d '{<your_record_data_here}'
</pre></code>

<div class="toccolours mw-collapsible mw-collapsed">This is a simple example for editing an existing entity, showcasing a couple of the new options (in comparison with the "new record" service). View by clicking "Expand" on the right.
<div class="mw-collapsible-content"><github gist="3917836"/></div>
</div>

Note that the sections "intrinsic_fields", "preferred_labels", "nonpreferred_labels", "attributes" and "related" are identical to the "creating a new record" part of the service API. For intrinsic fields, we simply overwrite existing values with the new ones set in the request body. As for the other sections, you can simply add information to the existing record using what you already know from the "new record" part of the service. To make most common editing operations possible we then added a couple of "remove" operations to get rid of old values. The table below lists and explains them.

{|border="1" cellpadding="5" cellspacing="0"
||'''Block key'''||'''Description'''
|-
||remove_attributes||List of attribute codes of values to remove from the current record
|-
||remove_all_attributes||Set to "true" (as boolean) to remove all attributes from the current record
|-
||remove_all_labels||Set to "true" (as boolean) to remove all labels from the current record
|-
||remove_relationships||List of related tables where relationships with the current record should be removed.
|-
||remove_all_relationships||Set to "true" (as boolean) to remove all relationships from the current record
|}

== Deleting records ==

You can delete records by simply sending a DELETE HTTP request to the "item" service endpoint you already know. Note that it is assumed you know what you're doing and there will not be a another warning or confirm question before the record is removed. The request

<pre>
$ curl -XDELETE 'http://localhost/service.php/item/ca_entities/id/1
</pre>

deletes the entity with entity_id 1. Note that most record types in CollectiveAccess support what we call "soft delete" where a record is simply marked as "deleted" in the database and then doesn't show up anywhere in the user interface or public frontends anymore but is never completely lost. This is the default mode. The service also supports two options that allow you to override the default behavior. 

{|border="1" cellpadding="5" cellspacing="0"
||'''Option key'''||'''Description'''
|-
||hard||Set to "true" (as JSON boolean value, not as string) if you want to use a "real" as opposed to the aforementioned "soft delete".
|-
||delete_related||Set to "true" (as JSON boolean value, not as string) if you want to delete related records as well. '''Use with caution and only if you know what you're doing!'''
|}

Here's an example that uses one of them:

<pre>
$ curl -XDELETE 'http://localhost/service.php/item/ca_entities/id/287?pretty=1' -d '{ "hard" : true }'
</pre>

== External libraries ==

Any third-party libraries for this API can go here.

=== PHP ===

[https://github.com/skeidel/ca-service-wrapper ca-service-wrapper]

=== Ruby ===

[https://github.com/CollectiveAccessProject/collectiveaccess collectiveaccess RubyGem]
