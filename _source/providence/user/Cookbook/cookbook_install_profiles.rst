Cookbook: Installation Profiles 
===============================

This section provides some real examples of common challenges that may arise when configuring installation profiles in CollectiveAccess.

Each scenario begins with a “problem,” describing a certain challenge or question that may occur during installation. There is an accompanying “solution” provided for each problem, which outlines how to carry out the necessary steps to reach a specific outcome. 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online Support Forum, Online Chat, Slack Channel for Developers, and Back- and Front-end GitHub Repositories.

Contents
--------

* `Changing a Field’s Repeatability`_
* `Restricting a Field by Type`_
* `Dealing with Subtypes in Type Restrictions`_
* `Creating a Relationship Record`_


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

Problem: You need to style your display so that a.) it only includes a heading when there is content in the field and b.) the heading is in bold text for easier viewing.

Solution: Use an <ifdef> tag to create a conditional heading, and format the text using HTML. When creating a display through the profile be sure to enclose the format template in <![CDATA[ ]] otherwise it will be parsed:

