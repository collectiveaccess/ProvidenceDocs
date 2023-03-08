.. _export_mappings:

Export Mappings
===============

* `Supported Output Formats`_
* `Creating an Export Mapping`_ 
* `Rule Types`_
* `Hierarchical Mappings`_
* `Source`_ 
* `Element Values and General Notes on Specific Formats`_ 
* `XML Element Values`_
* `MARC Element Values`_ 
* `Variables`_ 
* `Settings`_ 
* `Options`_ 
* `Processing Order`_ 
* `Replacements`_ 
* `Mapping Repetition`_ 
* `Running an Export`_ 
* `RDF Mode Configuration File Options`_ 
* `Node Type Definition Options`_ 
* `'Related' Options`_ 
* `Miscellaneous Settings and Options`_ 



Supported Output Formats
------------------------

Supported output formats currently include: 

* XML
* MARC21
* CSV

Creating an Export Mapping
--------------------------

To create a mapping, first download the Excel-based export mapping template available here:

:download:`Data Export Mapping Template <Data_Export_Mapping_template.xlsx>`

Once all of the mappings and settings have been entered into the template it can be `loaded directly <https://manual.collectiveaccess.org/providence/user/export/mappings.html#running-an-export>`_ into CollectiveAccess. The mapping is automatically checked using format-specific rules before it is added, so if your mapping has any errors or ambiguities, the mapping loader will let you know.

Creating the mapping is dependent on the format you want to export. Specific notes and examples can be found in `Element Values and General Notes on Specific Formats`_. 

Rule Types
----------

The first column of the main mapping spreadsheet is **Rule Type.** Similarly to Rule Types in an import mapping, in an export mapping, what you set here qualifies what this row does. There are several options available:

.. csv-table::
   :header-rows: 1
   :widths: 25, 75
   :file: 1_rule_types.csv

Hierarchical Mappings
---------------------

Some export formats support hierarchical relationships between mapping items. For XML this is a very core concept. To create a hierarchy, simply assign a number to a mapping in the 2nd column of the Mapping sheet and then reference that number in other rows (i.e. for other items) in the 3rd row, which is typically named "Parent ID". The second item will then become a direct child if the first one. In theory, those hierarchies can be nested very deep, but in practice, the format implementations may apply restrictions.

Source
------

The value for the 5th column in the mapping sheet can be any CollectiveAccess bundle specifier. See `API: Getting Data and Methods of Access <file:///Users/charlotteposever/Documents/ca_manual/providence/developer/api_getting_data.html>`_ for details. 

This usually specifies the actual data that is pulled into this item, and can be set to arbitrary text for items with static content or be left empty for items without content (e.g. wrapping elements in XML, or empty columns in CSV).

Note that if the context for the current mapping is changed, there are a couple of special keys available for the source column. For more information see the description for the `Context <file:///Users/charlotteposever/Documents/ca_manual/providence/user/export/mappings.html#options>`_ option in the table below.

Element Values and General Notes on Specific Formats
----------------------------------------------------

The 4th column of the mapping sheet is named 'Element'. This is a very format-specific setting where you enter the name of the element you want to put your field data in. See below for a description of the formats.

XML Element Values
------------------

