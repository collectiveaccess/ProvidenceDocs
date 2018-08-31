app.conf
========

WHAT: This is the main application configuration file for Providence, designed so that users can easy manage various system-wide settings in one convenient location.

WHEN TO CUSTOMIZE:  App.conf handles most customizations that are not controlled through the UI or profile (with the notable exceptions of: browse, id number configurations, and additional settings for dates, media and search). This document is broken into the following sections: Disable, Hierarchies, Titles & Ids, Search, Feature Settings, Access Control, Styling, Mapping, System Defaults, Media, Admin Configuration and Export.

                    
Menus
-----
                             
Control the "New" and "Find" menus in Providence                           


Menu bar preferences
^^^^^^^^^^^^^^^^^^^^


By default each of the follow record types has a sub-menu in the top-level "New" menu
list out the configured types. When you choose a type the creation of new record of that type
is initiated. If you have several types configured sub-menus make sense, but if your setup only
has one or two types, or is deeply nested then you may want to push the first level of types
directly onto the menu. Setting the directives below will force the first level of the sub-menu onto
the "new" menu itself.

.. code-block:: none

	ca_object_lots_no_new_submenu = 0
	ca_objects_no_new_submenu = 0
	ca_entities_no_new_submenu = 0
	ca_collections_no_new_submenu = 0
	ca_loans_no_new_submenu = 0
	ca_movements_no_new_submenu = 0
	ca_tours_no_new_submenu = 0
	ca_object_representations_no_new_submenu = 0

Find menu formatting
^^^^^^^^^^^^^^^^^^^^

By default only the top-level item classes ("objects", "entities", "collections") appear in the find menu
Set the following to a non-zero value to break out each top-level item into a submenu with types
This allows you do to type-specific searches and browses

.. code-block:: none

	ca_objects_breakout_find_by_type_in_submenu = 0
	ca_object_lots_breakout_find_by_type_in_submenu = 0
	ca_object_representations_breakout_find_by_type_in_submenu = 0
	ca_entities_breakout_find_by_type_in_submenu = 0
	ca_places_breakout_find_by_type_in_submenu = 0
	ca_occurrences_breakout_find_by_type_in_submenu = 0
	ca_collections_breakout_find_by_type_in_submenu = 0
	ca_loans_breakout_find_by_type_in_submenu = 0
	ca_movements_breakout_find_by_type_in_submenu = 0
	ca_sets_breakout_find_by_type_in_submenu = 1

Set the following to a non-zero value to put types directly into the find menu, replacing the top-level item class
This allows you do to type-specific searches and browses where the types are treated as generic top-level items

.. code-block:: none

	ca_objects_breakout_find_by_type_in_menu = 0
	ca_object_lots_breakout_find_by_type_in_menu = 0
	ca_object_representations_breakout_find_by_type_in_menu = 0
	ca_entities_breakout_find_by_type_in_menu = 0
	ca_places_breakout_find_by_type_in_menu = 0
	ca_occurrences_breakout_find_by_type_in_menu = 1
	ca_collections_breakout_find_by_type_in_menu = 0
	ca_loans_breakout_find_by_type_in_menu = 0
	ca_movements_breakout_find_by_type_in_menu = 0
	ca_sets_breakout_find_by_type_in_menu = 0

Navigation options
^^^^^^^^^^^^^^^^^^

If you only want to allow users to create new records with top-level types for
a give item type, set the appropriate directive below to 1; if set users will still be able
to create records for sub-types, but only from within an existing record with a top-level types
This can be useful if you have a system where sub-types need to be subsidiary to top-level records -
eg. sub-type records need to have a top-level parent and cannot exist on their own

.. code-block:: none

	ca_objects_navigation_new_menu_shows_top_level_types_only = 0
	ca_entities_navigation_new_menu_shows_top_level_types_only = 0
	ca_places_navigation_new_menu_shows_top_level_types_only = 0
	ca_occurrences_navigation_new_menu_shows_top_level_types_only = 0
	ca_collections_navigation_new_menu_shows_top_level_types_only = 0
	ca_object_lots_navigation_new_menu_shows_top_level_types_only = 0
	ca_storage_locations_navigation_new_menu_shows_top_level_types_only = 0
	ca_loans_navigation_new_menu_shows_top_level_types_only = 0
	ca_movements_navigation_new_menu_shows_top_level_types_only = 0
	ca_object_representations_navigation_new_menu_shows_top_level_types_only = 0

You can enumerate the types and sub-types shown in the new menu below. 

.. code-block:: none

	ca_objects_navigation_new_menu_limit_types_to = []
	ca_entities_navigation_new_menu_limit_types_to = []
	ca_places_navigation_new_menu_limit_types_to = []
	ca_occurrences_navigation_new_menu_limit_types_to = []
	ca_collections_navigation_new_menu_limit_types_to = []
	ca_object_lots_navigation_new_menu_limit_types_to = []
	ca_storage_locations_navigation_new_menu_limit_types_to = []
	ca_loans_navigation_new_menu_limit_types_to = []
	ca_movements_navigation_new_menu_limit_types_to = []
	ca_object_representations_navigation_new_menu_limit_types_to = []


Show/Hide Representations
^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you want representations enabled for relationship purposes but don't want
to have the option to create or edit them as free-standing records. You can control
whether the object representations, when enabled in general above, show up in the "new"
and "find" menus using the directives below. Set them to a non-zero value to remove
object representations from the specified menu.

.. code-block:: none

	ca_object_representations_dont_show_in_new_menu = 0
	ca_object_representations_dont_show_in_find_menu = 0


Show/Hide Tables
^^^^^^^^^^^^^^^^

If you don't want certain modules to show up in the "New" menu, you can disable them
here. They will still be searchable and can be created using QuickAdd or direct links
(e.g. in the editor inspector of a related record, like an Object created from a Lot)

.. code-block:: none

	ca_objects_dont_show_in_new_menu = 0
	ca_entities_dont_show_in_new_menu = 0
	ca_places_dont_show_in_new_menu = 0
	ca_occurrences_dont_show_in_new_menu = 0
	ca_collections_dont_show_in_new_menu = 0
	ca_object_lots_dont_show_in_new_menu = 0
	ca_storage_locations_dont_show_in_new_menu = 0
	ca_loans_dont_show_in_new_menu = 0
	ca_movements_dont_show_in_new_menu = 0

Menu bar caching
^^^^^^^^^^^^^^^^

Caching the menu bar can significantly increase performance
If you are developing a profile. caching can prevent you from seeing profile
changes in real-time, however. So you can disable it here if need be. When using
the system "in production" it is usually best to leave this enabled

.. code-block:: none

	do_menu_bar_caching = 0
                                    
Menus
-----
                                 
Turn off (or on) various features and database areas.
                  
Editor "disable" switches
^^^^^^^^^^^^^^^^^^^^^^^^^

If you're not using certain editors in your system (you don't catalogue places for example)
you can disable the menu items for them by setting the various *_disable directives below to a non-zero value

.. code-block:: none

	ca_objects_disable = 0
	ca_entities_disable = 0
	ca_places_disable = 0
	ca_occurrences_disable = 0
	ca_collections_disable = 0
	ca_object_lots_disable = 0
	ca_storage_locations_disable = 0
	ca_loans_disable = 0
	ca_movements_disable = 1
	ca_tours_disable = 1
	ca_tour_stops_disable = 1
	ca_object_representations_disable = 1

QuickAdd disable switches
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	ca_objects_disable_quickadd = 0
	ca_entities_disable_quickadd = 0
	ca_places_disable_quickadd = 0
	ca_occurrences_disable_quickadd = 0
	ca_collections_disable_quickadd = 0
	ca_object_lots_disable_quickadd = 0
	ca_storage_locations_disable_quickadd = 0
	ca_loans_disable_quickadd = 0
	ca_movements_disable_quickadd = 0

Disable "Add new <object> to lot" 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(in the object lot editor inspector)

.. code-block:: none

	disable_add_object_to_lot_inspector_controls = 0

Show related counts in the inspector?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	ca_objects_show_related_counts_in_inspector_for = []
	ca_entities_show_related_counts_in_inspector_for = [ca_objects]
	ca_places_show_related_counts_in_inspector_for = []
	ca_occurrences_show_related_counts_in_inspector_for = [ca_objects]
	ca_collections_show_related_counts_in_inspector_for = [ca_objects]
	ca_storage_locations_show_related_counts_in_inspector_for = []
	ca_loans_show_related_counts_in_inspector_for = []
	ca_movements_show_related_counts_in_inspector_for = []
	ca_tour_stops_show_related_counts_in_inspector_for = []

Show "add child record" control in editor inspector?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	ca_objects_show_add_child_control_in_inspector = 0
	ca_entities_show_add_child_control_in_inspector = 0
	ca_places_show_add_child_control_in_inspector = 1
	ca_occurrences_show_add_child_control_in_inspector = 0
	ca_collections_show_add_child_control_in_inspector = 1
	ca_storage_locations_show_add_child_control_in_inspector = 1
	ca_loans_show_add_child_control_in_inspector = 0
	ca_movements_show_add_child_control_in_inspector = 0
	ca_tour_stops_show_add_child_control_in_inspector = 0

Set duplication disable
^^^^^^^^^^^^^^^^^^^^^^^

If you want to disable the ability to duplicate all items in a set across the board set this

.. code-block:: none

	ca_sets_disable_duplication_of_items = 0

Set type controls
^^^^^^^^^^^^^^^^^

.. code-block:: none

	enable_set_type_controls = 0

Hierarchies
-----------

Settings for hierarchical properties and display.

Strict type hierarchies
^^^^^^^^^^^^^^^^^^^^^^^

When fully enabled, top-level records may only be created with top-level types, and sub-records may only be created
with types that are direct sub-types of the parent's type. This ensures conformance with the type hierarchy. So
if you have an object type hierarchy like this:

Book
	Page
		Figure
			Frontspiece

... then top-level records can only be of type "Book." Sub-records of books may only be "Page" or "Frontspiece";
and sub-records of "Page" can be "Figure." "Frontspiece" may not take sub-records.

We partially enabled, top-level records may only be created with top-level types, but sub-records may be of *any*
type below the top-level type, not just direct sub-types. In the example above, the sub-records of a "book" can be
of type "Page", "Figure" or Frontspiece; sub-records of a "Page" may be only of type "Figure."

When disabled, all types are allowed anywhere.

The type hierarchy behavior can be independently for each type of hierarchical record.
Set to 1 to fully enable, 0 to disable and ~ (tilde character) to partially enable restrictions.

