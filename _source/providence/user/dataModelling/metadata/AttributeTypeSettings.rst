Attribute Types Settings
========================

.. contents::
   :local:

Attribute settings: Containers
------------------------------
Unlike all other attribute types, containers do not represent data values. Rather their sole function is to organize attributes into groups for display. In a multi-attribute value set (for example an address with separate attributes for street number, city, state, country and postal code), there will be at least one container serving as the "root" (or top) of the attribute hierarchy. Other containers may serve to further group items in the multi-attribute set into sub-groups displayed on separate lines of a form.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: container_settings.csv

Attribute settings: Text
------------------------

Accepts text values up to 4gb in length. Text may include HTML formatting.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: text_settings.csv

Attribute settings: DateRange
-----------------------------

Accepts valid date/time expressions as described in [[Date_and_Time_Formats|this page.]]

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: daterange_settings.csv

Attribute settings: List
------------------------

Accepts values from lists. Can present lists of any size and structure, from simple check lists and flat down-down lists to large, deeply nested hierarchical lists.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: list_settings.csv

Attribute settings: Geocode
---------------------------

Represents one or more coordinates (latitude/longitude pairs) indicating the location of an item (collection object, geographic place, storage location or whatever else you want to place on a map).

Coordinates can be entered as decimal latitude/longitude pairs (ex. 40.321,-74.55) or in degrees-minutes-seconds format (ex. 40 23' 10N, 74 30' 5W). Multiple latitude/longitude coordinates must be separated with semicolons (";"). `UTM <https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system>`_ format coordinates is supported.

Non-coordinate entries are converted to coordinates using the OpenStreetMaps Geocoding service, which works well for most full and partial addresses worldwide. To unambiguously distinguish coordinate data from address data to be geocoded, it is strongly suggested that coordinate lists be enclosed in square brackets (ex. [40.321,-74.55; 41.321,-74.55;41.321,-75.55;40.321,-75.55;40.321,-74.55].


Adding rectified overlays
^^^^^^^^^^^^^^^^^^^^^^^^^

You can add layers that include rectified maps by creating serve-able tiles using a tool such as `MapWarper <http://mapwarper.net>`_ and the Google/OSM URL it provides as an export option. The OSM URL will be in the format ``http://mapwarper.net/maps/tile/0001/z/x/y.png``. You will need to change the x, y and z placeholders in ${x}, ${y} and ${z} respectively. The example OSM URL for CollectiveAccess would be ``http://mapwarper.net/maps/tile/3671/${z}/${x}/${y}.png``. This URL should be entered into the "Tile Server URL" option for the metadata element. You should also provide a layer name describing the content of the map. If you wish to allow users to toggle the layer on and off check the "Show layer switcher controls" checkbox.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: geocode_settings.csv

Attribute settings: Url
-----------------------

Accepts properly formatted URL values.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: url_settings.csv

Attribute settings: Currency
----------------------------

Accepts currency values composed of a currency specifier followed by a decimal number.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: currency_settings.csv

Attribute settings: Length
--------------------------

Accepts length measurements in metric, English and typographical points units.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: length_settings.csv

Attribute settings: Weight
--------------------------

Accepts weight measurements in metric and English units.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: weight_settings.csv

Attribute settings: TimeCode
----------------------------

Accepts time offsets in commonly used formats.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: timecode_settings.csv

Attribute settings: Integer
---------------------------

Accepts a properly formatted integer value.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: integer_settings.csv

Attribute settings: Numeric
---------------------------

Accepts numeric values and strings consisting of optional sign, any number of digits, optional decimal part and optional exponential part.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: numeric_settings.csv

Attribute settings: LCSH
------------------------

Accepts Library of Congress Subject Heading references.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: lcsh_settings.csv

Attribute settings: GeoNames
----------------------------

Accepts references to Geonames.org entries for locations.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: geonames_settings.csv

Attribute settings: File
------------------------

Accepts uploads of files of any type. Files are stored as binary data and returned as-is. No parsing or thumbnail generation is performed. 

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: file_settings.csv

Attribute settings: Media
-------------------------

Accepts uploads of media (image, sound video) files. Only types supported by CollectiveAccess and configured in media_processing.conf are accepted. Generation of previews is performed.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: media_settings.csv

Attribute settings: InformationService
--------------------------------------

Accepts values defined by an external information service. CollectiveAccess includes plugins for various external information services, including the Getty AAT, TGN and ULAN, Nomisma, Encylopedia of Life, GlobalNames and more. Generic SparQL endpoints are also supported.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: information_service_settings.csv

Attribute settings: ObjectRepresentations
-----------------------------------------

Accepts references to object representation records defined in the system.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: object_representations_settings.csv
   
Attribute settings: Entities
----------------------------

Accepts references to entity records defined in the system.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: entities_settings.csv
   
Attribute settings: Places
----------------------------

Accepts references to place records defined in the system.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: places_settings.csv

Attribute settings: Occurrences
-------------------------------

Accepts references to occurrence records defined in the system.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: occurrences_settings.csv

Attribute settings: Collections
-------------------------------

Accepts references to collection records defined in the system.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: collections_settings.csv

Attribute settings: StorageLocations
------------------------------------

Accepts references to storage location records defined in the system.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: storage_locations_settings.csv

Attribute settings: Loans
-------------------------

Accepts references to loan records defined in the system.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: loans_settings.csv

Attribute settings: Movements
-----------------------------

Accepts references to movement records defined in the system.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: movements_settings.csv

Attribute settings: Objects
---------------------------

Accepts references to object records defined in the system.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: objects_settings.csv

Attribute settings: ObjectLots
------------------------------

Accepts references to object lot records defined in the system.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: object_lots_settings.csv
   
Attribute settings: FloorPlan
-----------------------------

Accepts floor plan locations defined against a graphic attached to a place record. This allows objects related to locations within a building defined in the place hierarchy to be shown overlayed upon an uploaded floorplan graphic. Typically used for documentation of artwork in exhibitions. 

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: floorplan_settings.csv

Attribute settings: Color
---------------------------

Accepts color values. Values are stored internally as RGB hex color values.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: color_settings.csv
   
Attribute settings: Filesize
-----------------------------

Accepts digital file size values with commonly used suffixes: B, KB, KiB, MB, MiB, GB, GiB, TB, Tib, PB and PiB. Available from version 1.8.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: filesize_settings.csv
   
Attribute settings: ExternalMedia
---------------------------------

Accepts URLs to media stored on external services such as YouTube and Vimeo. Can parse URLs and generate embed tags. Available from version 1.8.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: external_media_settings.csv
   
