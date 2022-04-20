Configuring Providence
======================

Providence has many configuration options beyond the initial setup through installation profiles. These options are handle in .conf files in the **app/conf** directory of your Providence installation. You will also find a **/local** folder, where you should create blank copies of files to customize options.

.. ATTENTION::
   ALWAYS create a blank local version of your .conf file in app/conf/local and make edits there. Otherwise your changes can be overwritten.



.. toctree::
   :maxdepth: 2
   :caption: Main Configuration
   :titlesonly:

   App.conf <mainConfiguration/app>
   Browse.conf <mainConfiguration/browse>
   Global.conf <mainConfiguration/global.conf>
   Media_Processing.conf <mainConfiguration/media_processing.conf>
   Multipart_id_numbering.conf <mainConfiguration/multipart_id_numbering>
   Search_indexing.conf <mainConfiguration/search_indexing>


 
.. toctree::
   :maxdepth: 2
   :caption: Other Common Configurations
   :titlesonly:

   Authentication.conf <otherCommon/authentication>
   DateTime.conf <otherCommon/datetime>
   Dimensions.conf <otherCommon/dimensions.conf>
   External_Applications.conf <otherCommon/external_applications>
   Library_Services.conf <otherCommon/library_services.conf>
   OAI_Harvester.conf <otherCommon/oai_harvester.conf>
   OAI_Provider.conf <otherCommon/oai_provider.conf>
   Prepopulate.conf <otherCommon/prepopulate>
   Search.conf <otherCommon/search>
   Visualization.conf <otherCommon/visualization.conf>


.. toctree::
   :maxdepth: 2
   :caption: Rarely Edited Configuration Files
   :titlesonly:

   Attribute_Presets.conf <rarelyEdited/attribute_presets.conf>
   Default_Media_Icons.conf <rarelyEdited/default_media_icons.conf>
   External_Exports.conf <rarelyEdited/external_exports.conf>
   Linked_Data.conf <rarelyEdited/linked_data.conf>
   Media_Display.conf <rarelyEdited/media_display>
   Media_Metadata.conf <rarelyEdited/media_metadata.conf>
   Navigation.conf <rarelyEdited/navigation.conf>
   Replication.conf <rarelyEdited/replication.conf>
   Services.conf <rarelyEdited/services.conf>
   Statistics.conf <rarelyEdited/statistics.conf>
   Translations.conf <rarelyEdited/translations.conf>
   
.. toctree::
   :maxdepth: 2
   :caption: Developer Reference Only
   :titlesonly:

   Annotation_types.conf <developer/annotation_types.conf>
   Assets.conf <developer/assets.conf>
   Attribute_Types.conf <developer/attribute_types.conf>
   Datamodel.conf <developer/datamodel.conf>
   File_Volumes.conf <developer/file_volumes.conf>
   Find_Navigation.conf <developer/find_navigation.conf>
   Media_Volumes.conf <developer/media_volumes.conf>
   Monitor.conf <developer/monitor.conf>
   User_Actions.conf <developer/user_actions.conf>
   User_Pref_Defs.conf <developer/user_pref_defs.conf>