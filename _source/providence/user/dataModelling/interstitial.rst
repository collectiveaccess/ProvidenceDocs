Interstitial Data
=================

.. contents::
   :local:
   
As of version 1.4, CollectiveAccess supports relationship records also known as "interstitial" records. This feature allows cataloguers to describe a relationship beyond simply selecting a relationship type. Let's say, for example, that you have two entities that were married for a period of time, and then got divorced. The relationship record allows you to add a date range, narrative text and/or other metadata elements of your choosing to the interstice between these two individuals. Relationship records are entirely optional, and in fact won't be accessible unless a user interface is defined for the them. Relationship records are not just limited to entities. Any two records can carry this interstitial description, so long as metadata and a user interface has been created. Other common examples of relationships that could require interstitial metadata include objects to places; objects to entities; entities to places, etc.

Setting up relationship records in the installation profile
-----------------------------------------------------------

To create a metadata element with an interstitial type restriction in the profile requires adopting some of the syntax used for relationshipTable names. Here's how you would add the date range on an entity to entity relationship record:

   ::

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
          
After you've defined the metadata elements for your relationship record, you need to create the user interface. This follows the same syntax as the user interfaces for the main tables, except that the user interface "type" is the same string used in the typeRestriction "table" above:

   ::

      <userInterface code="interstitial_entity_ui" type="ca_entities_x_entities">
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
          
Note that these interstitial records are meant to be small and manageable, so only one screen per user interface is supported. If other screens are defined they simply won't appear.

Setting up relationship records through the graphical user interface
--------------------------------------------------------------------

Setting up a relationship record through the GUI is essentially just like creating a user interface for any other type of record. It follows the same steps wherein a metadata element is created and then added to the user interface.

The key difference is what "Type restrictions" are chosen for the elements and what "type" is used to create the user interface.

IMAGE:

The above metadata element will be used for an entity to entity relationship record.

IMAGE: New UI interface.png

The above user interface (created under Manage > Administration > User Interfaces) will be used for an object to storage location relationship record.

Editing Relationship Records
----------------------------

Once your metadata elements and user interface editors have been configured, you will notice a small edit icon on relevant relationships after they've been save the first time:

IMAGE: Paperclip.png

Clicking on the "E" will open the relationship record in an overlay.