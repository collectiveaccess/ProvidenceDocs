Cookbook: Import
================

This section provides some real examples of common challenges that may arise during a data import in CollectiveAccess. There are many options and possibilities when creating an import mapping spreadsheet, and preparing source data for import, and the plethora of choices can lead to many questions about formatting in the import mapping spreadsheet. 

This section is not an exhaustive, step-by-step guide for every possible option when creating an import mapping spreadsheet for a data import in CollectiveAccess. However, several typical scenarios are included with solutions explaining how to achieve specific outcomes in a data import. 

Each scenario begins with a “problem,” describing a certain challenge or question that may occur during a data import, or, the creation of an import mapping spreadsheet. There is an accompanying “solution” provided for each problem, which outlines how to carry out the necessary steps to reach a specific outcome for a data import or import mapping spreadsheet. 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online Support Forum, Online Chat, Slack Channel for Developers, and Back- and Front-end GitHub Repositories. 

Contents
--------

* `Mapping Related Object Lot Records`_
* `Creating Object Lot Records in an Object Lots Table`_
* `Mapping Entities to ca_entities Table`_
* `Uploading an Import Mapping Spreadsheet via the User Interface in CollectiveAccess`_
* `Importing a Constant Value`_
* `Grouping Data Together into One Container Element`_
* `Conditionally Skipping Data`_
* `Formatting a Title`_
* `Importing a List`_
* `Importing to Yes/No Checkboxes`_
* `Foreign Key Constraint in Object Lots`_
* `Mapping Object Lot Identification Numbers`_
* `Mapping Serial Identification Numbers from multipart_id_numbering.conf`_
* `Importing Multiple Relationship Types`_
* `Creating One Entity Record from Separate Data Source Columns`_
* `Mapping Entities into a Container Field`_
* `Building a Hierarchy Above Related Records`_
* `Building a Hierarchy with Variable Amount of Levels`_
* `Importing a Hierarchy Within a Collections Table (ca_collections)`_
* `Using Rules`_
* `Including Metadata in a Refinery Parameter`_
* `Mapping Measurements from one Source to Separate Fields`_
* `Setting a Unit Specifier for Mapping Dimensions`_
* `Using a Hierarchical Delimiter for Storage Locations`_
* `Importing XML`_
* `Importing MARC`_
* `Mapping a MARC element with multiple sub-fields`_
* `Importing Indented Hierarchical List Items`_
* `Values Importing Improperly from Excel`_

Mapping Related Object Lot Records
---------------------------------- 

**Problem**: The source data (mapping to Objects Table, ca_objects) contains metadata pertaining to Object Lots (Accessions). To create separate and related Object Lot records from this metadata in an import mapping spreadsheet: 

**Solution**: In Column 3 of the import mapping spreadsheet, map the source data column to ca_objects.lot_id. In Column 6, use the Refinery ObjectLotSplitter. In Column 7 use a Refinery Parameter to specify how the Object Lot records will be displayed in CollectiveAccess. For example, a Refinery Parameter could look like: 

.. code-block::

   {
    "objectLotType": "gift",
    "attributes": {
     "idno_stub": "^9",
     "lot_status_id": "accessioned"
    }
   }

where the objectLotType is specified as a Gift, with attributes that include the Accession ID no from the source data (column 9 in this example), and the status of the Object Lot as “accessioned.” 

Creating Object Lot Records in an Object Lots Table 
---------------------------------------------------

**Problem**: You have source data that contains information about Object Lots (Accessions), and would like to map these records to the Object Lots Table in CollectiveAccess in your import mapping spreadsheet, which will create Object Lot records. 

**Solution**: Object Lots require more than just a label and a type. They also have a non-optional lot_status_id, a value taken from the "object lot statuses" list in CollectiveAccess. This must be set to a valid value or the lot will fail to insert. Set a constant value to ca_object_lots.lot_status_id. 
ID Numbers for ca_object_lots don't map to the normal idno, but rather ca_object_lots.idno_stub.