The XML format implementation allows valid XML element names as values for the "Element" column. If you want to specify an XML attribute, prefix the name with an @. The attribute will then be appended to the hierarchy parent (which can't be another attribute). The mapping item hierarchy pretty much represents the XML tree that will be constructed from it.

Say you have the following very simple part of a mapping sheet and you export a single object.

.. csv-table::
   :header-rows: 1
   :widths: 20, 10, 10, 10, 20, 40
   :file: 2_-_element_values.csv

What you end up with as export for a given objects is something like the following:

.. code-block:: none

   <object idno="00001">
      <title>My very cool object</title>
   </object>

MARC Element Values
-------------------

Let's start off by saying that MARC is a very old and very specific format. Creating MARC mappings can be a bit painful. Make yourself familiar with the format before you dive into the following description.

In MARC mappings, the Element value is either a control field or a data field definition. For control field definitions, simply enter the field code (like '001') here. For data field definitions, enter the field code, followed by a forward slash and both indicator characters. For details on valid field codes and indicators, please refer to the MARC documentation. For empty/unused indicators, use the pound sign (#). Valid examples are: 001 300/## 490/1#.

Mapping items with data field definitions also shouldn't have any source definition or static data. The data resides in subfields, which should be separate mapping items with a hierarchical relationship (via Parent ID) to the field definition. For instance, you'd define an item for the data field "300/##". Suppose it had the ID 1. This field (like every data field) has a couple of subfields [1], namely a through g and 3, 6, 8 (leave out the $ character from the original documentation). Now create separate mapping items for each subfield you need, pull in the CA data you want using the 'Source' field in the mapping sheet and fill in the Parent ID "1", the identifier of the data field. Here's an example in table form (which may not make sense from a MARC standpoint but we're only trying to explain the format here, not the semantics of MARC fields):

.. csv-table::
   :widths: 20, 10, 10, 10, 20, 40
   :header-rows: 1
   :file: 3_-_marc_element_values.csv

An example export for a single object looks like this then. Note that we selected the 'readable' format for the MARC exporter, more info on format-specific settings are below.

.. code-block:: none

   LDR
   001     00001
   300 ## _bMy very cool object

Variables
---------

This feature allows you, using all the available features of the exporter, to assign a value to a user-defined identifier for later usage. The value can be anything you can pull from the database. The '''identifier''' should '''only contain alphanumeric text, dashes and underscores'''. Otherwise the mapping spreadsheet will fail to load. For example: type, my_variable, some-value, somethingCamelCase.

The identifier (essentially the name) that you assign to the variable goes into the element column. Since variable don't end up in the export, this column has no other use. Below is a simple example.

The main (and for the moment only) use for variables are conditional mappings. Say you have two objects, a document and a photo. And say you have an attribute 'secret_info' that is valid for both object types but that you only want to have in your export for photos. You could build two different mappings for these cases or you could use a variable to assign the object type to a user-defined identifier and then use the skipIfExpression option for the mapping in question.

A good way to think of variables is that they are mappings that don't end up in the actual export. They respect the current context, the current place in the hierarchy, everything.

.. csv-table::
   :widths: 20, 10, 10, 10, 20, 40
   :header-rows: 1
   :file: 4_-_variables.csv

We use the "type" variable in the skipIfExpression setting for the top_secret mapping. For more info on this setting, see the setting description below.

Settings
--------

These are configuration options that apply to the whole exporter mapping.

.. csv-table::
   :widths: 15, 25, 40, 20
   :header-rows: 1
   :file: 5_-_settings.csv

Options
-------
Each mapping item (i.e. a line in the mapping spreadsheet) can have its own settings as well. To set these settings, you can fill out the 6th column of the mapping sheet, called 'Options'. The options must be filled in in JavaScript Object Notation. If you set this value and it's not formatted properly, the mapping loading tool will throw an error. Here's a description of the available options:

.. csv-table::
   :widths: 15, 25, 40, 20
   :header-rows: 1
   :file: 6_-_options.csv

Below is a properly formatted example in JSON that uses some of these options:

.. code-block:: none

   {
       "default" : "No value",
       "delimiter" : ";",
       "maxLength" : 80,
       "filterByRegExp" : "[A-Z]+"
   }

Processing Order
----------------

In some cases the order in which the options and replacements (see next sub-section) are applied to each value can make a significant difference so it's important to note it here:

1) skipIfExpression (available for v1.5)
2) filterByRegExp
3) Replacements (see below)

   a) If value is empty, respect 'default' setting
   b) If value is not empty, use prefix and suffix

5) Truncate if result is longer than maxLength

Replacements
------------

While looking at the exporter mapping template you might have noticed that there's a second sheet called 'Replacements' in there. This can be used to assign replacements to each mapping item. The first column references the ID you set in the 2nd column of the mapping item table. The second column defines what is to be replaced. This again should be a PCRE-compatible regular expression without delimiters. The 3rd column defines what value should be inserted for the matched values. These conditions are applied to each matching value in the order they've been defined, i.e. if you have multiple replacements for the same mapping item, the incoming value is first passed through the first replacement, the result of this action is then passed in to the second replacement, and so on ...

.. note:: **For advanced users and PHP programmers**, the values are passed through preg_replace, the 'pattern' being the 2nd column value (plus delimiters) and the 'replacement' being the value from the 3rd column. This allows you to do pretty nifty stuff, for instance rewriting dates:

Search column:  (\w+) (\d+), (\d+)
Replace column: $2 $1 $3
value: April 15, 2003
result: 15 April 2003

Mapping Repetition
------------------

The 'RepeatMappings' rule type allows you to repeat a set list of mappings in a different context without actually defining them again. This is, for instance, very useful when creating EAD exports of hierarchical data where the basic structure is always the same (for archdesc, c01, c02, etc.) but the context changes. It's basically a shortcut that saves a lot of work in certain scenarios. Note that all hierarchy children of the listed items are repeated as well.

If you create a RepeatMappings rule, the mapping loader expects a comma-delimited list of references to the 2nd column in the Mapping sheet. It also really only makes sense to create this type of rule if you change the context in the same step. A simple example could look like this:

.. csv-table::
   :widths: 20, 10, 10, 10, 20, 40
   :header-rows: 1
   :file: 7_-_mapping_repetitions.csv

In this case, the 'child' element would be repeated for each hierarchy child of the exported item because of the context switch and for each of those children, the exporter would add the label and idno elements.

