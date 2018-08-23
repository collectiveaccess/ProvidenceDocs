Tracking current object location
================================

Overview
--------
Prior to version 1.5 collection object location and use history were tracked using standard metadata elements and relationships, in the same ways as other object-level information. Storage locations could be defined hierarchically and objects could be related to specific locations. Additional metadata could be recorded in the object and/or location records. For simple tracking this arrangement worked well enough, but it proved problematic for users seeking to maintain location histories, record complex per-move data (packing, insurance, etc.) or tracking usage across different classes of activity records (eg. loans, exhibitions, conservation, as well as movement). Starting with version 1.5, the available options have been expanded, with specialized tools for tracking location and use history of collection objects. (Of course, existing systems can continue to use the pre-1.5 location tracking methods if they wish.)

One size does not fit all when it comes to location tracking. To handle the range of tracking methodologies required by different types of museum and archival collections CollectiveAccess now offers three different mechanisms to track the location of collection objects:

    - **Direct object-location references.** Location is recorded using relationships between object and storage location records. Relationships are dated, with the most recent date considered "current". This allows construction of simple location histories and is similar to the pre-1.5 method save for the dating.
    - **Movement-based location tracking.** Location is recorded for objects in related movement records. Each movement record records details about a specific change in location for one or more objects. The current location for an object is considered to be the location referred to by the most recent movement by date. Movement of entire storage locations within the location hierarchy can be configured to record a movement, allowing current location tracking based upon individual object moves as well as movements of containers or other storage units.
    - **Workflow-based location tracking.** Location is recorded for an object across a range of record types representing various related activities, including loans, movements, occurrences (typically recording exhibitions), deaccession and location relationships. Locations recorded using direct object-location or movement-based location tracking can be part of the range of data used by to derive current location.

Although it is possible to simultaneously employ more than one of these mechanisms in your system, in general you should choose only one to use.

Which method should I use?
--------------------------
**Direct object-location** reference is the simplest option and is suitable for collections that have fairly uniform location reporting requirements. If everything in your collection has a standard location and there are relatively informal movements of items between locations use this option. Many archives, historical societies and house museums and the like will find this an effective and easy to deploy option.

**Movement-based location tracking** records detailed information about how one or more objects are transferred between locations, in addition to the location history. This option is intended for collections where documenting chain of custody, insurance and packing are critical. This additional documentation comes at the expense of added complexity and additional required data entry. Every movement of an object or group of objects to a new location requires completion of a full movement record. Collections that routinely move valuable, sensitive or fragile materials (fine art museums, artists studios, archives with privacy concerns) may find this option preferable.

**Workflow-based location tracking** is designed for institutions with a robust notion of location and expands upon either of the preceding two options. In contrast with other methods, which all record relationships between objects and locations (with or without movements), workflow-based location tracking takes into consideration several types of records to determine the current location of an object, including direct object-location or movement-based tracking. With this method location can be based upon a combination of reported storage location, occurrence (often an exhibition or event), loan, movement or deaccession. For institutions that often loan or exhibit objects workflow-based tracking can reduce redundant data entry by using the loan or exhibition record itself as documentation of location, rather than requiring hacky double entry and pseudo "loan" or "on exhibit" storage locations. This flexibility comes at the cost of more complex configuration and, potentially, additional required data entry.

For most users direct object-location tracking should be sufficient. Movement-based or workflow-based location tracking should only be considered if you require the specific functionality they provide.

Direct object-location reference
--------------------------------
Configuration
^^^^^^^^^^^^^

Basic configuration of object-location tracking is done in app.conf using the following directives:

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1L0ZQPJccg1J5soEd6AeLy2_LEhIPjygAU-DyBrYyYjE/pub?output=csv

There are two bundles available to implement location tracking in your editing user interfaces. The **ca_objects_location** bundle displays the current location, location history and adds a control to change the current location in the object editor.

The **ca_objects_location** bundle provides the following options when used with direct object-location tracking. These can be set in your installation profile or in the web-based configuration UI:

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1NVO8KVS00eYpD_mWWwJITrHFZhvR9tQcid2AH7msV8M/pub?output=csv
   
The **ca_storage_locations_contents** will display a list of all objects currently resident in a storage location. It provides the following options, which can be set in your installation profile or in the web-based configuration UI:

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1Jubu0-SaoSj0eFDMAlGP8bHgLNX9VoOdwCKi_Bp49LE/pub?output=csv

Note that when using direct object-location tracking, a ca_storage_locations relationship bundle placed in an object editor will display all object-location links, past, present and future, in a single undifferentiated list and can be configured to allow users to add object-location links. The ca_objects relationship bundle placed in a storage location editor will behave similarly. In general, the ca_objects and ca_storage_locations relationship bundles should not be placed in the storage location and objects editors respectively when direct object-location tracking is in use.

Movement-based location tracking
--------------------------------
Configuration
^^^^^^^^^^^^^
Basic configuration of movement-based location tracking is done in app.conf using the following directives:

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1VD9tznesFM3azkP3WOWMLvdnkx0WESi1Baq0EVkJNnQ/pub?output=csv

As with direct object-location tracking there are two bundles available to implement location tracking in your editing user interfaces. The ca_objects_location bundle displays the current location, location history and adds a control to change the current location in the object editor. The options are the same as for object-location tracking, but the locationTrackingMode option should be set to ca_movements.

The location of an object will be updated when any of the following occur:

    1. The location of an object is changed using the object location bundle in the object editor
    2. A storage location is moved within the location hierarchy and the record_movement_information_when_moving_storage_location option is app.conf is set
    3. A movement record is manually created, a storage location is set for it and objects added to it

Note that changing the storage location of an existing movement will change the storage location for all objects associated with that movement but not the date. It will be as if the new location had been chosen on the movement date.

Workflow-based location tracking
--------------------------------
Configuration
^^^^^^^^^^^^^
Unlike other location tracking options, which explicitly record location in a specific place in the database, workflow-based location tracking calculates the current location of an object by looking at a range of related records, comparing their dates, and selecting the most recently dated. What types of records are considered and which date elements in those records are used for comparison are entirely configurable.

Workflow-based location tracking can supplement direct object-location reference or movement-based tracking. That is, locations recorded with those two methods may be part of the mix of records workflow-based tracking considers when calculating the current location, but they don't have to be.

Primary configuration is done in **app.conf** through the **current_location_criteria** directive. current_location_criteria is an associative array the keys of which are the primary types you want considered. Relevant primary types for location tracking are: ca_storage_locations, ca_loans, ca_movements, ca_object_lots and ca_occurrences. Each primary type has a sub-array the keys of which are sub-types (except for ca_storage_locations for which it is a relationship type). Each sub-type/relationship type in turn has an array of options. For example:

.. code-block:: none

current_location_criteria = {
	ca_storage_locations = {
		related = { 
			template = ^ca_storage_locations.hierarchy.preferred_labels%delimiter=_➜_ 
		}
	},
	ca_movements = {
		shipping = { date = pickup_date, color = 9bae33 },
		framing = { date = pickup_date, color = 541353 },
		conservation = { date = pickup_date, color = 245442 },
		administrative = { date = pickup_date, color = 992222 },
	},
	ca_loans = {
		collection = { 
			date = loan_period,
			color = cccccc
		}
	},
	ca_occurrences = {
		exhibition = { 
			date = exh_dates,
			color = 00cc00
		}
	},
	# The entry for ca_objects controls if and how deaccessions are displayed
	ca_objects = {
		template = ^ca_objects.deaccession_notes (^ca_objects.deaccession_date),
		color = cc0000
	}
}

In this example, ca_movements is a primary type, shipping is a movement sub-type and date is an option for the shipping sub-type (and others as well) specifying what date element should be used to calculate this movement sub-types place in the object's history. (For the ca_storage_locations primary type in the example, related is an object-storage location relationship type, and template is an option of that relationship type).

Note that display of deaccessions (managed via the ca_objects_deaccession editor bundle) in the object use history is controlled using the ca_objects primary type. If it is present in the configuration deaccessions will be shown, formatted using the supplied template and color, as in the example above.

Sub-type/relationship type options affect both the what is considered current and how the current location is displayed. Options include:

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1IjF72I6XttAk_oeX0UANrN9CPS16eeAoW1uIPdec_XE/pub?output=csv

This configuration will be used to display current location in the editor inspectors, when browsing on workflow-based current location and by default in the Object Use History (ca_objects_history) editor bundle.

The Object Use History bundle is used to display the current location as well as a detailed history of previous use. It is intended as a convenient means to show where an object is and has been, but can also be configured to show any set of related records by date. The bundle has a variety of settings to customize the layout and contents of the location stream. All of these can be set in the current_location_criteria bundle in app.conf, described previously, and used as defaults in the bundle. Let's take a look at an example:


In the bundle seen above the cataloguer has configured different colors and templates to showcase Accession, Loan, and Storage Location activity and data. Each block is automatically sorted by the date chosen through the bundle settings for that table. For example, Artwork loans are sorted on the "Loan Period" as seen via the dates on the far right-hand side. When a new relationship is created to any of the three configured tables a new segment will appear in the stream in the appropriate order based on date. In addition to the tables shown in the example, Occurrences, Movements, and Deaccessions can also be configured.

The contents of each block in the stream are entirely configurable using metadata display templates. With this powerful syntax any metadata from the related record, or from those records related to the related record, can be displayed in the Use History bundle. An example of that relationship traversing can be seen above in the Artwork loan blocks. There, the "Borrower" is displayed using the below syntax which pulls entities related to the related loan:

.. code-block:: none

<l>^ca_loans.preferred_labels</l><br>
<ifdef code="ca_loans.loan_period">Loan Period:</ifdef> ^ca_loans.loan_period<br>
Borrower: <unit relativeTo="ca_loans">
<unit relativeTo="ca_entities" delimiter=", " restrictToRelationshipTypes="borrower">^ca_entities.preferred_labels</unit></unit>

Configuring bundle-specific settings through an installation profile

To add the Use History bundle to the installation profile, simply include the bundle placement and relevant settings on the appropriate UI screen. The use history settings defined in app.conf are taken as a system-wide universal, but defining the ca_objects_history setting in the profile allows for UI-specific customizations.

.. code-block:: none

            <placement code="ca_objects_history">
              <bundle>ca_objects_history</bundle>
              <settings>
                <setting name="ca_object_lots_purchase_dateElement">accession_date</setting>
                <setting name="ca_object_lots_purchase_color">#663A8C</setting>
              </settings>
            </placement>

The chart below lists settings per table that can be included in your profile. Be sure to replace #type# with the custom type configured in your profile. For example, if "purchase" was the item idno in your list ca_object_lot_types, then your setting would be: ca_object_lots_purchase_dateElement.

Note that there is no dateElement setting for storage locations. Storage locations are sorted on the date cataloged.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1Lt-pnE9XWyM8fyhg6FYjPWFz_Xe_nbSGWB67-Hw5HHk/pub?output=csv

Browsing by current location
----------------------------

Workflow-based location tracking will cache the current location of the object within the object record, which makes browsing possible. To set up a current location browse add a facet of type location in browse.conf. For example:

.. code-block:: none

current_location = {
			type = location,
			restrict_to_types = [],
			
			group_mode = none,
			
			collapse = {
				ca_loans = On loan,
				ca_movements/conservation = In conservation,
				ca_movements/shipping = Shipped,
				ca_movements/administrative = Consigned
			},
			
			display = {
				ca_storage_locations = {
					related = { template = ^ca_storage_locations.hierarchy.preferred_labels%delimiter=_➜_ (storage) }
				},
				ca_occurrences = {
					exhibition = { template = ^ca_occurrences.preferred_labels.name (exhibition) }
				},
			},
			maximumBrowseDepth = 1,
			include_none_option = No location specified,
			
			label_singular = _("current location"),
			label_plural = _("current location")
		},

The collapse, display, maximumBrowseDepth and include_none_option directives are specific to location facets:

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1Zv-II7dsfkVpDKaH554AcxCUYa-cni7wS5aCo-lkXxk/pub?output=csv

Updating the cache
^^^^^^^^^^^^^^^^^^

For performance reasons, the current location of the object is cached within the object record itself. Since locations are calculated based upon the settings in the app.conf current_location_criteria directive, and change in current_location_criteria will likely invalidate the cached data. To regenerate the cache and ensure accurate browse results be sure to run the following caUtils command on the command line:

.. code-block:: none
bin/caUtils reload-object-current-locations

Browsing current location when using non-workflow-based location tracking options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Browsing on current location is only supported in workflow-based location tracking. Since workflow-based location tracking supplements the other tracking options, enabling browse for any kind of location tracking involves setting up a minimal workflow-based configuration like this:

In app.conf, if you are using direct object-location location tracking:
.. code-block:: none

current_location_criteria = {
	ca_storage_locations = {
		[relationship type] = { 
			template = ^ca_storage_locations.hierarchy.preferred_labels%delimiter=_➜_ 
		}
	}
}

where [relationship type] is set to whatever you have object_storage_location_tracking_relationship_type in app.conf set to.

If you are using movement-based location tracking then:

.. code-block:: none

current_location_criteria = {
	ca_movements = {
		[movement type] = { 
			date = pickup_date,
			template = ^ca_storage_locations.hierarchy.preferred_labels%delimiter=_➜_ 
		}
	}
}

where [movement type] is a type of movement you want considered as indicating current location. You can list more than one type if needed.

Then in browse.conf add a facet definition like this for direct object-location tracking:

.. code-block:: none

current_location = {
			type = location,
			restrict_to_types = [],
			
			group_mode = none,
			
			display = {
				ca_storage_locations = {
					[relationship type] = { template = ^ca_storage_locations.hierarchy.preferred_labels%delimiter=_➜_ (storage) }
				}
			},
			
			include_none_option = No location specified,
			
			label_singular = _("current location"),
			label_plural = _("current location")
		},

where [relationship type] is set to whatever you have object_storage_location_tracking_relationship_type in app.conf set to.

For movement-based tracking:
.. code-block:: none

current_location = {
			type = location,
			restrict_to_types = [],
			
			group_mode = none,
			
			display = {
				ca_movements = {
					[movement type] = { template = ^ca_storage_locations.hierarchy.preferred_labels%delimiter=_➜_ (storage) }
				}
			},
			
			include_none_option = No location specified,
			
			label_singular = _("current location"),
			label_plural = _("current location")
		},

where [movement type] is a type of movement you want considered as indicating current location. You can list more than one type if needed.
General maintenance

Both direct object-location and movement-based location tracking rely on dates embedded in relationships between related records. If you are updating an older system, change app.conf configuration or otherwise have reason to believe these dates may be out of sync with the underlying movement and location data from which they are derived you can run the following caUtils command on the command line to refresh values:

.. code-block:: none

bin/caUtils reload-object-current-location-dates

For most data sets this command should take only seconds to a few minutes to run and will not have adverse effects. If you are getting odd ordering in use histories or display of current location try running this command to resolve the issues.

