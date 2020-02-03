Tracking current object location
================================

.. contents::
   :local:   
   
   
.. note:: The system for location tracking was completely rebuilt for version 1.7.9 with a new, more general, configuration format and additional features. Older configurations should work as before, but the configuration options described below should be used for new setups. To maintain compatibility with future releases consider updating your existing configuration to use the current options.


Overview
--------
CollectiveAccess provides a storage location hierarchy to describe the physical locations where collection objects may be located, displayed or stored. Storage locations are records like any other and may be associated with objects using relationships. One can record the current location of an object by simply creating a relationship between object and location. 

This arrangement has the advantage of simplicity but comes with serious drawbacks:

* If your objects move often you'll soon have a long list of previous locations, which can make it difficult to figure out what the *current* location is.
* While the current location can be distinguished using a specific relationship type (Eg. "past location" for previous locations and "current location" for the latest location), you must manage setting of these types yourself, which is labor intensive and prone to error.
* Removing previous locations and only recording only a single, current location will make for a simpler and easier to manage display, but means no location history is maintained. For most users, losing location history data is unacceptable.
* Only storage location records may be used to record location. If an object is on loan or exhibition workarounds must be employed, such as dummy "On loan" and "On exhibition" storage locations records.

The history value tracking system (available as of CollectiveAccess version 1.7.9) provides a flexible way to track object locations over time. It can also be used to track other time-varying information such as provenance and current collection. The system employs tracking *policies* to maintain chronologies based upon one or more data elements, and can return full histories as well as current values for any type of record. Tracking of location is the focus in this discussion, but the approaches described here may be applied to other types of time-varying information.

Tracking approaches
-------------------
To handle the range of tracking methodologies required by different types of museum and archival collections CollectiveAccess offers two approaches to location tracking:

    - **Workflow-based location tracking.** Current location is recorded for an object across a range of record types representing various related activities, including loans, movements, occurrences (typically representing exhibitions), collections, deaccession and storage location/inventory. The types of records considered part of the tracking workflow, how their dates are established for assembly into a chronology, and how they are displayed within the chronology are specified in a tracking *policy*. Policies are configured in the :ref:`app.conf <app_conf>` configuration file using the *history_tracking_policies* described below.
    - **Movement-based location tracking.** Location is recorded for objects in related movement records. Each movement record captures details about a specific change in location for one or more objects. The current location for an object is considered to be the location referred to by the most recent movement by date. Movement of entire storage locations within the location hierarchy can be configured to generate a movement record, allowing current location tracking to be based upon both individual object moves and movements of containers and other storage units. Movement-based tracking is more complicated to configure and use, and is only called for when capture of complex metadata (packing, transport, insurance, etc.) about chain of custody and methods used to transition groups of objects between locations is required. This additional documentation comes at the expense of added complexity and data entry, as every movement of an object or group of objects to a new location requires completion of a full movement record. 
    
.. note:: Movement-based tracking is only used when for object location tracking. If tracking non-location values such as provenance, use workflow-based tracking.


Configuration
-------------

Configuration for workflow and movement-based tracking use the configuration format, with minor differences. Most configuration occurs within the top-level ``history_tracking_policies`` entry in :ref:`app.conf <app_conf>`. Under this entry are two keys, both mandatory:

	- **policies** defines all available tracking policies. Most operational configuration resides under this key.

	- **defaults** specifies which policy should be used by default for a given :ref:`table <primary_tables>`. You may define multiple policies per table and declare specific policies be used in various contexts such as user interface bundles. Default policies are a convenience that reduce configuration complexity by setting a standard policy to be overridden as needed.

