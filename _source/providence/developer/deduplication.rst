Deduplication
--------------

Deduplication, available as of CollectiveAccess version 1.7, is only available as a command line utility, and as part of the   `Replication protocol. 

Using Deduplication
-------------------

To run deduplication by hand, there's a script in caUtils. It has one mandatory, and one optional, parameter: 

.. code-block:: php

   -t / --tables a table or list of tables to run the duplicate records report for. Lists are separated by commas or semicolons

   -d actually merge and delete duplicate records. Default is false

To generate a report, run the script without -d:

.. code-block:: php
 
   $ support/bin/caUtils remove-duplicate-records -t ca_entities
   CollectiveAccess 1.7 (133/GIT) Utilities
   (c) 2013-2016 Whirl-i-Gig

   Table ca_entities has 1 record that has potential duplicates.
   2 records have the checksum e6fece79354532493a45102948d80714bf773ef540c369de389a0483197f87ac
		entity_id: 1 (Homer J. Simpson)
		entity_id: 3 (Homer J. Simpson)

Once it is established that these are in fact duplicates, to merge them, backup your database and then rerun the script with the -d switch:

.. code-block:: 

   $ support/bin/caUtils remove-duplicate-records -t ca_entities -d
   CollectiveAccess 1.7 (133/GIT) Utilities
   (c) 2013-2016 Whirl-i-Gig

   Table ca_entities has 1 record that has potential duplicates.
   2 records have the checksum e6fece79354532493a45102948d80714bf773ef540c369de389a0483197f87ac
		entity_id: 1 (Homer J. Simpson)
		entity_id: 3 (Homer J. Simpson)
   Successfully consolidated them under id 1

Configuration
-------------

The default settings should work in most cases. The script uses checksums to find similar records. 

There are a few settings that control how these checksums are computed. To override the default values, you would add them to **app.conf**:

.. csv-table:: 
   :header-rows: 1
   :file: deduplication_table1.csv

Implementation Details
----------------------

The core implementation is in a trait "DeduplicateBaseModel", which is then mixed into BundlableLabelableBaseModelWithAttributes. It defines methods to compute checksums and some static utilities to list duplicates and merge records for the current table.

Computing the Checksum
----------------------

The record checksum is a simple sha256 hash of a serialized PHP array that contains: 

* The record idno (or not, this can be turned off, see above) 
* The type code, e.g. "image"
* All preferred labels
* All nonpreferred labels
* The checksum of the hierarchy parent record (e.g. for places or storage locations)
* The source code (source_id translated into a list item idno)
* Additional table-specific checksum components, for instance: 
    * ca_entities: lifespan
    * ca_lists: list_code
    * for anything under BaseRelationshipModel: the GUIDs of the left and right record, the relationship type code, and the effective date/source_info intrinsics

