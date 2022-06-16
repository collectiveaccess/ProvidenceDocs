Web Service API
===============

Collective Access provides a REST API (Representational State Transfer Application Programming Interface). Short of very few HTTP GET parameters, both the request parameters and the responses are encoded in JSON. 

.. note:: Most of the query examples described below assume that curl is installed. 

.. note:: For an introduction to development in CollectiveAccess, please see API:Accessing_Data. 

Global parameters
-----------------

Authentication
^^^^^^^^^^^^^^

Access to the whole service API or to certain parts of the CollectiveAccess data may be restricted to specific users, user groups, or user roles. This web service API respects those restrictions where possible. 

Available from CollectiveAccess Version 1.5, the API has a special service endpoint for authentication that will generate a temporary token used for subsequent calls. Login using HTTP Basic authentication, which can be done via HTTP header or directly in the URL. Most HTTP request libraries contain built-in support for HTTP basic authentication.
For testing by hand in a web browser, use the following pattern:

.. code-block::

   http://user:password@localhost/service.php/auth/login

Calling this service via GET will result in a JSON response that includes a 256bit authentication token (if the username/password combination is valid). It should look something like this:
   
.. code-block::

   {"ok":true, "authToken":"c55ccee391f972097267a4afd8da4eb6d32da0acd3311f41ea0806142169b7ca"}

Use that token to quickly authenticate all subsequent requests against the API, using the "authToken" GET parameter: 

.. code-block::

   http://localhost/service.php/item/ca_objects/id/1?authToken=c55ccee391f972097267a4afd8da4eb6d32da0acd3311f41ea0806142169b7ca

.. warning:: The token will expire within a few hours, resulting in a 401 Access Denied HTTP response. Simply re-authenticate using the auth/login service.

.. note.. Pre v1.5 you're going to have to add HTTP Basic authentication to every API call. This is still supported in v1.5 for compatibility reasons, but strongly discouraged.
http://user:password@localhost/service.php/<your_service_endpoint>
Note that anyone can easily sniff the password if the transport layer is not encrypted. If you're opening up your API for remote access, you should strongly consider enabling TLS in your web server.

JSON Pretty Printing
^^^^^^^^^^^^^^^^^^^^

Per default the API returns a JSON-encoded string without any indentation or line breaks which makes it difficult to read. To make it easy to read, simply add ?pretty=1 to every request. CollectiveAccess will then return the data in a more readable format. If processing the data programmatically, do not use this string, because without ?pretty=1, the response will arrive faster, and will be smaller.

Language / Locale
^^^^^^^^^^^^^^^^^

The results are returned in en_US by default. To generate results in a different locale, add the language parameter:

.. code-block::
   
   ?lang=en_AU

Where en_AU refers to the locale and the country (standardized, global language codes). 

Request Body in Non-POST HTTP Requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Almost all of the service endpoints and methods below support adding additional parameters as JSON in the HTTP request body. While adding this request body to GET, PUT or OPTIONS requests is not, strictly speaking, valid HTTP 1.1, many libraries and tools in various languages and environments support this notion. 

.. note:: (From v1.5) If your toolchain doesn't, you can pass the request body JSON (everything in the -d argument of curl in the examples below) as GET parameter source instead. In that case, you're going to have to URL-encode the content though.

Searching
---------

A simple search interface is available through the following service endpoint:

.. code-block:: 
   
   http://localhost/service.php/find/<table_name>?q=<your_query>

Possible values for table_name are: 

* ca_objects 
* ca_object_lots
* ca_entities 
* ca_places
* ca_occurrences
* ca_collections
* ca_lists 
* ca_list_items 
* ca_object_representations 
* ca_storage_locations 
* ca_movements 
* ca_loans 
* ca_tours 
* ca_tour_stops

The service takes the URL-encoded query string as "q" parameter and returns a simple JSON-encoded result list. Please refer to the Search_Syntax article to learn how to build queries. A simple example query that returns all objects could look like this:

.. code-block::

   $ curl -XGET 'http://localhost/service.php/find/ca_objects?q=*&pretty=1'

By default, only the primary key, the record's idno and a label for display are included in the result list, for example:

.. code-block::

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

To return additional data for each search hit, specify what should be added, and in which format, in the request body. The key "bundles" of the JSON you send should be a list of simple objects, keyed by the specifier of the bundle you want to get. The object is a hash of options (option-name-value pairs) for the bundle. Both the bundle specifiers and the available options are described in detail in section "Bundle specifiers" of the API:Accessing_Data#Bundle_specifiers. An example request could look like this:

.. code-block::

   $ curl -XGET 'http://localhost/service.php/find/ca_objects?q=*&pretty=1' -d '{
	"bundles" : {
		"access" : { "convertCodesToDisplayText" : true },
		"status" : { "convertCodesToDisplayText" : true },
		"ca_entities.entity_id" : {"returnAsArray" : true }
	}
   }'

Which would result in something like the following response:

.. code-block::

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

Sorting
^^^^^^^

Sorting is available through the GET parameter sort. List a single field or a semi-colon separated list of fields to sort the results. For example:

.. code-block::

   curl -XGET 'http://administrator:password@localhost/service.php/find/ca_entities?pretty=1&q=*&sort=ca_entity_labels.surname;ca_entity_labels.forename'

Browsing
--------

The following endpoint exposes our BrowseEngine through to the service API:

.. code-block::
   
    http://localhost/service.php/browse/<table_name>

Possible values for table_name are: "ca_objects", "ca_object_lots", "ca_entities", "ca_places", "ca_occurrences", "ca_collections", "ca_lists", "ca_list_items", "ca_object_representations", "ca_storage_locations", "ca_movements", "ca_loans", "ca_tours", "ca_tour_stops".

Since REST services are by definition stateless, we have to pass the state of the browse, which basically consists of the criteria that have already been set, to each call. The endpoint supports two types of calls: 

1. A simple OPTIONS call to the endpoint. This returns information about the currently available facets and their contents (i.e. the terms you can use to restrict the result set):

.. code-block::

   curl -XOPTIONS 'http://localhost/service.php/browse/ca_objects?pretty=1'

2. Returns the actual results for the set criteria. But before we get to that, we have to learn how to pass existing criteria (our browse state) to both services. The above call should return something like this:

.. code-block:: 

    ...  "type_facet":{
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

There is a facet "type_facet," which enables browsing objects on their types, and which can restrict on either "Boxes" (ID 24) or "Collections" (ID 21). To restrict it do ID 21, pass on the following in the request body:

.. code-block::

   "criteria" : {
    "type_facet" : [21]
   },

Note that the actual value is a list, meaning facets can be restricted on multiple values. This is actually useless in type facets because each object can only have one type and the criteria must all be matched, but we just want to demonstrate the syntax for now:

.. code-block::

   "criteria" : {
    "type_facet" : [21,24]
   },

We also note multiple criteria in typical JSON fashion:

.. code-block::

   "criteria" : {
    "type_facet" : [21],
    "status_facet" : [4],
    "access_facet" : [1]
   },

To put this all together, here's an example call to the facet returning part of the service:

.. code-block::
 
   curl -XOPTIONS 'http://localhost/service.php/browse/ca_objects?pretty=1' -d '{
    "criteria" : {
        "type_facet" : [21],
        "status_facet" : [4],
        "access_facet" : [1]
    }
   }'

The second part of the service (the one that returns the results) is called by sending GET requests to the same endpoint. Existing criteria are passed as described above. Note that returning results on a browse without criteria is not supported and will result in an error. Add at least one criterion. Here is an example using the same criteria as above: 