An example ``history_tracking_policies`` configuration for workflow-based location tracking is shown below:
::

	history_tracking_policies = {
		defaults = { 
			ca_objects = current_location
		},
		policies = {
			current_location = {
				name = _(Current location),
				table = ca_objects,
				mode = workflow, # movements or workflow
				elements = {
					ca_storage_locations = {
						__default__ = {
							date = ca_objects_x_storage_locations.effective_date,
							setInterstitialElementsOnAdd = [effective_date],
							useDatePicker = 0,
							template =
							<l>^ca_storage_locations.hierarchy.preferred_labels.name%delimiter=_➜_</l>  <ifdef code='ca_objects_x_storage_locations.movement_by'> <br>MOVED BY: ^ca_objects_x_storage_locations.movement_by</ifdef>  <ifdef code='ca_objects_x_storage_locations.movement_comments'> <br>COMMENTS: ^ca_objects_x_storage_locations.movement_comments</ifdef>,
							trackingRelationshipType = related,
							restrictToRelationshipTypes = [related]
						}
					},
					ca_occurrences = {
						exhibition = {
							date = ca_occurrences.exhibition_date,
							setInterstitialElementsOnAdd = [effective_date],
							template =
							 <l>^ca_occurrences.preferred_labels.name</l>,
						},
						__default__ = {
							date = ca_objects_x_occurrences.effective_date,
							setInterstitialElementsOnAdd = [effective_date],
							template =
							 <l>^ca_occurrences.idno</l> ^ca_occurrences.preferred_labels.name,
						}
					 },
					 ca_loans = {
						__default__  = { 
							date = ca_loans_x_objects.effective_date,
							setInterstitialElementsOnAdd = [effective_date],
							color = F78B8B,
							template = <l>^ca_loans.idno</l> ^ca_loans.preferred_labels (^ca_loans.institution ^ca_loans.date) <ifdef code='ca_loans_x_objects.movement_comments'> <br>COMMENTS: ^ca_loans_x_objects.movement_comments</ifdef>,
							restrictToRelationshipTypes = [loan]
						  }   
						}
					}
				}
			}  
	 }
	 
Within the ``policies`` section are keys for each configured policy. In the example, a single policy with the code ``current_location`` is defined. Within each policy are entries for ``name`` (the display name of the policy), ``table`` (the tables to which this policy applies), ``mode`` (workflow or movement-based tracking) and ``elements``. 

``Elements`` defines the various types of data tracked by the policy. Each key is a :ref:`table <primary_tables>` name. Within each table block are entries for types. The special ``__default__`` type is used to match any type not explicitly listed for the table. In the example the configuration for storage locations (ca_storage_locations) applies to all types of locations. The ca_occurrences entry includes a configuration specifically for occurrences of type "exhibition", and a default configuration for all other types.

Each per-type configuration must include entries for ``date`` and ``template``. ``date`` is a bundle specifier for a date field in either the related table or the relationship to that table. The value in the specified field will be used to determine where in the chronology of tracked values each related record is placed. In the example, the object-location relationship ``effective_date`` intrinsic field is used to track locations, which the occurrence ``exhibition_date`` metadata element is used to place exhibitions in time. ``template`` is a :ref:`display template <display_templates>` employed to format data for the related record in the chronology. The template will be evaluated relative to the relationship between the object and related record, allowing inclusion of both interstitial (relationship-based) and related-record metadata. In the example the template for loans includes data from both the related loan record as well as the object-loan relationship.

Other, optional keys in per-type configuration configuration include ``color`` (chronology color-coding), ``restrictToRelationshipTypes`` (a list of relationship types to limit chronology display to), ``setInterstitialElementsOnAdd`` (a list of interstitial fields to allow the user to set when creating a relationship from within the chronology). The full list of possible entries is:

.. csv-table::
   :widths: 20, 60, 20
   :header-rows: 1
   :file: tracking_workflow_config.csv

The chronology bundle
---------------------  

xxx

The current contents bundle
---------------------------

xxx
   
Inspector display
-----------------

inspector_home_location_display_template (app.conf)


Display in templates
--------------------

xxx

Searching and browsing on current values
----------------------------------------

xxx

Home locations
--------------

xxx

Updating the cache
------------------

For performance reasons, the current location of the object is cached in the database and used when browsing. Since current location values are calculated based upon the settings in the app.conf change in configuration will likely invalidate the cached data. To regenerate the cache and ensure accurate browse results be sure to run the following caUtils command on the command line:

``reload-current-values-for-history-tracking-policies``
