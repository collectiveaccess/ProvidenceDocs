Workflow-based location tracking
================================

.. contents::
   :local:   
   
Configuration
-------------

Unlike the other location tracking options, which only handle storage locations, workflow-based location tracking calculates the current location of an object by looking at a range of related records - including Loans and Occurrences - comparing their dates, and selecting the most recently dated. What types of records are considered and which date elements in those records are used for comparison are entirely configurable.

Workflow-based location tracking can supplement direct object-location reference or movement-based tracking. That is, locations recorded with those two methods may be part of the mix of records workflow-based tracking considers when calculating the current location, but they don't have to be.

Step 1
^^^^^^
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

In this example, ca_movements is a primary table, while shipping is a movement type and date is an option for the shipping type (and others as well) specifying what date element should be used to calculate this movement types place in the object's history. (For the ca_storage_locations primary type in the example, related is an object-storage location relationship type, and template is an option of that relationship type).

Note that display of deaccessions (managed via the ca_objects_deaccession editor bundle) in the object use history is controlled using the ca_objects primary type. If it is present in the configuration deaccessions will be shown, formatted using the supplied template and color, as in the example above.

Sub-type/relationship type options affect both the what is considered current and how the current location is displayed. Options include:

.. csv-table::
   :widths: 25, 50, 50
   :header-rows: 1
   :file: workflow-based_options.csv

This configuration will be used to display current location in the editor inspectors, when browsing on workflow-based current location and by default in the **Object Use History (ca_objects_history) editor bundle.**

Step 2
^^^^^^
The **Object Use History (ca_objects_history) editor bundle** bundle is used to display the current location as well as a detailed history of previous use when using Workflow-based tracking (As opposed to **Current Location (ca_objects_location)** which is for Direct object-location tracking). It is intended as a convenient means to show where an object is and has been, but can also be configured to show any set of related records by date. The bundle has a variety of settings to customize the layout and contents of the location stream. All of these can be set in the current_location_criteria bundle in app.conf, described previously, and used as defaults in the bundle. Let's take a look at an example:


In the bundle seen above the cataloguer has configured different colors and templates to showcase Accession, Loan, and Storage Location activity and data. Each block is automatically sorted by the date chosen through the bundle settings for that table. For example, Artwork loans are sorted on the "Loan Period" as seen via the dates on the far right-hand side. When a new relationship is created to any of the three configured tables a new segment will appear in the stream in the appropriate order based on date. In addition to the tables shown in the example, Occurrences, Movements, and Deaccessions can also be configured.

The contents of each block in the stream are entirely configurable using metadata display templates. With this powerful syntax any metadata from the related record, or from those records related to the related record, can be displayed in the Use History bundle. An example of that relationship traversing can be seen above in the Artwork loan blocks. There, the "Borrower" is displayed using the below syntax which pulls entities related to the related loan:

.. code-block:: none

   <l>^ca_loans.preferred_labels</l><br>
   <ifdef code="ca_loans.loan_period">Loan Period:</ifdef> ^ca_loans.loan_period<br>
   Borrower: <unit relativeTo="ca_loans">
   <unit relativeTo="ca_entities" delimiter=", " restrictToRelationshipTypes="borrower">^ca_entities.preferred_labels</unit></unit>

Configuring bundle-specific settings through an installation profile
--------------------------------------------------------------------
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
   :widths: 25, 75
   :header-rows: 1
   :file: bundle_specific_settings.csv

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
   }

The collapse, display, maximumBrowseDepth and include_none_option directives are specific to location facets:

.. csv-table::
   :widths: 25, 75, 25
   :header-rows: 1
   :file: browse_directive.csv

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