Creating an Import Mapping: Overview
====================================

.. contents::
   :local:

Introduction
------------

The purpose of an import mapping is to define specifically *how* and *where* source data will be imported into CollectiveAccess. Data must be imported into CollectiveAccess using an import mapping. 

An import mapping is a spreadsheet (XLSX or GoogleSheets) that defines how data is imported into CollectiveAccess. This spreadsheet acts as a crosswalk, detailing where data is coming from outside of CollectiveAccess, and where that same data will go in CollectiveAccess. For a tutorial using a Sample Import Mapping Spreadsheet and Sample Import Data, please see Putting it All Together: A First Import. 

Each import mapping spreadsheet contains a set of intrinsic columns. A comprehensive description and function of these columns will be described below. Each import mapping also contains specific, customized Settings. Unlike Putting it All Together: A First Import, this section will not use sample data or a sample spreadsheet to illustrate what the parts of an import mapping spreadsheet look like. Instead, tables will be used to list possible options and the functions of each aspect of the spreadsheet in more detail. 

Here is a column-by-column explanation of each component of the import mapping document. To follow along with this tutorial, download the following two files: 

Files here 


Parts of an Import Mapping: Settings, Columns, and More
-------------------------------------------------------

Settings
--------

Every import mapping requires general settings. Settings include the importer name, data format of the source data (for a comprehensive list of supported file formats, please see xxx), the selected CollectiveAccess table, and more. This section can be placed at the top or bottom of a mapping spreadsheet. Although the Settings are integrated into the spreadsheet, they do function separately from the main column-defined body of the import mapping.

.. note:: In Settings, the rule types in Column 1 must be set to “Settings.” 

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: import_settings.csv

Columns
-------

Column 1: Rule Types
^^^^^^^^^^^^^^^^^^^^

For each row in the import mapping spreadsheet, a Rule Type must be set. These rules determine how the importer will treat the record, or row. In other words, the rules define how each row will be imported. There are five rules available to choose from:

=============   ===========
**Rule type**   **Description**
=============   ===========
Mapping         Maps a data source (such as a column in an Excel spreadsheet or a specific tag in XML) to a CollectiveAccess metadata element. Set this rule to ensure that the row will be imported.
Skip            Use Skip to ignore a data source; it will not be included in the import when this rule is set.
Constant        Sets an arbitrary constant value. Add the value to the source column and the value will be set in the corresponding metadata element for every record that is imported. This is used when mapping to Containers. 
Setting         Sets general preferences for the mapping itself. This simply defines various settings as Settings.
=============   ===========

.. _import_source:

Column 2: Source
^^^^^^^^^^^^^^^^

As mentioned above, the purpose of an import mapping spreadsheet is to define specifically *how* and *where* source data will be imported into CollectiveAccess. The Source column defines *where* data is coming from outside CollectiveAccess; this is the first part of the crosswalk.  

How values go in the Source column depends on the file format of the source data that is being imported. CollectiveAccess supports a variety of file formats, and each format has a unique, corresponding Source column value. A few of these are described below: 

.. csv-table::
   :header-rows: 1
   :file: source_table1.csv

A full description of the supported import formats and how they may be referenced in an import mapping is available in the Supported File Formats page.

.. Note:: In the example we're using for this tutorial, the sample data is in Excel. However, you may need to import data that is in an XML format. XML sources are cited in xPath, which is the standard syntax for retrieving data encoded in XML. Documentation regarding xPath be found here.

Our source data sample contains 10 columns of data, and each are listed in the mapping document under Source.

Source data columns may also be referenced elsewhere in the import mapping (generally in the Options or Refinery columns described below) by prefixing the column number with a caret "^" (for example "^10"), which indicates to the mapping that the value from column 10 should be inserted.

This allows multiple columns to be combined by using the Options settings and is frequently used within the Refineries to create detailed related entities, collections etc.

.. _import_element:

Column 3: CA table.element
^^^^^^^^^^^^^^^^^^^^^^^^^^

As a crosswalk, the import mapping spreadsheet determines where data comes from outside of CollectiveAccess (source data), but it also determines where that data will go in CollectiveAccess. Similarly to how Column 2 defines the source data, Column 3 determines where that source data goes in CollectiveAccess, using various ca_table.element_codes. 

This column declares the bundle code or metadata element in CollectiveAccess that the source data will be mapped to. It is possible to view what metadata elements are available and their formatting directly in CollectiveAccess. To do so, Manage/My Preferences/Developer/Show Bundle Codes, and select a preference. Navigate back to any record’s page, and these codes will be displayed; these then can go directly into Column 3. To copy a bundle code, simply select it, and paste into the import mapping spreadsheet. 

When you are importing to simple free text, DateRange, Numeric, Currency, or other kinds of datatypes, ca_table.element code is about all you need.

.. note:: When creating Lot records in an import mapping, set the ca_table.element_code to ca_objects.lot_id. 

However, there are a few cases where some additional steps are involved.

1. Mapping to Containers: A Container is a metadata element that contains sub-elements. In order to import to specific sub-elements within a Container, you must cite the element codes for both the Container itself, as well as the code for the sub-element that is your ultimate target.

In our sample mapping, the Date import is an example of this. In the sample profile, you'll notice that the Date field is actually a container with two sub-elements: a date range field for the date itself, and a date type drop-down menu to qualify the date.

