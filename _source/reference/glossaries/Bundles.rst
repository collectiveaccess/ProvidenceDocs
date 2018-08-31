Bundles
=======

.. contents::
   :local:

Intro
-----

Bundles are elements that can be placed on UI screens, included in search forms or displays. They can be attributes of a specific element set or database fields intrinsic to a specific item type. Bundles can be functional elements that allow cataloguers to establish relationships between items, add and remove items from sets and manage an item's location in a larger hierarchy. Bundles are so named because they are essentially black-boxes that encapsulate various functionality.


Below is a break down of the bundle classes and the properties that are particular to each type.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/bundle_types.csv

User interface Settings
-----------------------

There are several settings that can be used to configure all bundles, regardless of type, when they are placed on a user interface screen.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/user_interface_bundles.csv

However, there are type-specific settings as well, outlined below.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/user_interface_-_specific.csv

Here's an example of how some of the settings above would look at the code-level in an xml profile:

   ::

      <placement code="ca_film">
        <bundle>ca_objects</bundle>
             <settings>
               <setting name="restrict_to_types">film</setting>
               <setting name="label" locale="en_US">Related films</setting>
               <setting name="add_label" locale="en_US">Add film</setting>
             </settings>
      </placement>

Display Settings
----------------

From /app/models/ca_bundle_displays.php

Global display settings:

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/global.csv

Bundle display settings for all types:

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/all_types.csv

Type-specific bundle display settings:

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/type-specific.csv

Search Form Settings
--------------------
Regardless of type, bundles can take the follow setting when they are used in search forms.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/search_form_settings.csv
