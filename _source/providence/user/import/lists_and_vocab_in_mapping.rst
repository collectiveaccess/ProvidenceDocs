Using Lists and Vocabularies in an Import Mapping Spreadsheet
=============================================================

Lists and Vocabularies are important in determining a number of aspects about a data import. The Lists and Vocabularies in a CollectiveAccess system are often incorporated into an import mapping spreadsheet to define types of relationships, entities, dimensions, and other aspects that can help inform how best to structure the import mapping spreadsheet.

To view the Lists and Vocabularies in a given CollectiveAccess system, navigate to **Manage > Lists and Vocabularies**. The Lists and Vocabularies hierarchy will be displayed: 

.. image:: lists_mapping_1.png
   :scale: 50%
   :align: center


Scrolling through the hierarchy, the various terms used in the system will be displayed. By selecting the **>** icon to the right of each heading, the list of relevant terms is displayed:  

.. image:: lists_mapping_2.png
   :align: center
   :scale: 50%

Below the hierarchy is a key for the icons used within the hierarchy. These classify each list and vocabulary, and include:

* **Default**: The default setting if no other type is defined in the import mapping. Indicated by |dot|. 

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

Using Lists and Vocabularies in a Mapping
-----------------------------------------

Defining Entity Types
^^^^^^^^^^^^^^^^^^^^^

A common example where Lists and Vocabularies should be used while making an import mapping spreadsheet is for defining Entity Types. 

For source data that contains people or organizations, and will create records and relationships for that source data, it is necessary to look at the Entity Types listed in Lists and Vocabularies to include the correct entityType in the Refinery Parameter column of the import mapping spreadsheet. 

For example, here are the Refinery and Refinery Parameters columns from the Sample Import Mapping Spreadsheet (:download:`Sample Import Mapping Spreadsheet <sample_mapping_tutorial.xlsx>`).

.. image:: lists_mapping_7.png
   :scale: 50% 
   :align: center

Note that the **entitySplitter** refinery references both a **relationship type** and an **entity type.** Both of these types come from Lists and Vocabularies in the Collective Access system. 

Finding Entity Types
^^^^^^^^^^^^^^^^^^^^

To define the **entityType** (**"ind"**), navigate to **Manage > Lists and Vocabularies.** Scroll down to **Entity Types**. 

.. image:: lists_mapping_8.png
   :scale: 50%
   :align: center

Two available options are listed for Entity Types defined in the system: Individuals (ind) (defualt) and Organization (org). The entity being mapped is an individual (see above, **"ind"**). Note that instead of including **"individual"** in the Refinery Parameter, the shorter code is used, **ind**, to indicate the EntityType. 

To define the **relationshipType**, see below.  

Defining Object Lot Types
^^^^^^^^^^^^^^^^^^^^^^^^^





Defining Relationship Types
---------------------------

The concept behind defining relationship types in an import mapping is the same as defining other types (outlined above) in an import mapping. However, finding the list of relationship types for a given system is slightly different. 

Navigate to **Manage > Administration > Relationship Types.** 