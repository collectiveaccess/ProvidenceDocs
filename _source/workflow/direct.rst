Direct object-location tracking
===============================

.. contents::
   :local:   
   
Configuration
-------------

Basic configuration of object-location tracking is done in app.conf using the following directives:

.. csv-table::
   :widths: 25, 75
   :header-rows: 1
   :file: ../_static/csv/direct_object-location_setting.csv

There are two bundles available to implement location tracking in your editing user interfaces. The **ca_objects_location** bundle displays the current location, location history and adds a control to change the current location in the object editor.

The **ca_objects_location** bundle provides the following options when used with direct object-location tracking. These can be set in your installation profile or in the web-based configuration UI:

.. csv-table::
   :widths: 25, 25, 75, 25, 25
   :header-rows: 1
   :file: ../_static/csv/settings_1.csv

The **ca_storage_locations_contents** will display a list of all objects currently resident in a storage location. It provides the following options, which can be set in your installation profile or in the web-based configuration UI:

.. csv-table::
   :widths: 25, 25, 50, 50, 25
   :header-rows: 1
   :file: ../_static/csv/settings_2.csv

Note that when using direct object-location tracking, a ca_storage_locations relationship bundle placed in an object editor will display all object-location links, past, present and future, in a single undifferentiated list and can be configured to allow users to add object-location links. The ca_objects relationship bundle placed in a storage location editor will behave similarly. In general, the ca_objects and ca_storage_locations relationship bundles should not be placed in the storage location and objects editors respectively when direct object-location tracking is in use.

Browsing current location when using direct object-location tracking
--------------------------------------------------------------------

Browsing on current location is technically only supported in workflow-based location tracking. Since workflow-based location tracking supplements the other tracking options, enabling browse for any kind of location tracking involves setting up a minimal workflow-based configuration like this:

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
   }

where [relationship type] is set to whatever you have object_storage_location_tracking_relationship_type in app.conf set to.


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

