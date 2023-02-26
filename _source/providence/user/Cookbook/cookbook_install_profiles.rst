Cookbook: Installation Profiles 
===============================

This section provides some real examples of common challenges that may arise when configuring installation profiles in CollectiveAccess.

Each scenario begins with a “problem,” describing a certain challenge or question that may occur during installation. There is an accompanying “solution” provided for each problem, which outlines how to carry out the necessary steps to reach a specific outcome. 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online `Support Forum <https://collectiveaccess.org/support/>`_, `Online Chat <https://gitter.im/collectiveaccess/support>`_, `Slack Channel for Developers <https://collectiveacc-uye7574.slack.com/join/signup#/domain-signup>`_, and `Back-end <https://github.com/collectiveaccess/providence>`_ and `Front-end <https://github.com/collectiveaccess/pawtucket2>`_ GitHub Repositories. 

See also: `Installation Profiles <https://manual.collectiveaccess.org/providence/user/dataModelling/Profiles.html?highlight=installation+profile>`_. 

Contents
--------

* `Changing a Field’s Repeatability`_
* `Restricting a Field by Type`_
* `Dealing with Subtypes in Type Restrictions`_
* `Creating a Relationship Record`_
* `Restricting a Relationship by Type`_
* `Restricting a Screen`_
* `Creating Multiple User Interfaces for one Table`_
* `Restricting Display`_
* `Formatting a Container`_
* `Setting default for Checkboxes`_
* `Validating the Profile`_
* `Creating a Login`_
* `Creating a Display`_
* `Formatting a Display`_
* `Formatting Repeating Containers in a Display`_
* `Pulling Data into a Display via an Indirect Relationship`_
* `Using Conditional Expressions in Displays`_
* `Changing Terminology`_
* `Changing how List Elements are Displayed`_
* `Setting "Yes" and "No" for "Yes/no checkboxes"`_
* `Concept, Facet, Guide term, vs. Hierarchy Name`_
* `Displaying an Entire Storage Location Path`_
* `Customizing Types for Nonpreferred Labels`_
* `Changing the Label Bundle for "Individuals" vs. "Organizations"`_
* `Customizing Dislay of Metadata in Relationship Bundles`_
* `Including Media Icon in a Bundle Display Template`_
* `Displaying Interstitial Metadata in Relationship Displays`_
* `Placing a Local Subject Authority on a User Interface`_
* `Changing the Size of a Preferred Labels Text Box`_
* `Using the DateRange Calendar`_
* `Using Hierarchical Records`_
* `Moving Records in a Hierarchy`_
* `Enabling a "cross-table" Hierarchy`_
* `Launching a New Record Only from Within Another Record`_

Changing a Field’s Repeatability 
--------------------------------

**Problem**: You want to create a field that can repeat up to 3 times in an object record.

**Solution**: Set the "maxAttributesPerRow" in the typeRestrictions for the metadataElement to 3.

.. code-block::

   <restriction>
          <table>ca_objects</table>
          <settings>
            <setting name="minAttributesPerRow">1</setting>
            <setting name="maxAttributesPerRow">3</setting>
            <setting name="minimumAttributeBundlesToDisplay">1</setting>
          </settings>
        </restriction>

Restricting a Field by Type 
---------------------------

**Problem**: You've created a "Duration" field and you want it only to display for objects of the type "video."

**Solution**: Set the <type> tag in the typeRestrictions for the metadataElement to match the code for "video." The type code is the item idno in the list object_types.

.. code-block::

    <restriction>
          <table>ca_objects</table>
          <type>video</type>
          <settings>
            <setting name="minAttributesPerRow">1</setting>
            <setting name="maxAttributesPerRow">1</setting>
            <setting name="minimumAttributeBundlesToDisplay">1</setting>
          </settings>
        </restriction>

Dealing with Subtypes in Type Restrictions
------------------------------------------

**Problem**: An object type has multiple subtypes and you want to make sure your type restriction applies to all of these.

**Solution**: Use the "includeSubtypes" setting and set it to "1": 

.. code-block::

   <restriction code = "r1">
           <table> ca_objects</table>
           <type> document</type>
           <includeSubtypes> 1</includeSubtypes>
           <settings>
             <setting name = "minAttributesPerRow"> 0</setting>
             <setting name = "maxAttributesPerRow"> 255</setting>
             <setting name = "minimumAttributeBundlesToDisplay"> 1</setting>
          </settings>
         </restriction>

If, however, you want to include a few subtypes, or even all subtypes save one, you need to list each one individually.

.. code-block::

   <restriction  code = "r1" >
             <table>ca_objects </table>
            <type>program </type>
             <settings>
               <setting  name = "minAttributesPerRow" >0 </setting>
               <setting  name = "maxAttributesPerRow" >255 </setting>
               <setting  name = "minimumAttributeBundlesToDisplay" >1
          </setting>
             </settings>
           </restriction>
            <restriction  code = "r2" >
             <table>ca_objects </table>
             <type>letter </type>
             <settings>
               <setting  name = "minAttributesPerRow" >0 </setting>
               <setting  name = "maxAttributesPerRow" >255 </setting>
               <setting  name = "minimumAttributeBundlesToDisplay" >1
        </setting>
             </settings>
           </restriction>

Creating a Relationship Record
------------------------------

**Problem**: You want to catalog metadata about a relationship between two records on the relationship.

**Solution**: Create a relationship user interface, just as you would a normal user interface, with the relationshipTable name set as the type.

.. code-block::

    <userInterface code="entity_relationship_ui" type="ca_entities_x_entities">
      <labels>
        <label locale="en_US">
          <name>Interstitial Entity Editor</name>
        </label>
      </labels>
      <screens>
        <screen idno="basic" default="1">
          <labels>
            <label locale="en_US">
              <name>Basic info</name>
            </label>
          </labels>
          <bundlePlacements>
            <placement code="ca_attribute_relationshipDate">
              <bundle>ca_attribute_relationshipDate</bundle>
            </placement>
          </bundlePlacements>
        </screen>
      </screens>
    </userInterface>

You'll also need to have created metadata elements to populate the user interface, for example:

.. code-block::

      <metadataElement code="relationshipDate" datatype="DateRange">
      <labels>
        <label locale="en_US">
          <name>Relationship date</name>
          <description/>
        </label>
      </labels>
     <settings/>
      <typeRestrictions>
        <restriction code="r1">
          <table>ca_entities_x_entities</table>
          <settings>
            <setting name="minAttributesPerRow">1</setting>
            <setting name="maxAttributesPerRow">1</setting>
            <setting name="minimumAttributeBundlesToDisplay">1</setting>
          </settings>
        </restriction>
      </typeRestrictions>
    </metadataElement>

Restricting a Relationship by Type
----------------------------------

**Problem**: You want to restrict a "related entities" field to just one type - "related playwrights."

**Solution**: Override the default "related entities" label and restrict to type "playwrights" using the following code:

.. code-block::

   <screen idno="relationships" default="0">
          <labels>
            <label locale="en_US">
              <name>Relationships</name>
            </label>
          </labels>
     <bundlePlacements>
        <placement code="ca_playwrights">
                <bundle>ca_entities</bundle>
                  <settings>
                   <setting name="restrict_to_relationship_types">playwright</setting>
                   <setting name="label" locale="en_US">Related playwrights</setting>
                  </settings>
         </placement>
        <placement code="ca_director">
                <bundle>ca_entities</bundle>
                  <settings>
                   <setting name="restrict_to_relationship_types">director</setting>
                   <setting name="label" locale="en_US">Related directors</setting>
                  </settings>
         </placement>
  </bundlePlacements>
 </screen>

Where the setting "playwright" in "restrict_to_relationship_types" exactly matches the relationship type defined between the record type your screen is for (i.e. objects) and the relationship field type (i.e. entities).

Restricting a Screen
--------------------

**Problem**: You need to restrict a relationship to just one object type's editing UI - for example, you want a "related director" for videos, but not for photos, and a "related photographer" field for photos, but not videos.

**Solution**: You need to create two separate screens, one for videos and one for photos, and restrict the entire screen by type using the following code:

.. code-block::

   <screen idno="relationships_video" default="0">
        <labels>
           <label locale="en_US">
             <name>Relationships</name>
           </label>
         </labels>
        <typeRestrictions>
           <restriction code="video" type="video"/>
         </typeRestrictions>
    <bundlePlacements>
       <placement code="ca_director">
               <bundle>ca_entities</bundle>
                 <settings>
                  <setting name="restrict_to_relationship_types">director</setting>
                  <setting name="label" locale="en_US">Related directors</setting>
                 </settings>
        </placement>
   </bundlePlacements>
   </screen>
   <screen idno="relationships_photo" default="0">
         <labels>
           <label locale="en_US">
             <name>Relationships</name>
           </label>
         </labels>
        <typeRestrictions>
           <restriction code="photo" type="photo"/>
         </typeRestrictions>
    <bundlePlacements>
       <placement code="ca_photographer">
               <bundle>ca_entities</bundle>
                 <settings>
                  <setting name="restrict_to_relationship_types">photographer</setting>
                  <setting name="label" locale="en_US">Related photographers</setting>
                 </settings>
        </placement>
   </bundlePlacements>
   </screen>

Creating Multiple User Interfaces for one Table
-----------------------------------------------

**Problem**: Your organization has two departments, museum and archives, and they have two different accession systems. You want museum employees to have access to only their Accession records, and archive employees to be restricted to archive Accessions.

**Solution**: In your profile, create two different user interfaces for the table "ca_object_lots." Make sure that they have unique codes:

.. code-block::

   <userInterface code="archive_object_ui" type="ca_objects">

and

.. code-block::

   <userInterface code="standard_museum_object_lots_ui" type="ca_object_lots">

When the profile is installed, go to **Preferences > Editing** to choose the appropriate user interface for each side of the organization: 
   
Restricting a Display
---------------------

**Problem**: You've configured a summary display for one Object type (photo), but it's not relevant for another Object type (video).

**Solution**: You need to restrict the display to the appropriate subtype, as you would a user interface:

.. code-block::

   <display code="object_summary" type="ca_objects" system="1">
    <labels>
      <label locale="en_US">
        <name>Photo Summary</name>
      </label>
    </labels>
      <typeRestrictions>
        <restriction code="photo" type="photo"/>
      </typeRestrictions>

Formatting a Container
----------------------

**Problem**: You need to fit multiple sub-elements in a container and you don't want them to spill off the screen.

**Solution**: Format your container with line breaks so that not all sub-elements are in the same row using setting "lineBreakAfterNumberofElements":

.. code-block::

    <settings>
        <setting name="lineBreakAfterNumberOfElements">2</setting>
      </settings>

Setting default for Checkboxes
------------------------------

**Problem**: You want to use a yes/no checkbox, but you need it to default to "no."

**Solution**: Use the following code:

.. code-block::

   <list code="yes_no" hierarchical="0" system="0" vocabulary="0">
      <labels>
        <label locale="en_US">
          <name>Yes/No</name>
        </label>
      </labels>
      <items>
        <item idno="yes" rank="1" enabled="1" default="0">
          <labels>
            <label locale="en_US" preferred="1">
              <name_singular>Yes</name_singular>
              <name_plural>Yes</name_plural>
            </label>
          </labels>
        </item>
        <item idno="no" rank="2" enabled="1" default="1">
          <labels>
            <label locale="en_US" preferred="1">
              <name_singular>No</name_singular>
              <name_plural>No</name_plural>
            </label>
          </labels>
        </item>
      </items>
    </list>

in which you've added "rank."

Validating the Profile
----------------------

**Problem**: Your installation fails because your profile is invalid. Maybe you've gotten the message: There were errors parsing the profile(s): Profile validation failed. Your profile doesn't conform to the required XML schema.

**Solution**: Validate your profile against the profile syntax XML schema. The schema is located in install/profiles/xml/profile.xsd. Simply copy the schema to the same directory as the profile you are editing and use a validating XML editor such as OxygenXML.

Creating a Login
----------------

**Problem**: You need to create an administrator login within the profile.

**Solution**: Use the code:

.. code-block::

   <logins>
   <login user_name="admin" password="password" fname="CollectiveAccess" lname="Administrator"
     email="you@email.com">
     <role code="admin"/>
     <group code="admin"/>
   </login>
   </logins>

Creating a Display
------------------

**Problem**: You need to create custom default displays within the configuration profile.

**Solution**: Use the following code, adding bundle placements for whichever metadata elements you wish to see in the display:

.. code-block::

   <displays>
    <display code="general_object_report" type="ca_objects" system="1">
        <labels>
            <label locale="en_US">
                <name>General Object Report</name>
            </label>
        </labels>
        <bundlePlacements>
            <placement code="idno">
                <bundle>ca_objects.idno</bundle>
            </placement>
            <placement code="preferred_labels">
                <bundle>ca_objects.preferred_labels</bundle>
            </placement>
            <placement code="description">
                <bundle>ca_objects.description</bundle>
            </placement>
            <placement code="dimensions">
                <bundle>ca_objects.dimensions</bundle>
            </placement>
            <placement code="date">
                <bundle>ca_objects.date</bundle>
            </placement>
            <placement code="entities">
                <bundle>ca_entities</bundle>
            </placement> 
            <placement code="locations">
                <bundle>ca_storage_locations</bundle>
            </placement>          
        </bundlePlacements>
    </display>    
    <display code="entity_report" type="ca_entities" system="1">
        <labels>
            <label locale="en_US">
                <name>General Entity Display</name>
            </label>
        </labels>
        <bundlePlacements>
            <placement code="preferred_labels">
                <bundle>ca_entities.preferred_labels</bundle>
            </placement>  
            <placement code="address">
                <bundle>ca_entities.address</bundle>
            </placement> 
            <placement code="email">
                <bundle>ca_entities.email</bundle>
            </placement> 
            <placement code="telephone">
                <bundle>ca_entities.telephone</bundle>
            </placement> 
            <placement code="related_objects">
                <bundle>ca_objects</bundle>
            </placement>         
        </bundlePlacements>
    </display>
   </displays>

Formatting a Display
--------------------

**Problem**: You need to style your display so that a.) it only includes a heading when there is content in the field and b.) the heading is in bold text for easier viewing.

**Solution**: Use an <ifdef> tag to create a conditional heading, and format the text using HTML. When creating a display through the profile be sure to enclose the format template in <![CDATA[ ]] otherwise it will be parsed:

.. code-block::

   <placement code="cataloguer">
          <bundle>ca_objects.museum_cataloguer</bundle>
          <settings>
         <setting name="format"><![CDATA[<ifdef code="cataloguers_museum"><b>Catalogued by: </b></ifdef> ^cataloguers_museum </ifdef> <ifdef code="dates_catalogued"><b>Date:</b></ifdef> ^dates_catalogued <ifdef code="cataloguer_notes"><b>Cataloguer Notes:</b></ifdef> ^cataloguer_notes]]>
          </setting>
          </settings>
        </placement>

Formatting Repeating Containers in a Display
--------------------------------------------

**Problem**: You have a repeating address field, and it's showing up on your display like so:

Address Line 1 A; Address Line 1 B
Address Line 2 A; Address Line 2 B
Address Line 3 A; Address Line 3 B

**Solution**: Use the <unit> tag in the bundle display template to make the display look like this:

Address Line 1 A
Address Line 2 A
Address Line 3 A
Address Line 1 B
Address Line 2 B
Address Line 3 B

.. code-block::

   <unit delimiter="<br/>">^ca_entities.address.address1<br/>^ca_entities.address.address2<br/>^ca_entities.address.address3<brr/><br/></unit>

Pulling Data into a Display via an Indirect Relationship
--------------------------------------------------------

**Problem**: A is related to B which is related to C. You want A's metadata on C's summary so you must pull through the connecting B relationship.

**Solution**: The display template below pulls repeating artist statement metadata from an Entity record. It could be used in an Object bundle to pull data into a Collection display. In this example Collections are related to Objects which are related to Entities (but there is no direct relationship between Collections and Entities).

.. code-block::

   <em><strong>^ca_objects.preferred_labels</strong></em><br>
   ^ca_entities.preferred_labels
   <br><unit relativeTo="ca_entities" delimiter="<br><br/>">
   ^ca_entities.statement.statement_text<br/>^ca_entities.statement.statement_date<br/>^ca_entities.statement.statement_source
   </unit>

Using Conditional Expressions in Displays
-----------------------------------------

**Problem**: You want to only output the display based on a conditional, such as if "current" is selected from the type drop-down in a repeating "Credit line" container.

**Solution**: It's possible to use expressions to control when you see displayed data. To do so, use the if rule. Here's an example using the "Credit line" container mentioned above. Your display template would look like this (with your correct codes of course):

