Mappings
========

.. contents::
   :local:

Introduction
------------

An import mapping is a spreadsheet that defines how data is imported into CollectiveAccess. A basic introduction to writing and running an import mapping is provided in our :doc:`tutorial`. This page provides a detailed look at the available settings and options available through the import mapping. It is organized by column (again, see the tutorial for a simpler breakdown of the available columns), with a description of the function of each column along with the available settings for that column.

Import Mappings operate under two basic assumption about your data:
1. That each row in a data set corresponds to a single record
2. That each column corresponds to a single metadata element.

.. note::

   This is not universal. In general most mappings will follow the one row one record principle, but they can support an option called treatAsIdentifiersForMultipleRows that will explode a single row into multiple records. This is very useful if, say, you're doing a merge_on_idno (more on that below) and you have a data source that references common metadata shared by many pre-existing records in a single row.

Settings
--------

The overall settings, including the name, the format of the input data and other import settings are defined here. This section can be placed at the top or bottom of a mapping spreadsheet with the setting in the first column and the provided parameter in the second. It functions separately from the main, column defined, body of the import mapping.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../_static/csv/mappingsettings.csv

Rules
-----

Each row in the mapping must have a rule defined that determins how the importer will treat the record. Available rules are:

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../_static/csv/importerrules.csv

Source
------

The Source column is used to set precisely which element from the data source is to be mapped or skipped. You can also set a constant data value, rather than a mapping, by setting the rule type to "Constant" and the Source column as the value or list item idno from your CollectiveAccess configuration.

Supported import formats are:

Currently: XLSX, XLS, MYSQL, Filemaker XML, Inmagic XML, PastPerfect XML, Vernon XML, TEI XML, PBCore XML, RDF, ULAN-linked data, MARC, MARCXML, Omeka, EXIF, CollectiveAccess (for migrations from one system to another), WorldCat, TabDelimited, and CSVDelimited.

Planned imminently: OAI-PMH/DC

A full description of the supported import formats and how they may be referenced is available in the :doc:`formats` page.

CA_table.element
----------------

This column declares the destination where the data identified in the Source column will be mapped to in CollectiveAccess. If you are setting the Source to Skip, of course, you do not need to complete this step. If you are mapping data or applying a constant value, you do need to set the destination. This is accomplished by writing the ca_table.element_code.

CA Table corresponds to the CollectiveAccess basic tables, while element_code is simply the unique code you assigned to a particular metadata element in your CA configuration.

For example, to map a Title column from your source data into CollectiveAccess, you may wish to set the CA table.element as:

``ca_objects.preferred_labels``

This would map the data from your Source declaration to the Title field in an Object record in CollectiveAccess.

Group
-----

In many cases, distinct lines in a data set will map into their corresponding metadata elements that happen to be bundled together inside of a single container. For example, a common container is Date, wherein there are actually two metadata elements - one for the date itself, and the other a drop-down menu to declare the date's type (Date Created, Date Accessioned, etc.)

Let's say in your source data there is one column that contains date values, while the next column over contains the date types.

If the corresponding metadata elements in CA are bundled into a container, you must tell this to the mapping document by placing these Source elements into a group. Otherwise, the date value would be mapped to one container, while the date type would be mapped to another container (and each would be missing their counterpart!)

Declaring a Group is simple. Just assign a name to each line that is to be mapped into a single container.

If Source "2" is mapping to ca_objects_date.date_value, and Source "3" is mapping to ca_objects_date.date_type, then simply give each line the group name "Date." This will tell the mapping that these two lines are going to a single container - and won't create a whole new container for each.

Refineries
----------

Frequently the data being imported into CollectiveAccess does not exactly match the fields available, or some data should have a relationship to one or more other records in CollectiveAccess. Refineries manage this complexity by providing tools that can **Split**, **Make**, **Join**, **Get** and **Build** the data, transforming it according to a provided set of rules. These roles these tools play are:

Splitters
^^^^^^^^^

Splitter refineries can either create records or match data to existing records (following a mapping’s existingRecordPolicy) or break a single string of source data into several metadata elements in CollectiveAccess. Splitters for relationships are used when several parameters are required, such as setting a record type and setting a relationship type. Using the entitySplitter, a name in a single location (i.e. column) in a data source can be parsed (into first, middle, last, prefix, suffix, et al.) within the new record. Similarly the measurementSplitter breaks up, for example, a list of dimensions into to a CollectiveAccess container of sub-elements. “Splitter” also implies that multiple data elements, delimited in a single location, can be “split” into unique records related to the imported record.

===============================  =================================================================================================================================================================================================
Splitter                         Refinery Options
===============================  =================================================================================================================================================================================================
collectionSplitter               :term:`attributes <attributes>`, :term:`collectionType <collectionType>`, :term:`collectionTypeDefault <collectionTypeDefault>`, :term:`delimiter <delimiter>`, :term:`dontCreate <dontCreate>`, :term:`ignoreParent <ignoreParent>`
entitySplitter                   :term:`attributes <attributes>`, :term:`delimiter <delimiter>`, :term:`displayNameFormat <displayNameFormat>`, :term:`dontCreate <dontCreate>`, :term:`entityType <entityType>`, :term:`entityTypeDefault <entityTypeDefault>`, :term:`ignoreParent <ignoreParent>`
listItemSplitter                 :term:`attributes <attributes>`, :term:`delimiter <delimiter>`, :term:`dontCreate <dontCreate>`, :term:`ignoreParent <ignoreParent>`
loanSplitter                     :term:`attributes <attributes>`, :term:`delimiter <delimiter>`, :term:`dontCreate <dontCreate>`, :term:`ignoreParent <ignoreParent>`
measurementsSplitter             :term:`attributes <attributes>`, :term:`delimiter <delimiter>`, :term:`elements <elements>`
movementSplitter                 :term:`attributes <attributes>`, :term:`dontCreate <dontCreate>`, :term:`ignoreParent <ignoreParent>`
placeSplitter                    :term:`attributes <attributes>`, :term:`dontCreate <dontCreate>`, :term:`ignoreParent <ignoreParent>`
objectSplitter                   :term:`attributes <attributes>`, :term:`dontCreate <dontCreate>`, :term:`ignoreParent <ignoreParent>`
objectLotsSplitter               :term:`attributes <attributes>`, :term:`dontCreate <dontCreate>`, :term:`ignoreParent <ignoreParent>`
occurrenceSplitter               :term:`attributes <attributes>`, :term:`dontCreate <dontCreate>`, :term:`ignoreParent <ignoreParent>`
tourStopSplitter                 :term:`attributes <attributes>`, :term:`dontCreate <dontCreate>`, :term:`ignoreParent <ignoreParent>`
===============================  =================================================================================================================================================================================================