Mapping Entities to ca_entities Table 
-------------------------------------

**Problem**: You are running an import mapping with ca_entities as the target table. The source data for entity names is formatted as First Last (i.e. Jane Doe) with no delimiter separating the names. You would like to import this data as Entity records, requiring parsed first and last names. 

**Solution**: Set Column 3 in your import mapping spreadsheet to ca_entities.preferred_labels. In Column 5 of your import mapping spreadsheet, set the Refinery to entitySplitter. In column 6 of your import mapping spreadsheet, set the Refinery Parameters to {"entityType": "entity_type", "skipIfValue": ["unknown"]}. 

Uploading an Import Mapping Spreadsheet via the User Interface in CollectiveAccess
----------------------------------------------------------------------------------

**Problem**: You have finished creating your import mapping spreadsheet, and have followed the steps to successfully import through the User Interface in CollectiveAccess. However, the worksheet will not upload. 

**Solution**: You may have an improperly formatted JSON in your import mapping, which can be found in the Options Column and in the Refinery Parameters Column. Without valid code, the import mapping spreadsheet will not upload. You may have simply missed a necessary comma or bracket in your code. To quickly validate your JSON, go `here <jsonlint.com>`_.

Importing a Constant Value 
--------------------------

**Problem**: You want a list called "Language" in your CollectiveAccess system to be set as "English" for all records brought in through your data import.

**Solution**: In the Rule Type column in your import mapping spreadsheet (Column 1), for that mapping row, choose Constant. In the Source column (Column 2) set the value, English, by using the unique list code for that item (i.e. "eng"). 

Grouping Data Together into One Container Element
-------------------------------------------------

**Problem**: You want to map several fields in your source data to a single field (Container element) in CollectiveAccess. For example, your source data contains Addresses, States, and Zip Codes in separate columns, and these go into a single Address field (Container) in CollectiveAccess. 

**Solution**: In Column 3 of your import mapping spreadsheet, make sure each bundle code from the Container is input correctly; different codes exist for States, Zip Codes, Address, and so on. Then, Create an arbitrary group name, for example, “address,” and place it in the Group column (Column 4) of your import mapping spreadsheet in each row that contains these associated fields. Any row that includes this Group name will be automatically linked inside that Container element upon import. 

Conditionally Skipping Data
----------------------------

**Problem 1**: You want to prevent import of the value "n/a" in your source data, which has been input instead of data in some cells. 

**Solution 1**: Use the skipGroupIfValue Option in Column 5 of your import mapping spreadsheet. This Option will look like: {"skipGroupIfValue": ["n/a"]}. 

**Problem 2**: You want to skip a whole row of data, only if a specific value is used in a particular column.

**Solution 2**: Use the skipRowIfValue Option in Column 5 of your import mapping spreadsheet, or alternately, use the skipRowIfNotValue Option. These Options will look different, depending on the specific value you want to skip, but could look like: {"skipRowIfValue": ["abc"]} and {"skipRowIfNotValue": ["abc"]}. 

**Problem 3**: Your source data has two columns relating to Date values, one called Date and one called Date Type. You want to skip any values that may be in the Date Type column in the source data if there is no corresponding Date. 

**Solution 3**: Create a Group in Column 4 of your import mapping spreadsheet. In Column 5, use the "skipGroupIfEmpty" Option. This would look like: 

.. code-block::

   {"skipGroupIfEmpty": ["1"]}

Formatting a Title
------------------

**Problem 1**: You want to create titles for the records you're importing based on a set format.

**Solution 1**: Use the formatWithTemplate Option in Column 5 of your import mapping spreadsheet. This could look like: {"formatWithTemplate": "Oral History #^15 with Interviewee ^12"} where ^15 and ^12 are references to columns in the data source where identifiers and entity names can be found.

