.. _search_syntax:

Search Syntax
=============

No matter what back-end `search engine`_ you configure CA with, the `Lucene search syntax`_ is always used to specify queries. This helps to provide a consistent experience for users across implementations and also leverages the Lucene syntax, which is well designed and widely adopted. Note that not all back-end engines support all aspects of the Lucene syntax. In general you can rely upon core functionality always being supported: text searches, field-level limiting, parenthetical grouping and booleans. Features such as boosting, fuzzy matching and range searches may not be available in all engines. 

.. _Lucene search syntax: http://lucene.apache.org/core/2_9_4/queryparsersyntax.html
.. _search engine: http://docs.collectiveaccess.org/sphinx/_build/html/searchBrowse/engines.html

Fulltext searches
-----------------

To search across all indexed fields in the database (as defined in the search_indexing.conf configuration file) simply type in a word or words. Depending upon the engine, your input may be stemmed (suffixes removed before comparison with the index) to improve results. Most engines will only return results that contain all of the words specified, but some may employ logic to return seemingly relevant partial matches.

Limiting your search to a specific field
----------------------------------------

If you wish to restrict your search to a specific field in the CA database, specify the table name and field separated by a dot, like this:

``<table>.<field> (ex. ca_object_labels.name)``

A query in the form of

``ca_object_labels.name:Rollercoasters``

would return only objects whose label (eg. its title) contains the word rollercoasters

Note that this applies only to "intrinsic" fields that are hardcoded into the CA database. That is, they are always present no matter how you have CA configured - although you may not be using them. There are only a few of this type of field in common usage: label fields (for ca_objects, ca_entities, etc.), idno identifier fields (for ca_objects, ca_entities, etc.), and the extent and extent_units fields (for ca_objects and ca_object_lots).

Limiting your search to a specific metadata elements
----------------------------------------------------

Metadata elements are data fields specific to your installation. They may or may not exist in other installations. Searching on them is similar to searching on intrinsic fields:

``<ca_table>.<element code> (for example, ca_objects.description to search within the "description" element attached to objects.)``

You can see a list of all metadata elements (and their codes) available in your configuration in the metadata element editor available under the "System Configuration" option in the "Manage" menu. (Note: only system administrators have access to this editor).

In all engines you can perform text searches on any element. In some engines - specifically the MysqlFulltext engine that is the default engine upon installation - you can also perform specialized searches on certain types of elements. These searches are described in the following section.

Limiting searches to specific relationship types
------------------------------------------------

By default, when searching on related content (Eg. search for objects using names of related entities) all relationships are considered. If you wish to limit your search to specific types of relationships append the relationship type code (or codes, separated by commas) following the field qualifier and a forward slash. For example this query:

``ca_entities.preferred_labels.displayname/depicts:"Cynthia Hopkins")``

when used to find objects will return all objects related to Cynthia Hopkins with a "depicts" relationship.


Searching on dates
------------------

To search on a date or date range, simply restrict your search to a date range element and then search on the desired date, using one of the formats described on the date and time format page. You can use any supported format and any precision - the search engine will find any date (and optionally times) that overlap your search date range. Matching is by default very loose: items with any overlap will be returned. You can restrict matching to items with dates that are completely encompassed by your search date by prepending a "#" to your search data. Eg. "#May 10 2005"

Searching on lengths and widths
-------------------------------

To search on a length or width, restrict your search to a length or width element and use the desired quantity with units specified. You must specify units - there is no default no matter what your "units of measurement" preference is set to (this preference governs display of measurements only). If you want to find items that match a measurement exactly simply search on the quantity. CA will convert the quantity to the required units for comparison, so even if an item was measured in inches, a metric search will find it - if the measurements match of course.

``ca_objects.width:12in``

You can use almost any unit abbreviation listed on the measurement input format page. A few, such as " for inches and ' for feet have special meaning in the Lucene search syntax and should not be used.

If you want to search for items within a range of measurements, specify the upper and lower bounds of the range with units. The boundary values should be separated with the word "to" and enclosed in square brackets. Do not put spaces between the quantity and units. For example:

``ca_objects.width:[12in to 24in]``

would find all objects with a width between 12 and 24 inches (inclusive). Note that there is no space between "12" and "in" and "24" and "in"

Searching on numbers
--------------------

Searching on numbers is very similar to searching on measurements, except that no units are necessary. To search on an integer or decimal value element restrict your search to the element and specify the number either singly or as a range. For example, to find objects with a user_ranking value of 5:

``ca_objects.user_ranking:5``

To find objects with user_ranking values between 1 and 5 (inclusive):

``ca_objects.user_ranking:[1 to 5]``

Searching on currency
---------------------

Searching on currency is very similar to searching on numbers, except that a currency type is required. To search on an currency value element restrict your search to the element and specify the currency amount either singly or as a range. The amount should be prefixed with a three letter currency specified (eg. EUR for Euros, USD for US dollars) or one of the supports symbolic specifiers ($, ¥, £ and €). For example, to find objects with an appraisal_value value of $500:

``ca_objects.appraisal_value:$500``

To find objects with appraisal_value values $500 or under:

``ca_objects.appraisal_value:[$0 to $500]``

Searching on geographic locations
---------------------------------

When searching on geographic locations, you have two options. You can either search within a bounding box specified by two latitude/longitude pairs or you can search for anything with a specified distance of a latitude/longitude point.

To search within a bounding box:

``ca_objects.georeference:ca_objects.georeference:"[40.341,-71.011 to 45.322, -75.963]"``

