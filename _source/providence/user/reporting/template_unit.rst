.. _template_unit:

Unit templates
=======================

.. contents::
   :local:

Repeating containers
---------------------

To include a repeating container in a display you must use the ``<unit>`` tag. Without ``<unit>`` tags a repeating address container would look like this:

.. code-block:: text

    Address Line 1 A; Address Line 1 B
    Address Line 2 A; Address Line 2 B
    Address Line 3 A; Address Line 3 B

Although of course we'd like it to look like this:

.. code-block:: text

    Address Line 1 A
    Address Line 2 A
    Address Line 3 A
    Address Line 1 B
    Address Line 2 B
    Address Line 3 B

To achieve the ideal layout above a ``<unit>`` tag is used to define the format of each discrete block, which then repeats as many times as the container does.

Let's say you're pulling this address into a "Related entities" bundle, so as to display the address with the entity name. The display template would look like this:

.. code-block:: xml

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

In the above code the unit delimiter (``,``) is used between instances of the full address container. The ``<ifdef>`` code is used between lines of the individual container placement. It ensures that if no data has been catalogued you won't get a string of empty spaces and commas.

Relative to relationships
--------------------------
The ``<unit>`` tag also supports a ``relativeTo`` setting which is used to shift the frame of reference of a display to a specified target. This is vital for interstitial record displays, hierarchical displays and indirect relationships (see below).

Hierarchical relationships
--------------------------

The ``<unit>`` tag allows users to organize and display metadata for hierarchically related records. For example, you might have a hierarchy within the Collections table, wherein one parent collection houses smaller child collections. Without the ``<unit>`` tag, you would only be able to display the preferred label of each child, and you wouldn't be able to specify delimiters such as line breaks. With the ``<unit>`` tag, however, you can break the child records up into discrete chunks, and you can include additional metadata about each. If you want to display child records along with their idno's, for example, you could do this:

.. code-block:: xml

    <unit relativeTo="ca_collections.children">^ca_collections.preferred_labels,
       ^ca_collections.idno</unit>

In which ``relativeTo`` specifies the table in question and asks the display to find child records. Once the ``relativeTo`` frame has been set, however, you can drop the ``.children`` and simply reference the collections table, wherein the child records live. If you were to continue including ``children``, (i.e. ``ca_collections.children.preferred_labels``) you would essentially be looking for child records within child records. To use this template in the opposite direction, to display the immediate parent of the record at hand, you would simply format it as ``<unit relativeTo="ca_collections.parent">``. To display all parents, you can format the template with respect to the entire hierarchy: ``<unit relativeTo="ca_collections.hierarchy">``. If you are dealing with multiple records, either as ``children`` or as ``hierarchy``, you'll want to enclose the entire template within a ``<unit>``, so that each record's metadata can be displayed in an organized manner. For example,

.. code-block:: xml

    <unit>
      <unit relativeTo="ca_collections.children" delimiter="</br>">^ca_collections.preferred_labels,
         ^ca_collections.idno
      </unit>
    </unit>

would display records like this:

.. code-block:: text

    Mini Collection X, 100.1
    Mini Collection Y, 100.2

instead of this:

.. code-block:: text

    Mini Collection X, Mini Collection Y, 100.1, 100.2

You can also nest additional layers of ``<unit>`` tags within the syntax discussed above by following the directions in the following section.

Indirect relationships
----------------------

One use of the ``<unit>`` tag is to allow cataloguers to display metadata with some relative distance to the chosen record. 

Let's say you're creating a Collection summary and you'd like to display metadata about Entities, but Entities aren't related directly to Collections. Perhaps they are related to Objects related to the Collection. Entities are also 2 degrees away from Collections thanks to their relativity to Objects.

How does this look in practice? Here's a display template that is used on the object bundle (through the GUI) or object placement (in a profile). It pulls statement metadata from a container on each Entity record related to each Object.

.. code-block:: xml

    <unit relativeTo="ca_objects">
    <unit><em><strong>^ca_objects.preferred_labels</strong></em><br></unit>
    <unit relativeTo="ca_entities" delimiter=", ">^ca_entities.preferred_labels</unit><br>
    <unit relativeTo="ca_entities.statement" delimiter="<br/><br/>">
    ^ca_entities.statement.statement_text<br/>
    ^ca_entities.statement.statement_date<br/>
    ^ca_entities.statement.statement_source</unit>
    </unit><br/><br/>

The result is a list of artwork titles, artist names and their statements for the works in the collection. Note that in the Falling Water example entity John Smith has two repeats of the statements container:

.. image:: RelativityDisplay.png
   :scale: 50%
   :align: center

Restricted indirect relationships
----------------------------------

You can further restrict indirect relationships by including ``restrictToTypes`` and/or ``restrictToRelationshipTypes``. For example to restrict the relationship included in the display to just ``individual`` entities linked as ``artist`` you'd use the following:

.. code-block:: xml

    <unit relativeTo="ca_objects">
    <unit><em><strong>^ca_objects.preferred_labels</strong></em><br></unit>
    <unit relativeTo="ca_entities" delimiter=", "
         restrictToRelationshipTypes="artist" restrictToTypes="ind">
            ^ca_entities.preferred_labels</unit>
    <br/><br/>

Sorting
-------

You may sort the order in which units are output by adding sort and optionally sortDirection to the unit. For example to sort output by the name of a the related object do something like this:

.. code-block:: xml

   <unit relativeTo="ca_objects" sort="ca_objects.preferred_labels.name" sortDirection="ASC">
   <unit><em><strong>^ca_objects.preferred_labels</strong></em><br></unit>
   <unit relativeTo="ca_entities" delimiter=", "
      restrictToRelationshipTypes="artist" restrictToTypes="ind">
         ^ca_entities.preferred_labels
   </unit><br/><br/>

Notice that the sort direction is ``ASC``. Sort direction may be either ASCending or DESCending. If you omit a value, ascending is assumed. You may sort on more than one bundle value by listing each bundle value in sequence separated by semi-colons.

Skipping units
---------------

From CollectiveAccess Version 1.5, you can skip records selected by unit tags using the ``skipIfExpression`` attribute. It takes an :ref:`Expression <expressions>` as parameter. Note that the ``skipIfExpression`` attribute is evaluated on record level, so while you can use it if your ``relativeTo`` spec is a container or an attribute, it doesn't really make sense to do so. Below is a simple example that would skip all entities where the ``idno`` had the sequence ``test`` in it.

.. code-block:: xml

    <unit relativeTo="ca_entities" delimiter=" / " skipIfExpression="^ca_entities.idno =~ /test/">
        ^ca_entities.preferred_labels
    </unit>