**Problem 2**: You want to label certain Notes fields in your CollectiveAccess system as they are labeled in your source data. For example, you have a column in your source data called “Technique” (for example, in column 3) and you would like this data to go into a Notes field in CollectiveAccess. In addition, some of these fields are empty in your source data. 

**Solution 2**: Use the formatWithTemplate Option in Column 5 of your import mapping spreadsheet. This would look like: 
	
{"formatWithTemplate": "Technique: ^3", "skipIfEmpty": 1}

where Technique: will be the text that appears in the Notes field, ^3 references the number of the Technique column in the source data, and the skipIfEmpty option ensures empty cells won’t be imported, for records that do not contain this field. 

Importing a List
----------------

**Problem**: You want to import a list into CollectiveAccess from your source data, but the values in your data don't 100% match the values in CollectiveAccess.

**Solution**: Use the Original Value and Replacement Value columns in your import mapping spreadsheet (Columns 8 and 9). If your source data includes "Y" and "N," but the CollectiveAccess list codes are "yes" and "no," simply input those values on your mapping with a line breaks (returns) between each value per column. This would look like: 
Y		Yes
N		No
N		No

Importing to Yes/No Checkboxes 
------------------------------

**Problem**: You want to import Yes/No values from your source data to a list element rendered as a Yes or No checkbox field in CollectiveAccess.

**Solution**: The yes_no_checkbox treats the first value in the list as “checked” and the second as “not checked.” Therefore the yes_no_checkbox relies on the order of the list items to determine the visual state of the control, so list sorting matters. Be sure to change the sorting for your Yes/No list to “by value” and then change the item_value of “yes” to “0_yes” and “no” to “1_no” so it would sort with “yes” first. This will ensure that "Yes" values in your source data transform to "checks" in the target element. Use Original and Replacement Values to transform source data to list value item codes, if necessary.

Foreign Key Constraint in Object Lots
-------------------------------------

**Problem**: Your Object Lot import failed. You may have received the error: Could not insert new record Cannot add or update a child row: a foreign key constraint fails (`project`.`ca_object_lots`, CONSTRAINT `fk_ca_object_lots_lot_status_id` FOREIGN KEY (`lot_status_id`) REFERENCES `ca_list_items` (`item_id`)). 

**Solution**: Make sure that for Object Lot records, ca_object_lots.lot_status_id in your import mapping spreadsheet. 

Object Lots have a non-optional "lot_status_id" that is a value taken from the "object lot statuses" list. It must be set to a valid value or a constant value, mapping to ca_object_lots.lot_status_id in your import mapping spreadsheet. 

Mapping Object Lot Identification Numbers 
-----------------------------------------

**Problem**: You want to map Object Lot identification numbers from your source data into CollectiveAccess. 

**Solution**: Numbers for ca_object_lots don't map to the normal ca_object_lots.idno. Instead, make sure your mapping has ca_object_lots.idno_stub in Column 3 of your import mapping spreadsheet where applicable. 

Mapping Serial Identification Numbers from multipart_id_numbering.conf
----------------------------------------------------------------------

**Problem**: You want to import a set of data that needs to be automatically numbered according to your settings in multipart_id_numbering.conf.

**Solution**: Set your mapping as follows:
Rule Type: Constant 
Source: %
CA table.element_code: ca_table.idno 
If the idno has more than one component, you can use more than one "%" placeholder (%.%)

Importing Multiple Relationship Types
-------------------------------------

**Problem**: You want to define a relationship type in a refinery parameter, but there is more than one relationship type in your source data column. 

**Solution**: Instead of writing {"relationshipType":"creator"} or something else that refers to a specific value in Column 6 of your import mapping, use {"relationshipType":"^1"}. The caret is followed by the number of the data source column from which you wish to draw relationship types (note: 1 is just an example), and will therefore include all types available in your source data column. 

Creating One Entity Record from Separate Data Source Columns
------------------------------------------------------------

