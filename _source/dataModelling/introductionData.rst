Introduction to Data in CollectiveAccess
=========================================

.. contents::
   :local:
   
Primary Tables and Records
``````````````````````````

CollectiveAccess is structured around several primary tables of metadata elements, such as Objects, Entities, Collections, and more. Each primary table has intrinsic bundles and its own set of preferred and non-preferred labels bundles. 

Read more: :doc:`Primary Tables <primaryTables>`


Bundles
```````

`Bundle` is a high-level term for the various structures in CollectiveAccess used to store catalogued content. There are four distinct types of bundles, each with their own unique set of characteristics and uses: `labels`, `intrinsics`, `metadata elements` and `relationships`. Records are simply assemblages of various bundles, chosen to meet specific representational requirements.

Labels
******

Labels are used to store names or titles for records. Labels come in two varieties: preferred and non-preferred. Each record has one, and only one, preferred label that represents the record's current "name", and is used as the default display title. 

Records may have any number of non-preferred labels. Non-preferred labels are typically used to record alternative names/titles, which may be used in searches and optionally displayed. 

Both preferred and non-preferred labels are always available for all records in CollectiveAccess. No special configuration is required. Note that (with some exceptions) every record in CollectiveAccess is `required` to have a preferred label. Configuration options may be set to manadate uniqueness of labels with a system, to distinguish between different types of non-preferred labels (a requirement of some knowledge representation standard) and more. 

Read more: :doc:`Labels <labels>`.

Intrinsics
**********

Intrinsics are integral fields present in all CollectiveAccess systems. As with labels, intrinsics are always available and do not require special configuration. Intrinsics are simple, non-repeating values that typically exist to support specific functionality or, less often, for historical reasons. They cannot be removed from CollectiveAccess, but in most cases can be hidden if not needed.

Commonly used intrinsics include `idno` (record identifier), `type_id` (record type), `access` (public web site visibility) and `status` (record workflow status). Descriptions of all available intrinsic fields may be found in the :doc:`primary table <primaryTables>` documentation.

Metadata elements
***************** 

Metadata elements are configurable data fields bound to the various :ref:`records <primary_tables>` in your data schema. Metadata element are able to accept a rich and varied range of data types, can repeat, can support multilingual values, and may be composed into complex, multi-value fields using container elements. The bulk of the data schema for a typical system will be implemented using metadata elements to build installation-specific data structures.

Read more: :doc:`Metadata Elements <metadata>`

Relationships
**************

Relationships are bi-directional links between pairs of records. They may be created between records in any :doc:`primary table <primaryTables>` without restriction. All relationships include references to `relationship types` – configurable specifiers that distinguish different kinds of relationships that may occur. Relationship types between object and entity records might include, for example, "creator", "donor" and "subject". 

Any number of relationships can be created between a pair of records, and each relationship can optionally incorporate additional metadata elements. Relationships also support a handful of intrinsics, but do not take labels. 

Read more: :doc:`Relationships <relationships>` 


Installation Profiles
``````````````````````

Installation profiles are the XML documents that create your data model and set up your database. Every CollectiveAccess instance must have an installation profile. Many options are pre-loaded, but typically you need to customize one for your needs.  

Read more: :doc:`Installation Profiles <Profiles>`