Note that the latitudes and longitudes should be decimal and separated with "to", " - " or ".."; the entire range should be enclosed in both square brackets ("[" and "]) and quotes. If you don't use quotes on the part of the query up to the first space will be parts as geographic - not what you want.

To search the area within a specified radius of a point, use this kind of search:

``ca_objects.georeference:ca_objects.georeference:"[40.5759250,-73.9911350 ~ 5km]"``

As with the bounding box query, enclose the search expression in square brackets and quotes. The maximum distance from the point can be specified in any of the units of length supported by the "Length" attribute type. The above query will find anything geocoded as being within 5 kilometers of the specified point.

Searching for blank values
--------------------------

As of version 1.4 you may search for item that have no content in a specific field using the special [BLANK] search term. [BLANK] must be used in conjunction with field specification and must be enclosed in double quotes. The following example will return all objects lacking descriptions:

``ca_objects.description:"[BLANK]"``

Access points
-------------

Typing ca_objects.description:grafitti every time you want to search for the word "grafitti" in the element "description" gets old quick, and certainly doesn't look very pretty. To simplify the specification of field and element-limited searches, CA supports the definition of "access points." Access points are simply lists of field and element specifications, defined in the search_indexing.conf configuration file, the names of which may be used in place of the actual specification. For example, you could do the 'description' search like this:

``picText:grafitti``

assuming that an access point like this was defined in search_indexing.conf:

.. code-block:: none
	
	picText = {
		fields = [ca_objects.description]
	},

Boolean combination
-------------------

Search expressions can be combined using the standard boolean "AND" and "OR" operators. Simply join together your search expressions with the words AND and OR. For example the query

``ca_objects.appraisal_value:[$0 to $500] AND ca_objects.description:broken``

will find all objects with BOTH an appraisal value of $500 or less and the word "broken" is their description. In contrast the query

``ca_objects.appraisal_value:[$0 to $500] OR ca_objects.description:broken``

will find objects with EITHER an appraisal value of $500 or less or the word "broken" in their description.

If you omit AND/OR between two search expressions, AND is assumed.

Wildcards
---------

The asterisk ("*") is used as a wildcard character. That is, it matches any text. Wildcards may only be used at the end of a word, to match words that start your search term. For example:

``wri*``

would find records associated with words starting with the text "wri" Note that if your installation has "stemming" enabled, many English language words will automatically have their suffixes truncated and a wildcard appended. Thus, with stemming on, a query for "baking" or "baked" or "baker" would be transformed to "bak*" The stemmer is smart enough to not attempt truncation of a term you've added a wildcard to yourself. If you search for "bake*" the stemmer will leave it as-is.

Searching on creation and modification dates
--------------------------------------------

You can search on the creation and modification dates of records using the special created and modified access points together with a valid date/time expression. For example, to find everything created on April 12, 2012 you can search using:

``created:"April 12 2012"``

or

``created:"4/12/2012"``

or with any other valid date/time expression. Any range will work, including ones that specify time and ones that are by month or year.

You can limit the returned items to those created or modified by a specific user by adding a valid user name after the access point. For example, to find things modified by user "catherine" on April 2012 you can search using:

``modified.catherine:"4/2012"``

Note that the user name is separated from the access point by a period ("."), and that the name of the user is their login user name, not their full name. Their login user name may be, but is not always, the user's email address.

Searching on counts
-------------------

As of version 1.7 it is possible to index the number of relationships and repeating per metadata element for search. For relationships, counts may be broken out by relationship type, related item type, or both. Count queries are useful for locating records without specific relationships (eg. find objects without entities related as artist) or with potential problems (eg. find objects with between 10 and 100 related entities).

By default count indexing is only enabled on object-entity relationships, and broken out by relationship type. You may configure indexing of other counts in the search_indexing.conf configuration file.

Relationship counts may be queried using the relationship table name followed by the special count field. For example, in an object search to find all objects related to exactly one entities search for:

``ca_objects_x_entities.count:1``

To find all objects with exactly one entity related with the relationship type "artist":

``ca_objects_x_entities.count/artist:1``

To find all objects without related "artist" entities:

``ca_objects_x_entities.count/artist:0``

To find all objects with between 2 and 10 related entities:

``ca_objects_x_entities.count:[2 to 10]``

And to find all objects with between 2 and 10 related "artist" entities:

``ca_objects_x_entities.count/artist:[2 to 10]``

Note that the the table name used in these examples is "ca_objects_x_entities" rather than "ca_entities". When ca_objects_x_entities is indexed with count in search_indexing.conf (it is by default), counts are broken out by relationship type, which is what enables the count queries on relationship type.

You may also index counts on the related record itself (in this case ca_entities), breaking out counts by record type. Assuming your system is configured with the entity types "individual" and "organization" these queries would be possible:

Find objects with related organizations:

``ca_entities.count/organization:[1 to 100000]``

Find objects with only related individuals:
<code>

``ca_entities.count/individual:[1 to 100000] and ca_entities.count/organization:0``

We use a range with an upper bound of 100000 here to ensure that we include objects with any number of entities. Expressions with < and > are not currently supported.

Similarly, the number of values present for each metadata element is indexed and may be queried. This can be useful for locating records that lack a value in a field, or have many values. For example:

To find all object records that lack at least one value in the "dimensions" field:

``ca_objects.dimensions.count:0``

To find all objects that have more than 5 values in the "dimensions" field:

``ca_objects.dimensions.count:[5 to 100000]``

As with any other search field specification, you may create more convenient aliases for commonly used counts in search_indexing.conf by creating an access point. 