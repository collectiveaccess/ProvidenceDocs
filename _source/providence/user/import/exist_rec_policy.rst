.. _import_exist_rec_policy:

Existing Record Policies
========================

**Existing Record Policies** are an option in the Settings section of a data import mapping spreadsheet. There are various policies to choose from when making a mapping, and these policies determine how records that are already in a CollectiveAccess system are handled and checked against the source data being imported. Although a policy exists for a CollectiveAccess system that has no imported records, or, in other words, is empty and awaiting an import, most of these policies apply to data imports that are going into a CollectiveAccess system which already contains data of some kind. Please note that only one existing record policy can be set per each import mapping, and the policy will apply to all records in an import mapping. 

.. note:: To understand Existing Record Policies and their meanings, it is useful to know that In CollectiveAccess, the primary identifying field for each record is **“idno”** (identifying number) while the primary title/name field is a **“preferred_label.”** 

Existing Record Policies determine how records created by the import mapping are integrated, merged, or separated from other existing records. These policies are designed to be used in data imports that contain multiple parts, or, in other words, utilize multiple import mappings. Additionally, these policies can be used when revising an import mapping spreadsheet. All available Existing Record Policies, as of CollectiveAccess Version 1.8, are defined below:

When Should Each Existing Record Policy be Used? 
------------------------------------------------

It is useful to think about exactly *what* kind of data is represented in an import mapping, and, to think about exactly *what* data is already imported into the CollectiveAccess system, if any. 

It is also useful to envision the greater context of *how* source data will be represented in CollectiveAccess. Sometimes this can be challenging, as the import mapping spreadsheet is only a crosswalk, and is not meant to represent how the source data will actually look once imported into a CollectiveAccess system. 

Some useful questions to ask when choosing an Existing Record Policy include:

* Do I already have data imported into my CollectiveAccess system? 

* What kind of data is already imported, if any?

* What kind of data is represented in my source data and subsequent import mapping? (This can be seen in the “Table” Setting). 

* How do I want this data to interact with other data I have already imported? 

Existing Record Policies
------------------------

**none**
^^^^^^^^ 
A CollectiveAccess system is “empty,” containing no other imported data. No existing record policy needs to be set, as there are no existing records in the system. For imports with multiple parts, this setting often applies to the very first data import. 

**skip_on_idno**
^^^^^^^^^^^^^^^^ 

**merge_on_idno**
^^^^^^^^^^^^^^^^^
Records in the import mapping spreadsheet will be merged with any existing records in the CollectiveAccess system based on a shared record idno, or a record’s identifying number. 

**merge_on_idno_with_replace**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Records in the import mapping spreadsheet will be merged with any existing records in the CollectiveAccess system based on a shared record idno, or a record’s identifying number. Further, records specified in the import mapping that share an idno with records in the system will replace those that already exist in the CollectiveAccess system. 

**overwrite_on_idno**
^^^^^^^^^^^^^^^^^^^^^

**skip_on_preferred_labels**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**merge_on_preferred_labels**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Records in the import mapping spreadsheet will be merged with any existing records in the CollectiveAccess system based on a record’s shared title or name, or its preferred_label. 

**merge_on_preferred_labels_with_replace**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Records in the import mapping spreadsheet will be merged with any existing records in the CollectiveAccess system by matching on a record’s shared title or name, or its preferred_label. Further, records specified in the import mapping that share titles or names with records in the system will replace those that already exist in the CollectiveAccess system. 

**overwrite_on_preferred_labels**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**skip_on_idno_and_preferred_labels**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**merge_on_idno_and_preferred_labels**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Records in the import mapping spreadsheet will be merged with any existing records in the CollectiveAccess system based on a shared record idno, or a record’s identifying number, and a shared preferred_label. 

**merge_on_idno_with_preferred_labels_with_replace**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**overwrite_on_idno_and_preferred_labels**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




