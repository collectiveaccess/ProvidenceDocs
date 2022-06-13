API: Models and Tables
======================

Each table in the CollectiveAccess database has a corresponding model class. Model classes provide functionality that eases reading, editing and writing data to its table, including:

1. Insert, update and delete functions (you don't need to, and should not, write SQL for these operations)
2. Navigating of hierarchies for tables supporting hierarchical tables
3. Support for extended data types, including date ranges, georeferences, uploaded media, timecode and more
4. Support for user defined, repeating fields
5. Support for retrieving data from rows in related tables (many-one and many-to-many)
6. Support for fields restricted to lists defined in the list/vocabulary manager
7. Generation of HTML form element widgets for specific fields

Model classes
-------------

Models are located in *app/models*. 

More to Come

Model Inheritance
-----------------

All models inherit from *BaseModel* (located in *app/lib/core/BaseModel.php*), which provides a baseline of functionality. Some models may inherit from subclasses of BaseModel that layer on additional functionality. These include:

1. *BaseModelWithAttributes*
2. *LabelableBaseModelWithAttributes*
3. *BundlableLabelableBaseModelWithAttributes*
4. *BaseRelationshipModel*
 

More to Come