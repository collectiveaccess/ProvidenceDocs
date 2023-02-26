API: Getting Data and Methods of Access
=======================================

* `Use Direct SQL Queries on the Database`_ 
* `Load a Specific Row in a Specific Table Using an Instance of the Table's Model Class`_ 
* `Load a Specific Row in a Specific Table Using an Instance of the Table's Model Class`_ 
* `Load a Set of Rows from a Specific Table Using the Search Engine`_
* `Types of Information`_
* `Bundle Specifiers`_ 
* `Intrinsic Fields`_ 
* `Labels`_ 
* `Attributes`_ 
* `Related Items`_ 
* `Transversing Hierarchical Items`_ 
* `Getting Data from Model Instances and Search Results`_ 
* `Getting Data from Direct Databse Queries using the Db Class`_

Getting data out of CollectiveAccess is one of the most commonly performed tasks when writing code. In a typical database application, executing `SQL queries <https://manual.collectiveaccess.org/providence/user/searchBrowse/searchEngines/sql.html>`_ yields results. Because it is a relational database, direct queries in Collective Access may return the same content in several languages, leaving you to figure out which is the most appropriate language to use. Therefore, there are three main methods of accessing data stored in CollectiveAccess. 

Use Direct SQL Queries on the Database
--------------------------------------

Data can always be accessed using the standard MySQL database client. Additionally, CollectiveAccess' database access library, Db, located in *app/lib/core/Db.php* can also be used. 

Performing direct queries in CollectiveAccess accesses the raw data store. Some values (dates for example), are stored in specific formats that must be parsed prior to display. Attributes (user defined, possibly repeating, fields) are stored in a generic fashion that depending upon field type may require some parsing as well. And media fields must be processed to resolve URL and server paths prior to use. 

Further, all multilingual content must be processed to extract the particular language you require. (It may seem simple to filter on language, but unless your database has full translation of all content – a rare occurrence – you must negotiate languages to find the best match given the user. This is a more complicated task.)

Load a Specific Row in a Specific Table Using an Instance of the Table's Model Class
------------------------------------------------------------------------------------

All tables in the CollectiveAccess database have corresponding model classes located in *app/models*, so they can be directly accessed. Any row in a table can be accessed by creating an instance of the model and load()ing the row, either by unique row_id, or by one or more field values.

Load a Set of Rows from a Specific Table Using the Search Engine
----------------------------------------------------------------

