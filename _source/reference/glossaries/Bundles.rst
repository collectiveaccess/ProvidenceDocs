Bundles
=======

.. contents::
   :local:

Intro
-----

Bundles are elements that can be placed on UI screens, included in search forms or displays. They can be attributes of a specific element set or database fields intrinsic to a specific item type. Bundles can be functional elements that allow cataloguers to establish relationships between items, add and remove items from sets and manage an item's location in a larger hierarchy. Bundles are so named because they are essentially black-boxes that encapsulate various functionality.


Below is a break down of the bundle classes and the properties that are particular to each type.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1-XBLw6K_12Y4PtuYd-ov2fvQW-vtmVPMB-zv_EFptGM/pub?gid=0&single=true&output=csv
   

User interface Settings
-----------------------

There are several settings that can be used to configure all bundles, regardless of type, when they are placed on a user interface screen.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1LgGsjff6Iyco5b7xkAbdmTj4I7uJvfGWzt3cGdi9hFg/pub?gid=0&single=true&output=csv
   

However, there are type-specific settings as well, outlined below.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1qelsfVWP_9af5Ftew1UI_WyRSb-XmgxPw_QQLqDVrUc/pub?gid=0&single=true&output=csv

   
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
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1JFnHegfNAG65U9yz0enRSaye9_0ntlYjc_bt36l0cfE/pub?gid=0&single=true&output=csv
   
Bundle display settings for all types:

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1YsBPRnqRSLtGX2MELoa0wgpLUFBgKXtkcWMQAAqec2o/pub?gid=0&single=true&output=csv
   
Type-specific bundle display settings:

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1yBMv5XTannJQAmdtN1eO3Im2jcgHiCvrTorQFK1xig0/pub?gid=0&single=true&output=csv
   

Search Form Settings
--------------------
Regardless of type, bundles can take the follow setting when they are used in search forms.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1UyzVedoV01j6QQ6qCjyW_5SVpsyXeLRbpjgyYfLdRvI/pub?gid=0&single=true&output=csv
