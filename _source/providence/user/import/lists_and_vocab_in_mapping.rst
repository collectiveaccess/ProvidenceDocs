.. _import_lists_and_vocab_in_mapping:

Using Lists and Vocabularies in an Import Mapping Spreadsheet
=============================================================

Lists and Vocabularies are important in determining a number of aspects about a data import. The Lists and Vocabularies in a CollectiveAccess system are often incorporated into an import mapping spreadsheet to define types of relationships, entities, dimensions, and other aspects that can help inform how best to structure the import mapping spreadsheet. 

Lists and Vocabulaies in an import mapping define what types of relationships will be created upon import, what kind of entity records will be created upon import, and other key aspects to performing a successful data import. 

For other uses of Lists and Vocabularies in CollectiveAccess, see `Lists and Vocabularies <file:///Users/charlotteposever/Documents/ca_manual/providence/user/editing/lists_and_vocab.html>`_. 

How to find Lists and Vocabularies in CollectiveAccess
------------------------------------------------------

To view the Lists and Vocabularies in a given CollectiveAccess system, navigate to **Manage > Lists and Vocabularies**. The Lists and Vocabularies hierarchy will be displayed: 

.. image:: lists_mapping_1.png
   :scale: 50%
   :align: center

Scrolling through the hierarchy, the various terms used in the system will be displayed. By selecting the **>** icon to the right of each heading, the list of relevant terms is displayed:  

.. image:: lists_mapping_2.png
   :align: center
   :scale: 50%

Below the hierarchy is a key for the icons used within the hierarchy. These classify each list and vocabulary, and include:

* **Default**: The default setting upon import if no other type is defined in the import mapping. Indicated by |dot|. 

.. |dot| image:: lists_mapping_3.png
         :scale: 50%

* **Disabled**: The list/vocabulary/term is disabled, and is not used. Indicated by |x|. 

.. |x| image:: lists_mapping_4.png
       :scale: 50%

* **Vocabulary list**: The list/vocabulary/term is used as a controlled vocabulary for cataloging. Indicated by |triangle|.

.. |triangle| image:: lists_mapping_5.png 
              :scale: 50%

* **System list**: The list/vocabulary/term is used by the system to populate a specific field; these are defined by the system installer. Indicated by |cross|.

.. |cross| image:: lists_mapping_6.png
           :scale: 50%

How are Lists and Vocabularies used in an Import Mapping?
---------------------------------------------------------

Lists and Vocabularies are used to define the types of relationships, entities, lot types, and other aspects of a mapping that incorporate related records of various types. These types are specified in the import mapping spreadsheet in the Refinery Parameters column. 

Here is an example taken from the Sample Import Mapping Spreadsheet (:download:`Sample Import Mapping Spreadsheet <sample_mapping_tutorial.xlsx>`). To the left is the Refinery Column, and to the right is the Refinery Parameters column, with code.

.. image:: lists_entitySplitter.png
   :scale: 50%
   :align: center

Highlighted in red are the relationship type and entity type for the entitySplitter. These are defined in quotes as parts of the Parameter for each Refinery (see `Refineries and Refinery Parameters <file:///Users/charlotteposever/Documents/ca_manual/providence/user/import/mappings/refineries.html?highlight=refineries>`_ for more). These types can be found in Lists and Vocabularies. 

When the types taken from Lists and Vocabularies, as well as Relationship Types (explained below), are put into the mapping, CollectiveAccess will know to create those specific types of relationships and records. Read on for a few examples of how to find the types and relationships needed in an import mapping spreadsheet. 

Finding Entity Types
--------------------

For source data that contains people or organizations like the Sample above, it is necessary to look at the Entity Types listed in Lists and Vocabularies to include the correct entityType in the Refinery Parameter column of the import mapping spreadsheet. In the example above, the entityType (in red) is **"ind"** and the relationshipType is **"creator"**. 

To find these types, and to determine which type to include in an import mapping spreadsheet: 

1. Navigate to **Manage > Lists and Vocabularies.** The hierarchy will be displayed.
2. Scroll down in the hierarchy to **Entity Types**. 

.. image:: lists_entityTypes.png
   :scale: 50%
   :align: center

3. Select the arrow icon **>** to open the terms list. 
4. Select which type best describes the entity records being created. Note that the full type is not used in an import mapping; instead, the code in parentheses next to it is used. 

