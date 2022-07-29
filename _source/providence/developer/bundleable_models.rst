Addressing Data in Bundleable Models
====================================

.. warning:: incomplete 

* `Types of Data`_ 
* `Metadata Element and Attribute Model`_ 
* `Labelable Models`_ 
* `Intrinsic Fields`_ 
* `Relationships`_ 
* `Bundleable Models`_ 
* `Data`_ 
* `Data Access Contexts`_ 

Types of Data
-------------

Each primary table in the CollectiveAccess database schema has a corresponding model class in **app/models**. 

All models inherit from the *BaseModel* class, which provides a variety of basic functionality, including field-level data validation, generation of insert, update and delete SQL, support for "special" field types. These fields may include historic and inexact date ranges, processed media, and automated generation for field editing HTML, for example. Some models inherit from *BaseModelWithAttributes*, a subclass of *BaseModel* that provides attribute (user defined data fields based on the  **ca_metadata_elements table**) functionality for its subclasses. Being user defined allows for flexible run-time, and configurable cataloging schema. 

Metadata Element and Attribute Model
------------------------------------

The metadata element and attribute system in CollectiveAccess provides several benefits over standard SQL table-level fields, including:

1. Attributes may repeat
2. Attributes may be comprised of multiple values arranged in a value hierarchy
3. Attribute values may be parsed, validated, stored and indexed using plugins. This allows CA to support many specialized field types, and makes it easy for developers to add new field types without modification to the core of the application. 

Of course, the fact that attributes are user-defined is the biggest advantage, as any Collective Access system can be configured to support most any cataloguing standard. With a few exceptions, most data stored in a CollectiveAccess system is stored in attributes.

Any model that inherits from *BaseModelWithAttributes* is effectively endowed with the ability to have any number of repeating, complex user-defined data fields.

Labelable Models
----------------

Attributes provide storage for all sorts of data. However, there are a few categories of information that play special roles in CollectiveAccess, and therefore require somewhat different handling. 

One such category is **labels**. Labels are names or titles for key cataloguing items such as Objects, Entities, Geographic places, Collections, and Storage locations. Labels aren't just bits of text attached to a record; they are key to the identification of individual catalogued items and are required by the CollectiveAccess user interface in various locations. 

Models that inherit from *BundleableLabelableBaseModelWithAttributes* are endowed with the ability to take on labels as well as attributes. When displaying a catalogued item, typically it will be identified by using the label methods provided by *BundleableLabelableBaseModelWithAttributes* to fetch the appropriate label. 

*BundleableLabelableBaseModelWithAttributes* also provided methods to add, edit and delete labels as well as define 'non-preferred' alternate labels.

Intrinsic Fields
----------------

There are a few basic fields, however, that are essential to any Collective Access database schema. Called intrinsic fields, these data elements are implemented as standard database fields. They never repeat, and do not take attribute value types; they are restricted to the basic field types supported by *BaseModel*. 

There are relatively few intrinsic fields in CollectiveAccess. A few common intrinsic fields include:

* idno and idno_stub: Identifier for Objects, Entities, Places, Occurrences, Object Lots, and Collections.
* entity dates?/lifespan
* extent and extent_units fields in object records.
* type_id, which indicates the specific type for each item record. The types of attributes that may be attached to a given item record are determined by the type_id.
 
Relationships
-------------
To Come 

Bundleable Models
-----------------
To Come 

Data
----

To write any back-end code, customize a front-end, or to write a script to dump or manipulate CollectiveAccess-hosted metadata, access to lableables, bundleables, and intrinsics in CollectiveAccess is necessary.

Each type is stored in its own way:

* **Attributes** are stored in related records in the ca_attributes and ca_attribute_values tables.
* **Labels** are stored in their own related tables.
* **Intrinsic fields** are stored in the core item table and relationships in both related item records and "linking" records. 

CollectiveAccess provides interfaces for standardized and convenient retrieval of all types of stored data. These interfaces minimize the need to write custom data access code, and abstract the underlying storage implementation so your code can focus on processing and manipulating data, rather than figuring out where the data is located.

Data Access Contexts
--------------------

There are two contexts in CA where your code will need to access stored item data. The interfaces for each are very similar with a few differences to be aware of:

1. Search results representing many items

To Come

2. From a model representing a single item

To Come 