.. code-block:: none

	ca_objects_enforce_strict_type_hierarchy = 0
	ca_entities_enforce_strict_type_hierarchy = 0
	ca_places_enforce_strict_type_hierarchy = 0
	ca_occurrences_enforce_strict_type_hierarchy = 0
	ca_collections_enforce_strict_type_hierarchy = 0
	ca_storage_locations_enforce_strict_type_hierarchy = 0
	ca_loans_enforce_strict_type_hierarchy = 0
	ca_tour_stops_enforce_strict_type_hierarchy = 0
	ca_list_items_enforce_strict_type_hierarchy = 0

Hierarchy browser items
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	ca_objects_hierarchy_browser_display_settings = ^ca_objects.preferred_labels.name (^ca_objects.idno)
	ca_object_lots_hierarchy_browser_display_settings = ^ca_object_lots.preferred_labels (^ca_object_lots.idno_stub)
	ca_entities_hierarchy_browser_display_settings = ^ca_entities.preferred_labels (^ca_entities.idno)
	ca_places_hierarchy_browser_display_settings = ^ca_places.preferred_labels (^ca_places.idno)
	ca_occurrences_hierarchy_browser_display_settings = ^ca_occurrences.preferred_labels (^ca_occurrences.idno)
	ca_collections_hierarchy_browser_display_settings = ^ca_collections.preferred_labels (^ca_collections.idno)
	ca_list_hierarchy_browser_display_settings = ^ca_lists.preferred_labels.name (^ca_lists.list_code)
	ca_list_items_hierarchy_browser_display_settings = ^ca_list_items.preferred_labels.name_plural (^ca_list_items.idno)
	ca_storage_locations_hierarchy_browser_display_settings = ^ca_storage_locations.preferred_labels (^ca_storage_locations.idno)
	ca_tour_stops_hierarchy_browser_display_settings = ^ca_tour_stops.preferred_labels (^ca_tour_stops.idno)
	ca_relationship_types_hierarchy_browser_display_settings = ^ca_relationship_types.preferred_labels (^ca_relationship_types.type_code)
	ca_loans_hierarchy_browser_display_settings = ^ca_loans.preferred_labels (^ca_loans.idno)
	ca_movements_hierarchy_browser_display_settings = ^ca_movements.preferred_labels (^ca_movements.idno)

.. code-block:: none

	ca_objects_hierarchy_browser_sort_values = [ca_objects.idno_sort]
	ca_objects_hierarchy_browser_sort_direction = asc
	ca_object_lots_hierarchy_browser_sort_values = [ca_object_lots.idno_stub_sort]
	ca_object_lots_hierarchy_browser_sort_direction = asc
	ca_entities_hierarchy_browser_sort_values = [ca_entities.preferred_labels.surname, ca_entities.preferred_labels.forename]
	ca_entities_hierarchy_browser_sort_direction = asc
	ca_places_hierarchy_browser_sort_values = [ca_places.rank, ca_places.preferred_labels.name_sort]
	ca_places_hierarchy_browser_sort_direction = asc
	ca_occurrences_hierarchy_browser_sort_values = [ca_occurrences.preferred_labels.name_sort]
	ca_occurrences_hierarchy_browser_sort_direction = asc
	ca_collections_hierarchy_browser_sort_values = [ca_collections.rank, ca_collections.preferred_labels.name_sort]
	ca_collections_hierarchy_browser_sort_direction = asc
	ca_list_items_hierarchy_browser_sort_values = [ca_list_items.preferred_labels.name_sort_plural]
	ca_list_items_hierarchy_browser_sort_direction = asc
	ca_list_items_hierarchy_browser_disabled_items_mode = disabled
	ca_storage_locations_hierarchy_browser_sort_values = [ca_storage_locations.rank, ca_storage_locations.preferred_labels.name_sort]
	ca_storage_locations_hierarchy_browser_sort_direction = asc
	ca_storage_locations_hierarchy_browser_disabled_items_mode = disabled
	ca_tour_stops_hierarchy_browser_sort_values = [ca_tour_stops.preferred_labels.name_sort]
	ca_tour_stops_hierarchy_browser_sort_direction = asc
	ca_relationship_types_hierarchy_browser_sort_values = [ca_relationship_types.preferred_labels.typename]
	ca_relationship_types_hierarchy_browser_sort_direction = asc
	ca_loans_hierarchy_browser_sort_values = [ca_loans.preferred_labels.name_sort]
	ca_loans_hierarchy_browser_sort_direction = asc
	ca_movements_hierarchy_browser_sort_values = [ca_movements.preferred_labels.name_sort]
	ca_movements_hierarchy_browser_sort_direction = asc

Collection hierarchies on the Summary screen 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The summary screen includes a visual hierarchy by default for hierarchical collections. 
Use these directives to set the sort value for the hierarchical display, as well as the display
template used for format data. If nothing is set below the system will default to the settings
outlined in ca_collections_hierarchy_browser_sort_values.
            
.. code-block:: none
                                      
	ca_collections_hierarchy_summary_display_settings =
	ca_collections_hierarchy_summary_sort_values =
	ca_objects_hierarchy_summary_display_settings =
	ca_collections_hierarchy_summary_show_full_object_hierarachy = 0

