Cookbook: Configuration Files
=============================

This section provides some real examples of common challenges that may arise during the set up of configuration files. This section is aimed at developers who can configure code and set up configuration files in the installation profile for CollectiveAccess.

Each scenario begins with a “problem,” describing a certain challenge or question that may occur during installation. There is an accompanying “solution” provided for each problem, which outlines how to carry out the necessary steps to reach a specific outcome. 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online `Support Forum <https://collectiveaccess.org/support/>`_, `Online Chat <https://gitter.im/collectiveaccess/support>`_, `Slack Channel for Developers <https://collectiveacc-uye7574.slack.com/join/signup#/domain-signup>`_, and `Back-end <https://github.com/collectiveaccess/providence>`_ and `Front-end <https://github.com/collectiveaccess/pawtucket2>`_ GitHub Repositories. 

Contents
--------

* `Browsing on a Metadata Element`_
* `Browsing on Related Authorities`_
* `Changing Currency Settings`_
* `Defining Textual Expressions of Historic Time Periods for dateRange Elements`_
* `Expressing an Open-ended DateRange`_
* `Adding Title Types`_
* `Creating a Search Shortcut`_
* `Creating a Search Shortcut for a Container`_
* `Privileging the Index of a Field`_
* `Flexible Indexing of Identifiers`_
* `Disabling Editors`_
* `Limit Creation of New Records to Top-Level Type`_
* `Enforcing a Strict Hierarchy`_
* `Translating "Find" and "New" Menus`_
* `Changing Related Item Lookup Settings`_
* `Setting Sort Order in a Hierarchy Browser`_
* `Setting ID Numbers to Automatically Generate`_
* `Configuring a Numbering System for Hierarchical Records`_
* `Modifying a Search on a Record’s Idno`_
* `Indexing a Metadata Element (other than idno) as an Identifier`_
* `Enabling Item-Level Access Checking`_
* `Changing the Order of "New" and "Find" Menus`_
* `Create a Record with a Duplicate idno`_
* `Defaulting to Summary Screen`_
* `Changing Import Folder Default Location`_
* `Customize Report Print-outs`_

Browsing on a Metadata Element 
------------------------------

**Problem**: You need to set up the browse function in CollectiveAccess so users are able to browse on a particular metadata element, such as a list.

**Solution**: In the *browse.conf* file, configure a browsing facet of type:Attribute for whichever primary type you need to browse for. You should only configure browsing on metadata elements that have a relatively small range of possible values; for example, browsing on List elements works quite well. Attributes with narrative text content will not work well.

Determine the primary table for which you are configuring a browse (Objects, Entities, Collections, etc.). For example, all the browse facets for Objects are preceded by the following code:

.. code-block::

   # Configuration for object browse
   ca_objects = {
   facets = {

Then, enter the following:

.. code-block::

   name_your_facet = {
   type = attribute,
   element_code = your_metadata_element_code,

   group_mode = none,

   label_singular = _("Enter a Label Here"),
   label_plural = _("Enter a Label Here")
   },

Where **"your_metadata_element_code"** would be replaced by the element code for your chosen field. Be sure to name_your_facet uniquely, and assign the appropriate labels for the facet as well.

Browsing on Related Authorities
-------------------------------

**Problem**: You need to set up the browse function in CollectiveAccess so that users can browse for Objects by related authorities, such as Occurrences.

**Solution**: In browse.conf, Authority facets allow for browsing on cataloging applied to the browsed item from a related authority. If you want to browse for objects by place name, you'd set up a facet of type authority with options to cover the places authority. Here is an example of the code you would enter to browse by Related Occurrences:

.. code-block::

   occurrence_facet = {
			type = authority,
			table = ca_occurrences,
			generate_facets_for_types = 1,
			relationship_table = ca_objects_x_occurrences,
			restrict_to_types = [],
			restrict_to_relationship_types = [],			
			
			groupings = {
				label = _("Name"), 
				type = _("Type"),
				relationship_types = _("Role"),
				ca_attribute_dates_value:years = _("Years"),
				ca_attribute_dates_value:decades = _("Decades")
			},
			
			group_mode = alphabetical,
			
			label_singular = _("occurrence"),
			label_plural = _("occurrences")
		},

Note that if there are multiple Occurrence types, and you wish for a unique browsing facet to be generated for each type, you can use the following setting:

.. code-block::

   generate_facets_for_types = 1,

On the other hand, if there are multiple Occurrence types, and you wish to restrict the browse to a particular type or types, or if you wish to restrict the browse to particular relationship types, enter the List Identifier, or Relationship Type identifier, in the following brackets:

.. code-block::

   restrict_to_types = [],
   restrict_to_relationship_types = [],

Changing Currency Settings
--------------------------

**Problem**: You need a "Value" datatype to read "$" as CAD, rather than USD. 

**Solution**: In *app.conf*, you can change the default dollar currency. If no currency is set, then the default will be "USD."

.. code-block::

   default_dollar_currency = CDN	

Defining Textual Expressions of Historic Time Periods for dateRange Elements
----------------------------------------------------------------------------

**Problem**: You want your users to be able to type a commonly used textual expression to refer to a time period inside a Date field, but the 'dateRange' datatype only accepts valid dates.

**Solution**: In *datetime.conf*, text expressions can be defined if you wish to have the date/time parser convert to dates. The text expression on the left side of the equal sign must be all lowercase; the date/time expression on the right side must be valid and parsable.

Examples:

.. code-block::

    expressions = {
	us civil war = 1861 to 1865,
	world war 2  = 1939 to 1945,
	nickel empire = 1920s,
   }

Expressing an Open-ended DateRange
----------------------------------

**Problem**: You want to be able to express a date such as "11/22/2013 - present."

**Solution**: There are several ways to set this up in datetime.conf. First, check the dateFormat:

.. code-block::

   # Format to use for dates; valid values are (text|delimited|iso8601|original)	[default is text]
   # "original" is the date as entered by the user; other values will normalize all date/time input
   # to the selected standard format
   dateFormat = text

If the dateFormat is anything other than "original," you can use the "afterQualifier" to convert an open-ended date to the format "after 11/22/2013" to indicate that the range is ongoing:

.. code-block::

   # Text to place before a date/time to indicate that it is no earlier than the specified date; must be valid for the current language or default will be used; [default is first indicator in language config file]
   #	afterQualifier = after

If that format doesn't work for you, then you may want to change the dateFormat to "original," so that the date will be saved as it was entered.

Adding Title Types
------------------

**Problem**: You want to add a Title type drop-down list to your preferred and alternate label fields. 

**Solution**: Create a list for your types in the installation profile. Make note of the list code. In *app.conf*, find "#Label type lists" and input your list code for the correct option (i.e. ca_objects_preferred_label_type_list. As you will see, there can be different lists for every record type.

Creating a Search Shortcut
--------------------------

**Problem**: You want to create a search shortcut to quickly find metadata values, for example: style: "stone sculpture" (where "style" searches two fields called Materials and Techniques).

**Solution**: Create an access point in *search_indexing.conf*, by including the following in the ca_objects section:

.. code-block::

   # ------------------------------------
	_access_points = {
		style = {
			fields = [ca_objects.materials, ca_objects.techniques],
			options = { DONT_INCLUDE_IN_SEARCH_FORM }
		},

where "materials" and "techniques" are the elementCodes of those fields.

Creating a Search Shortcut for a Container
------------------------------------------

**Problem**: You want to create a search shortcut to quickly find specific metadata values in a single field within a container, for example: width: "5 in" (where width is inside a larger "measurements" container).

**Solution**: Create an access point in search_indexing.conf by including the following in the ca_objects section:

.. code-block::

   # ------------------------------------
	_access_points = {
		width = {
			fields = [ca_objects.measurements.width],
			options = { DONT_INCLUDE_IN_SEARCH_FORM }
		},

where "measurements" is the elementCode of the whole container and "width" is the elementCode of the sub-element. Remember to use periods, as shown above.

Privileging the Index of a Field
--------------------------------

**Problem**: You want a certain field to have more weight when sorting for relevance in your search index.

**Solution**: Use the field-level option BOOST to add weight. BOOST takes a numeric value, where a higher value counts for more weight. For example:

.. code-block::

   ca_objects = {
		fields = {

			idno = { STORE, DONT_TOKENIZE, INDEX_AS_IDNO, BOOST = 100 },

Flexible Indexing of Identifiers
--------------------------------

**Problem**: You want your identifier (idno) to be indexed with some flexibility, so that different permutations are retrieved in a search. For example: a search for KA1 should return KA.0001. 

**Solution**: Use the field-level option INDEX_AS_IDNO.

.. code-block::

   ca_objects = {
		fields = {

			idno = { STORE, DONT_TOKENIZE, INDEX_AS_IDNO, BOOST = 100 },

Disabling Editors
-----------------

**Problem**: You want to simplify your system so that Places, Movements, Loans, and other primary tables. don't appear in your "New" and "Find" drop-down menus in CollectiveAccess. 

**Solution**: Scroll down to Editor "disable" switches in app.conf, and set all those you wish to disable to "1.” 

.. code-block::

   a_objects_disable = 0
   ca_entities_disable = 0
   ca_places_disable = 1
   ca_occurrences_disable = 0
   ca_collections_disable = 0
   ca_object_lots_disable = 0
   ca_storage_locations_disable = 0
   ca_loans_disable = 0
   ca_movements_disable = 1
   ca_tours_disable = 1
   ca_object_representations_disable = 1

Limit Creation of New Records to Top-Level Type
-----------------------------------------------

**Problem**: You have a hierarchy of Object types, but you don't want users to be able to create a new sub-type without first creating a new primary type.

**Solution**: Set the "Navigation options" in app.conf to allow users to see only top-level types in the New menu by setting the directive below to "1.” 

.. code-block::

   ca_objects_navigation_new_menu_shows_top_level_types_only = 1

Enforcing a Strict Hierarchy
----------------------------

**Problem**: You have certain collection types that should only be catalogued as child records, and you don't want them to be accessible through the "New" menu in CollectiveAccess. 

**Solution**: Enforce a strict type hierarchy in app.conf, and be sure to enable the appropriate "add child record" control.

First, set the desired type hierarchy to "1.” 

.. code-block::

   ca_objects_enforce_strict_type_hierarchy = 0
   ca_entities_enforce_strict_type_hierarchy = 0
   ca_places_enforce_strict_type_hierarchy = 0
   ca_occurrences_enforce_strict_type_hierarchy = 0
   ca_collections_enforce_strict_type_hierarchy = 1
   ca_storage_locations_enforce_strict_type_hierarchy = 0
   ca_loans_enforce_strict_type_hierarchy = 0
   ca_tour_stops_enforce_strict_type_hierarchy = 0
   ca_list_items_enforce_strict_type_hierarchy = 0

Then, be sure to set the appropriate "add child record" control to "1.” 

.. code-block::

   ca_objects_show_add_child_control_in_inspector = 0
   ca_entities_show_add_child_control_in_inspector = 0
   ca_places_show_add_child_control_in_inspector = 0
   ca_occurrences_show_add_child_control_in_inspector = 0
   ca_collections_show_add_child_control_in_inspector = 1
   ca_storage_locations_show_add_child_control_in_inspector = 0
   ca_loans_show_add_child_control_in_inspector = 0
   ca_movements_show_add_child_control_in_inspector = 0
   ca_tour_stops_show_add_child_control_in_inspector = 0

Translating "Find" and "New" Menus
----------------------------------

**Problem**: You used poedit, or another translation editor, to change all instances of "Lots" in your system to "Accessions," but the "New" and "Find" menus still employ the old terminology.

**Solution**: Manually change the desired "displaynames" in navigation.conf to reflect your chosen terminology.

.. code-block::

   "navigation" = {
			"object_lots" = {
				"displayName" = _("Accessions"),

Be sure to change the display name in both the New and Find menus.

Changing Related Item Lookup Settings
-------------------------------------

**Problem**: Only preferred labels are displayed inside the "draggable bubbles" in a relationship bundle, and you wish for the IDs to be displayed in addition to the preferred labels.

**Solution**: In app.conf, add the ca_table.element_code you wish to be displayed for the appropriate primary table in the section titled "related item lookup settings."

For example, you could change the following if you wanted Entity identifiers to be displayed inside parentheses preceding Entity names:

.. code-block::

   ca_entities_lookup_settings = [^ca_entities.preferred_labels]
   ca_entities_lookup_delimiter = ➔

to 

.. code-block::

   ca_entities_lookup_settings = [(^ca_entities.idno) ^ca_entities.preferred_labels]
   ca_entities_lookup_delimiter = ➔

More detailed formatting of relationship bundles can also be done through the user interface.

Setting Sort Order in a Hierarchy Browser
-----------------------------------------

**Problem**: You've added a hierarchy browser to your configuration so that you can see Objects nested within Collections. However, you want the Objects to be sorted in alphabetical order by title, instead of by idno.

**Solution**: Under "Hierarchy browser items" in app.conf, you can set the hierarchy_browser_sort_values and the sort_direction. First, find the table type for the values you want to sort in the browser. In this case you're working with Objects, so at the top of the list find: 

.. code-block::

   ca_objects_hierarchy_browser_sort_values = [ca_objects.idno_sort]

and then change the setting from [ca_objects.idno_sort] to [ca_objects.preferred_labels_sort] so that you see this:

.. code-block::

   ca_objects_hierarchy_browser_sort_values = [ca_objects.preferred_labels_sort]

Then, to set sort direction, visit the line below the values setting and, depending on your needs, set it to either "asc" (ascending) or "desc" (descending).

.. code-block::

   ca_objects_hierarchy_browser_sort_direction = asc

Setting ID Numbers to Automatically Generate
--------------------------------------------

**Problem**: You don't have an institutional numbering system for new accessions of the type "Purchase,” and you want CA to automatically generate ID Numbers for that Lot type.

**Solution**: Use Multipart_ID_Numbering.conf to set up an automatic numbering system for Lots. For example, you might want the first part of the number to be the year, with a second part that's simply sequential:

.. code-block::

   ca_object_lots = {
		purchase = {
			separator = .,
			
			elements = {
				lot_number = {
					type = YEAR,
					width = 30,
					editable = 1,
					
					description = _(Lot year)
					},
				sub_number = {
					type = SERIAL,
					width = 30,
					editable = 1,
					table = ca_object_lots,
					field = idno_stub,
					sort_field = idno_stub_sort,
					zeropad_to_length = 2,
					
					description = _(Lot number)	
			}
		}
	},
	gift = {
			separator =,
			
			elements = {
				lot_number = {
					type = FREE,
					width = 30,
					editable = 1,
					
					description = _(Lot number)
				}
			}
		},

In the example above, there are two Lot types, "purchase" and "gift." "Purchase" needs an automatic number, whereas you want "gift" to be entered by hand. First, you must define your type using the exact same code used in the profile. Then, define the "elements" of the number. Use the type code "YEAR" to create the first part of the ID number. For the second, sequential part, you can use the type code "SERIAL." Make sure you indicate what the system should refer to when creating the serial number - in this case, the previous id number (idno_stub). Remember that "idno" for other table types is "idno_stub" for Lots. For "gift," the type can simply be "FREE," which is the default.

Configuring a Numbering System for Hierarchical Records
-------------------------------------------------------

**Problem**: You want child records to automatically generate id numbers in an ascending order based on the idno of the parent record.

**Solution**: Use the multipart_id_numbering.conf file to create a numbering format for the idno of the relevant table type. For example, say that you have a hierarchical collection system, in which one collection could have several sub-collections. In this case, scroll down to ca_collections in multipart_id_numbering.conf, and set the numbering convention for the parent type (named "main" in this example):

.. code-block::

   ca_collections = {
	main = {
			separator = .,
			elements = {
				collection_no = {
					type = FREE,
					width = 12,
					description = collection year,
				
					editable = 1

Then, for each sub-type (we'll show one, called "sub" in this example), repeat the settings for the parent record idno for the first half of the numbering system, and then set the second half as follows:

.. code-block::

   sub = {
			separator = .,
			elements = {
				collection_no = {
					type = FREE,
					width = 12,
					description = collection year,
				
					editable = 1
				},
				sub_number = {
					type = SERIAL,
					width = 4,
					description = sub#,
					editable = 1,
					zeropad_to_length = 2,
	
					table = ca_collections,
					field = idno,
					sort_field = idno_sort,
					
					child_only = 1
				}
			}
		}

The type "serial" will add a numeric value of 1,2,3,4,5, etc. after the initial portion of the idno, which will simply be a repeat of the idno for the parent record.

Modifying a Search on a Record’s idno
-----------------------------------

**Problem**: You are trying to search for objects or accession records by their identifier, but searches on valid ID numbers are returning zero results in the search.

**Solution**: The problem is likely because your identifiers include punctuation being interpreted by the search engine as characters on which to break your search into separate words. For example, if the search engine is set to consider periods (".") as breaks between words then a search for 2012.051.001 will be transformed into a search for items with the "words" 2012 051 001. This problem can be easily fixed in search.conf.

If your collection's ID numbering system follows a well-defined format, you can add a regular expression matching the format to the "as-is regexes" list in search.conf. For example, the regular expression below allows searching on IDs following the form of 2013.7.2 and 2013-7-2

.. code-block::

   asis_regexes = [
	"^[\d]+[\.\-][A-Za-z0-9\.\-]+$"
   ]

If the formatting of your identifiers contains any special characters, you will also need to add whatever punctuation is used (or may be used) to both the search_tokenizer_regex and the indexing_tokenizer_regex in search.conf. This represents the character class defining characters to be considered as word boundaries in user searches. Note that the default search_tokenizer_regex character class begins with a caret ("^"), which negates the class – in other words the caret means that the character class defines characters that will not be considered as word boundaries.

Thus adding punctuation to this class has the effect of leaving it intact for comparison with identifiers.

.. code-block::

   search_tokenizer_regex = ^\pL\pN\pNd/_#\@\&\.
   indexing_tokenizer_regex = ^\pL\pN\pNd/_#\@\&\.

Once you have modified search.conf with these changes, you must rebuild the search indices in order for the changes to take place.

Indexing a Metadata Element (other than idno) as an Identifier
--------------------------------------------------------------

**Problem**: Your CA configuration tracks objects with several different kinds of identifiers, in addition to the standard ca_objects.idno. You have a metadata element configured to be free text, where your catalogers input IDs in a format similar to the primary identifier. You've indexed special characters, and have followed the instructions, but no IDs input into the custom ID element (the free text metadata element), are coming up in the search.

**Solution**: The changes you made in search.conf to as_is_regexes, search_tokenizer_regex, and indexing_tokenizer_regex only apply to idno. To mimic this behavior on a custom metadata element of type: free text, you must tell search_indexing.conf to treat this element as if it were an idno.
In the example below, I've set the metadata element "Catalog Number" (element code: catalog_number) to be indexed as an idno.

In search_indexing.conf:

.. code-block::

   ca_objects = {
		fields = {
			_metadata = { },					# forces indexing of all attributes
			parent_id = {STORE, DONT_TOKENIZE, DONT_INCLUDE_IN_SEARCH_FORM },
			source_id = {},
			lot_id = {},
			idno = { STORE, DONT_TOKENIZE, INDEX_AS_IDNO, BOOST = 100 },	
			type_id = { STORE, DONT_TOKENIZE },
			source_id = { STORE, DONT_TOKENIZE },
			hier_object_id = { STORE, DONT_TOKENIZE },
			access = { STORE, DONT_TOKENIZE },
			status = { STORE, DONT_TOKENIZE },
			deleted = { STORE, DONT_TOKENIZE },
			ca_attribute_catalog_number = { DONT_TOKENIZE, INDEX_AS_IDNO }
		}
	},

Enabling Item-Level Access Checking
-----------------------------------

**Problem**: You don't see record level access controls in your installation.

**Solution**: Make sure that item-level access checking is enabled in the local copy of app.conf:

.. code-block::

   # -------------------------
   # Item-level access control
   # -------------------------
   perform_item_level_access_checking = 1
   default_item_access_level = __CA_ACL_EDIT_DELETE_ACCESS__
   If you want controls to be restricted to some tables but not others, you can also specify that in app.conf:
   # You can control item-level access control support 
   # for each type of item using these directives
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

Changing the Order of "New" and "Find" Menus
--------------------------------------------

**Problem**: You want "Objects" to be listed last in the "New" menu, instead of first.

**Solution**: Re-order the tables in nav.conf. You should change the order under both "New" and "Find." Be sure to copy the entire JSON when you're moving the table.

Create a Record with a Duplicate idno
-------------------------------------

**Problem**: When creating a new record, you sometimes get this message: "Identifier already exists and duplicates are not permitted" and you're not able to save the record.

**Solution**: Change settings in app.conf to allow duplicates (if you have them in your archive, of course):

.. code-block::

   # Allow dupe id numbers? (0=no, 1=yes)
   #
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

Defaulting to Summary Screen
----------------------------

**Problem**: You want to see "Summary" screens of completed records before looking at any of the editing screens.

**Solution**: Change settings in *app.conf*:

.. code-block::

   #
   # Default to summary when opening item for editing?
   #
   ca_objects_editor_defaults_to_summary_view = 1
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

Note that you must choose settings for each possible editor. When you create a New record, it will still default to "Basic Info" until you have saved for the first time.

Changing Import Folder Default Location
---------------------------------------

**Problem**: You need to change the default location for import folders.

**Solution**: In *app/conf/app.conf*, look for this heading:

.. code-block::

   # ----
   # Batch media processing
   # ----

Then change "batch_media_import_root_directory" to your desired location.

Customize Report Print-outs
---------------------------

**Problem**: You want to add your own logo to the top of an Object Summary print-out.

**Solution**: Go to app/conf/app.conf and look for the header:

.. code-block::

   # -------------------------
   # Record PDF Summary configuration
   # -------------------------

below that, you will see a number of options for customizing your reports. For example:

.. code-block::

   # To display your logo at the top of a PDF report, upload it to the graphics/logos/ folder in all themes
   # directory and enter the filename below.  To change the header color (summary_color) and header text color (summary_text_color), enter the six digit HTML color code below
   # and omit the leading '#' sign.
   #
   summary_header_enabled = 1
   summary_footer_enabled = 1
   summary_img = ca_wide.png
   summary_color = FFFFFF
   summary_text_color = 000000
   summary_footer_color = FFFFFF
   summary_footer_text_color = 000000



   