.. glossary::

   attributes
      Sets or maps metadata for the entity record by referencing the metadataElement code and the location in the data source where the data values can be found

      See below for additonal ``attribute`` settings for the entitySplitter and objectRepresentationSplitter

      **Example**

      .. code-block:: none

         {"attributes": {
            "address": {
               "address1": "^24",
               "address2": "^25",
               "city": "^26",
               "stateprovince": "^27",
               "postalcode": "^28",
               "country": "^29"
            }
         }
		 }

      **entitySplitter Additional Properties**

      To map source data to idnos in an entitySplitter, see the 'attributes' parameter above. An exception exists for when idnos are set to be auto-generated. To create auto-generated idnos within an entitySplitter, use the following syntax.

      ``"attributes": {"idno":"%"}``

      **objectRepresentationSplitter Additional Properties**

      Sets the attributes for the object representation. "Media" sets the source of the media filename in the data, which is what will match on the actual media file in the import directory. Note: filenames in source data may or may not the include file extension, but source data must match filename exactly. Set the media filename to idno, using "idno". Additional attributes, such as the example, "internal_notes", can also be set here.

      .. code-block:: none

         {"attributes":{
            "media": "^1",
            "internal_notes": "^2",
            "idno": "^1"
         }
         }

      *Applicable refineries*: collectionSplitter, entitySplitter, listItemSplitter, loanSplitter, measurementsSplitter, movementSplitter, placeSplitter, objectSplitter, objectLotsSplitter, occurrenceSplitter, tourStopSplitter

   collectionType
      Accepts a constant list item idno from the list collection_types or a reference to the location in the data source where the type can be found

      ``{"collectionType": "box"}``

      *Applicable Refineries*: collectionSplitter

   collectionTypeDefault
      Sets the default collection type that will be used if none are defined or if the data source values do not match any values in the CollectiveAccess list collection_types

      ``{"collectionTypeDefault":"series"}``

      *Applicable Refineries*: collectionSplitter

   delimiter
      Sets the value of the delimiter to break on, separating data source values

      ``{"delimiter": ";"}``

      *Applicable Refineries*: collection Splitter, entitySplitter, listItemSplitter, loanSplitter, measurementsSplitter, movementSplitter, placeSplitter, objectSplitter, objectLotSplitter, objectRepresentationSplitter, occurrenceSplitter, tourStopSplitter

   displayNameFormat
      Allows you to format the output of the displayName. Options are: “surnameCommaForename” (forces display name to be surname, forename); “forenameCommaSurname” (forces display name to be forename, surname); “forenameSurname” (forces display name to be forename surname); “original” (is the same as leaving it blank; you just get display name set to the imported text). This option also supports an arbitrary format by using the sub-element codes in a template, i.e. “^surname, ^forename ^middlename”. Doesn't support full format templating with <unit> and <ifdef> tags, though.

      ``{"displaynameFormat": "surnameCommaForename"}``

   	  *Applicable Refineries*: entitySplitter

   dontCreate
      If set to true (or any non-zero value) the splitter will only do matching and will not create new records when matches are not found.

      ``{"dontCreate": "1"}``

      *Applicable Refineries*: collectionSplitter, entitySplitter, listItemSplitter, loanSplitter, movementSplitter, objectLotsSplitter, objectRepresentationSplitter, objectSplitter, occurrenceSplitter, placeSplitter, tourStopSplitter

   elements
      Maps the components of the dimensions to specific metadata elements

      .. code-block:: none

         {"elements": [
            {
               "quantityElement": "measurementWidth",
               "typeElement": "measurementsType",
               "type": "width"
            },
            {
               "quantityElement": "measurementHeight",
               "typeElement": "measurementsType2",
               "type": "height"
            }
         ]}

      Note: the typeElement and type sub-components are optional and should only be used in measurement containers that include a type drop-down.

      *Applicable Refineries*: measurementsSplitter

   entityType
      Accepts a constant list item idno from the list entity_types or a reference to the location in the data source where the type can be found

      ``{"entityType": "person"}``

      *Applicable Refineries*: entitySplitter

   entityTypeDefault
      Sets the default entity type that will be used if none are defined or if the data source values do not match any values in the CollectiveAccess list entity_types

      ``{"entityTypeDefault":"individual"}``

      *Applicable Refineries:* entitySplitter

   ignoreParent
      For use with collection hierarchies. When set to true this parameter allows global match across the entire hierarchy, regardless of parent_id. Use this parameter with datasets that include values to be merged into existing hierarchies but that do not include parent information. Paired with matchOn it's possible to merge the values using only name or idno, without any need for hierarchy info. Not ideal for situations where multiple matches can not be disambiguated with the information available.

      ``{"ignoreParent": "1"}``

      *Applicable Refineries*: collectionSplitter, entitySplitter, listItemSplitter, loanSplitter, movementSplitter, objectLotsSplitter, objectSplitter, occurrenceSplitter, placeSplitter, tourStopSplitter

   interstitial
      Sets or maps metadata for the interstitial movementRelationship record by referencing the metadataElement code and the location in the data source where the data values can be found.

      .. code-block:: none

         {
            "interstitial": {
               "relationshipDate": "^4"
            }
         }

      *Applicable Refineries*: collectionSplitter, entitySplitter, listItemSplitter, loanSplitter, movementSplitter, objectLotsSplitter, objectSplitter, occurrenceSplitter, placeSplitter, tourStopSplitter

   list
      Enter the list_code for the list that the item should be added to. This is mandatory - if you forget to set it or set it to a list_code that doesn't exist the mapping will fail.)

      ``{"list": "list_code"}``

      *Applicable Refineries*: listItemSplitter

   listItemType
      Accepts a constant list item idno from the list or a reference to the location in the data source where the type can be found.

      ``{"listItemType": "concept"}``

      *Applicable Refineries*: listItemSplitter

   listItemTypeDefault
      Sets the default list item type that will be used if none are defined or if the data source values do not match any values in the CollectiveAccess list list_item_types

      ``{"listItemTypeDefault":"concept"}``

      *Applicable Refineries*: listItemSplitter

   loanType
      Accepts a constant list item from the list loan_types

      ``{"loanType":"out"}``

      *Applicable Refineries*: loanSplitter

   loanTypeDefault
      Sets the default loan type that will be used if none are defined or if the data source values do not match any values in the CollectiveAccess list loan_types.

      ``{"loanTypeDefault":"in"}``

      *Applicable Refineries*: loanSplitter

   matchOn
      From version 1.5. Defines exactly how the splitter will establish matches with pre-existing records. You can set the splitter to match on idno, or labels. You can also include both labels and idno in the matchOn parameter, and it will try multiple matches in the order specified.

      "``{""matchOn"": [""labels"", ""idno""]}`` -Will try to match on labels first, then idno.

``{""matchOn"": [""idno"", ""labels""]}`` - Will do the opposite, first idno and then labels.

You can also limit matching by doing one or the other. Eg:
{""matchOn"": ""idno""]} will only match on idno.

{""matchOn"": [""^ca_collections.your_custom_code""]} will match on a custom metadata element in the collection record. Use the syntax ^ca_collections.metadataElement code."
