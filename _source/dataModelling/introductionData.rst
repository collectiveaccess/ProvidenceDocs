Introduction to Data in CollectiveAccess
=========================================

.. contents::
   :local:
   

Bundles
```````
CollectiveAccess stores catalogued content in `bundles`. A "bundle" is a catch-all term for the various structures that contain content. There are, broadly speaking, four kinds of bundles:

Labels
******

Labels are record names or titles. Labels come in two varieties: preferred and non-preferred. Each record has one, and only one, preferred label that is used as the record's default display title. Records may have any number of non-preferred alternative titles and may be used in searches. Labels are always present and do not need to be configured to exist.

Intrinsics
**********

Intrinsics are fields that are integral to CollectiveAccess, are always present and do not need to be configured. They are simple, non-repeating values that typically exist to support specific functionality or, less often, for historical reasons. Whether you want them in your data schema or not, intrinsic fields will always be there. In most cases, however, they can be hidden if not needed.

Metadata elements
***************** 

Metadata elements are configurable data fields added to the various :ref:`records <primary_tables>` in your data schema. Metadata element are able to accept a rich and varied range of data types, can repeat, can support multilingual values, and may be composed into complex, multi-value fields. The bulk of your data schema will be implemented using metadata elements. Read more: :doc:`Metadata Elements <metadata>`


Relationships
**************

link two records to each other. Relationships are always bi-directional. If an object is related to an entity, then the entity is automatically related to the object as well. The simplest possible relationship will link two records and include a `relationship type`. Relationship types are configurable specifiers that distinguish different sorts of relationships between any pair of record types. Relationship types between object and entity records might include, for example, "creator", "donor" and "subject". Relationships may repeat – any number of relationships can be created between a pair of records – and can optionally incorporate additional metadata elements. Relationships also support a handful of intrinsics, but do not take labels. Read more: :doc:`Relationships <relationships>` 


Installation Profiles
``````````````````````

Installation profiles are the XML documents that create your data model and set up your database. Every CollectiveAccess instance must have an installation profile. Many options are pre-loaded, but typically you need to customize one for your needs.  Read more: :doc:`Installation Profiles <Profiles>`

Primary Tables
``````````````

CollectiveAccess is structured around several primary tables of metadata elements, such as Objects, Entities, Collections, and more. Each primary table has intrinsic bundles and its own set of preferred and non-preferred labels bundles. Read more: :doc:`Primary Tables <primaryTables>`