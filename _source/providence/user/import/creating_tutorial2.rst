Creating an Import Mapping
==========================

Introduction
------------

The purpose of an import mapping is to define specifically *how* and *where* source data will be imported into CollectiveAccess. Data must be imported into CollectiveAccess using an import mapping. 

An import mapping is a spreadsheet (XLSX or GoogleSheets) that defines how data is imported into CollectiveAccess. This spreadsheet acts as a crosswalk, detailing where data is coming from outside of CollectiveAccess, and where that same data will go in CollectiveAccess. For a tutorial using a Sample Import Mapping Spreadsheet and Sample Import Data, please see Putting it All Together: A First Import. 

Each import mapping spreadsheet contains a set of intrinsic columns. A comprehensive description and function of these columns will be described below. Each import mapping also contains specific, customized Settings. Unlike Putting it All Together: A First Import, this section will not use sample data or a sample spreadsheet to illustrate what the parts of an import mapping spreadsheet look like. Instead, tables will be used to list possible options and the functions of each aspect of the spreadsheet in more detail. 

Parts of an Import Mapping: Settings, Columns, and More
------------------------------------------------------- 

Settings
^^^^^^^^

Every import mapping requires general settings. Settings include the importer name, data format of the source data (for a comprehensive list of supported file formats, please see xxx), the selected CollectiveAccess table, and more. This section can be placed at the top or bottom of a mapping spreadsheet. Although the Settings are integrated into the spreadsheet, they do function separately from the main column-defined body of the import mapping.

.. note:: In Settings, the rule types in Column 1 must be set to “Settings.” 




