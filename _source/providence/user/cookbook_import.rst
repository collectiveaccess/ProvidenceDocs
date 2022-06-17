Cookbook: Import
================

This section provides some real examples of common challenges that may arise during a data import in CollectiveAccess. There are many options and possibilities when creating an import mapping spreadsheet, and preparing source data for import, and the plethora of choices can lead to many questions about formatting in the import mapping spreadsheet. 

This section is not an exhaustive, step-by-step guide for every possible option when creating an import mapping spreadsheet for a data import in CollectiveAccess. However, several typical scenarios are included with solutions explaining how to achieve specific outcomes in a data import. 

Each scenario begins with a “problem,” describing a certain challenge or question that may occur during a data import, or, the creation of an import mapping spreadsheet. There is an accompanying “solution” provided for each problem, which outlines how to carry out the necessary steps to reach a specific outcome for a data import or import mapping spreadsheet. 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online Support Forum, Online Chat, Slack Channel for Developers, and Back- and Front-end GitHub Repositories. 

Contents
--------

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

Problem: 
You want to define a relationship type in a refinery parameter, but there is more than one relationship type in your source data column. 

Solution: 
Instead of writing {"relationshipType":"creator"} or something else that refers to a specific value in Column 6 of your import mapping, use {"relationshipType":"^1"}. The caret is followed by the number of the data source column from which you wish to draw relationship types (note: 1 is just an example), and will therefore include all types available in your source data column. 