.. code-block::

    <unit relativeTo="ca_objects.credit_line"><if rule="^credit_type =~ /current/">^ca_objects.credit_line.credit_text 
        (^ca_objects.credit_line.credit_type)</if></unit>

Changing Terminology
--------------------

**Problem**: You need to change a default CollectiveAccess term, Object Lots, to a custom one, Accessions. 

**Solution**: Open and edit messages.po using a GetText-compatible editor such as POEdit and translate each English string into your target language. If using POEdit, the .mo file will be automatically created or updated every time you save your .po file. Then, change the display names in the "Find" and "New" menus using navigation.conf:

.. code-block::

   "navigation" = {
   "object_lots" = {
   "displayName" = _("Accessions"),

Changing how List Elements are Displayed
----------------------------------------

**Problem**: You have a metadata element of datatype=List and you need to render its display to something other than a drop-down menu.

**Solution**: List elements can be rendered in numerous other ways besides drop-down menus. The can be configured as checklists, radio buttons, hierarchy browsers, and type-ahead lookups, and others. In <settings> for the metadata element, use the following syntax to render a List a certain way:

.. code-block::

     <settings>
        <setting name="render">radio_buttons</setting>
      </settings>

Options:
Yes/no checkbox (code="yes_no_checkboxes");
Radio buttons (code="radio_buttons");
Checklist (code="checklist");
Type-ahead lookup (code="lookup");
Horizontal hierarchy browser (code="horiz_hierbrowser");
Horizontal hierarchy browser with search (code="horiz_hierbrowser_with_search");
Vertical hierarchy browser (code="vert_hierbrowser")

Setting "Yes" and "No" for "Yes/no checkboxes"
----------------------------------------------

**Problem**: You'd like to create a yes/no checkbox and want to make sure "checked" is set to "yes."

**Solution**: The checked state of a yes/no checkbox is taken to be the first item in the list, and the unchecked is taken as the second item in the list. Because order matters, the sort is critical. Set the rank or item value for yes to, say, 10 and the rank or item value for no to 20, then make sure the list sort is set to rank or item value (whichever you’re using). Note that you should set "default" to 0 for both - otherwise the checkbox will default to a check on new records.

.. code-block::

   <list code="extinct" hierarchical="0" system="0" vocabulary="0">
      <labels>
        <label locale="en_US">
          <name>is extinct?</name>
        </label>
      </labels>
      <items>
        <item idno="yes" enabled="1" default="0" rank="10">
          <labels>
            <label locale="en_US" preferred="1">
              <name_singular>yes</name_singular>
              <name_plural>yes</name_plural>
            </label>
          </labels>
        </item>
        <item idno="no" enabled="1" default="0" rank="20">
          <labels>
            <label locale="en_US" preferred="1">
              <name_singular>no</name_singular>
              <name_plural>no</name_plural>
            </label>
          </labels>
        </item>
      </items>
    </list>

Concept, Facet, Guide term, vs Hierarchy Name
---------------------------------------------

**Problem**: In Lists & Vocabularies, what is the meaning and function of Concept, Facet, Guide term, and Hierarchy name?

**Solution**: These are distinguishing types for list items analogous to those used in the Getty Art and Architecture Thesaurus (AAT). They are part of the default configuration defined in install/profiles/xml/base.xml and inherited by most installation profiles. Although they may seem ubiquitous they can be overridden with other values at any time and in any configuration profile if desired. As with types for other catalogue records (Eg. object types, entity types, place types), list item types serve both to distinguish items by general function and to allow metadata elements to vary across items. The default values are intended to provide compatibility with a variety of vocabularies in general and the AAT in particular. When the AAT is imported these types indicate the following:
1. Concept: a list item that represents a unique concept and may be used for descriptive cataloguing.
2. Facet: a list item that is the parent for thematic unit of vocabulary concepts. Facets are primarily an organizational element and not typically used for cataloguing.
3. Guide term: a list item that groups those under it for convenience. Guide terms are purely organizational and never used for cataloguing.
4. Hierarchy name: A list item that defines a sub-unit of a vocabulary. These are typically high-level organizational elements.
There is no technical difference between the four types. The designation is purely semantic.

Displaying an Entire Storage Location Path
------------------------------------------

**Problem**: You've noticed that while viewing an object's Related Storage Locations, the field only displays a relationship to the lowest level in the storage location hierarchy and not the full hierarchy. So, for example, instead of showing Room 1 -> Cabinet 3 -> Shelf 5, you only see "Shelf 5."

**Solution**: Format the relationship display template to show the entire path. This can be done through the UI if the system is already in use, or directly in the profile if you still haven't done your final installation. Add ^ca_storage_locations.hierarchy.preferred_labels to a display template inside the ca_storage_locations bundle.

Customizing Types for Nonpreferred Labels
-----------------------------------------

**Problem**: You have a nonpreferred labels field on your Objects UI that looks like this:

.. code-block::

   <placement code="nonpreferred_labels">
              <bundle>nonpreferred_labels</bundle>
              <settings>
                <setting name="label" locale="en_US">Alternate titles</setting>
                <setting name="add_label" locale="en_US">Add name</setting>
              </settings>
            </placement>

but when you install the profile, you only have two label types in this bundle - "Use for" and "alternate." You want to include one called "working title."

**Solution**: Use the list object_label_types (or entity_label_types, occurrence_label_types, etc., depending on the table in which you're working), to add new label types. These can be found in the base profile if you don't see them in your configuration. Just add a list item as you would to any other list.

Changing the Label Bundle for "Individuals" vs "Organizations"
--------------------------------------------------------------

**Problem**: You have no need for forenames, middlenames and surnames when cataloging organizational entities. You want the preferred_label field to change based on entity class.

**Solution**: In the installation profile, add this special setting to the list entity_types:

.. code-block::

   <list code="entity_types" hierarchical="1" system="0" vocabulary="0">
      <labels>
        <label locale="en_US">
          <name>Entity Types</name>
        </label>
      </labels>
      <items>
        <item idno="ind" enabled="1" default="1">
          <labels>
            <label locale="en_US" preferred="1">
              <name_singular>Individual</name_singular>
              <name_plural>Individuals</name_plural>
            </label>
          </labels>
              <settings>
                <setting name="entity_class">IND</setting>
              </settings>
        </item>
        <item idno="org" enabled="1" default="0">
          <labels>
            <label locale="en_US" preferred="1">
              <name_singular>Organization</name_singular>
              <name_plural>Organizations</name_plural>
            </label>
          </labels>
              <settings>
                <setting name="entity_class">ORG</setting>
              </settings>
        </item>
      </items>
    </list>

This can also be set through the graphical user interface via the Entity Class setting on the records of the entity_types list items (*Manage > Lists & vocabularies > entity_types > Individuals*).

Customizing Display of Metadata in Relationship Bundles
-------------------------------------------------------

**Problem**: You want to display metadata attached to related items in relationship bundles. For example, if you want to display both the name and life dates for related entities you can use a bundle display template to both extract and format the metadata.

**Solution**: Set the relationship list format to 'list.' Then, use bundle display template formatting to configure the metadata inside the display_template setting. You must wrap the display template in <![CDATA[ ]] otherwise the template will be parsed:

.. code-block::

    <placement code="ca_entities">
              <bundle>ca_entities</bundle>
              <settings>
                <setting name="restrict_to_types">individual</setting>
                <setting name="label" locale="en_US">Related Entities</setting>
                <setting name="list_format">list</setting> 
                <setting name="display_template"
                   <![CDATA[<l>^ca_entities.preferred_labels</l>
                   <ifdef code="ca_entities.life_dates">Life Dates:   
                   </ifdef>^ca_entities.life_dates]]></setting>
               </settings>
            </placement> 

Including Media Icon in a Bundle Display Template
-------------------------------------------------

**Problem**: You want to see a media thumbnail in Object relationships, so that you can more easily identify the related Object by sight.

**Solution**: Use ^ca_object_representations.media.icon in your bundle display template.

Displaying Interstitial Metadata in Relationship Displays
---------------------------------------------------------

**Problem**: As in the example above, you want to include additional metadata in your relationship bundle. However, in this case the metadata is located on the Relationship Record (the interstitial record located between the two related records).

**Solution**: As in the above example, set the relationship list format to 'list.' Then, use bundle display template formatting to configure the metadata inside the display_template setting. You must wrap the display template in <![CDATA[ ]] otherwise the template will be parsed. However, in this particular case, you must include the code for the interstitial record itself (i.e. ca_entities_x_collections) as follows:

.. code-block::

   <placement code="ca_org">
              <bundle>ca_entities</bundle>
              <settings>
                <setting name="label" locale="en_US">Related Organization</setting>
                  <setting name="add_label" locale="en_US">Add Related Organization</setting>
                <setting name="restrict_to_types">org</setting> 
                <setting name="list_format">list</setting>
                <setting name="display_template"><![CDATA[<l>^ca_entities.preferred_labels</l> ^ca_entities_x_collections.subsidiary_name]]></setting>
              </settings>
            </placement>

In this example, ca_entities_x_collections is the code for the relationship record UI, and subsidiary.name is the metadata element that will be displayed in the relationship bundle.

Placing a Local Subject Authority on a User Interface
-----------------------------------------------------

**Problem**: You will be using a local subject authority and you want to place "subjects" on your Object Editing UI.

**Solution**: Use "ca_list_items" and place on the UI in the following format:

.. code-block::

   <placement code="ca_list_items">
              <bundle>ca_list_items</bundle>
              <settings>
                <setting name="restrict_to_lists">local_vocab</setting>
                <setting name="label" locale="en_US">Subject Access</setting>
                <setting name="add_label" locale="en_US">Add term</setting>
              </settings>
            </placement> 

in which the list holding your subject authority will be specified in the setting "restrict_to_lists."
 
Changing the Size of a Preferred Labels Text Box
------------------------------------------------

**Problem**: You want to make the Preferred Labels text box wider, but it's not listed among the other metadata elements because it's a baked-in element.

**Solution**: You can simply add "height" and "width" settings to the bundle placement in the UI.

.. code-block::

   <placement code="preferred_labels">
              <bundle>preferred_labels</bundle>
              <settings>
                <setting name="label" locale="en_US">Object Name</setting>
                <setting name="add_label" locale="en_US">Add Object Name</setting>
                <setting name="height">1</setting>
                <setting name="width">90</setting>
              </settings>
            </placement>

Make sure that the "height" and "width" settings don't include locale settings, as this will create errors.

Using the DateRange Calendar Feature
------------------------------------

**Problem**: You've noticed that there's a small calendar icon inside DateRange elements, but nothing happens when you click on it.

**Solution**: You need to use the "useDatePicker" setting when configuring the metadata element and be sure that it is set to "1."

.. code-block::

   <metadataElement code="start" datatype="DateRange">
          <labels>
            <label locale="en_US">
              <name>Exhibit Start Date</name>
            </label>
          </labels>
        <settings>
        <setting name="fieldWidth">40</setting>
        <setting name="fieldHeight">1</setting>
        <setting name="minChars">0</setting>
        <setting name="maxChars">65535</setting>
        <setting name="useDatePicker">1</setting>
      </settings>
    </metadataElement>

Using Hierarchical Records
--------------------------

**Problem**: You want to create a record hierarchy for example nested Collection records.

**Solution**: In app.conf, set:

.. code-block::

   ca_collections_show_add_child_control_in_inspector = 1
   
Then make your record types hierarchical either through the installation profile:

.. code-block::

   <list code="collection_types" hierarchical="1" system="0" vocabulary="0">
      <labels>
        <label locale="en_US">
          <name>Collection types</name>
        </label>
      </labels>
      <items>
        <item idno="collection" enabled="1" default="1">
          <labels>
            <label locale="en_US" preferred="1">
              <name_singular>collection</name_singular>
              <name_plural>collection</name_plural>
            </label>
          </labels>
          <items>
            <item idno="fonds" enabled="1" default="0">
              <labels>
                <label locale="en_US" preferred="1">
                  <name_singular>fonds</name_singular>
                  <name_plural>fonds</name_plural>
                </label>
              </labels>
              <items>
                <item idno="series" enabled="1" default="0">
                  <labels>
                    <label locale="en_US" preferred="1">
                      <name_singular>series</name_singular>
                      <name_plural>series</name_plural>
                    </label>
                  </labels>
                  <items>
                    <item idno="file" enabled="1" default="0">
                      <labels>
                        <label locale="en_US" preferred="1">
                          <name_singular>file</name_singular>
                          <name_plural>file</name_plural>
                        </label>
                      </labels>
                    </item>
                  </items>
                </item>
              </items>
            </item>
          </items>
        </item>
      </items>
   </list>

The final step is to include the Location in hierarchy bundle on the Collections user interface, either through the installation profile:

.. code-block::

   <userInterface code="collection_ui" type="ca_collections">
      <labels>
        <label locale="en_US">
          <name>Collection editor</name>
        </label>
      </labels>
      <screens>
        <screen idno="basic" default="1">
          <labels>
            <label locale="en_US">
              <name>Basic Info</name>
            </label>
          </labels>
          <bundlePlacements>
            <placement code="hierarchy_location">
              <bundle>hierarchy_location</bundle>
            </placement>

or the graphical user interface under Manage > Administration > User interfaces > Collection editor > Basic info > Location in hierarchy bundle.

Moving Records in a Hierarchy
-----------------------------

**Problem**: You want to move objects from one location in a hierarchy to another (document A is currently located in File A, but you want to move it to File B).

**Solution**: As described in the above topic, make sure that the "Location in Hierarchy Bundle" is available:

.. code-block::

   <userInterface code="collection_ui" type="ca_collections">
      <labels>
        <label locale="en_US">
          <name>Collection editor</name>
        </label>
      </labels>
      <screens>
        <screen idno="basic" default="1">
          <labels>
            <label locale="en_US">
              <name>Basic Info</name>
            </label>
          </labels>
          <bundlePlacements>
            <placement code="hierarchy_location">
              <bundle>hierarchy_location</bundle>
            </placement>

If it's not already configured in the profile, insert it through the graphical user interface by visiting: Manage > Administration > User interfaces > Collection editor > Basic info and then choosing "location in hierarchy" from the list of available metadata elements. If the hierarchy is not in the "Collections" table, of course, then navigate to the user interface for the appropriate table.
Then, click on the "move" tab in the hierarchy browser to choose a new location in the hierarchy for your object.

Enabling a "cross-table" Hierarchy
----------------------------------

**Problem**: You want to be able to nest Object records underneath Collections hierarchically.

**Solution**: In app.conf, set:
   ca_objects_x_collections_hierarchy_enabled = 1
   ca_objects_x_collections_hierarchy_relationship_type = part_of

Make sure part_of is defined as a relationship type between objects and collections:

.. code-block::

    <relationshipTable name="ca_objects_x_collections">
      <types>
        <type code="part_of" default="1">
          <labels>
            <label locale="en_US">
              <typename>is part of</typename>
              <typename_reverse>contains</typename_reverse>
            </label>
          </labels>
          <subTypeLeft> </subTypeLeft>
          <subTypeRight></subTypeRight>
        </type>
      </types>
    </relationshipTable>

And back in app.conf, enable:

   ca_collections_show_add_child_control_in_inspector = 1

As with any hierarchical cataloging, you'll need to place the Location in hierarchy bundle on the user interfaces (Objects and Collections), either through the installation profile:

.. code-block::

     <userInterface code="collection_ui" type="ca_collections">
      <labels>
        <label locale="en_US">
          <name>Collection editor</name>
        </label>
      </labels>
      <screens>
        <screen idno="basic" default="1">
          <labels>
            <label locale="en_US">
              <name>Basic Info</name>
            </label>
          </labels>
          <bundlePlacements>
            <placement code="hierarchy_location">
              <bundle>hierarchy_location</bundle>
            </placement>

or the graphical user interface under Manage > Administration > User interfaces > Collection editor > Basic info > Location in hierarchy bundle.

.. note:: Note that in versions prior to 1.7 newly created objects will inherit the collection identifier as the first part of their own identifier. As of version 1.7 you can disable this behavior by setting ca_objects_x_collections_hierarchy_disable_object_collection_idno_inheritance in app.conf.

Launching a New Record ONLY from Within Another Record
------------------------------------------------------

**Problem**: You want to limit a cataloguer's ability to create stand-alone records, for example: a new object can only be created through a Lot.

**Solution**: Set the list item value that should be suppressed from the new menu (i.e. "artwork" which can only be launched from Lots) to "Render in new menu = no" or in the profile via:

.. code-block::
 
   
   <item idno="artwork" enabled="1" default="0">
          <labels>
            <label locale="en_US" preferred="1">
              <name_singular>Artwork</name_singular>
              <name_plural>Artworks</name_plural>
            </label>
          </labels>
          <settings>
            <setting name="render_in_new_menu">0</setting>
          </settings>
        </item>