Use the search engine (via a table-specific subclass such as *ObjectSearch* or *PlaceSearch* (located in *app/lib/ca/Search*) to find and access rows. The engine returns the result set in a subclass of *SearchResult* (located in *app/lib/core/Search*). For example, for searches via *ObjectSearch* on the ca_objects table the result set object will be of class *ObjectSearchResult*. 

The result object will provide functionality for getting information out of the search result for display, as well as functionality specific to the type of data being search for. (For example, *ObjectSearchResult* includes special methods for getting related media for display; the other *SearchResult* sub-classes don't have these functions because they don't support related media.) 

The browse engine returns results in a similar manner, with its own classes (eg. *ObjectBrowseResult*) that inherit from the same parent and implement the same functionality as their search counterparts. In general, whatever you can do with a search result can be done with a browse result too.

Types of Information
--------------------

The four main ways CollectiveAccess stores information relating to catalogued items include:

1. **Intrinsic fields**: Standard database fields hardcoded into the database and guaranteed to exist in all installations. They do not repeat, and do not take field-level language/locale values. 
2. **Label**: Representative names or titles of catalogued items. Labels take locales/languages and are divided into two types: preferred labels and non-preferred labels. A preferred label is the one "true" title or name of an item used for display. There can only be one preferred label per item per locale. That is, if you are cataloguing in three languages you can have up to three preferred labels, one in each language. Non-preferred labels are alternative names that can be used to enhance searching or preserve identity. Non-preferred labels can repeat without limit, take locales and optionally take type values which may be employed to distinguish valid "alternate" labels from simple search enhancing non-preferred labels.
3. **Attributes**: Typically the majority of information in a CollectiveAccess database, attributes are values of various types attached to items and structured according to an installation-specific schema. The structure and meaning of attributes are defined by metadata element definitions. These definitions can be simple fields (eg. a single text value) or complex values made up of many elements assembled into a hierarchy (sometimes referred to as an "element set" or "compound attribute"; an address with separate fields for street, city, state, postal code, etc. is an example of a complex value). Whether simple or complex, each metadata element definition is bound via type restrictions to any type of item (object, entity, place, etc.) and, optionally, to specific types of item. The binding includes restrictions on how the element repeats (or not) when used with a given type of item. In short: attributes are user defined data elements that may contain many types of structured data, can be single values or collections of many values, can repeat any number of times (or not) and can be tagged with a locale (or not).
4. **Related items**: Relationships may be established between items. For example, if an object was painted by a person, then the object's record will have a relationship to the entity record for the painter. Relationships are qualified by relationship types; in the previous example the relationship would likely have a type of "artist" or perhaps "painter." The precise set of relationship types will vary from installation to installation, but the set of possible relationships will not. With a few exceptions, all primary item types (objects, object lots, entities, places, occurrences, collections, list items, storage locations, loans and movements) may be interrelated without restriction.

Bundle Specifiers
-----------------

The four types of information described above are collectively referred to as bundles. When using the CollectiveAccess API to access a bundle, a bundle specifier must be used. This is just a fancy-speak for a name. The rules for creating these names are simple. Each bundle specifier is composed of between one and four parts joined together with periods. The first part is always the table name for the item you want to pull data from. The table names for primary item types are:

.. csv-table::
   :header-rows: 1
   :file: getting_data_table1.csv

The second part is a field name (for intrinsic fields), a metadata element code (for attributes), *preferred_labels* or *nonpreferred_labels*. The third part is a sub-element code, when used with complex attributes, or a sub-field name when used with preferred or nonpreferred labels. Complex attributes and labels both have more than a single value associated with them. For example, an entity label contains fields for each piece of a name, including forename, surname, middle name, and title/prefix. The sub-element/sub-field lets you specify which value in the collection you want.

If you are dealing with an item that is part of a hierarchy, you can specify values immediately up or down the hierarchy from the item you are working with by setting the second element to either *parent* or *children*. The other elements function similarly except that they slide down to the third and fourth positions respectively.

Intrinsic Fields
---------------

The bundle specifier for an intrinsic field is simply the table name + the field name. For example, the specifier for the object identifier (aka "accession number") is *ca_objects.idno* to get the status value for an entity the specifier in *ca_entities.status*. You can get a list of fields for the various items by looking at the table definition in the database schema (located in *install/inc/schema_mysql.sql*).

Labels
------

There are two formats for preferred label specifiers. The simplest specifier is table name + *preferred_labels*, which will return the "display" value for the label. For most labels this is the name or title. For entities, which has a more complex label structure than other items, this is the displayname field.

The specifier for a specific label field is table name + *preferred_labels* + label field name. For example, if you want the surname field of the preferred entity label, you would use *ca_entities.preferred_labels.surname.*

Non preferred labels work similarly, except of course that you use *nonpreferred_labels* in place of *preferred_labels*.

Attributes
----------

To form a specifier for a simple single-value attribute, use table name + element code. For complex attributes use table name + the element code of the root (top-of-hierarchy) container + sub-element code. The namespace for element codes is flat, so no matter how deep the hierarchy you need only specify the code of the specific sub-element. You don't have to mimic the hierarchical structure.

For instance, to get the internal_notes attribute from an object, you might use *ca_objects.internal_notes*. To get the city value from an entity address, where the element code for city is *city* and the element code for the root container is *address*, you would use *ca_entities.address.city*. Naturally, the element codes depend upon how your system is configured.

Related Items
-------------

When used with the table name of the item at hand, all of the specifier formats described so far fetch values directly attached to that item. That is, if you have an object record and invoke *ca_objects.description* you will get the value of the description attribute attached to the object record. If you use other table names, CA will automatically traverse relationships and fetch values from related records in the specified table. For example, if you are working with an object record and use the specifier *ca_entities.preferred_labels.displayname* you'll fetch all of the display names of entities related to the object. Similarly, if you use *ca_places.idno* you'll obtain a list of place identifiers for places related to the object at hand.

Anything directly attached to the record at hand can also be fetched from related records by varying the table name.

If you wish to get "self relations" - entities related to an entity for example - you must use the *related* qualifier. For example, to fetch the names of entities related to an entity use the specified *ca_entities.related.preferred_labels.displayname*. If you omit the *related* in this case you'd get the name of the entity at hand rather than the related ones.

You can include the *related* qualifier in any relationship specifier but it is only required when traversing self-relations.

Traversing Hierarchical Items
-----------------------------

Many types of items can be assembled into hierarchies. Some, notably places, list items and storage locations, are almost always hierarchical. Others, including objects and collections, can be optionally assembled into hierarchies as required. You can specify values from records immediately above or below the one at hand in the hierarchy by using parent and children values as the second element of your specifier. The other elements continue to function normally when using *parent* and *children* – they just apply to records elsewhere in the hierarchy.

For example, for a given place you can fetch the name of the parent using *ca_places.parent.preferred_labels.name*. You can fetch the plural names of children of a list item *using ca_list_items.children.preferred_labels.name_plural.*

If you simply need the entire hierarchical path to the item at hand, use the "hierarchy" specifier. For example, getting *ca_places.hierarchy* will return the name of the place at hand as well as the names of some or all of its hierarchical parents, in order. By default the value returned for each item in the hierarchy is the label display field (eg. *name* for *ca_objects*, ca_places and several others; displayname for *ca_entities*), but you can also specify other label fields if required. For example *ca_objects.hierarchy.name_sort* will return the hierarchy using sortable name fields for the objects. There are several special options available when getting hierarchies:

1. **direction** determines how the hierarchy is sorted. "ASC" (the default) will return the hierarchy with root first. "DESC" will return the hierarchy with the lowest child element first.
2. **hierarchicalDelimiter** sets what characters are displayed between items in the hierarchy list, when you get the list as a string. If this is not set then the value of the delimiter option is used.
3. **top,** if set to a non-zero number, limits the returned hierarchy to the first X items root down.
4. **bottom**, if set to a non-zero number, limits the returned hierarchy to the last X items from the lowest child up.
5. **removeFirstItems**, if set to a non-zero number, will cause the removal of the specified number of items off of the hierarchy, starting with the root, before sorting or any other processing is performed.

If the returnAsArray option is set then the hierarchy is returned as an array of items. The returnAllLocales is not supported for the hierarchy specifier.

Getting Data from Model Instances and Search Results
----------------------------------------------------

In the discussion above we refer to the "item at hand." In order to actually fetch a value, all bundle specifiers need to be evaluated relative to a specific item record. It's not enough to ask to the description of an object record. We need to know which object record.
There are two ways to load a record for "getting" of data:

1. **Model instances**: every table in the CA database has a corresponding model class that when instantiated can represent a single row in that table. The model includes methods for writing data and many utility functions as well as an interface for fetching data. If you need to get data from a single row and have either the row's id or some other intrinsic value that uniquely identifies the row then a model instance is a good choice.
2. **Search engine**: use the search engine to select rows for "getting" of data if you need to get values from many rows and there is a search expression that can cleanly select the desired items.

Model instances and search result objects (as well as browse result objects) provide identical *get()* methods for getting of data. The method takes two parameters: a mandatory bundle specifier and an array of options, if required.

Examples of code using get with either class are shown below:

.. code-block:: 

   // instantiate a model 
 $t_object = new ca_objects(40);   // load ca_object record with object_id = 40
 print "The title of the object is ".$t_object->get('ca_objects.preferred_labels.name')."<br/>\n";    
   // get the preferred name of the object
 
 // do a search and print out the titles of all found objects
 $o_search = new ObjectSearch();
 $qr_results = $o_search->search("Dreamland Park");    // ... or whatever text you like
 
 $count = 1;
 while($qr_results->nextHit()) {
     print "Hit ".$count.": ".$qr_results->get('ca_objects.preferred_labels.name')."<br/>\n";
     $count++;
 }


In the examples above the values returned are text ready for display in the user's current locale. Multiple values, from repeating attributes, multiple non-preferred labels or from several related items, are concatenated into a string using a delimiter.

You can use the options array parameter of *get()* to change how values are returned. The key options are:

.. csv-table:: 
   :header-rows: 1
   :file: getting_data_table2.csv

For information on options relating to the hierarchy specifier see the Traversing hierarchical items section above.

For example, to print an array of all values in all languages of the preferred label for objects:

.. code-block:: 

     // do a search and print out the titles of all found objects
 $o_search = new ObjectSearch();
 $qr_results = $o_search->search("Sea Gate");    // ... or whatever text you like
 
 // dump preferred labels in all languages
 while($qr_results->nextHit()) {
     print_r($qr_results->get('ca_objects.preferred_labels.name', array('returnAllLocales' => true, 'returnAsArray' => true)))";
 }
 
 // dump preferred labels in just the current language
 while($qr_results->nextHit()) {
     print_r($qr_results->get('ca_objects.preferred_labels.name', array('returnAllLocales' => false, 'returnAsArray' => true)))";
 }
 
 // dump preferred labels in all languages as a simple string delimited by semicolons (";")
 while($qr_results->nextHit()) {
     print_r($qr_results->get('ca_objects.preferred_labels.name', array('returnAllLocales' => false, 'returnAsArray' => false, 'delimiter' => '; ')))";  // you could omit returnAllLocales and returnAsArray since the defaults are false
 }

When only *returnAsArray* is enabled, but not returnAllLocales, the returned array will be a simple numerically indexed list of values. The values may be complex, however, based upon the nature of the bundle being fetched. Intrinsics will be simple string or numeric values while complex attributes will be arrays with keys set to element codes and values corresponding to those codes. Repeating values will be in numerically indexed value lists.

When *returnAllLocales* is return the returned array will be multi-dimensional: the first key will be the item_id (the unique internal identifier for the item itself), the second key will be the locale_id (as defined in the ca_locales table). The value of the second key will be the value which will be either a discrete value, an array with keys set to field names and corresponding values or a numerically indexed array of values (if the bundle being fetched is repeating, such as an attribute or non-preferred label).

If this sounds complicated, that's because it is a bit. Perhaps the best way to understand the return array structures is to print_r() the returned values and study the output. However, keep in mind that the default behavior of get() is usually what you want: a text value in the current locale ready for display.

Getting Data from Direct Database Queries using the Db Class
------------------------------------------------------------

You can execute any SQL query directly on the CA MySQL database using the Db class (*app/lib/core/Db.php*). Typical code to perform a SQL SELECT statement and print out identifiers is below:

.. code-block:: 
   $o_data = new Db();
 $qr_result = $o_data->query("
    SELECT * 
    FROM ca_objects 
    WHERE idno LIKE '2008.%'
 ");
 
 while($qr_result->nextRow()) {
      print "GOT ACCESSION NUM=".$qr_result->get('idno')."<br/>\n";
 }

Note that direct queries do not use bundle specifiers. Rather simple field names – no table names or other elements – are used in the database. Only intrinsic fields or field in those tables you explicitly join in and fetch are available. All returned data will be "raw" as-stored in the database.

You should not use direct database queries (INSERT, UPDATE, DELETE) to change the database unless you know exactly what you are doing. Direct database write operations may cause search indices to go out of sync with database content or worse, cause data damage or loss.
