Cookbook: Troubleshoot and FAQ
==============================

This section provides some solutions to common problems in CollectiveAccess as well as addresses some of the Frequently Asked Questions about aspects of CollectiveAccess. 

Each scenario in this section begins with a “problem,” describing a certain challenge or question that may occur. There is an accompanying “solution” provided for each problem, which outlines how to carry out the necessary steps to reach a specific outcome. 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online `Support Forum <https://collectiveaccess.org/support/>`_, `Online Chat <https://gitter.im/collectiveaccess/support>`_, `Slack Channel for Developers <https://collectiveacc-uye7574.slack.com/join/signup#/domain-signup>`_, and `Back-end <https://github.com/collectiveaccess/providence>`_ and `Front-end <https://github.com/collectiveaccess/pawtucket2>`_ GitHub Repositories. 

Contents
--------

Missing Relationship Table
--------------------------

**Problem**: You want to create a new relationship type for a specific combination of records, but the table does not show up in the leftmost column under Manage > Administration > Relationship Types.

**Solution**: The error is caused by a missing hierarchy root. If you've updated your database from previous versions, it's possible that the relationship table was added at some point, but the system failed to create the corresponding hierarchy root record in the relationship types table. That record is needed to build the list of tables in the left column of the relationship type list.

The solution is relatively simple: The record must be created by hand using a **mysql query**. First you'll have to find out the table number for the missing table. To do that, take a look at datamodel.conf and look for the name of your table. There will be a line that assigns a 2 or 3-digit number to that table name, like so:

.. code-block::

   "ca_occurrences_x_collections"				= 68,

Now, create a backup of your database. 

Then, using that number, you're going to run the following query on your mysql server. How you do that depends on your setup. Some users will have web tools like PHPMyAdmin at their disposal, some will have to use the MySQL command line or some other query tool.

.. code-block::

   INSERT INTO `ca_relationship_types` (`parent_id`, `sub_type_left_id`, `sub_type_right_id`, `hier_left`, `hier_right`, `table_num`, `type_code`, `rank`, `is_default`) 
   VALUES (NULL,NULL,NULL,1.00000000000000000000,4294967296.00000000000000000000,68,'root_for_68',10,0);

Note that if you're doing this for a different table, you'll want to change the number in two places: In the table_num and type_code columns. The query can be a little hard to read, so make sure you change the right numbers.

After you've run the query, the table should show up in the list. 

Cataloging and Metadata Standards
---------------------------------

Does CollectiveAccess Support DublinCore?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. An installation profile configuring CollectiveAccess as a DublinCore-compliant cataloguing system is provided in the software distribution.

Is CollectiveAccess SPECTRUM Compliant?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CollectiveAccess is an open-source platform, and therefore is not able to participate in the Scheme. CollectiveAccess provides a SPECTRUM installation profile that should be usable ‘out of the box’ for most SPECTRUM-seekers, but is not able to state that the system is ‘SPECTRUM Compliant. 

Does CollectiveAccess Support Other Required Standards? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Implementing support for a data standard – either a recognized standard or one of your own design – is an involved undertaking. You have to consider many details and perform a lot of iterative testing. Fortunately, CA ships with a selection of profiles that can be used as-is, or as a starting point, for your own setup.

For the more popular standards (like DublinCore and PBCore) you should be able to use pre-built installation profiles included with the software. For data standards of your own design, or for projects to which no standard clearly applies, you should be able to use one of the included pre-built installation profiles as a starting point, and configure it as you please. In general, you should never have to start an installation profile from scratch.

Writing an Installation Profile for Other Required Standards? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your first step should be to locate the existing profile that best matches your requirements that is supported already by CollectiveAccess; choose one that can be configured but best suits your needs as-is. Then, make a copy of it, and start editing. Be sure to look both at the profiles included with the CollectiveAccess installer located in **install/profiles**. Then, see Installation Profiles in the CollectiveAccess user manual. 

Choosing an Installation Profile that Can be Configured
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before choosing an installation profile for a system that you will configure to suit our own needs, it is always possible to use a pre-built profile. If you need more guidance, ask questions at support@collectiveaccess.org. 

Once you've found the best match for your project and read the manual, the next steps are:

* Carefully consider the data requirements of your project. Enumerate the data you need to record - the "fields" - and define the required limits on each. By limits we mean things like type ("this field contains a date"), value boundaries ("the date should never be before 1900"), value enumeration ("the value should be one from this proscribed list"), specificity ("this field only applies to objects that are postcards") and repeatability ("each record can take up to 10 date fields").