Two available options are listed for Entity Types defined in the system for the example above: Individuals (ind) (marked as the default) and Organization (org). The entity being mapped is an individual (see above, **"ind"**). Note that instead of including **"individual"** in the Refinery Parameter, the shorter code is used, **ind**, to indicate the EntityType. 

Finding Relationship Types
--------------------------

Finding the relationship types that exist within a given CollectiveAccess system is similar to finding other types. However, relationship types are located in a different part of the system.

Navigate to **Manage > Administration > Relationship Types.** The Relationship Type hierarchy will be displayed: 

.. image:: lists_relationship_hierarchy.png
   :scale: 50%
   :align: center

Similarly to selecting types of entities, selecting the > will display the various types of relationships included in the CollectiveAccess system (thus, types displayed will vary). 

When selecting the correct relationship type, it is important to consider two things: 

1. What kind of Refinery is used in the import mapping spreadsheet?
2. What is the relationship between the records created through the Refinery, and the import table set in the import Settings?

For the example above, an **entitySplitter** is used. In the Sample Import Mapping spreadsheet, the table is set to **ca_objects.** Therefore, the relationship being created is **object-entity**. This relationship can be found and selected by scrolling through the hierarchy: 

.. image:: lists_relationship_object.png
   :scale: 50%
   :align: center

Where a large list of descriptors is available to choose from. Select the best word to describe the relationship benign created in the mapping. In the example above, that is **"creator"**. Note that the word in parentheses is the one to be used in the import mapping refinery parameter. 

To find other relationship types for various kinds of relationships defined in a mapping, follow these same steps. 

Finding Object Lot Types 
------------------------

Another common example where Lists and Vocabularies should be used while making an import mapping spreadsheet is for defining Object Lot Types. An example of this is seen in the Sample Import Mapping Spreadsheet. 

.. image:: lists_lotSplitter.png
   :scale: 50%
   :align: center

Note that the **objectLotSplitter** refinery references an **object lot type**. This type comes from Lists and Vocabularies in the Collective Access system. 

Where an **objectLotSplitter** is used to create Lot records from the source data. Note that the **objectLotSplitter** refinery references an **object lot type**, outlined in red, as well as an **object lot status type**, outlined in red, in the Refinery Parameters column. 

To find these types, and to determine which type to include in an import mapping spreadsheet: 

1. Navigate to **Manage > Lists and Vocabularies.** The hierarchy will be displayed.
2. Scroll down in the hierarchy to **Object Lot Types**. 

.. image:: lists_mapping_9.png
   :scale: 50%
   :align: center

3. Select the arrow icon **>** to open the terms list. 
4. Select which type best describes the lot records being created. Note that the full type is not used in an import mapping; instead, the code in parentheses next to it is used. 

Two available options are listed for Object Lot Types defined in the system for the example above: Accessions and Gifts. The lots being mapped are gifts. 

To find the object lot status type, which is also part of the same Refinery Parameter:

1. Navigate to **Manage > Lists and Vocabularies.** The hierarchy will be displayed.
2. Scroll down in the hierarchy to **Object Lot Statuses**. 

.. image:: lists_statuses.png
   :scale: 50%
   :align: center

3. Select the arrow icon **>** to open the terms list. 
4. Select which type best describes the lot records being created. Note that the full type is not used in an import mapping; instead, the code in parentheses next to it is used. 

Four available options are listed for Object Lot Statuses Types defined in the system for the example above: Accessioned, Non-Accessioned, Pending Accession, and Potential Acquisitions. The lots being mapped are Accessioned. 

Checking the Correct Term is Used
---------------------------------

To ensure the right type is being used in a mapping, it is sometimes necessary to select the type itself from the List. When the list item is selected, the list item viewer for that item or term will be displayed: 

.. image:: lists_list_item_view.png
   :scale: 50%
   :align: center

To check that the term is the correct one to use in the mapping, scroll down to the **Identifier** field, which displays the unique identifier used for this list item throughout the CollectiveAccess system. 

.. image:: lists_unique_id.png
   :scale: 50%
   :align: center

In this example, the list item as displayed in the list and as displayed in the Identifier field match, so **accessioned** is the correct term to use in the import mapping spreadsheet. 

However, it is important to ensure these terms match; if not, there will be errors upon import relating to the different types used and defined in the import mapping spreadsheet. This applies to all types. 
