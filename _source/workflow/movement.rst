Movement-based location tracking
================================

.. contents::
   :local:   

The third and perhaps most complex method of location tracking is Movement based. It should only be employed if you need to record complex data (beyond merely the date, location, and contents of a movement) about movements *themselves.* For example, information about a movement might include packing, shipping, and authorization information. The second criteria justifying movement-based location tracking would be if multiple objects are being moved in a single instance (For example, more than one item is shipped in a single box as part of an outgoing loan).   

Before you can configure movement-based location tracking, you must enable the Movements table in app.conf and then create a User Interface for Movements that includes metadata elements for all that you wish to record about Movements.

Provided you have a Movement editor configuration in place, configuring Movement-based location tracking is relatively straightforward and similar to Direct object-location tracking.
    
Configuration
-------------

Step 1
^^^^^^
Basic configuration of movement-based location tracking is done in app.conf using the following directives:

.. csv-table::
   :widths: 25, 75
   :header-rows: 1
   :file: ../_static/csv/movement-based_settings.csv

Step 2
^^^^^^
As with direct object-location tracking there are two bundles available to implement location tracking in your editing user interfaces. The **Current Location (ca_objects_location)** bundle displays the current location, location history and adds a control to change the current location in the object editor. The options are the same as for object-location tracking, but the locationTrackingMode option should be set to *ca_movements.*

The location of an object will be updated when any of the following occur:

    1. The location of an object is changed using the object location bundle in the object editor
    2. A storage location is moved within the location hierarchy and the record_movement_information_when_moving_storage_location option is app.conf is set
    3. A movement record is manually created, a storage location is set for it and objects added to it

Note that changing the storage location of an existing movement will change the storage location for all objects associated with that movement but not the date. It will be as if the new location had been chosen on the movement date.

Step 3
^^^^^^
In the Storage Location user interface, there is an available bundle named **Current contents of location (ca_storage_locations_contents)**. If added to the storage location editor, this will display a list of all objects currently resident in the storage location. It provides the following options, which can be set in your installation profile or in the web-based configuration UI:

.. csv-table::
   :widths: 25, 25, 50, 50, 25
   :header-rows: 1
   :file: ../_static/csv/settings_2.csv

Browsing current location when using direct movement-based location tracking
----------------------------------------------------------------------------

Browsing on current location is technically only supported in workflow-based location tracking. Since workflow-based location tracking supplements the other tracking options, enabling browse for any kind of location tracking involves setting up a minimal workflow-based configuration like this:

In app.conf, if you are using movement-based location tracking:

.. code-block:: none

   current_location_criteria = {
      ca_movements = {
         movement_type = {
            date = pickup_date,
            template = ^ca_storage_locations.hierarchy.preferred_labels%delimiter=_➜_
         }
      }
   }

where movement_type is a type of movement you want considered as indicating current location. You can list more than one type if needed.

Then in browse.conf add a facet definition like this for movement-based tracking:

.. code-block:: none

   current_location = {
      type = location,
      restrict_to_types = [],
      table = ca_objects,
      
      group_mode = none,
      
      display = {
         ca_movements = {
            movement_type = { template = ^ca_storage_locations.hierarchy.preferred_labels%delimiter=_➜_ (storage) }
         }
      },
      
      include_none_option = No location specified,
      label_singular = _("current location"),
      label_plural = _("current location")
   }

where movement_type is a type of movement you want considered as indicating current location. You can list more than one type if needed.

Updating the cache
------------------

For performance reasons, the current location of the object is cached within the object record itself. Since locations are calculated based upon the settings in the app.conf current_location_criteria directive, and change in current_location_criteria will likely invalidate the cached data. To regenerate the cache and ensure accurate browse results be sure to run the following caUtils command on the command line:

``bin/caUtils reload-object-current-locations``

General maintenance
-------------------

Both direct object-location and movement-based location tracking rely on dates embedded in relationships between related records. If you are updating an older system, change app.conf configuration or otherwise have reason to believe these dates may be out of sync with the underlying movement and location data from which they are derived you can run the following caUtils command on the command line to refresh values:

``bin/caUtils reload-object-current-location-dates``

For most data sets this command should take only seconds to a few minutes to run and will not have adverse effects. If you are getting odd ordering in use histories or display of current location try running this command to resolve the issues.

Displaying current locations in reports
---------------------------------------

As of version 1.6 an object's current location can be included in reports via the Displays editor. To include the location, simply drag the "Current Location" bundle (also shown as "Object Location") onto your Display.

By default this bundle will display the Current Location as it is defined by the current_location_criteria (see above). Put another way, the report will output the same formatting used for location tracking in the cataloging interface. To override this formatting, use the "display format" setting on the "Object Location" bundle. To include the activity date use the syntax: ^ca_objects.ca_objects_location_date. To show the current_location_criteria use the syntax: ^ca_objects.ca_objects_location.