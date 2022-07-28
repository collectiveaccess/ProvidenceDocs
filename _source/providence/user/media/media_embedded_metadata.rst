Embedding Media Metadata
========================

* `Creating an Export Mapping`_
* `Target table / Precedence`_ 
* `Configuration`_

CollectiveAccess allows embedding metadata from related records into downloaded media files. This is useful, for instance, to embed copyright or licensing information into an image file before it "leaves" a system.

For this feature to function properly, exiftool must be installed, which is available through most Linux package managers, or via homebrew on Mac OS X. Make sure to point the exiftool_app setting in external_applications.conf to the right location.

Creating an Export Mapping
--------------------------

Use the generic CollectiveAccess Data_Exporter to generate the data for the embedding process. To create a spreadsheet that maps CollectiveAccess bundles to media metadata fields (e.g. XMP, EXIF, IPTC), use the sample mapping: 

.. warning:: file here

The exporter mapping should have the exporter_type "ExifTool" set. It must be non-hierarchical (flat) and should only contain valid fields for exiftool's XML format. Take an image and create an example for such an XML file on a Terminal by typing:

.. code-block::

   exiftool <path_to_your_file.jpg> -X > test.xml

Use the export mapping to run the bare XML export for a record and look at the resulting file to debug the mapping. To try embedding exiftool XML metadata into an image by hand: 

.. code-block::
 
   exiftool -tagsfromfile <your_metadata_file>.xml -all:all <your_media_file>.jpg

This is also the exact command CollectiveAccess will run.

.. note:: Do not set any of the technical metadata fields like file size, width, height, color space or depth by hand. 

Target table / Precedence
-------------------------

The mapping target (the Table setting in the export mapping) can be either the subject table, i.e. the table the downloaded representation is attached to - usually ca_objects, or it can be ca_object_representations to pull metadata directly from the representation record. 

For example, when downloading a representation file from the media screen in the object editor, CollectiveAccess will first run any ca_objects mappings that apply and then after that, any ca_object_representations mappings that are set up. exiftool's metadata embedding is non-destructive, meaning that even if the mapping only sets a few fields, it won't nuke any other existing metadata in the file. If both "subject table" (object) and representation mappings are set up, both will end up getting merged with the representation mapping, winning out on any conflicting fields.

Configuration
--------------

Once the mapping(s) are ready, point to them in media_metadata.conf. Near the bottom, there is the setting "export_mappings,” a list of table names which then map to a list of "type code => mapping code" mappings. 

Set a different mapping for each object type. If no mapping is set for a given type code, it will fall back to the "__default__" setting. A working example that has mappings for both objects and representations looks like this:

.. code-block::

   export_mappings = {
	ca_objects = {
		__default__ = exiftool_test,
	},
	ca_object_representations = {
		__default__ = exiftool_photocredit,
	}
   }

There are two other settings in that config file that disable metadata extraction for downloads of huge sets of media:

1. **do_metadata_embedding_for_search_result_media_download = 1**

2. **do_metadata_embedding_for_lot_media_download = 1**

Set these to 0 to disable metadata embedding for search result media downloads or object lot media downloads, respectively. Since CollectiveAccess has to create a copy of the original media, and then run exiftool for each downloaded file, the process can get very slow for large file numbers.
