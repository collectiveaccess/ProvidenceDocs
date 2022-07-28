Configuring Displays
====================

* `Codes for Displays`_ 
* `Using Related Records`_ 
* `Refining Displays`_
* `Using Type Restrictions`_

Displays allow users to access and view selected metadata in a summary-style format. They can be used to generate reports and provide information to users with read-only access. Displays can be configured through the user interface, but it is most efficient to go ahead and set them in the profile before installing.

Codes for Displays
------------------

The basic code needed to configure displays in the installation profile is as follows:

.. code-block:: php

   <display code="object_display" type="ca_objects" system="1">
      <labels>
        <label locale="en_US">
          <name>Object Summary</name>
        </label>
      </labels>
      <bundlePlacements>
        <placement code="metadata_element">
          <bundle>ca_objects.element</bundle>
        </placement>  
      </bundlePlacements>
    </display>

Displays are configured similarly to user interfaces in that they require defined bundles. However, the syntax is slightly different; the table as well as the element code must be specified: 

.. code-block:: php

   <placement code="ca_objects.description">
              <bundle>ca_objects.description</bundle>
            </placement>

Using Related Records
---------------------

To pull related records into your display, you simply need to express the desired table in your bundle placement:

.. code-block:: php

   <placement code="entities">
          <bundle>ca_entities</bundle>
        </placement>

Refining Displays
-----------------

Displays can be refined by using various settings within the bundle placement:

.. code-block:: php
   
   <placement code="entities">
          <bundle>ca_entities</bundle>
          <settings>
            <setting name="restrict_to_types">organization</setting>
            <setting name="render">makeEditorLink</setting>
            <setting name="delimiter"><![CDATA[<br/><br/>]]></setting>
            <setting name="label" locale="en_US">Related Organizations</setting>
          </settings>
        </placement>

.. note:: The **delimiter** setting employs a **<![CDATA[]]> block**. Without it, the installer would try to parse the tags it contains. This comes in handy when you're designing more complex templates. Please see Bundle Display Templates and displaying units for more on formatting display elements.

Using Type Restrictions
-----------------------
To create different displays for multiple types in a given table, use type restrictions as they would be used for a user interface:

.. code-block::

   <display code="photo_summary" type="ca_objects" system="1">
    <labels>
      <label locale="en_US">
        <name>Photo Summary</name>
      </label>
    </labels>
      <typeRestrictions>
        <restriction code="photo" type="photo"/>
      </typeRestrictions>

In which you wish to use the display only for type "photo" (and "photo" exactly matches the code in the **object_types list**). 

.. csv-table:: 
   :header-rows: 1
   :file: config_displays_table1.csv



