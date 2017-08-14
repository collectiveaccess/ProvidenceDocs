Supported File Formats
======================

.. contents::
   :local:

Overview
--------

Data may be imported into CollectiveAccess in a range of formats, including from Excel, CSV, a range of XML formats and others including external databases such as WorldCat. The fields from these sources are matched to CollectiveAccess tables and fields using the Mapping document's "Source" column, described here.

This page provides an overview of formats compatible with data import as well as how to identify a specific element from the source file for the Mapping document.

Currently Supported File Formats
--------------------------------


XLS, XLSX, CSV, TSV
^^^^^^^^^^^^^^^^^^^

Spreadsheets are mapped by column, with numeric identifiers provided in the Source column of the import mapping. If you wish to map from Column B of an Excel spreadsheet, you would list the Source as 2. (A = 1, B = 2, C = 3, and so on.)

XML (Including FileMaker XML, Inmagic XML, PastPerfect XML, Vernon XML, TEI XML, PBCore XML, MediaBin, MARCXML & MODS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

XML sources are referenced using `xPath <https://en.wikipedia.org/wiki/XPath>`_, a query language for selecting nodes and computing values from XML documents (a `basic tutorial <http://www.w3schools.com/xsl/xpath_intro.asp>`_ is available from W3C). 

In general the Source column should be set to the name of the XML tag, proceeded with a forward slash (i.e. /Sponsoring_Department or /inm:ContactName)

Common examples of xPath expressions are provided in the table below.

.. csv-table::
   :widths: 10, 25, 25, 25, 15
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1ky6LwTMPkNVOJJIr4IaptM_k4cCmyQlquJ-7hKhJ72w/pub?output=csv

MARCXML files can also be imported using the xPath syntax. Standard fields and indicators can be selected as Sources as follows:

.. csv-table::
   :widths: 20, 20, 30, 30
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1Wl5HAuelGuIXSdmHnb45gK8lmY7l68ESGhhzOOnfYOE/pub?output=csv

FileMakerPro XMLRESULT files generally follow the XML and xPath conventions described above but require some special formatting considerations due to inclusion of invalid characters in field names in certain databases (i.e. ArtBase). Source field names in the mapping must follow these rules:

- Field name should be preceeded with a forward slash (i.e. /Inventory::ArtistLast)
- The importer does not trim trailing spaces in field names so watch out for that!
- Only A-Z a-z 0-9 and these special characters are accepted _ - & # ? % :
- For all other special characters, including a space, replace the character with a single _ (underscore).
- If two invalid special characters fall in a row, use only a single _ (underscore) rather than two


MARC
^^^^

MARC records, in addition to MARCXML files, can be imported by using...

EXIF, IPTC, XMP
^^^^^^^^^^^^^^^

These embedded metadata standards can be imported from uploaded media (images, video, audio, etc.) using the same import mappings as described above. The *inputFormat* should always be set to "EXIF".

.. note::

   **SYSTEM REQUIREMENT**

   To import EXIF data your server must have the free `ExifTool <http://www.sno.phy.queensu.ca/~phil/exiftool/>`_  application installed on your server. Make sure the ExifTool entry in your external_application.conf configuration file is set to point to the installed application.

EXIF data can be difficult to decifer and locate the desired fields for import as the labels that appear in applications such as Photoshop that use the data often do not match the names given in the underlying EXIF file.

These names can be found by running the ExifTool command-line application. Once installed it can be run as:

``exiftool -json -a -gl my_file.tiff``

This will return a set of JSON encoded metadata, which matches the format used by the CollectiveAccess importer, allowing the names of fields within the metadata to be accurately identified. For example this block of EXIF metadata can be used to identify the type of lens used for a photograph:

.. code-block:: none

   "XMP-aux": {
      "SerialNumber": 1260413208,
      "LensInfo": "18-55mm f/?",
      "Lens": "18.0-55.0 mm",
      "ImageNumber": 0,
      "ApproximateFocusDistance": 4294967295,
      "FlashCompensation": 0,
      "OwnerName": "Erik Garcia Gomez",
      "Firmware": "1.1.1"
   },

To extract the lens information the block heading "XMP-aux" would be joined with the sub-section "Lens" with a slash to create "XMP-aux/Lens". This would be added to the Source column of the import mapping and matched with a target field in CollectiveAccess.

As this import format is used frequently in conjunction with media import, two more options are available to help identify uploaded media and match metadata to the correct files within the system. Use *_filename_* as a source if you wish to set any field in CollectiveAccess as the filename. And more importantly, *_filepath_* points to the media in the import directory, and can be used to trigger ingestion of the media itself.

.. csv-table::
   :widths: 20, 40, 40
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1k5lnRifRqNrlEMbZMoeCZCg72ElBHETvZcqyQCKmqCg/pub?output=csv

RDF
^^^

This is an option for importing linked data in RDF format...

ULAN-Linked Data
^^^^^^^^^^^^^^^^

ULAN Data can be imported through an interface available in the Import menu dropdown in CollectiveAccess. 

Omeka
^^^^^

Omeka data may be imported by...

WorldCat
^^^^^^^^

WorldCat objects can be searched and imported using the WorldCat interface available in the Import menu dropdown. This tool uses standard import mappings to match the WorldCat source fields to fields in the CollectiveAccess profile.

These import mappings are written as described above in the xPath notation used for MARCXML. 

CollectiveAccess
^^^^^^^^^^^^^^^^

Migrating data from one CollectiveAccess installation to another can be done by setting the Source column to the appropriate ca_table.element identifier. This will map the originating data to the fields of the new installation.