.. code-block::

   curl -XGET 'http://localhost/service.php/browse/ca_objects?pretty=1' -d '{
    "criteria" : {
        "type_facet" : [21],
        "status_facet" : [4],
        "access_facet" : [1]
    }
   }'

Similar to the simple search service, this part of the service returns only the primary key, an idno, and a display label by default, like so:

.. code-block:: 

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

For more information on the results, add a "bundles" definition. Here's an example that makes use of this feature:

.. code-block::

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

Getting Item-Level Data
-----------------------

The generic endpoint for requesting item-level record data is: 

.. code-block::

   http://localhost/service.php/item/<table_name>/id/<record_id>

The two parameters to fill in are the table_name and the primary key identifier of the record. 

There are two possibilities to query this service: The first one is a simple GET request to the service endpoint. In this case, a generic summary of the record data will be retrieved. The other variant is meant for advanced users, and specifies exactly what data and in what format it should be returned.

This service endpoint has another unique parameter called "include_deleted". If set to a non-zero value, data is returned for "softly deleted" items (which have only been marked as inactive in the database but weren't really deleted) as well. This can be useful to restore accidentally deleted records. Example usage:

.. code-block:: 

   $ curl -XGET 'http://localhost/service.php/item/ca_entities/id/287?include_deleted=1&pretty=1'

Getting a Generic Summary
-------------------------

Sending a simple HTTP GET request to the service endpoint described above will generate a generic summary. The complexity of the return format can be attributed to the potential complexity of CollectiveAccess metadata (multilingual, nested containers, and the like). The request: 

.. code-block::

   $ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1'

should return the summary for the object with object_id 1. The object_id of a record in the URL is displayed by the browser while navigating in the object editor for an existing record.

[Expand]An example response can be seen by clicking the "Expand" button to the right.

As of CollectiveAccess Version 1.4, it is possible to get a summary in a format that is closer to what the 'item' service endpoint expects for adding and editing items (see the "Creating new records" section below). To do this, add a GET parameter named 'format' to your request and set it to 'edit', like this:

.. code-block::

   $ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1&format=edit'

The response is not quite as verbose as the more generic one above, but it can be used to add a similar record to the database as-is:

.. code-block::

   $ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1&format=edit' > new.json
   // modify object if necessary in new.json
   $ curl -XPUT http://localhost/service.php/item/ca_objects -d @new.json

It's also a great starting point to edit an existing object:

.. code-block::

   $ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1&format=edit' > edit.json
   // edit object in edit.json
   $ curl -XPUT http://localhost/service.php/item/ca_objects/id/1 -d @new.json

Building Advanced Requests
--------------------------

It is possible to specify exactly what should be returned by the service, and in what format, by adding a JSON-encoded body to a HTTP request. The key "bundles" of the JSON should be a list of simple objects, keyed by the specifier of the bundle. The object is a hash of options (option-name-value pairs) for the bundle. Both the bundle specifiers, and the available options, are described in detail in section "Bundle specifiers" 

An example request could look like this:

.. code-block::

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

The response is a json_encoded array of the return values of the underlying CA API, in the above case it looks like this:

.. code-block::

   {
  "ok":true,
  "ca_objects.access":"not accessible to public",
  "ca_objects.preferred_labels.name":"My new test object",
  "ca_entities.entity_id":[
    "1",
    "2"
  ]
   }

Getting Model Information
-------------------------

The service endpoint for getting model information like available types, available metadata elements, and relationship types is: 

.. code-block::

   http://localhost/service.php/model/<table_name>

Possible values for table_name are: 

* ca_objects
* ca_object_lots
* ca_entities 
* ca_places
* ca_occurrences
* ca_collections
* ca_lists
* ca_list_items
* ca_object_representations
* ca_storage_locations
* ca_movements
* ca_loans 
* ca_tours
* ca_tour_stops

An example request could look like this:

.. code-block:: 

   $ curl -XGET 'http://localhost/service.php/model/ca_entities?pretty=1'

Querying the service without an additional request body will return a generic, JSON-encoded summary about the table in question, including all available types, metadata elements, and relationship types. The service also allows restricting the response to a list of predefined types. 

To get information for a single entity type with the idno "ind" (as in "individual"), the following request would look like: 

.. code-block::

   $ curl -XGET 'http://localhost/service.php/model/ca_entities?pretty=1' -d '{
    "types" : ["ind"]
   }'

