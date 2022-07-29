Displaying Units
================

* `Repeating Containers`_ 
* `Relative to Relationships: relativeTo`_ 
* `Hierarchical Relationships`_ 
* `Indirect Relationships`_ 
* `Restricted Indirect Relationships`_ 
* `Sorting`_ 
* `Skipping Units`_ 

More  here

Repeating Containers
--------------------

The **<unit>** tag allows users to organize and display metadata for hierarchically related records. To include a repeating container in a display, use the **<unit>** tag. Without **<unit>** tags, a repeating address container would look like this:

.. code-block::

   Address Line 1 A; Address Line 1 B
   Address Line 2 A; Address Line 2 B
   Address Line 3 A; Address Line 3 B

With **<unit>** tags, it should look like this:

.. code-block::

   Address Line 1 A
   Address Line 2 A
   Address Line 3 A
   Address Line 1 B
   Address Line 2 B
   Address Line 3 B

To achieve the ideal layout, a **<unit>** tag is used to define the format of each discrete block, which then repeats as many times as the container does.

To pull this example address into a "Related entities" bundle ( so as to display the address with the entity name), the display template would look like this:

.. code-block::

   <unit relativeTo="ca_entities">
   <unit><l>^ca_entities.preferred_labels</l><br/><br/></unit>
   <unit relativeTo="ca_entities.address" delimiter=", ">
   ^ca_entities.address.address1<ifdef code="ca_entities.address.address2">, </ifdef>
   ^ca_entities.address.address2<ifdef code="ca_entities.address.city">, </ifdef>
   ^ca_entities.address.city<ifdef code="ca_entities.address.stateprovince">, </ifdef>
   ^ca_entities.address.stateprovince<ifdef code="ca_entities.address.postalcode">, </ifdef>
   ^ca_entities.address.postalcode<ifdef code="ca_entities.address.country">, </ifdef>
   ^ca_entities.address.country</unit>
   </unit>

In the above code the unit delimiter *(,)* is used between instances of the full address container. The ifdef code is used between lines of the individual container placement. This ensures that if no data has been catalogued, a string of empty spaces and commas will not be imported.

Relative to Relationships: relativeTo
-------------------------------------

The **<unit>** tag also supports a "relativeTo" setting which is used to shift the frame of reference of a display to a specified target. This is vital for interstitial record displays, hierarchical displays, and indirect relationships, all of which are supported by CollectiveAccess. 

Hierarchical Relationships
--------------------------

CollectiveAccess supports the formatting of Hierarchical relationships. An example of these might be in a Collections table, wherein one parent collection houses smaller child collections. To display these relationships, the **<unit>** tag is needed. 

Without the **<unit>** tag, only the preferred label of each child would be displayed; delimiters such as line breaks could not be specified. With the **<unit>** tag, however, the child records can be broken up into discrete pieces. Additional metadata about each can also be included. To display child records along with their idnos:

.. code-block::

   <unit relativeTo="ca_collections.children">^ca_collections.preferred_labels, ^ca_collections.idno</unit>

In which "relativeTo" specifies the table in question, and asks the display to find child records. Once the "relativeTo" frame has been set, however, drop the ".children" and simply reference the collections table, wherein the child records live. 

To display the immediate parent of the record at hand, format it as:

.. code-block::

   <unit relativeTo="ca_collections.parent">

To display all parents, format the template with respect to the entire hierarchy:

.. code-block::

    <unit relativeTo="ca_collections.hierarchy">

If you are dealing with multiple records, either as children or as "hierarchy," enclose the entire template within a <unit>, so that each record's metadata can be displayed in an organized manner. For example:

.. code-block::

   <unit><unit relativeTo="ca_collections.children" delimiter="</br>">^ca_collections.preferred_labels, ^ca_collections.idno</unit></unit> 

would display records like this:

.. code-block:: 

   Mini Collection X, 100.1
   Mini Collection Y, 100.2

instead of this:

.. code-block::

   Mini Collection X, Mini Collection Y, 100.1, 100.2

Nest additional layers of <unit> tags within the syntax discussed above by following the directions in the following section.

Indirect Relationships
----------------------

The **<unit>** tag also allows cataloguers to display metadata with some relative distance to the chosen record. 
In a Collection summary where Entities aren't related directly to Collections, but instead are related to specific objects related to that collection, it is possible to display information about that indirect relationship. 

The display template that is used on the object bundle (through the GUI) or object placement (in a profile) is given below. It pulls statement metadata from a container on each Entity record related to each Object:

.. code-block::

   <unit relativeTo="ca_objects">

   <unit><em><strong>^ca_objects.preferred_labels</strong></em><br></unit>

   <unit relativeTo="ca_entities" delimiter=", ">^ca_entities.preferred_labels</unit><br>

   <unit relativeTo="ca_entities.statement" delimiter="<br/><br/>">

   ^ca_entities.statement.statement_text<br/>

   ^ca_entities.statement.statement_date<br/>

   ^ca_entities.statement.statement_source</unit>

   </unit><br/><br/>

The result is a list of artwork titles, artist names, and their statements for the works in the collection. Note that in the Falling Water example entity John Smith has two repeats of the statements container:

Restricted Indirect Relationships
---------------------------------

Indirect relationships can be restricted further by including restrictToTypes and/or restrictToRelationshipTypes. 
For example, to restrict the relationship included in the display to just "individual" entities linked as "artist," use the following:

.. code-block::

   <unit relativeTo="ca_objects">

   <unit><em><strong>^ca_objects.preferred_labels</strong></em><br></unit>

   <unit relativeTo="ca_entities" delimiter=", " restrictToRelationshipTypes="artist" restrictToTypes="ind">

   ^ca_entities.preferred_labels</unit><br/><br/>

Sorting
-------

The order in which units are output can be sorted by adding sort and optionally, sortDirection, to the unit. Outputs can be sorted but also arranged within that output in ascending or descending order. 

To sort output by the name of a the related object do something like this:

.. code-block::

   <unit relativeTo="ca_objects" sort="ca_objects.preferred_labels.name" sortDirection="ASC">

   <unit><em><strong>^ca_objects.preferred_labels</strong></em><br></unit>

   <unit relativeTo="ca_entities" delimiter=", " restrictToRelationshipTypes="artist" restrictToTypes="ind">

   ^ca_entities.preferred_labels</unit><br/><br/>

Where the notations for the sort order are ASC or DESC (ascending order or descending order). The default sorting is set to ascending. Sort on more than one bundle value by listing each bundle value in sequence separated by semicolons.

Skipping Units
--------------

As of CollectiveAccess Version 1.5, records selected by unit tags can be skipped using the skipIfExpression attribute. It takes an [[Expressions] Expression] as a parameter. Note that the skipIfExpression attribute is evaluated on record level. 

Below is a simple example that would skip all entities where the idno had the sequence "test" in it: 

.. code-block::

   <unit relativeTo="ca_entities" delimiter=" / " skipIfExpression="^ca_entities.idno =~ /test/">

   ^ca_entities.preferred_labels 
   </unit>