Show/Hide hierarchy root (Storage Locations & Places)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hide hierarchy root for storage locations or places in New and Find screens
Note that if you haven't added any items to the hierarchies yet, enabling
this might prevent you from doing so (because you can't select a parent).

.. code-block:: none

	ca_storage_locations_hierarchy_browser_hide_root = 0
	ca_places_locations_hierarchy_browser_hide_root = 0
                          
Show/Hide child records in search/browse results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Normally all results, regardless of their position in a hierarchy are displayed
in search/browse results. Set this option for alternative policies. Possible
settings are:
		show			= 	show all results by default; allow user to filter children if they wish
		hide			=   hide all child records (those that are not at the top of their hierarchy) by default; allow user to remove filtering if desired
		alwaysShow 		=	show all results; do not allow filtering
		alwaysHide		=	hide all child records; do not allow the user to disable filtering

"alwaysShow" is the default.

While this option may be set for any table, it is typically used only for objects.

.. code-block:: none

	ca_objects_children_display_mode_in_results = alwaysShow

Enable display of collections and objects as a single hierarchy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	ca_objects_x_collections_hierarchy_enabled = 1
	ca_objects_x_collections_hierarchy_relationship_type =
	ca_objects_x_collections_hierarchy_disable_object_collection_idno_inheritance = 

Titles + IDs
------------
                                                    
Set whether or not titles and identifiers are required and unique.                                                      

Require input id number value to conform to format? (0=no, 1=yes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	require_valid_id_number_for_ca_objects = 0
	require_valid_id_number_for_ca_object_lots = 0
	require_valid_id_number_for_ca_entities = 1
	require_valid_id_number_for_ca_places = 1
	require_valid_id_number_for_ca_collections = 1
	require_valid_id_number_for_ca_occurrences = 1
	require_valid_id_number_for_ca_loans = 0
	require_valid_id_number_for_ca_movements = 0
	require_valid_id_number_for_ca_tours = 0
	require_valid_id_number_for_ca_tour_stops = 0
	require_valid_id_number_for_ca_object_representations = 0
	require_valid_id_number_for_ca_storage_locations = 0

Allow dupe id numbers? (0=no, 1=yes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	allow_duplicate_id_number_for_ca_objects = 1
	allow_duplicate_id_number_for_ca_object_lots = 1
	allow_duplicate_id_number_for_ca_entities = 1
	allow_duplicate_id_number_for_ca_places = 1
	allow_duplicate_id_number_for_ca_collections= 1
	allow_duplicate_id_number_for_ca_occurrences= 1
	allow_duplicate_id_number_for_ca_list_items= 1
	allow_duplicate_id_number_for_ca_loans= 0
	allow_duplicate_id_number_for_ca_movements= 0
	allow_duplicate_id_number_for_ca_tours= 0
	allow_duplicate_id_number_for_ca_tour_stops= 0
	allow_duplicate_id_number_for_ca_object_representations = 1
	allow_duplicate_id_number_for_ca_storage_locations = 1

Allow dupe labels? (0=no, 1=yes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If set to no, then atttempting to save records with a label already
in use by another record will fail

.. code-block:: none

	allow_duplicate_labels_for_ca_objects = 1
	allow_duplicate_labels_for_ca_object_lots = 1
	allow_duplicate_labels_for_ca_entities = 0
	allow_duplicate_labels_for_ca_places = 1
	allow_duplicate_labels_for_ca_collections= 0
	allow_duplicate_labels_for_ca_occurrences= 0
	allow_duplicate_labels_for_ca_storage_locations= 1
	allow_duplicate_labels_for_ca_list_items= 1
	allow_duplicate_labels_for_ca_loans = 1
	allow_duplicate_labels_for_ca_movements= 1
	allow_duplicate_labels_for_ca_object_representations= 1
	allow_duplicate_labels_for_ca_relationship_types= 1
	allow_duplicate_labels_for_ca_set_items= 1
	allow_duplicate_labels_for_ca_search_forms= 1
	allow_duplicate_labels_for_ca_bundle_displays= 1
	allow_duplicate_labels_for_ca_metadata_alert_rules = 1
	allow_duplicate_labels_for_ca_editor_uis= 1
	allow_duplicate_labels_for_ca_editor_ui_screens= 1
	allow_duplicate_labels_for_ca_tours= 1
	allow_duplicate_labels_for_ca_tour_stops= 1

Entity dupe name?
^^^^^^^^^^^^^^^^^
Set this to 1 if you want to display a warning when a new entity with
a name that already exists (preferred or nonpreferred) is about to be created

.. code-block:: none
	ca_entities_warn_when_preferred_label_exists = 0

Require preferred label? (0=no, 1=yes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If set to yes, then attempting to save records without a preferred label
will fail. If set to no (default) then attempting to save a record without
a preferred label will automatically set the preferred label to "[BLANK]"

.. code-block:: none

	require_preferred_label_for_ca_objects = 0
	require_preferred_label_for_ca_object_lots = 0
	require_preferred_label_for_ca_entities = 0
	require_preferred_label_for_ca_places = 0
	require_preferred_label_for_ca_collections = 0
	require_preferred_label_for_ca_occurrences = 0
	require_preferred_label_for_ca_storage_locations = 0
	require_preferred_label_for_ca_list_items = 0
	require_preferred_label_for_ca_loans = 0
	require_preferred_label_for_ca_movements = 0
	require_preferred_label_for_ca_object_representations = 0
	require_preferred_label_for_ca_relationship_types = 0
	require_preferred_label_for_ca_set_items = 0
	require_preferred_label_for_ca_search_forms = 0
	require_preferred_label_for_ca_bundle_displays = 0
	require_preferred_label_for_ca_editor_uis = 0
	require_preferred_label_for_ca_editor_ui_screens = 0
	require_preferred_label_for_ca_tours = 0
	require_preferred_label_for_ca_tour_stops = 0

Require preferred label value be present in a list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If set to a valid list code then any entered label value must match
a preferred label for an item in that list.

.. code-block:: none

	preferred_label_for_ca_objects_must_be_in_list =
	preferred_label_for_ca_object_lots_must_be_in_list = 
	preferred_label_for_ca_entities_must_be_in_list = 
	preferred_label_for_ca_places_must_be_in_list = 
	preferred_label_for_ca_collections_must_be_in_list = 
	preferred_label_for_ca_occurrences_must_be_in_list = 
	preferred_label_for_ca_storage_locations_must_be_in_list = 
	preferred_label_for_ca_list_items_must_be_in_list = 
	preferred_label_for_ca_loans_must_be_in_list = 
	preferred_label_for_ca_movements_must_be_in_list = 
	preferred_label_for_ca_object_representations_must_be_in_list = 
	preferred_label_for_ca_relationship_types_must_be_in_list = 
	preferred_label_for_ca_set_items_must_be_in_list = 
	preferred_label_for_ca_search_forms_must_be_in_list = 
	preferred_label_for_ca_bundle_displays_must_be_in_list = 
	preferred_label_for_ca_editor_uis_must_be_in_list = 
	preferred_label_for_ca_editor_ui_screens_must_be_in_list = 
	preferred_label_for_ca_tours_must_be_in_list = 
	preferred_label_for_ca_tour_stops_must_be_in_list = 

Allow automated renumbering objects with lot idno + sequence number?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(when object number don't conform to that format)

If you're managing lots with related object-level records and the lot and
object numbering get out of sync (because you change the lot number after
the fact, for example) then this can be useful. But it can also be dangerous in the
sense that letting cataloguers renumber sets of objects at a click may not be the
idea. Only enable this if you need it. Keep in mind that the automated renumbering format
is fixed at lot <lot identifier> + <separator> + <sequential number starting from one>. So if
your lot number is 2010.10 and your separator is '.', then objects will be numbered 2010.10.1,
2010.10.2, 2010.10.3, etc.

.. code-block:: none

	allow_automated_renumbering_of_objects_in_a_lot = 0

Label-less objects
^^^^^^^^^^^^^^^^^^

If you don't want to specify preferred labels for objects set this to a non-zero value
This can be useful for collections where individual items lack working names, such as in
paleontology.

.. code-block:: none

	ca_objects_dont_use_labels = 0

Label-specific sort
^^^^^^^^^^^^^^^^^^^

Set to assume a specific language when generating sortable titles regardless of the locale set for the title. This can be useful when content 
has been entered specific (or accurate) locale settings. The value can be a specific locale (Ex. "en_US") or a language code (Ex. "en") 

.. code-block:: none

	use_locale_for_sortable_titles =

Search
------

Search engine configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	search_engine_plugin = SqlSearch

Browse Panel Styles 
^^^^^^^^^^^^^^^^^^^
(for best results, choose a number between 1 and 5)

.. code-block:: none

	browse_row_size = 4

Quicksearch - order and results ("live" search in search box in header)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What sorts of results does Quicksearch return?
List table names here to include them in the search, in the order they should appear. This is only the default 
display configuration, which can be overriden by user preferences. Syntax is ca_table/type, i.e ca_objects/video

.. code-block:: none

	quicksearch_default_results = [ca_objects, ca_entities, ca_places, ca_occurrences, ca_collections, ca_object_lots, ca_storage_locations, ca_loans, ca_movements, ca_tours, ca_tour_stops]

Quicksearch - break out by type?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What table types are broken out in the result list? Syntax is list within square brackets, i.e [ca_objects, ca_entities]

.. code-block:: none

	quicksearch_breakout_by_type = 
    
Restrict facets shown to specific facet groups?

.. code-block:: none

	<table_name>_browse_facet_group limits facets on the main browse landing page
	<table_name>_refine_facet_group limits facets in the "refine" browse on detail pages
	<table_name>_search_refine_facet_group limits facets in the "refine" browse on search results

.. code-block:: none

	ca_objects_browse_facet_group = main
	ca_objects_refine_facet_group = refine
	ca_objects_search_refine_facet_group = refine
          
One table search 
^^^^^^^^^^^^^^^^

If set to a controller in the "find" module, will use that for quicksearch rather
than the regular "Quicksearch" controller. This is useful for having the Quicksearch
operate on a single table

.. code-block:: none

	one_table_search =
					   
Out of process search indexing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Switch to disable out of process search indexing

.. code-block:: none

	disable_out_of_process_search_indexing = 0

Hostname to use when triggering out of process indexing
By default the site hostname configured in setup.php is used but you can override it
here if the hostname resolvable on the server differs from that used for incoming requests
out_of_process_search_indexing_hostname =

Caption formatting for search/browse "thumbnail" results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set a display template here to customize display of captions under thumbnails in the thumbnail result view. The 
template will be evaluated relative to each record in the result set.

.. code-block:: none

	ca_objects_results_thumbnail_caption_template = ^ca_objects.preferred_labels.name%truncate=27&ellipsis=1<br/><l>^ca_objects.idno</l>
	ca_occurrences_results_thumbnail_caption_template = ^ca_occurrences.preferred_labels.name%truncate=27&ellipsis=1<br/><l>^ca_occurrences.idno</l>
	ca_entities_results_thumbnail_caption_template = ^ca_entities.preferred_labels.name%truncate=27&ellipsis=1<br/><l>^ca_entities.idno</l>
	ca_collections_results_thumbnail_caption_template = ^ca_collections.preferred_labels.name%truncate=27&ellipsis=1<br/><l>^ca_collections.idno</l>
								 
Features
--------

Settings related to various features such as: location tracking, deaccessioning, WorldCat, check in/check out and more.                                       

Location tracking options
^^^^^^^^^^^^^^^^^^^^^^^^^

Direct object-location reference storage location tracking
(also set this for movement-based storage location tracking)

.. code-block:: none

	object_storage_location_tracking_relationship_type =  

Movement-based storage location tracking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	movement_storage_location_tracking_relationship_type = 
	movement_object_tracking_relationship_type = 
	record_movement_information_when_moving_storage_location = 0
	movement_storage_location_date_element =   

Deaccession options
^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	deaccession_force_access_private = 1
	deaccession_dont_allow_editing = 0
	deaccession_use_disposal_date = 1

Library-style check-out of objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: none

	enable_library_services = 0
	enable_object_checkout = 0

User generated content
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	enable_user_generated_content = 1

ResourceSpace import
^^^^^^^^^^^^^^^^^^^^
The ResourceSpace data importer allows records and media to be imported from a ResourceSpace Installation
The importer connects using a username and API Key that is unique to that user and can be found in the
edit user page under the Admin > Manage Users tab in ResourceSapce

Also required is the base URL for your ResourceSpace installation which all API calls are based on
This should be your root url + /api/

.. code-block:: none

	resourcespace_apis = {
		EXAMPLE_CARE_SYSTEM = {
			resourcespace_label = ,
			resourcespace_base_api_url = ,
			resourcespace_user = 
		}
	}

WorldCat import
^^^^^^^^^^^^^^^

The data importer can access OCLC WorldCat via either their web service API or Z39.50 service.
Using the web service API requires that PHP be installed with libCURL support. Using Z39.50
requires that PHP be built with libyaz support (http://www.indexdata.com/yaz). Many PHP installations
have libCURL installed by default; most do not have libyaz installed.

The importer will connect ia Z39.50 if a username and password are configured below and libyaz is available, otherwise
the web service API will be used as a fallback, assuming a valid API key is configured below and libCURL is available.

.. code-block:: none

	worldcat_api_key = MY_WORLDCAT_API_KEY
	worldcat_z39.50_user =
	worldcat_z39.50_password =

Optionally mark WorldCat items already present in system using ISBN
To enable set "worlcat_isbn_element_code" to the ca_objects metadata element code containing the ISBN code for the book.
worlcat_isbn_element_code =

Display template used to format "ISBN present" message. Evaluated relative to the existing object. 
You can use standard display template codes (eg. ^ca_objects.idno) to display details about the match.

.. code-block:: none

	worlcat_isbn_exists_template = <span class="caWorldCatExistingObjectIcon"><l><i class="fa fa-external-link" aria-hidden="true"></i></span></l>

Template formatting the "key" displayed below WorldCat query results. Use this to define any icons used  in the "worlcat_isbn_exists_template"

.. code-block:: none

	worlcat_isbn_exists_key = <div class="caWorldCatExistingObjectKey"><i class="fa fa-external-link" aria-hidden="true"></i> = Previously imported</div>

Taxonomy web services
^^^^^^^^^^^^^^^^^^^^^
To access the uBio taxonomic name service (http://www.ubio.org)
via a 'Taxonomy' attribute you must enter your uBio API keycode here
If you don't care about taxonomy (or even know what is it) then leave this as-is

.. code-block:: none

	ubio_keycode = enter_your_keycode_here

Flickr API
^^^^^^^^^^
.. code-block:: none

	flickr_api_key =

"Rich text" (aka. wysiwyg) editor options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can read more about available text editor options here: http://docs.cksource.com/CKEditor_4.x/Developers_Guide/Toolbar

Defines options available in the toolbar

.. code-block:: none

	wysiwyg_editor_toolbar = {
		formatting = [Bold, Italic, Underline, Strike, -, Subscript, Superscript, Font, FontSize, TextColor],
		lists = [-, NumberedList, BulletedList, Outdent, Indent, Blockquote],
		links = [Link, Unlink, Anchor],
		misc = [SelectAll, Undo, Redo, -, Source, Maximize, Image, CALink]
	}

Defines options available in the toolbar

.. code-block:: none

	wysiwyg_content_editor_toolbar = {
		formatting = [Bold, Italic, Underline, Strike, -, Subscript, Superscript, Font, FontSize, TextColor],
		lists = [-, NumberedList, BulletedList, Outdent, Indent, Blockquote],
		links = [Link, Unlink, Anchor],
		misc = [SelectAll, Undo, Redo, -, Source, Maximize, Media, CALink]
	}

Enable dependent field visibility feature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See here for more information: http://docs.collectiveaccess.org/wiki/Dependent_Field_Visibility

.. code-block:: none

	enable_dependent_field_visibility = 0

Global template values (Pawtucket content management)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Globals are text values that may be set in the Pawtucket web UI and substituted
into any view template, including headers and footers. Values defined here 
will be editable in the "Global Values Editor" (available to users with the can_edit_theme_global_values priv)
and usable in templates under their name (Eg. {{{operating_hours}}} in the example below).

Options controlling how the editor displays the value may be set for each global. Width and height control the size 
of the element; usewysiwygeditor enables a "wysiwyg" rich text editor for formatted text.

.. code-block:: none

	global_template_values = {
		hours_of_operation = {
			name = Hours of operation,
			description = List current operating hours here,
			width = 600px,
			height = 150px,
			usewysiwygeditor = 0
		}
	}

Site page templates (Pawtucket content management)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Allow PHP code in content-managed site pages

By default only value tags in the form {{{tag-name}}} are allowed in Pawtucket site page templates. 
If you need the flexibility and power afforded by direct embedding of PHP code in your templates
set this option to a non-zero value. Note that enabling this option will allow execution of ANY
code embedded in the template on EVERY page load. Depending upon your point of view this is either a
feature or a security hole. It doesn't have to be a problem, but keep it in mind...

Note that this setting only affects page previews in Providence. To allow PHP code execution in Pawtucket
you must also set this option in your theme.

.. code-block:: none

	allow_php_in_site_page_templates = 0

Access Control
^^^^^^^^^^^^^^

Structural mechanisms that control who can see what, and how (optional).
                                                                
Bundle-level access control
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none
	default_bundle_access_level = __CA_BUNDLE_ACCESS_EDIT__

Type-level access control
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	perform_type_access_checking = 0
	default_type_access_level = __CA_BUNDLE_ACCESS_EDIT__

Source-level access control
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	perform_source_access_checking = 0
	default_source_access_level = __CA_BUNDLE_ACCESS_EDIT__

Item-level access control
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	perform_item_level_access_checking = 0
	default_item_access_level = __CA_ACL_EDIT_DELETE_ACCESS__

You can control item-level access control support
for each type of item using these directives

.. code-block:: none

	ca_objects_dont_do_item_level_access_control = 0
	ca_object_lots_dont_do_item_level_access_control = 0
	ca_entities_dont_do_item_level_access_control = 0
	ca_places_dont_do_item_level_access_control = 0
	ca_occurrences_dont_do_item_level_access_control = 0
	ca_collections_dont_do_item_level_access_control = 0
	ca_lists_dont_do_item_level_access_control = 0
	ca_list_items_dont_do_item_level_access_control = 0
	ca_loans_dont_do_item_level_access_control = 0
	ca_movements_dont_do_item_level_access_control = 0
	ca_object_representations_dont_do_item_level_access_control = 0
	ca_representation_annotations_dont_do_item_level_access_control = 0
	ca_storage_locations_dont_do_item_level_access_control = 0
	ca_tours_dont_do_item_level_access_control = 0
	ca_tour_stops_dont_do_item_level_access_control = 0

Defaults for collection-to-object ACL inheritance settings
	Set to 1 to make default to inherit; 0 for default to be no inheritance
	
.. code-block:: none
	
	ca_collections_acl_inherit_from_parent_default = 0
	ca_objects_acl_inherit_from_ca_collections_default = 0
	ca_objects_acl_inherit_from_parent_default = 0

Administrator
^^^^^^^^^^^^^
User_id to consider "administrator" - not subject to access control measures.
By default, user_id=1 is considered administrator for convenience and compatbility with older
installations. You can make any user_id "administrator" if you want, however, if disable this completely
by setting it to a blank value.

.. code-block:: none

	administrator_user_id = 1

email user when account is activated in Manage > Access control?

.. code-block:: none

	email_user_when_account_activated = 0

Set Access
^^^^^^^^^^
If you want all users to see all sets regardless of ownership or access control set this to one
(Yes, some people apparently want to do this)

.. code-block:: none

	ca_sets_all_users_see_all_sets = 0

"Access" inheritance
^^^^^^^^^^^^^^^^^^^^
Allows child records to receive the "access" field value of their immediate parent. This can be useful when
you generally want child record access to mirror that of the parent, but with occasional cataloguer-defined exceptions

Currently only supported for ca_objects

.. code-block:: none

	ca_objects_allow_access_inheritance = 0

Default inheritance status for newly created ca_objects records

.. code-block:: none

	ca_objects_access_inheritance_default = 1

Styling
-------
Controls for visual elements such as logos, colors, etc. within the application and exported reports and labels       

Theme configuration
^^^^^^^^^^^^^^^^^^^
To display your logo in the menu bar, upload it to the graphics/logos/ folder in the Default theme
directory and enter the filename below.  For the best results, your logo must not exceed
45 pixels in height.  To change the menu color, enter the six digit HTML color code below
and omit the leading '' sign.

.. code-block:: none

	header_img = menu_logo.png
	menu_color = ffffff
	footer_color = ffffff
	login_logo = ca_logo.png

Search Result Reporting configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To display your logo at the top of a PDF report, upload it to the graphics/logos/ folder in all themes
directory and enter the filename below.  To change the header color (report_color) and header text color (report_text_color), enter the six digit HTML color code below
and omit the leading '' sign.

.. code-block:: none

	report_header_enabled = 1
	report_img = menu_logo.png
	report_color = FFFFFF
	report_text_color = 000000

The following options control what additional information can be printed on your PDF reports. Enter a non-zero
value to include the following information.

.. code-block:: none

	report_show_timestamp = 1
	report_show_number_results = 1
	report_representation_version = preview
	report_show_search_term = 1

Record PDF Summary configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To display your logo at the top of a PDF report, upload it to the graphics/logos/ folder in all themes
directory and enter the filename below.  To change the header color (summary_color) and header text color (summary_text_color), enter the six digit HTML color code below
and omit the leading '' sign.

.. code-block:: none

	summary_header_enabled = 1
	summary_page_numbers = 1
	summary_footer_enabled = 1
	summary_img = ca_wide.png
	summary_color = FFFFFF
	summary_text_color = 000000
	summary_footer_color = FFFFFF
	summary_footer_text_color = 000000

The following options control what additional information can be printed on your PDF summary. Enter a non-zero
value to include the following information.

.. code-block:: none

	summary_show_identifier = 1
	summary_show_timestamp = 1

/* Image path for icon to display when no image is available in thumbnail view */
/* Image must be uploaded to graphics/buttons in your theme folder */

.. code-block:: none

	no_image_icon = glyphicons_138_picture.png

Print labels (ie. stickers)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
As of CollectiveAccess version 1.5 a new label generator is available that is easier to
configure and customize. The new generator uses HTML/CSS to specify the layout of label formats,
unlike the old system which uses a set of complex configuration files. Any existing
label formats you wish to use with the new generator must be completely reimplemented. There is
no automated conversion process.

.. code-block:: none

	Set this if you want a dashed border around all printed labels
	add_print_label_borders = 0

Annotation options
^^^^^^^^^^^^^^^^^^
element code of ca_representation_annotation list metadata element that should be used to classify and color code annotations

.. code-block:: none

	annotation_class_element =

Additional theme
^^^^^^^^^^^^^^^^
theme to use when user is not logged in (when they're logged in their preferred theme is used)

.. code-block:: none

	theme = default
	themes_directory = <ca_base_dir>/themes
	themes_url = <ca_url_root>/themes
	views_directory = <themes_directory>/<theme>/views

Mapping
-------

Settings for GeoNames and Mapping plugins (Google Maps/Open Layers)


GeoNames web services
^^^^^^^^^^^^^^^^^^^^^

To access the GeoNames services for geographic names
via a 'GeoNames' attribute you must enter your GeoNames username and password
here. You can get a free account at http://www.geonames.org/login. After
you confirmed your registration you have to enable your account for web
service usage at http://www.geonames.org/manageaccount, otherwise the search
won't return any results.
If you don't care about GeoNames (or even know what is it) then leave this as-is

.. code-block:: none

	geonames_user = enter_your_username_here

The api.geonames.org URL should not be changed if you're using the free GeoNames
web service. The free offering should be sufficient for most users. If you have
a paid/premium account, geonames provides you with a list of additional hostnames
available for use over https here: http://www.geonames.org/account
Enter one of those hostnames to make use of your premium subscription

.. code-block:: none

	geonames_api_base_url = http://api.geonames.org

Mapping plugins
^^^^^^^^^^^^^^^

Name of plugin class to use for mapping
	Currently supported values: OpenLayers, Leaflet

OpenLayers is deprecated. Use Leaflet unless you have a reason to do otherwise.
mapping_plugin = Leaflet

**Leaflet options**
Show zoom in/out control
``leaflet_maps_show_scale_controls = 1``

Path color for polygons and circles
``leaflet_maps_path_color = "0000cc"``

Path weight (in pixels) for polygons and circles
``leaflet_maps_path_weight = 2``

Path opacity for polygons and circles (0 is transparent, 1 is opaque)
``leaflet_maps_path_opacity = 0.6``

Fill color for polygons and circles
``leaflet_maps_fill_color = "ff0000"``

Fill opacity for polygons and circles (0 is transparent, 1 is opaque)
``leaflet_maps_fill_opacity = 0.1``

URL for base layer when using Leaflet mapping plugin
See https://leaflet-extras.github.io/leaflet-providers/preview/ for previews of various base maps

``leaflet_base_layer = https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}{r}.png``

**OpenLayers options**
Tile to use for base layer; Ex. OpenLayers.Layer.OSM() [OpenStreetMaps] or OpenLayers.Layer.Stamen('toner') [Stamen 'Toner' theme]

``openlayers_base_layer = OpenLayers.Layer.OSM()``

Radius, in pixels, of plotted points
``openlayers_point_radius = 5``

Fill color (hex) for points and regions
``openlayers_fill_color = ffcc66``

Stroke width, in pixels, for points, regions and paths
``openlayers_stroke_width = 2``

Stroke color (hex) for points, regions and paths
``openlayers_stroke_color = ff9933``

 Fill color (hex) for points and regions when selected
``openlayers_fill_color_selected = 66ccff``

 Stroke color (hex) for points regions and paths when selected
``openlayers_stroke_color_selected = 3399ff``

**Generic mapping options**
Attribute object records to use to map search results

``ca_objects_map_attribute = georeference``

Defaults
--------
                                 
System defaults to control layouts, displays, templates and more.

Related item lookup settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	ca_objects_lookup_settings = [<unit relativeTo='ca_objects'>^ca_object_representations.media.icon (^ca_objects.idno) ^ca_objects.preferred_labels</unit>]
	ca_objects_lookup_delimiter =
	ca_objects_lookup_relationship_type_position = right
	ca_objects_lookup_sort = _natural;ca_objects.idno_sort
	ca_objects_lookup_relationship_type_editable = 0

	ca_object_lots_lookup_settings = [^ca_object_lots.preferred_labels (^ca_object_lots.idno_stub)]
	ca_object_lots_lookup_delimiter = ➔
	ca_object_lots_lookup_relationship_type_position = right
	ca_object_lots_lookup_sort = _natural;ca_object_lots.idno_stub_sort
	ca_object_lots_lookup_relationship_type_editable = 0

	ca_entities_lookup_settings = [^ca_entities.preferred_labels]
	ca_entities_lookup_delimiter = ➔
	ca_entities_lookup_relationship_type_position = right
	ca_entities_lookup_sort = _natural;ca_entity_labels.name_sort
	ca_entities_lookup_relationship_type_editable = 0

	ca_places_lookup_settings =  [^ca_places.hierarchy.preferred_labels.name%maxLevelsFromBottom=4]
	ca_places_lookup_delimiter =  ➔
	ca_places_lookup_relationship_type_position = right
	ca_places_lookup_sort = _natural;ca_places.idno_sort
	ca_places_lookup_relationship_type_editable = 0

	ca_occurrences_lookup_settings = [^ca_occurrences.preferred_labels]
	ca_occurrences_lookup_delimiter = ➔
	ca_occurrences_lookup_relationship_type_position = right
	ca_occurrences_lookup_sort = _natural;ca_occurrences.idno_sort
	ca_occurrences_lookup_relationship_type_editable = 0

	ca_collections_lookup_settings = [^ca_collections.preferred_labels (^ca_collections.idno)]
	ca_collections_lookup_delimiter = ➔
	ca_collections_lookup_relationship_type_position = right
	ca_collections_lookup_sort = _natural;ca_collections.idno_sort
	ca_collections_lookup_relationship_type_editable = 0

	ca_storage_locations_lookup_settings = [^ca_storage_locations.hierarchy.preferred_labels.name]
	ca_storage_locations_lookup_delimiter = ➔
	ca_storage_locations_lookup_relationship_type_position = right
	ca_storage_locations_lookup_sort = _natural;ca_storage_locations.idno_sort
	ca_storage_locations_lookup_relationship_type_editable = 0

	ca_list_items_lookup_settings = [^ca_list_items.hierarchy.preferred_labels.name_plural]
	ca_list_items_lookup_delimiter = ➔
	ca_list_items_lookup_relationship_type_position = right
	ca_list_items_lookup_sort = _natural;ca_list_items.idno_sort
	ca_list_items_lookup_relationship_type_editable = 0

	ca_relationship_types_lookup_settings = [^ca_relationship_types.parent.preferred_labels ➔ ^ca_relationship_types.preferred_labels (^ca_relationship_types.type_code)]
	ca_relationship_types_lookup_delimiter = ➔
	ca_relationship_types_lookup_sort = _natural;ca_relationship_types.type_code

	ca_loans_lookup_settings = [^ca_loans.preferred_labels]
	ca_loans_lookup_delimiter = ➔
	ca_loans_lookup_relationship_type_position = right
	ca_loans_lookup_sort = _natural;ca_loans.idno_sort
	ca_loans_lookup_relationship_type_editable = 0

	ca_movements_lookup_settings = [^ca_movements.preferred_labels]
	ca_movements_lookup_delimiter = ➔
	ca_movements_lookup_relationship_type_position = right
	ca_movements_lookup_sort = _natural;ca_movements.idno_sort
	ca_movements_lookup_relationship_type_editable = 0

	ca_users_lookup_settings = [^ca_users.fname ^ca_users.lname (^ca_users.email)]
	ca_users_lookup_delimiter = ➔
	ca_users_lookup_sort = _natural;ca_users.user_name

	ca_user_groups_lookup_settings= [^ca_user_groups.name]
	ca_user_groups_lookup_delimiter = ➔
	ca_user_groups_lookup_sort = _natural;ca_user_groups.code

	ca_tours_lookup_settings = [^ca_tours.preferred_labels]
	ca_tours_lookup_delimiter = ➔
	ca_tours_lookup_sort = _natural;ca_tours.tour_code

	ca_tour_stops_lookup_settings = [^ca_tour_stops.preferred_labels]
	ca_tour_stops_lookup_delimiter = ➔
	ca_tour_stops_lookup_sort = _natural;ca_tour_stops.idno_sort
	ca_tour_stops_lookup_relationship_type_editable = 0

	ca_object_representations_lookup_settings = [^ca_object_representations.media.icon ^ca_object_representations.preferred_labels]
	ca_object_representations_lookup_delimiter = ➔
	ca_object_representations_lookup_sort = _natural;ca_object_representations.idno_sort
	ca_object_representations_lookup_relationship_type_editable = 0

	ca_representation_annotations_lookup_settings = [^ca_representation_annotations.preferred_labels.name]
	ca_representation_annotations_lookup_delimiter = ➔
	ca_representation_annotations_lookup_sort = _natural

	ca_sets_lookup_settings = [^ca_sets.preferred_labels.name (^ca_sets.set_code)]
	ca_sets_lookup_delimiter = ➔
	ca_sets_lookup_sort = _natural

	ca_object_checkouts_lookup_settings = [^ca_objects.preferred_labels.name (^ca_objects.idno) <i>Borrowed on ^ca_object_checkouts.checkout_date%timeOmit=1 by ^ca_users.fname ^ca_users.lname</i>]
	ca_object_checkouts_lookup_delimiter = ➔

Default bundle display templates for related bundles (Eg. ca_entities, ca_occurrences, etc.)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	ca_objects_default_bundle_display_template = <unit relativeTo="ca_objects"><l>^ca_objects.preferred_labels.name</l> (^relationship_typename)</unit>
	ca_entities_default_bundle_display_template = <unit relativeTo="ca_entities"><l>^ca_entities.preferred_labels.displayname</l> (^relationship_typename)</unit>
	ca_places_default_bundle_display_template = <unit relativeTo="ca_places"><l>^ca_places.preferred_labels.name</l> (^relationship_typename)</unit> 
	ca_occurrences_default_bundle_display_template = <unit relativeTo="ca_occurrences"><l>^ca_occurrences.preferred_labels.name</l> (^relationship_typename)</unit>
	ca_object_lots_default_bundle_display_template = <unit relativeTo="ca_object_lots"><l>^ca_object_lots.preferred_labels.name</l> (^ca_object_lots.idno_stub)</unit>
	ca_storage_locations_default_bundle_display_template = <unit relativeTo="ca_storage_locations"><l>^ca_storage_locations.preferred_labels.name</l> (^relationship_typename)</unit>
	ca_loans_default_bundle_display_template = <unit relativeTo="ca_loans"><l>^ca_loans.preferred_labels.name</l> (^relationship_typename)</unit>
	ca_movements_default_bundle_display_template = <unit relativeTo="ca_movements"><l>^ca_movements.preferred_labels.name</l> (^relationship_typename)</unit>
	ca_object_representations_default_bundle_display_template = <unit relativeTo="ca_object_representations" delimiter="<br/>"><l>^ca_object_representations.media.thumbnail</l><br/><l>^ca_object_representations.preferred_labels.name</l> (^relationship_typename)</unit>
	ca_list_items_default_bundle_display_template = <unit relativeTo="ca_list_items"><l>^ca_list_items.preferred_labels.name_plural</l> (^relationship_typename)</unit>

Default template for media viewer caption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: none

	media_overlay_titlebar_template = "^ca_objects.preferred_labels.name <ifdef code='ca_objects.idno'>(^ca_objects.idno)</ifdef>"

Label type lists
^^^^^^^^^^^^^^^^

Labels, both preferred and non-preferred, for primary items (objects, entities, etc.)
can include a type. By default the range of types is defined by a list named for the item.
For objects, the types for preferred labels are object_label_types_preferred while the
non-preferred label types are defined by the object_label_types list. You can set other
lists for each kind of label below. If you don't want to use types for a given category of
label set it to an empty list.

.. code-block:: none

	ca_objects_preferred_label_type_list = object_label_types_preferred
	ca_objects_nonpreferred_label_type_list = object_label_types
	ca_object_lots_preferred_label_type_list = object_lot_label_types_preferred
	ca_object_lots_nonpreferred_label_type_list = object_lot_label_types
	ca_entities_preferred_label_type_list = entity_label_types_preferred
	ca_entities_nonpreferred_label_type_list = entity_label_types
	ca_places_preferred_label_type_list = place_label_types_preferred
	ca_places_nonpreferred_label_type_list = place_label_types
	ca_collections_preferred_label_type_list = collection_label_types_preferred
	ca_collections_nonpreferred_label_type_list = collection_label_types
	ca_occurrences_preferred_label_type_list = occurrence_label_types_preferred
	ca_occurrences_nonpreferred_label_type_list = occurrence_label_types
	ca_loans_preferred_label_type_list = loan_label_types_preferred
	ca_loans_nonpreferred_label_type_list = loan_label_types
	ca_movements_preferred_label_type_list = movement_label_types_preferred
	ca_movements_nonpreferred_label_type_list = movement_label_types
	ca_storage_locations_preferred_label_type_list = storage_location_label_types_preferred
	ca_storage_locations_nonpreferred_label_type_list = storage_location_label_types
	ca_list_items_preferred_label_type_list = list_item_label_types_preferred
	ca_list_items_nonpreferred_label_type_list = list_item_label_types
	ca_object_representations_preferred_label_type_list = object_representation_label_types_preferred
	ca_object_representations_nonpreferred_label_type_list = object_representation_label_types
	ca_representation_annotation_preferred_label_type_list = representation_annotation_label_types_preferred
	ca_representation_annotation_nonpreferred_label_type_list = representation_annotation_label_types
                                     
Default to summary when opening item for editing?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	ca_objects_editor_defaults_to_summary_view = 0
	ca_object_lots_editor_defaults_to_summary_view = 0
	ca_entities_editor_defaults_to_summary_view = 0
	ca_places_editor_defaults_to_summary_view = 0
	ca_occurrences_editor_defaults_to_summary_view = 0
	ca_collections_editor_defaults_to_summary_view = 0
	ca_lists_editor_defaults_to_summary_view = 0
	ca_list_items_editor_defaults_to_summary_view = 0
	ca_loans_editor_defaults_to_summary_view = 0
	ca_movements_editor_defaults_to_summary_view = 0
	ca_storage_locations_editor_defaults_to_summary_view = 0
	ca_object_representations_editor_defaults_to_summary_view = 0
	ca_tours_editor_defaults_to_summary_view = 0
	ca_tour_stops_editor_defaults_to_summary_view = 0
	ca_representation_annotations_defaults_to_summary_view = 0

Find defaults
^^^^^^^^^^^^^

.. code-block:: none

	items_per_page_options_for_ca_objects_search = [12,24,36,48]
	items_per_page_default_for_ca_objects_search = 24
	view_default_for_ca_objects_search = list

	items_per_page_options_for_ca_object_lots_search = [15,30,45]
	items_per_page_default_for_ca_object_lots_search = 30
	view_default_for_ca_object_lots_search = list
	enable_full_thumbnail_result_views_for_ca_object_lots_search = 0

	items_per_page_options_for_ca_entities_search = [15,30,45]
	items_per_page_default_for_ca_entities_search = 30
	view_default_for_ca_entities_search = list
	enable_full_thumbnail_result_views_for_ca_entities_search = 0

	items_per_page_options_for_ca_places_search = [15,30,45]
	items_per_page_default_for_ca_places_search = 30
	view_default_for_ca_places_search = list

	items_per_page_options_for_ca_occurrences_search = [15,30,45]
	items_per_page_default_for_ca_occurrences_search = 30
	view_default_for_ca_occurrences_search = list
	enable_full_thumbnail_result_views_for_ca_occurrences_search = 0

	items_per_page_options_for_ca_collections_search = [15,30,45]
	items_per_page_default_for_ca_collections_search = 30
	view_default_for_ca_collections_search = list
	enable_full_thumbnail_result_views_for_ca_collections_search = 0

	items_per_page_options_for_ca_storage_locations_search = [15,30,45]
	items_per_page_default_for_ca_storage_locations_search = 30
	view_default_for_ca_storage_locations_search = list

	items_per_page_options_for_ca_objects_browse = [12,24,36,48]
	items_per_page_default_for_ca_objects_browse = 24
	view_default_for_ca_objects_browse = list

	items_per_page_options_for_ca_object_lots_browse = [15,30,45]
	items_per_page_default_for_ca_object_lots_browse = 30
	view_default_for_ca_object_lots_browse = list
	enable_full_thumbnail_result_views_for_ca_object_lots_browse = 0

	items_per_page_options_for_ca_entities_browse = [15,30,45]
	items_per_page_default_for_ca_entities_browse = 30
	view_default_for_ca_entities_browse = list
	enable_full_thumbnail_result_views_for_ca_entities_browse = 0

	items_per_page_options_for_ca_places_browse = [15,30,45]
	items_per_page_default_for_ca_places_browse = 30
	view_default_for_ca_places_browse = list

	items_per_page_options_for_ca_occurrences_browse = [15,30,45]
	items_per_page_default_for_ca_occurrences_browse = 30
	view_default_for_ca_occurrences_browse = list
	enable_full_thumbnail_result_views_for_ca_occurrences_browse = 0

	items_per_page_options_for_ca_collections_browse = [15,30,45]
	items_per_page_default_for_ca_collections_browse = 30
	view_default_for_ca_collections_browse = list
	enable_full_thumbnail_result_views_for_ca_collections_browse = 0

	items_per_page_options_for_ca_storage_locations_browse = [15,30,45]
	items_per_page_default_for_ca_storage_locations_browse = 30
	view_default_for_ca_storage_locations_browse = list

	items_per_page_options_for_ca_loans_browse = [15,30,45]
	items_per_page_default_for_ca_loans_browse = 30
	view_default_for_ca_loans_browse = list

	items_per_page_options_for_ca_movements_browse = [15,30,45]
	items_per_page_default_for_ca_movements_browse = 30
	view_default_for_ca_movements_browse = list

	items_per_page_options_for_ca_lists_browse = [15,30,45]
	items_per_page_default_for_ca_lists_browse = 30
	view_default_for_ca_lists_browse = list

	items_per_page_options_for_ca_list_items_browse = [15,30,45]
	items_per_page_default_for_ca_list_items_browse = 30
	view_default_for_ca_list_items_browse = list

	items_per_page_options_for_ca_tours_browse = [15,30,45]
	items_per_page_default_for_ca_tours_browse = 30
	view_default_for_ca_tours_browse = list

	items_per_page_options_for_ca_tour_stops_browse = [15,30,45]
	items_per_page_default_for_ca_tour_stops_browse = 30
	view_default_for_ca_tour_stops_browse = list

	items_per_page_options_for_ca_object_representations_browse = [15,30,45]
	items_per_page_default_for_ca_object_representations_browse = 30
	view_default_for_ca_object_representations_browse = list

Set item display templates
^^^^^^^^^^^^^^^^^^^^^^^^^^
Used to format records in set item lists when no specific formatting has been specified

.. code-block:: none

	ca_objects_set_item_display_template = ^ca_objects.preferred_labels.name (^ca_objects.idno)
	ca_object_lots_set_item_display_template = ^ca_object_lots.preferred_labels.name (^ca_object_lots.idno_stub)
	ca_entities_set_item_display_template = ^ca_entities.preferred_labels.displayname
	ca_places_set_item_display_template = ^ca_places.preferred_labels.name
	ca_occurrences_set_item_display_template = ^ca_occurrences.preferred_labels.name
	ca_collections_set_item_display_template = ^ca_collections.preferred_labels.name
	ca_loans_set_item_display_template = ^ca_loans.preferred_labels.name 
	ca_movements_set_item_display_template = ^ca_movements.preferred_labels.name
	ca_storage_locations_set_item_display_template = ^ca_storage_locations.preferred_labels.name
	ca_object_representations_set_item_display_template = ^ca_object_representations.preferred_labels.name
	ca_list_items_set_item_display_template = ^ca_list_itmes.preferred_labels.name_plural (^ca_list_items.idno)
	ca_tours_set_item_display_template = ^ca_tours.preferred_labels.name
	ca_tour_stops_set_item_display_template = ^ca_tour_stops.preferred_labels.name

enable this to always show a default bundle preview for attribute bundles,
even if the display template for that particular element isn't set

.. code-block:: none

	always_show_bundle_preview_for_attributes = 0

Default type to use when creating sets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(in search results "sets" options, for example)

.. code-block:: none

	ca_sets_default_type = user

Timecode output
^^^^^^^^^^^^^^^

Controls how timecode values are displayed
Valid settings are:
	COLON_DELIMITED = format with colons. Ex. 1:20:10
	HOURS_MINUTES_SECONDS = format with h/m/s labels. Ex. 1h 20m 10s
	RAW = the number of seconds in the interval. Ex. 4810

.. code-block:: none

	timecode_output_format = COLON_DELIMITED

Currency settings
^^^^^^^^^^^^^^^^^

By default currency values using the "$" symbol are considered to be in US dollars.
You can change that here to another currency using its standard 3-letter code.
Ex. CDN = Canadian dollars

.. code-block:: none

	default_dollar_currency = USD

Length settings
^^^^^^^^^^^^^^^
Use Unicode fraction glyphs such as (ex. ¼) in place of the text equivalent (ex. 1/4)

As of version 1.7.6 these settings are DEPRECATED. In a future version these settings will be removed.
Use the settings in the dimensions.conf configuration file if possible.

.. code-block:: none

	use_unicode_fractions_for_measurements = 1
	force_use_of_fractions_for_measurements = 0

Record duplication
^^^^^^^^^^^^^^^^^^
By default duplicated records have the word "duplicate" appended to their preferred label. You can disable this behavior by setting this option.

.. code-block:: none

	dont_mark_duplicated_records_in_preferred_label = 0

Log options
^^^^^^^^^^^
By default a timestamp is shown for every change in the record-based change log.
Enable this to limit the display to the date of the change.

.. code-block:: none

	dont_show_timestamp_in_change_log = 0


When deleting an item it is possible to move any references to or from that item to another. 
Alternatively references can be deleted with the item. The system-wide default behavior may be set here 
and will be used when the user has not set a preference.
Valid options are "remove" or "transfer"
Note that you can set per-table defaults by prefacing "delete_reference_handling_default" with a table name. 
(For example, "ca_objects_delete_reference_handling_default")

.. code-block:: none

	delete_reference_handling_default = remove

Components
^^^^^^^^^^^

.. code-block:: none

	ca_objects_container_types = []
	ca_objects_component_types = []
	ca_objects_component_display_settings = <l>^ca_objects.preferred_labels.name</l> (^ca_objects.idno)

Media
-----

Media processing tweaks
^^^^^^^^^^^^^^^^^^^^^^^
If you have the PECL Imagick extension installed on your server
and don't want to use it with CollectiveAccess (it has a bad habit of choking and crashing
on some types of files) you can force CA to ignore it by setting 'dont_use_imagick' to 1; leave it
set to zero if you want to use Imagick. When Imagick works, it performs well so you should give it a try
and see how it works before disabling support for it.

.. code-block:: none

	dont_use_imagick = 0


If you have ImageMagick or GraphicsMagick installed and PDFs are being inexplicably rejected try setting the corresponding
option to 1. It has been observed that ImageMagick chokes on some PDFs. Setting this option will force CA to use Zend_PDF
to identify uploaded PDF's, which often resolves the issues at the expense of greater memory consumption.

.. code-block:: none

	dont_use_imagemagick_to_identify_pdfs = 0
	dont_use_graphicsmagick_to_identify_pdfs = 0

If you're mostly dealing with large video files or images and don't care about PDF support (or you're using Graphics/ImageMagick
for identifying PDFs), you can disable Zend PDF support here. Zend PDF always tries to load the whole fine into memory,
which for video files can be several GB and usually results in memory_limit errors.

.. code-block:: none

	dont_use_zendpdf_to_identify_pdfs = 1

CollectiveAccess supports three methods for generating PDF output for download and printing: dompdf (slower; built-in), 
wkhtmltopdf (faster; requires additional software installation) and phantomjs (faster; requires additional software installation). 
By default it will favor using wkhtmltopdf if available, falling back to phantomjs and then to dompdf which is always available. 

You can override the build in preference and force the use of a specific PDF generator by uncommenting and setting this 
option to one of the following:
		wkhtmltopdf, phantomjs, dompdf 
		
.. code-block:: none
		
	use_pdf_renderer = wkhtmltopdf

Only media than can be identified by a plugin may be uploaded. If you want to be able to upload any file
and have it treated as media, even if the internals of the file cannot be parsed set this to a non-zero value.
When set the BinaryFile media plugin is enabled, which will store any unidentifiable uploaded file as binary data.
No previews or in-browser viewing will be possible for these files.

.. code-block:: none

	accept_all_files_as_media = 0

PHPs builtin function exif_read_data (http://php.net/manual/en/function.exif-read-data.php) is known to cause
unexpected crashes with some files in some versions of PHP, particularly those shipped with RedHat or CentOS Linux.
If you experience any weird behavior while processing large files with extensive EXIF metadata, try enabling this setting.
If enabled, CollectiveAccess tries to extract metadata using alternate sources like exiftool or GraphicsMagick.

.. code-block:: none

	dont_use_exif_read_data = 0

Alternatively if you experiencing out-of-memory issues while importing media it may well be due to very large EXIF
metadata blocked embedded in the file. You can limit the size of metadata to be imported here by specifying the threshold in bytes (Eg. 1048576 = 1mb)

.. code-block:: none

	dont_use_exif_read_data_if_larger_than = 2097152

Files with large embedded metadata blocks may cause out-of-memory errors and/or complicate backup of the datase. You can 
limit the size of embedded metadata to be extracted during media loading here by specifying the threshold in bytes (Eg. 1048576 = 1mb)
Extraction of embedded metadata for media with metadata exceeding the threshold will be skipped. Set to zero or omit  if you want all metadata 
regardless of length to be extracted.

.. code-block:: none

	dont_extract_embedded_media_metdata_when_length_exceeds = 2097152

If you wish to allow the importing of object representation media and icons via http, https and ftp urls set this to 1.
Letting users employ your CA installation as a proxy for downloading arbitrary URLs could be seen as a security hole in
some cases, so enable this option only if you really need it.

.. code-block:: none

	allow_fetching_of_media_from_remote_urls = 0

If you wish to allow the linking to existing object representations in the manner other relationships
set the relevant directives below to 1. Using representations as records that can be targets of
relationships can be confusing and, well, odd for many common setups. Still, when you need this behavior
you need it, so here it is :-)

.. code-block:: none

	ca_objects_allow_relationships_to_existing_representations = 0
	ca_object_lots_allow_relationships_to_existing_representations = 0
	ca_entities_allow_relationships_to_existing_representations = 0
	ca_places_allow_relationships_to_existing_representations = 0
	ca_occurrences_allow_relationships_to_existing_representations = 0
	ca_collections_allow_relationships_to_existing_representations = 0
	ca_storage_locations_allow_relationships_to_existing_representations = 0
	ca_list_items_allow_relationships_to_existing_representations = 0
	ca_loans_allow_relationships_to_existing_representations = 0
	ca_movements_allow_relationships_to_existing_representations = 0

If you have OpenCV (http://www.opencv.org) and PHP-facedetect (http://www.xarg.org/project/php-facedetect/) installed
on your server and want CA to try and crop images to include faces set this to a non-zero value. Note that detection
can slow image processing significantly and isn't 100% accurate.

.. code-block:: none

	enable_face_detection_for_images = 0

Video preview frame generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can have CA generate preview frames from uploaded video
These settings control how (and if) the preview frames are generated

Should we generate frames? (Set to 1 for yes, 0 for no)

.. code-block:: none

	video_preview_generate_frames = 1

The minimum number of preview frames to generate in any situation
CA will adjust timing parameters to ensure at least this number of frames is generated.

.. code-block:: none

	video_preview_min_number_of_frames = 10

The maximum number of preview frames to generate in any situation
CA will always stop generating frames when it hits this limit

.. code-block:: none

	video_preview_max_number_of_frames = 100

The time between extracted frames; you can enter this is timecode notation (eg. 10s = 10 seconds; 1:10 = 1 minute, 10  seconds)

.. code-block:: none

	video_preview_interval_between_frames = 30s

The time relative to the start of the video at which to start extracting preview frames; this can be used to ensure you don't generate frames from blank leader footage

.. code-block:: none

	video_preview_start_at = 2s

The time interval relative to the end of the video at which to stop extracting preview frames; this can be used to ensure you don't generate frames from blank footage at the end of a video

.. code-block:: none

	video_preview_end_at = 2s

The time relative to the start of the video at which the "main" video poster preview is being extracted.
Express as an absolute time (Ex. 1h 5m 3s) or as a precentage of duration (Ex. 50%)

.. code-block:: none

	video_poster_frame_grab_at = 5s

Document preview page generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can have CA generate preview page images from uploaded documents (only PDFs currently)
These settings control how (and if) the preview pages are generated

Should we generate pages? (Set to 1 for yes, 0 for no)

.. code-block:: none

	document_preview_generate_pages = 1

The maximum number of preview pages to generate in any situation
CA will always stop generating page images when it hits this limit

.. code-block:: none

	document_preview_max_number_of_pages = 500

The number of pages between extracted pages; set to 1 if you want to generate all pages; set to 10 if you only want to generate every 10th page

.. code-block:: none

	document_preview_interval_between_pages = 1

The page number at which to start extracting pages

.. code-block:: none

	document_preview_start_page = 1

Resolution to rasterize PDF pages with, in DPI

.. code-block:: none

	document_preview_resolution = 300

JPEG quality to rasterize PDF pages with (0-100)

.. code-block:: none

	document_preview_quality = 95

Set to non-zero value if you do not wish to generate representation annotation previews
These previews are discrete audio/video files covering a given annotation.

.. code-block:: none

	dont_generate_annotation_previews = 1

Batch media processing
^^^^^^^^^^^^^^^^^^^^^^

Root directory of staging area for media import – any media in this
directory will appear in media importer file listings

.. code-block:: none

	batch_media_import_root_directory = <ca_base_dir>/import

Allow data importer to pull media from arbitrary directories using paths
in the data to be imported. If you don't trust the data being uploaded (or the people
doing the uploading) leave this set to zero.

.. code-block:: none

	allow_import_of_media_from_any_directory = 0

.. code-block:: none

	mediaFilenameToObjectIdnoRegexes = {
		filename_exactly = {
			displayName = _(Filename exactly),
			regexes = { "^(.*)$" }
		},
		filename_without_extension = {
			displayName = _(Filename without extension),
			regexes = { "(.*?)\\.[A-Za-z0-9]+$" }
		},
		filename_with_page_number_included = {
			displayName = _(Filename with page number - page number included),
			regexes = { "(.*?\\.[A-Za-z0-9\\-]+)\\.[A-Za-z]+$", "(.*?)\\.[A-Za-z0-9]+$" }
		},
		filename_with_page_number = {
			displayName = _(Filename with page number - page number stripped),
			regexes = { "(.*?)\\.[A-Za-z0-9\\-]+\\.[A-Za-z]+$" }
		}
	}

Uncomment and customize the following if you want to transform the names of your media
files using Perl-compatible regular expressions (http://pcre.org). The setting is basically
a wrapper around PHP's preg_replace function (http://php.net/manual/en/function.preg-replace.php).
Each replacement consists of a key (basically a name), a list of "search" regular expressions
(usually 1) and a list of "replace" patterns. Both lists must have the same length, i.e. there must
be a "replace" pattern for each search regular expression. For more information on the syntax,
please refer to the documentation for preg_replace.
Note that the media importer will try to mach the results of these replacements to CollectiveAccess
records using the "mediaFilenameToObjectIdnoRegexes" list above for each file or directory name
IN ADDITION to whatever the original name was. The original file name is matched first.

.. code-block:: none

	mediaFilenameReplacements = {
		replace_period_w_dash = {
			search = { "([A-Za-z0-9]+)\\.([0-9]+)\\.([A-Za-z0-9]+)" },
			replace = { "$1-$2.$3" }
		},
	}

List of fields to attempt to match filename-extracted data on
Matching will be performed on fields in order, with the first matching
record used for import.

You can specify intrinsic field names (Eg. idno), metadata element codes or
"preferred_labels" and "nonpreferred_labels" to match on labels

.. code-block:: none

	batch_media_import_match_on = [idno]

Batch metadata import
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	batch_metadata_import_log_directory = <ca_base_dir>/app/log

Directory to temporarily stash ajax-based uploads of media in

.. code-block:: none

	ajax_media_upload_tmp_directory = <ca_app_dir>/tmp

Max time in seconds to let media live in tmp directory before it can be removed

.. code-block:: none

	ajax_media_upload_tmp_directory_timeout = 86400

Object representation download options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Media versions to provide downloads of

.. code-block:: none

	ca_object_representation_download_versions = [original, large, medium, small]

Set maximum number of files to allow to be downloaded in one go. Leave set to 0 or blank for no limit.
maximum_download_file_count = 

Task queue set up (deferred processing of uploaded media)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	taskqueue_handler_plugins = <ca_lib_dir>/Plugins/TaskQueueHandlers
	taskqueue_tmp_directory = <ca_app_dir>/tmp
	taskqueue_max_opo_processes = 4
	taskqueue_process_timeout = 3600
	taskqueue_max_items_processed_per_session = 100

Admin
-----

Nit picky stuff related to system configuration and administration.                               

Character set to use (usually utf-8; might be ISO-8859-1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	character_set = utf-8

System configuration check options (under "Manage" > "Administrate" > "Configuration Check")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	The configuration check can do a thorough, but time consuming, check of file permissions and other settings.
	These checks can be useful but on some servers, especially those using file systems mounted over a network, they can be very slow.
	If you are on such a server you can disable all "expensive" configuration checks here.

.. code-block:: none

	dont_do_expensive_configuration_checks_in_web_ui = 0

Configuration exporter options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	configuration_export_only_system_displays = 1
	configuration_export_only_system_search_forms = 1

Exclude lists from configuration export with more than a specified number of items. If set to zero no limit is enforced. 

.. code-block:: none

	configuration_export_exclude_lists_larger_than = 0

list of list codes to exclude from configuration export

.. code-block:: none

	configuration_export_exclude_lists = []

Object lot inheritance
^^^^^^^^^^^^^^^^^^^^^^
don't inherit lot relationship from parent object

.. code-block:: none

	ca_objects_dont_inherit_lot_id_from_parent = 0

Restrict editing of codes for list and metadata elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Allowing free editing and code and data type settings can result in invalid configuration.
The ability to edit these values once set can be restricted here.

.. code-block:: none

	ca_lists_dont_allow_editing_of_codes_when_in_use = 0
	ca_list_items_dont_allow_editing_of_codes_when_in_use = 0
	ca_metadata_elements_dont_allow_editing_of_codes_when_in_use = 0
	ca_metadata_elements_dont_allow_editing_of_data_types_when_in_use = 0


SMS notifications
^^^^^^^^^^^^^^^^^

.. code-block:: none

	enable_sms_notifications = 0

Each SMS plugin supports a specific gateway. For now only SendHub.com is supported.

.. code-block:: none

	sms_plugin = SendHub
	sms_user = MY_SENDHUB_USERNAME
	sms_api_key = MY_SENDHUB_API_KEY


Session settings
^^^^^^^^^^^^^^^^

.. code-block:: none

	session_lifetime = 31536000
	session_domain =

Email notifications
^^^^^^^^^^^^^^^^^^^

Settings for  notifications system used for metadata-based alerts

.. code-block:: none

	notification_email_sender = no-reply@<site_hostname>
	notification_email_subject = (<app_display_name>) Metadata Notification from CollectiveAccess

Export
------

File names for data export download files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the given display template doesn't yield a usable result, the exporter falls back to relatively
nondescript defaults single item exports via inspector in the corresponding editor

.. code-block:: none

	ca_objects_single_item_export_filename = ^ca_objects.idno
	ca_object_lots_single_item_export_filename = ^ca_object_lots.idno_stub
	ca_entities_single_item_export_filename = ^ca_entities.idno
	ca_places_single_item_export_filename = ^ca_places.idno
	ca_occurrences_single_item_export_filename = ^ca_occurrences.idno
	ca_collections_single_item_export_filename = ^ca_collections.idno
	ca_lists_single_item_export_filename = ^ca_lists.list_code
	ca_list_items_single_item_export_filename = ^ca_list_items.idno
	ca_loans_single_item_export_filename = ^ca_loans.idno
	ca_movements_single_item_export_filename = ^ca_movements.idno
	ca_object_representations_single_item_export_filename = ^ca_object_representations.idno
	ca_representation_annotations_single_item_export_filename = ^ca_representation.annotations.annotation_id
	ca_storage_locations_single_item_export_filename = ^ca_storage_locations.idno
	ca_tours_single_item_export_filename = ^ca_tours.tour_code
	ca_tour_stops_single_item_export_filename = ^ca_tours_stops.idno

batch exports via sets or browse results

.. code-block:: none

	ca_objects_batch_export_filename = objects_batch_export
	ca_object_lots_batch_export_filename = lots_batch_export
	ca_entities_batch_export_filename = entities_batch_export
	ca_places_batch_export_filename = places_batch_export
	ca_occurrences_batch_export_filename = occurrences_batch_export
	ca_collections_batch_export_filename = collections_batch_export
	ca_lists_batch_export_filename = lists_batch_export
	ca_list_items_batch_export_filename = list_items_batch_export
	ca_loans_batch_export_filename = loans_batch_export
	ca_movements_batch_export_filename = movements_batch_export
	ca_object_representations_batch_export_filename = representations_batch_export
	ca_representation_annotations_batch_export_filename = annotations_batch_export
	ca_storage_locations_batch_export_filename = storage_locations_batch_export
	ca_tours_batch_export_filename = tours_batch_export
	ca_tour_stops_batch_export_filename = tour_stops_batch_export

List of alternate destinations for data exports. The only supported type for now is 'github'.

For GitHub repositories it's highly recommended to *not* enter your main account password
here but to use a personal access token instead. You can create it in the GitHub account
settings under "Applications">"Personal Access Tokens". The token has to have 'repo' access.

.. code-block:: none

	exporter_alternate_destinations = {
		github = {
			type = github,
			display = GitHub repository,
			user credentials
			username = your_github_username,
			token = enter_access_token_here,
			repository information
			owner = enter_repository_owner,
			repository = collectiveaccess_export,
			base_dir = exports/from_ca,
			branch = master,
			update_existing = 1
		},
	}


You're done...
--------------
                                                       
 ....probably. Most users don't modify the configs below.

URL configuration (paths to controllers and themes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	auth_login_path = system/auth/login
	auth_login_url = <ca_url_root>/index.php/system/auth/login
	auth_logout_url = <ca_url_root>/index.php
	controllers_directory = <ca_app_dir>/controllers

Url path to error display page; user will be directed here upon unrecoverable error (eg. bad controller or action)

.. code-block:: none

	error_display_url = <ca_url_root>/index.php/system/Error/Show

Url to redirect user to when nothing is specified (eg. they go to /index.php)
ONLY PUT THE CONTROLLER/ACTION PATH HERE - leave out the 'index.php'

.. code-block:: none

	default_action = /Dashboard/Index

Services

.. code-block:: none

	service_controllers_directory = <ca_app_dir>/service/controllers
	service_default_action = /search/rest/doSearch
	service_view_path = <ca_app_dir>/service/views

Paths to other config files
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	data_model = <ca_conf_dir>/datamodel.conf
	user_pref_defs = <ca_conf_dir>/user_pref_defs.conf
	external_applications = <ca_conf_dir>/external_applications.conf
	media_volumes = <ca_conf_dir>/media_volumes.conf
	file_volumes = <ca_conf_dir>/file_volumes.conf
	default_media_icons = <ca_conf_dir>/default_media_icons.conf
	search_config = <ca_conf_dir>/search.conf
	browse_config = <ca_conf_dir>/browse.conf
	media_processing_settings = <ca_conf_dir>/media_processing.conf
	annotation_type_config = <ca_conf_dir>/annotation_types.conf
	attribute_type_config = <ca_conf_dir>/attribute_types.conf
	application_monitor_config = <ca_conf_dir>/monitor.conf
	assets_config = <ca_conf_dir>/assets.conf
	bundle_type_config = <ca_conf_dir>/bundle_types.conf
	xml_config = <ca_conf_dir>/xml.conf
	user_actions = <ca_conf_dir>/user_actions.conf
	find_navigation = <ca_conf_dir>/find_navigation.conf
	media_display = <ca_conf_dir>/media_display.conf
	media_metadata = <ca_conf_dir>/media_metadata.conf
	access_restrictions = <ca_conf_dir>/access_restrictions.conf
	datetime_config = <ca_conf_dir>/datetime.conf
	authentication_config = <ca_conf_dir>/authentication.conf
	services_config = <ca_conf_dir>/services.conf
	visualization_config = <ca_conf_dir>/visualization.conf
	prepopulate_config = <ca_conf_dir>/prepopulate.conf
	linked_data_config = <ca_conf_dir>/linked_data.conf

Path to navigation config file - defines menu structure

.. code-block:: none

	nav_config = <ca_conf_dir>/navigation.conf

OAI configuration

.. code-block:: none

	oai_harvester_config = <ca_conf_dir>/oai_harvester.conf
	oai_provider_config = <ca_conf_dir>/oai_provider.conf

Path to application plugins
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	application_plugins = <ca_app_dir>/plugins

Path to dashboard widgets
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	dashboard_widgets = <ca_app_dir>/widgets

Password reset parameters
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	password_reset_url = <site_host><ca_url_root>/index.php?action=reset_password&form_action=reset

ID numbering (for objects, object lots and authorities)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	multipart_id_numbering_config = <ca_conf_dir>/multipart_id_numbering.conf

Media and file processing paths
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

	media_plugins = <ca_lib_dir>/Plugins/Media
	file_plugins = <ca_lib_dir>/Plugins/File

Directory to use for Tilepic generation temporary files

.. code-block:: none

	tilepic_tmpdir = <ca_app_dir>/tmp


Name of plugin class to use for id number field in objects, object lots
and authorities that support id numbering (entities, places, collections and occurrences)

.. code-block:: none

	ca_objects_id_numbering_plugin = MultipartIDNumber
	ca_object_lots_id_numbering_plugin = MultipartIDNumber
	ca_entities_id_numbering_plugin = MultipartIDNumber
	ca_places_id_numbering_plugin = MultipartIDNumber
	ca_collections_id_numbering_plugin = MultipartIDNumber
	ca_occurrences_id_numbering_plugin = MultipartIDNumber
	ca_list_items_id_numbering_plugin = MultipartIDNumber
	ca_loans_id_numbering_plugin = MultipartIDNumber
	ca_movements_id_numbering_plugin = MultipartIDNumber
	ca_tours_id_numbering_plugin = MultipartIDNumber
	ca_tour_stops_id_numbering_plugin = MultipartIDNumber
	ca_object_representations_id_numbering_plugin = MultipartIDNumber
	ca_storage_locations_id_numbering_plugin = MultipartIDNumber
	ca_site_pages_id_numbering_plugin = MultipartIDNumber
	ca_site_page_media_id_numbering_plugin = MultipartIDNumber

Formats for form elements
^^^^^^^^^^^^^^^^^^^^^^^^^

If set text of "required_field_marker" will be displayed for bundles in editors for which input is required

.. code-block:: none

	show_required_field_marker = 0

Text to display for bundles in editors for which input is required

	required_field_marker = <span style="color: bb0000; font-size:10px; font-weight: bold;">(Required) </span>

These are used to format data entry elements in various editing formats. Don't change them unless
you know what you're doing
Used for intrinsic fields (simple fields)

.. code-block:: none

	form_element_display_format = <div class='formLabel'>^EXTRA^LABEL<br/>^ELEMENT</div>
	form_element_display_format_without_label = <div class='formLabel'>^ELEMENT</div>
	form_element_error_display_format = <div class='formLabel'>^EXTRA^LABEL (<span class='formLabelError'>^ERRORS</span>)<br/>^ELEMENT</div>

Used for bundle-able fields such as attributes

.. code-block:: none

	bundle_element_display_format = <div class='bundleLabel'>^LABEL ^DOCUMENTATIONLINK ^ELEMENT</div>
	bundle_element_display_format_without_label = <div class='formLabel'>^ELEMENT</div>
	bundle_element_error_display_format = <div class='bundleLabel'>^LABEL (<span class='bundleLabelError'>^ERRORS</span>)<br/>^ELEMENT</div>

Used for the 'idno' field of bundle-providers (Eg. ca_objects, ca_places, etc.)

.. code-block:: none

	idno_element_display_format = <div class='formLabel'>^LABEL<br/>^ELEMENT <span id='idnoStatus'></span></div>
	idno_element_display_format_without_label = <div class='formLabel'>^ELEMENT <span id='idnoStatus'></span></div>
	idno_element_error_display_format = <div class='formLabel'>^LABEL (<span class='formLabelError'>^ERRORS</span>)<br/>^ELEMENT <span id='idnoStatus'></span></div>

Proxy server configuration for web services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In some larger networks servers are required to run their HTTP/HTTPS requests
through a proxy server. If this applies to your setup, uncomment the following lines
and enter your proxy configuration here.

.. code-block:: none

	web_services_proxy_url = tcp://127.0.0.1:8080