A fairly big example response for two entity types is available if you use the "Expand" button to the right.

Creating New Records
--------------------

New records are created using the same service endpoint from the "Getting Data" section. Use HTTP PUT requests with the actual record data encoded in the request body. To create brand new entity, send the following request:

.. code-block::

   $ curl -XPUT http://localhost/service.php/item/ca_entities -d '{<your_record_data_here}'

A Complete Request
------------------
 
This is a simple example for creating a new entity with some basic data in each category. View by clicking "Expand" on the right.

Clone the GitHub gist above to the local filesystem to have a great starting point:

.. code-block::

   $ git clone git://gist.github.com/3871797.git item_request
   $ cd item_request/
   // edit item_request.json to fit your datamodel!
   $ curl -XPUT http://localhost/service.php/item/ca_entities -d @item_request.json
   // now view the new record
   $ curl -XGET http://localhost/service.php/item/ca_entities/id/<insert_new_id_here>?pretty=1 | less

Export an existing record using the 'edit' format and use this as starting point:

.. code-block::

   $ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1&format=edit' > new.json 
   // edit new.json

   $ curl -XPUT http://localhost/service.php/item/ca_objects -d @new.json
   // now view the new record

   $ curl -XGET http://localhost/service.php/item/ca_objects/id/<insert_new_id_here>?pretty=1 | less

The request body has a section for each part that defines a CollectiveAccess record: intrinsic fields, labels, metadata attributes and relationships. For more, see Installation Profiles. 

The table below describes each block key, and how it should be formatted.

.. csv-table::
   :header-rows: 1
   :file: web_service_api_table1.csv

Editing Records
---------------

Editing existing records is possible by sending a PUT HTTP request to the "item" service endpoint. To send a request for editing:

.. code-block::

   $ curl -XPUT http://localhost/service.php/item/<table_name>/id/<record_id> -d '{<your_record_data_here}'

This is a simple example for editing an existing entity, showcasing a couple of the new options (in comparison with the "new record" service). View by clicking "Expand" on the right.

Note that the sections "intrinsic_fields", "preferred_labels", "nonpreferred_labels", "attributes" and "related" are identical to the "creating a new record" part of the service API. For intrinsic fields, simply overwrite existing values with the new ones set in the request body. As for the other sections, add information to the existing record using information from the "new record" part of the service. To make most common editing operations possible, add a couple of "remove" operations to get rid of old values.

The table below lists block keys for editing and removing operations. 

.. csv-table::
   :header-rows: 1
   :file: web_service_api_table1.csv

Deleting Records
----------------

To delete records, send a DELETE HTTP request to the "item" service endpoint. The request:

.. code-block::

   $ curl -XDELETE 'http://localhost/service.php/item/ca_entities/id/1

deletes the entity with entity_id 1. Most record types in CollectiveAccess support a "soft delete" where a record is simply marked as "deleted" in the database; it doesn't show up anywhere in the user interface or public frontends, but is never completely lost. This is the default mode. 

The service also supports two options that allow you to override this default behavior.

.. csv-table::
   :header-rows: 1
   :file: web_service_api_table2.csv

Here's an example that uses one of them:

.. code-block::

   $ curl -XDELETE 'http://localhost/service.php/item/ca_entities/id/287?pretty=1' -d '{ "hard" : true }'


External Libraries
------------------
Any third-party libraries for this API can go here.

PHP
---
ca-service-wrapper

Ruby
----
collectiveaccess RubyGem