**Problem**: An Entity's name is split up into two different columns in a source data spreadsheet, but you want to merge both columns to create a single Entity record in CollectiveAccess. 

**Solution**: Use the entityJoiner refinery in your import mapping in Column 6, being sure to include full container paths in the attributes parameter (since you'll be creating a new record). Parameters include entityType, entityTypeDefault, forename, surname, other_forenames, middlename, display name, prefix, suffix, attributes, nonpreferred_labels, relationshipType, relationshipTypeDefault, and skipIfValue.

Mapping Entities into a Container Field 
---------------------------------------
	
**Problem**: Your source data contains information regarding condition reporting, and includes an Entity (the person who performed the last condition report). You want this Entity to be mapped into the same Condition field (Container) as other Condition information. 

**Solution**: Create a Group in Column 4 of your import mapping spreadsheet for all fields that will go into the Condition container, for example, “condition,” including the Entity. 
Use the entitySplitter Refinery in Column 6 of your import mapping spreadsheet. In Column 7, use the Refinery Parameter **{"entityType": "ind"}** to declare the Entity as an individual. You do not need to include a relationship type in this Refinery Parameter, as this Parameter is not creating a separate and related record for this Entity. 

Building a Hierarchy Above Related Records
------------------------------------------

**Problem**: You're trying to import related Collections using the collectionSplitter Refinery in Column 6 of your import mapping, but you want to build a hierarchy above those records through a Refinery Parameter.

**Solution**: Use the collectionSplitter refinery with the Refinery Parameter "Parents." This will build parent record levels above the record that is laterally related to the imported data. In other words, if you're importing items that are laterally related to files, and you then need to build a series above the files you're creating via the collectionSplitter, you would use the "parents" parameter. "Parents" includes several sub-parameters, including idno, name, type, attributes, and rules. 

A Parents parameter may look like this:

.. code-block::

   {
   "parents": [
       {
           "idno": "^/inm:SeriesNo",
           "name": "^/inm:SeriesTitle",
           "type": "series",
           "attributes": { "ca_collections.description": "^7"}
       },
       {
           "idno": "^/inm:CollectionNo",
           "name": "^/inm:CollectionTitle",
           "type": "collection",
           "rules": [
               {
                   "trigger": "^/inm:Status = 'in progress'",
                   "actions": [
                       {
                           "action": "SET",
                           "target": "ca_collections.status",
                           "value": "edit"
                       }
                   ]
               }
           ]
       }
   ]
   }

Building a Hierarchy with Variable Amount of Levels
---------------------------------------------------

**Problem**: You are importing Storage Locations from an Excel spreadsheet, formatted in a hierarchy spanning 5 separate columns (Building A | Floor 2 | Room A | Cabinet A9 | Drawer 29), while other times it's only 3 columns deep (Building A | Floor 3 | Open Storage Area). For the case of 3 columns you don't want to import 2 blank levels, but rather would like to treat "Open Storage Area" as the subject of the mapping (as Drawer 29 is for the 5 column example). The value of this approach (beyond handling the blank levels) is that the subject level will be the target of the general mapping. This allows for the mapping of other relationships (i.e. the objects stored at the location) to whatever the "lowest" level happens to be.

**Solution**: Use the ParentAsSubject Option in Column 5 of your import mapping spreadsheet, along with a storageLocationHierarchyBuilder Refinery in column 6 of your import mapping spreadsheet. In this example, the last level before the first blank level will be the target for the objectSplitter. Make sure to map the storageLocationHierarchyBuilder to ca_storage_locations.parent_id, rather than just ca_storage_locations.

Importing a Hierarchy Within a Collections Table (ca_collections)
-----------------------------------------------------------------

**Problem**: You want to build a Collections hierarchy when importing to the table ca_collections.

**Solution**: Use the collectionHierarchyBuilder Refinery in column 6 of your import mapping with the Refinery Parameter "parents" in Column 7 of your import mapping. This will map parent levels above the imported data. It can be used to map more than one level, for example a series above a file, and a collection above a series, all at once. The parent parameter includes several sub-parameters, as you can see above, such as idno, name, type, attributes, and rules.

For example:

.. code-block::

   {
   "parents": [
       {
           "idno": "^/inm:SeriesNo",
           "name": "^/inm:SeriesTitle",
           "type": "series",
           "attributes": { "ca_collections.description": "^7"}
       },
       {
           "idno": "^/inm:CollectionNo",
           "name": "^/inm:CollectionTitle",
           "type": "collection",
           "rules": [
               {
                   "trigger": "^/inm:Status = 'in progress'",
                   "actions": [
                       {
                           "action": "SET",
                           "target": "ca_collections.status",
                           "value": "edit"
                       }
                   ]
               }
           ]
       }
   ]
   }

Using Rules
-----------

**Problem**: You want to conditionally skip data whenever a certain element appears in the data source. Any time a record's description says "do not use," for example, you want to skip that entire record, and not import it into CollectiveAccess.

**Solution**: Use "Rules" to set an action that will be triggered by the presence of a certain value. To do this, use expression statements to create the trigger. For example, if you wish to skip a record containing the phrase "do not use," you must first create the expression statement that denotes "do not use" and indicates that it is to be found in the "description" source. In this case, you could use a regular expression operator for "do not use": =~/do not use/. This will return the text "do not use" as true. Then, to complete the expression statement, add the variable (let's say that "description" is column 5 in an excel spreadsheet). The expression would then be: (^5=~/do not use/). Once the rule trigger is set, you can set the resultant action - in this case, "SKIP." The rule, then would be:

Rule Triggers: (^5=~/do not use/)
Rule Action: SKIP

Including Metadata in a Refinery Parameter
------------------------------------------

**Problem**: You are using an entitySplitter in Column 6 of your import mapping spreadsheet, and you want to use the Refinery Parameter to import address information about the Entity record you are creating. 

**Solution**: Use the Refinery Parameter attributes, which is used when defining multiple aspects of a Container (in this case, Address), and use the source data column numbers for clarity. In Column 7, this would look like: 

.. code-block::

   "Attributes": {"address":{"address1":"^24", "address2":"^25","city":"^26", "stateprovince":"^27", "postalcode":"^28", "country":"^29"}}}

Mapping Measurements from one Source to Separate Fields
-------------------------------------------------------

**Problem**: All of the data relating to dimensions located in your source data are in the same column, but you want to map them to separate dimension fields in CollectiveAccess.

**Solution**: Use the measurementsSplitter Refinery in column 6 of your import mapping spreadsheet to divide the dimensions into fields of the dataType Length or Weight. Use the delimiter Refinery Parameter in column 7 of your import mapping to separate the measurement values on the delimiter used in the source data. Use "units" to specify the unit of measurement, use "elements" to map the components of the dimensions to their respective fields, and use "attributes" to include any other elements (such as a notes field) that may be in a measurements container.

Setting a Unit Specifier for Mapping Dimensions
-----------------------------------------------

**Problem**: You are mapping dimensions data into CollectiveAccess, but the unit specifier (cm, in, ft, etc.) for these dimensions is not set within each data cell, but rather declared in the data column header in your source data. 

**Solution**: Use the suffix formatting in the Option Column (Column 5) of your import mapping spreadsheet to set the unit specifier for all Dimensions in the source column:

.. code-block::

   {"suffix": "cm"}
   {"suffix": "in"}

Using a Hierarchical Delimiter for Storage Locations
----------------------------------------------------

**Problem**: The Storage Locations in your source data are expressed only with numbers, 4.2.1 where 4 indicates a room, 2 indicates a rack, and 1 indicates a cabinet.

**Solution**: Use the storageLocationSplitter Refinery in Column 6 of your import mapping spreadsheet, with two key Refinery Parameters that work in tandem: "hierarchicalStorageLocationTypes" and "hierarchicalDelimiter." 
The hierarchicalStorageLocationTypes adds labels to the numbers in order so that you know what they mean, and the hierarchicalDelimiter tells those labels where to go (as opposed to the regular "delimiter" parameter which would create new records on each delimiter.) In this example, the parameter would be expressed: 

.. code-block::

   {"hierarchicalStorageLocationTypes" : ["room", "rack", "cabinet"], "hierarchicalDelimiter":"."}

Importing XML
-------------

**Problem**: You need to import data that is in an XML file format.

**Solution**: As of CollectiveAccess Version 1.4, two XML formats are supported:
FMPDSORESULT (Filemaker Pro XML data export format)
InMagic XML (Export format for the InMagic archival application)

If you're working with FMPDSORESULT or InMagic XML, set the mapping document's inputType to "FMPDSO" or "Inmagic" respectively and format your source data as /xml_tag in place of <xml_tag>.
If you need to work with some other XML-based format, you'll need to develop a data reader plugin for it. For most formats you can start by copying the FMPDSORESULT plugin (in app/lib/ca/Import/DataReaders/FMPDSOResultReader.php) to a new file in app/lib/ca/Import/DataReaders/ with the name of the new format + "Reader.php" Then change the class name and specifics in the copy to align with your new format.

Importing MARC
--------------

**Problem**: You are importing a MARC database, rather than XLSX or XLS.

**Solution**: Set the mapping document's inputType to "MARC" and format your source data by MARC Rule and Subfield as "rule/subfield" (ex. 035/a) and ignore indicators, if you choose.
If you do need to use MARC indicators, you append them after the sub-field and another '/'.

Example:

100/a (no indicators)
100/a/x (indicator 1=x)
100/a/xy (indicator 1=x; indicator 2=y)
A concrete example:
MARC:
245 18$aThe ... annual report to the Governor.
The Import mapping source would be:
245/a/18 (as in rule/subfield/indicator1indicator2).

Mapping a MARC element with multiple sub-fields
-----------------------------------------------

**Problem**: You want to map MARC elements into CollectiveAccess that contain multiple sub-fields. 

**Solution**: Sub-fields are denoted by the "$" sign, which can be ignored in the mapping document. Use display formatting to map a MARC element with multiple sub-fields to a single metadata element.
For example:
245 10$aTrade Union Fellowship Program :$b[announcement].
Here, the source is set to 245/a, and the following format is set in options:
{"formatWithTemplate": "^245/a  ^245/b"}

Importing Indented Hierarchical List Items
------------------------------------------

**Problem**: You are trying to import a hierarchical list from an Excel spreadsheet that uses indentations (empty cells) to display the hierarchy. 

**Solution**: Use the listItemIndentedHierarchyBuilder Refinery in Column 6 of your import mapping spreadsheet. You can use this to import the list on its own, import as a vocabulary, or import as metadata attached to Objects. The Refinery Parameters for this refinery include "levels" (to indicate source columns), "levelTypes" (to define hierarchy levels), "mode" (either "returnData" or "processOnly"). An example in JSON for the sample above would be:

.. code-block::

   {"list": "categories", "levels":["^1", "^2", "^3"], "levelTypes":["concept", "concept", "concept"], "mode": "processOnly"}

Values Importing Improperly from Excel
--------------------------------------

**Problem**: You're importing data from an Excel spreadsheet; the document looks normal, but when it's imported text fields seem to render as dates.

**Solution**: There is hidden formatting in your Excel spreadsheet; this is a common problem and can be responsible for a variety of import errors. Open the file in Excel, select all cells, and then select "Clear -> Formats" from the "Edit" menu. Save, and import the new copy of the file.

.. warning:: extra stuff here at bottom in old wiki