* Decide where these fields (or "attributes" in CA parlance) live in the CA data model. The CA model includes structures for collection objects and entity (aka "people"), geographic place, and collection (arbitrary groups of objects) authorities. It also includes a generic authority structure - what we call occurrences - that can be used to model any number of additional authorities. Occurrences are typically used to maintain authorities for events, exhibitions and productions (anything that's not an entity, place or collection). The process of linking your attributes to the data model should make it obvious what sorts of occurrences you need (if any).

* Figure out what types of objects, entities, places and collections will be needed. Determining the type lists can be a little tricky: attributes can be restricted to a specific type (implementing the specificity limits mentioned above), and your type lists need to take this into account.

* Define the types or relationships that are possible between objects and the various authorities.

* Specify how user interfaces to edit all of these types and fields work. This includes breaking interfaces for each type of database item into screens and laying out fields on each screen.

* Encode all of this information as an installation profile.

Does CollectiveAccess Support the Art and Architecture Thesaurus?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, CollectiveAccess supports the incorporation of the AAT into any system, and also supports a number of other third-party web-based information services. For instructions on how the AAT works, and how it is incorporated into a CollectiveAccess database, see the user manual. 

Does CollectiveAccess Support the Library of Congress Subject Headings?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, CollectiveAccess supports the incorporation of the LCSH into any system, and also supports a number of other third-party web-based information services. 

Will CollectiveAccess Automatically Generate Accession Numbers?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The multipart ID numbering system in CollectiveAccess provides flexible support for the varied types of numbering systems typically seen in museum and archival work. It is capable of auto-generating unique numbers at both the lot and object (item) level. If CollectiveAccess's standard numbering system does fall short in some way, you can always develop your own numbering plug-in.

Interoperability with Other Systems and Services
------------------------------------------------

Does CollectiveAccess work with Fedora, IRODS, or other Digital Object Repositories?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There was support for storage of CollectiveAccess-hosted media and object item-level metadata in Fedora and IRODS-based repositories in a branch of pre-Version 1.0, however, this never made it into the 1.0 mainline code. We are working to re-implement this functionality for Fedora for version 1.5. There are no plans to restore IRODS support at this time.

What web services are supported when I download? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* the Google Maps service is supported for both generation of maps and translation of addresses into coordinates
* the Amazon S3 storage service is supported experimentally as a replicated storage target
* the Apache SOLR search service is supported as a back-end search engine (can be used in place of the default MySQL-based search engine)
* the GeoNames geographic place name service is supported. Integration includes searching of the GeoNames database and linking of names to any type of record
* the uBio taxonomic name service
* the Library of Congress Subject Heading web service is supported. Integration includes searching of LCSH terms and linking of terms to any type of record

Media Support
-------------

Can I Import Any File Format into CollectiveAccess?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CollectiveAccess can import and convert a fairly long list of image, audio, video, and document formats. These include: JPEG, PNG, TIFF, Photoshop, MP3, MPEG-4 and WAV, and well as many more esoteric formats. For a complete list on the supported media formats page.

Does CollectiveAccess Automatically Generate Derivatives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CollectiveAccess can convert any supported media format into web-viewable derivatives at specified sizes. By default, JPEGs are created for images, PDFs, MP3, and FLV for audio, and MPEG-4 (h.264) and FLV for video. 
JPEG frame previews are also created for video files. The derivative formats, sizes and qualities (compression or bitrate) can all be customized by editing a configuration file.

Can CollectiveAccess watermark images?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CollectiveAccess can add visible watermarks to derivative images. Invisible watermarks are not currently supported, but we are considering support for it in the future.

Does CollectiveAccess Extract Metadata Embedded in Uploaded Media?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. IPTC, XMP, and EXIF metadata are extracted from uploaded images and stored in the database. 

Can CollectiveAccess search text contained within PDF and/or Microsoft Word files?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, so long as you have the appropriate helper applications installed on your server: ABIWord (for extraction of text from Microsoft Word files) and/or PDFToText (for extraction of text from PDF files), or LibreOffice. You'll also need to make sure you've configured your external_applications.conf file with the proper paths to each helper application.

What happens when I upload a file to CollectiveAccess that is not one of the supported filetypes?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Only media that is in a supported format can be uploaded. If CollectiveAccess can’t verify the media file, extract metadata, and produce preview images, then it will reject it. If you need to upload files in unsupported formats to CollectiveAccess:

1. For Developers: Implement a media processing plugin to handle the format.
2. For Non-Developers: Create a metadata element of type File. File elements simply store uploaded files as-is. No attempt is made to identify, verify or process the incoming file.

Configuring the User Interface
------------------------------

How do I Change the Sort Order of List items?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The sort order of list items will be alphabetical by default, unless you declare the default sort value to “rank” and assign ranks for each list value. You can do this from the User Interface, or from within a profile configuration.

To do this in the user interface, find the list you wish to re-order under Manage > Lists & Vocabularies. In the editor for the list, change the “Default sort order” to “by rank” from “by label.” Then return to the hierarchy browser to find the list items. Access each value contained within the list and assign each a numerical rank under “Sort order.” Declare “1” for the first item, “2” for the second, and so on.

If you are establishing rank order within the profile configuration, here is the proper syntax, where defaultSort enables the ranking of values, and Rank sets the sort order for each value:

.. code-block::

   <list code="object_types" hierarchical="1" system="0" vocabulary="0" defaultSort="1">
    <labels>
       <label locale="en_US">
         <name>Item Types</name>
       </label>
     </labels>
     <items>
       <item idno="artwork" rank="1" enabled="1" default="0">
         <labels>
           <label locale="en_US" preferred="1">
             <name_singular>Artwork</name_singular>
             <name_plural>Artworks</name_plural>
           </label>
         </labels>
         </item>
       <item idno="archival_material" rank="2" enabled="1" default="0">
         <labels>
           <label locale="en_US" preferred="1">
             <name_singular>Archival Material</name_singular>
             <name_plural>Archival Materials</name_plural>
           </label>
         </labels>
       </item>
     </items>
   </list>

Editing the Dimensions of a Metadata Element (Field)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can access metadata elements, or fields, for editing by navigating to Manage> Administration > Metadata Elements. A table containing all metadata elements in your profile configuration will be displayed. Select the edit icon for the element you wish to edit. Clicking the red X icon will delete the element altogether and all the data entered in that field system-wide. Once inside the editor for a specific metadata element you will see a menu of choices. You may change the height or width of the field, the minimum/maximum characters allowed in the field entry, and more.

Be careful not to change an element’s datatype if you are working on a live system with data, unless you are absolutely sure. Here, you run the risk of wiping data. If, for example, you change a text field (Datatype: Text) to a List (datatype: List), you will delete all text previously entered in the field.

How can I make a Metadata Element Repeatable, Required, or Restricted by Type? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To bind an element to a specific record type, go to the Type Restrictions menu in a metadata element’s editor. You will find drop-down menus to bind the attribute to: Record table (object, lot, entity, etc.) and Record type (photo, document, image, etc.)

Required/Optional:

“Minimum number of characters”

Setting this to “1” or more will make the element required. Setting it to “0” will make this an optional field. If your element is a list, check “Require value”.

Repeatable/Unrepeatable:

“Maximum number of attributes of this kind that can be associated with an item:”

Setting this to “1” will make this element unrepeatable. To make the element repeatable, select the maximum number of repeats for the element.

Number of placements:

“Minimum number of attribute bundles to show in an editing form.”

This number will determine how many times the element is placed on the editor.

How can I restrict a Relationship bundle placement to a specific record type?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlike metadata elements, you cannot restrict Relationship bundles to a specific record type per se. Instead, if you need to restrict Relationship bundles to a specific record type, you actually make the restriction at the Screen level in the User Interface. Then you repeat the same screen, without the bundle, for the other record types.

Say, for example, your system has two basic object types: Photographs and Objects. You wish for “Related Photographer” (ca_entities) to appear on the Basic Info screen for Photograph records but not Object records. In the profile configuration, you will make two Basic Info screens – one for each type. These screens will be nearly identical, except the screen for Photographs will contain the related entity bundle and the screen for Object will not. Here is the syntax to restrict a Screen to an object type, where “type” equals the item idno for the object type you are restricting the screen to:

.. code-block::
    
      <screen idno="basic_photograph" default="1">
         <labels>
           <label locale="en_US">
             <name>Basic info</name>
           </label>
         </labels>
         <typeRestrictions>
           <restriction code="TypePhotograph" type="photograph"/>
         </typeRestrictions>  
         <bundlePlacements>
           <placement code="idno">
             <bundle>idno</bundle>
           </placement>
           <placement code="preferred_labels">
             <bundle>preferred_labels</bundle>
             <settings>
               <setting name="label" locale="en_US">Title</setting>
             </settings>
           </placement>
           <placement code="ca_entities">
             <bundle>ca_entities</bundle>
             <settings>
               <setting name="label" locale="en_US">Related Photographer</setting>
               <setting name="restrict_to_types">individual</setting>
               <setting name="restrict_to_relationship_types">photographer</setting>
             </settings>
           </placement>
         </bundlePlacements>
       </screen>