Running an Export
-----------------

The export can be executed through caUtils. To see all utilities ask for help after cd-ing into support. 

.. code-block:: 

   cd /path_to_Providence/support bin/caUtils help

To get further details about the load-export-mapping utility:

.. code-block:: 

   bin/caUtils help load-export-mapping

To load the mapping:

.. code-block::

   bin/caUtils load-export-mapping --file=~/my_export_mapping.xlsx

Next you’ll be using the utility export-data. First, have a look at the help for the command to get familiar with the available options.

.. code-block:: 

   bin/caUtils help export-data

Essentially there are 3 export modes:

1) Export a Single Record
^^^^^^^^^^^^^^^^^^^^^^^^^

Since the scope of a mapping is usually a single record, it's easy to use a mapping to export a record by its identifier. Suppose you have a ca_objects XML mapping with the code 'my_mapping'. To use this to export the ca_objects record with the primary key identifier (not the custom idno!) 550 to a new file ~/export.xml, you'd run this command:

.. code-block::

   bin/caUtils export-data -m my_mapping -i 550 -f ~/export.xml

2) Export a Set of Records Found by Custom Search Expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In most real-world export projects you'll need to export a set of records or even all your records into a single file. The exporter utility allows this by letting you specify a search expression with the -s parameter that selects the set of records used for export. The records are simply exported sequentially in the order returned by the search engine. This sequence is wrapped in the wrap_before and wrap_after settings of the exporter, if set. If you want to export all your records, simply search for "*". This example exports all publicly accessible files to a file ~/export.xml:

.. code-block::

   bin/caUtils export-data -m my_mapping -s "access:1" -f ~/export.xml

3) Export a Diverse Set of Records ("RDF mode")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[For advanced users] The error handling in this portion of the code is very poor so you're pretty much left on an island if something goes wrong.

Sometimes a limited export scope to for example ca_objects like in the previous example is not enough to meet the target format requirements. Occasionally you may want to build a kind of 'mixed' export where records from multiple database entities (objects, list items, places, ...) are treated equally. We have found this requirement when trying to use the exporter to generate an RDF graph, hence the name. The export framework originally wasn't designed for this case but the caUtils export-data command offers a way around that. The switch --rdf enables this so called "RDF mode". In this mode, you again use -f to specify the output file and you have to provide an additional configuration file (see Configuration_File_Syntax) which tells the exporter about the records and corresponding mappings which will be used for this export.

Here is a minimal example that uses all the available features:

``wrap_before = ""``
``wrap_after = ""``

.. code-block:: none

   nodes = {
      my_images = {
         mapping = object_mapping,
            restrictBySearch = "access:1",
            related = {
               concepts = {
                  restrictToRelationshipTypes = [depicts],
                  mapping = concept_mapping,
               },
               agents = {
                  restrictToTypes = [person],
                  mapping = agent_mapping,
               },
           }
       },
   }

While processing this configuration, the exporter essentially builds one big list of records and corresponding mappings to export. There are no duplicates in this list, if object_id 23 is selected by two different node type definitions or by multiple related definitions, it is still only exported once, using the mapping provided by the first definition.

Here is an example of how to run an RDF mode export:

``bin/caUtils export-data --rdf -c ~/rdf_mode.conf ~/export.xml``

RDF Mode Configuration File Options
-----------------------------------

.. csv-table::
   :widths: 25, 75
   :header-rows: 1
   :file: 8_-_rdf_mode.csv

Node Type Definition Options
----------------------------

.. csv-table::
   :widths: 25, 75
   :header-rows: 1
   :file: 9_-_node_options.csv

'Related' Options
-----------------

.. csv-table::
   :widths: 25, 75
   :header-rows: 1
   :file: 10_-_related_options.csv

Miscellaneous Settings and Options
----------------------------------

Exporting values from Information Services (e.g Library of Congress, Getty)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your CollectiveAccess configuration includes information services, such as Library Of Congress Subject Headings or Getty's Art and Architecture Thesaurus, you can export these in the exact same way as you would export other kinds of metadata elements.

However, in order to comply with certain XML formats (like MODS of TEI) you may find that you need to extract the terms' URI and export these to an attribute while exporting the label name to an element.

To grab an information service term's URI, you can simply append ".uri" or ".url" to the Source.

For example, if your Getty AAT element happens to be called "ca_objects.aat" and you wish to export the URI, simply express the source as "ca_objects.aat.uri". This will give you the URI while the simple "ca_objects.aat" will get you the label name as before.

LC services work a little differently. For these, you must append to the source ".text" to get the label name and ".id" to get the URI.

For example:

``ca_objects.lcsh_terms.text`` will get you the label name of all lcsh terms on the record. ``ca_objects.lcsh_terms.id`` will get you the URI for these terms.