Finally, all of the above is assuming that your data corresponds to the primary table of your import mapping. That is, you have object-level data importing to the object table.

However, data will usually contain references to related tables, such as related entities, related lots, related collections, related storage locations, and so on.

.. _import_group:

Column 4: Group
^^^^^^^^^^^^^^^

In many cases, data will map into corresponding metadata elements bundled together in a container. Declaring a Group in Column 4 of an import mapping is a simple way to ensure that all of your mappings to a Container actually end up in the same place. Group names are arbitrary; CollectiveAccess will recognize a group of any name for any number of metadata elements, as long as the name is consistent. 

To create a group, assign the arbitrary group name to a line in the Group column. This will direct the mapping to place rows of data into a single container. 

In the example mapping, we are mapping column 3 to ca_objects.date.date_value and using the constant rule to set ca_objects.date.date_type to "date created".

But without declaring both of these distinct mapping lines members of the same Group, you'd end up with one Date container instance with the Date itself, and another Date container instance with the Date Type! To make sure both the Date itself and the date type end up in the same instance of the Date container, simply assign them to the same group in the fourth mapping column.

The name you assign the group is arbitrary, but it should be something that is recognizable to you. In our example, I've simply called the group "Date".

.. _import_options:

Column 5: Options
^^^^^^^^^^^^^^^^^

Options can be used in an import mapping to set a variety of formatting choices and set conditions on the import itself. Options can also help process data that needs a clean-up, or can  format data with a variety of templates. Some Options are designed to set parameters on the import mapping behavior, such as preventing the import of certain fields. 

Options are written in code. Within that code are specific terms for Options that function to manipulate the behavior of the source data. Current Options for import mappings are listed and described below:

==============  ================================================================================  =======================  =======================================
Type of Option  Description                                                                       Parameter notes          Example for "Options" column of mapping
==============  ================================================================================  =======================  =======================================
skipIfEmpty     If the data value corresponding to this mapping is empty, skip the mapping line.  set to a non-zero value  {"skipIfEmpty": 1}
delimiter       Delimiter to split repeating values on.                                           delimiter value          {"delimiter": ";"}
==============  ================================================================================  =======================  =======================================

In the sample mapping, note the delimiter option set on our mapping to ca_objects.subject. Now refer to the second record in our sample data. You'll notice that there are multiple subject values in the same cell that are separated by semi-colons. By setting the delimiter option in the mapping, you are ensuring that these subject values get parsed and imported to discrete instances of the Subject field. Without the delimiter option, the entire string would end up a single instance of the Subject field.

.. _import_refinery:

Column 6: Refinery
^^^^^^^^^^^^^^^^^^

A refinery is designed to take a specific data format and transform it via a specific behavior as it is imported into CollectiveAccess. Refineries allow for greater complexity in data representation, and can be used to create separate but related records from the import spreadsheet. For more on Refineries, their definitions, types, and how to use them, see the Refineries page. 

If your data import requires related records, then you need to use refineries. 

While you can get really complex with refinery parameters, at its most basic a refinery simply creates a record, or matches on an existing record, and creates a relationship between it and the record you are importing directly from the source data.

In our example mapping, we are importing Images as ca_objects records. But using refineries, we are also creating and relating Entity records to those Object records.

Our example uses an entitySplitter, but these same principles apply to the splitters for other tables: placeSplitter, collectionSplitter, and so on.

The objectLotSplitter requires a few extra settings, all of which are cited in our example mapping.

Lastly, Splitters aren't the only type of Refinery - they're just the most common. For a complete list of refineries, go here.

.. _import_parameters:

Column 7: Refinery parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Refinery parameters define the conditions for the refinery being used in the import mapping. Where a Refinery declares what data is being manipulated, the refinery parameter dictates how the data will be changed. 

Refinery parameters are written in code, and require valid code to function properly in the import mapping. 

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: refineryparameters.csv
.. _import_original:

Columns 8 and 9: Original Values/Replacement Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An import mapping can find values within source data and replace them with new values upon import. This is a necessary step for data that does not match the list item code for corresponding values in CollectiveAccess. Values for the source data will be input in Column 8, while the values replacing those will be input in Column 9. Multiple values may be added to a single cell in an import mapping, so long as the replacement value matches the original value line by line.

In our example, there is a list element called "Reproduction" with values for reproduction, original, and unknown. In our source data, however, you'll notice that the data input for these values are abbreviated (e.g "orig", "repro", and "dontknow"). By using original and replacement values, our mapping transforms "orig" to "original" and "repro" to "reproduction" so that they can match on the list item code for the corresponding values in CollectiveAccess.

.. note:: Original Values and Replacement Values are ideal for smaller replacements. For large transformation dictionaries, use the Option “transformValuesUsingWorksheet” `http://manual.collectiveaccess.org/import/mappings.html#transform-values-using-worksheet`_.

For an example of when to use these columns and how, please see 

.. _import_notes:

Columns 10 and 11: Source Description and Notes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Source Description and Notes are the final two columns included in an import mapping spreadsheet, and are optional. Used to clarify the source data and purpose of each line in the import mapping itself, these columns can be useful for keeping track of where exactly data in the import mapping is coming from. The Notes column provides a space to explain how and why a certain line is mapped in the manner that it is. Both columns allow for easy reference, and are particularly useful when multiple users are creating an import mapping. 

These columns can be useful for future reference, if a mapping is intended to be used repeatedly. These columns also ensure that the mapping matches the source data.
