.. _import_introduction:

Importing Data in CollectiveAccess
==================================

Basic Concepts: What is an Import Mapping? 
------------------------------------------

In order to import data into CollectiveAccess, it is necessary to define exactly *how* and *where* the source data will be imported. This information, along with other settings and criteria, is defined in an **import mapping spreadsheet.**

An import mapping spreadsheet (XLSX or GoogleSheets) defines how data is imported into CollectiveAccess. This spreadsheet acts as a crosswalk, detailing where data is coming from outside of CollectiveAccess (source), and where that same data will go once it is in CollectiveAccess (destination). There are many settings and options available in an import mapping to help organize and manipulate source data, and to ensure that data gets imported in a logical way, while also meeting a variety of user needs. These settings and options are described in more detail on the `Creating an Import Mapping: Overview <file:///Users/charlotteposever/Documents/ca_manual/providence/user/import/c_creating_mapping.html>`_ page. 

Why use an Import Mapping?
--------------------------

Data must be imported into CollectiveAccess using an import mapping spreadsheet. 
To import data in CollectiveAccess, it is necessary to first have source data available in a supported format (see below), and to then create an import mapping spreadsheet. 

Import mappings operate under two basic assumptions about the data being imported: 

1. Each **row** in a data set corresponds to a **single record.**

2. Each **column** in a data set corresponds to a **single metadata element**, or **field.**

A **row** in an import mapping spreadsheet contains all the metadata about a single, specific record: title, date, location, and other metadata that is present in the source data, and is arbitrary to the data set(s). A **column** groups these metadata elements together: all titles, all dates, all locations, and so on. This organization through rows and columns is a key aspect of creating an import mapping. 

.. note:: The exception to these assumptions is an option called treatAsIdentifiersForMultipleRows that will explode a single row into multiple records. This is very useful if you have a data source that references common metadata shared by many pre-existing records in a single row. See `Options <https://manual.collectiveaccess.org/import/tutorial.html#options-column-5>`_ for more details.

.. note:: Excel Tip for Import Mapping Spreadsheets: Translating A, B, C… to 1, 2, 3… can be time-consuming. Excel’s preferences allow you to change columns to display numerically rather than alphabetically. Go to Excel Preferences and select “General.” Click “Use R1C1 reference style.” This will display the column values as numbers.

Supported Data Input Formats 
----------------------------

Data can only be imported into CollectiveAccess in a supported data format. Supported data formats include: XLXS, Exif, MODS, RDF, Vernon, FMPDSOResult, MediaBin, ResourceSpace, WordpressRSS, CSVDelimited, FMPXMLResult, MySQL, SimpleXML, WorldCat, CollectiveAccess (CA-to-CA imports), Inmagic, Omeka, TEI, iDigBio, EAD, MARC, PBCoreInst, TabDelimited, Excel, MARCXML, PastPerfectXML, and ULAN. 

A full description of the supported import formats, and how they may be referenced in an import mapping, is available in the Supported File Formats page.

The following pages, A First Import Tutorial, and Running a Data Import, will walk the user through the different parts of an import mapping, how to create an import mapping, and finally, how to run an import mapping to import data. 

Sample Import Mapping Spreadsheet, Sample Source Data, and Sample Installation Profile
--------------------------------------------------------------------------------------

To follow along with the tutorial, download the following three files: 

`Sample Import Mapping Spreadsheet <../_static/_files/sample_mapping_tutorial.xlsx>`_: The import mapping spreadsheet; a schema crosswalk. For every data source, a target “destination” in CollectiveAccess is defined. This file is in the supported file format of XLXS; therefore, columns and rows are numbered using 1, 2, 3, and so on. 

`Sample Import Data (Source Data) <../_static/_files/sample_import_data_tutorial.xlsx>`_: The sample source data. This sample data includes three records (one row = one record), with 10 examples of possible metadata fields (one column = one field). The sample data is in the supported file format of XLXS; therefore, columns and rows are numbered using 1, 2, 3, and so on. 

`Sample Installation Profile <../_static/_files/Sample_import_profile.xml>`_: The sample Providence installation profile. This profile, written in XML format, defines the aspects of the CollectiveAccess system, into which the example data is imported. The profile tells the software how to set up various aspects of Providence. For more on installation profiles in CollectiveAccess, please see `Profiles <https://manual.collectiveaccess.org/dataModelling/Profiles.html>`_. 



