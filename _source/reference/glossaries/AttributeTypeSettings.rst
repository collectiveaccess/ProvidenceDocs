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
   :file: ../../_static/csv/container_settings.csv

Attribute settings: Text
------------------------

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/text_settings.csv

Attribute settings: DateRange
-----------------------------

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/daterange_settings.csv

Attribute settings: Lists
-------------------------

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/list_settings.csv

Attribute settings: Geocode
---------------------------

The Geocode attribute type represents one or more coordinates (latitude/longitude pairs) indicating the location of an item (collection object, geographic place, storage location or whatever else you want to place on a map).

Coordinates can be entered as decimal latitude/longitude pairs (ex. 40.321,-74.55) or in degrees-minutes-seconds format (ex. 40� 23' 10N, 74� 30' 5W). Multiple latitude/longitude coordinates should be separated with semicolons (";"). `UTM <https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system>`_ format coordinates is also supported.

Non-coordinate entries are converted to coordinates using the Google Maps Geocoding service, which works well for most full and partial addresses worldwide. To unambiguously distinguish coordinate data from address data to be geocoded, it is strongly suggested that coordinate lists be enclosed in square brackets (ex. [40.321,-74.55; 41.321,-74.55;41.321,-75.55;40.321,-75.55;40.321,-74.55].

Google Maps integration
^^^^^^^^^^^^^^^^^^^^^^^

The Google Maps mapping service is used to produce maps displaying your coordinates. The Geocode attribute used to support either version 2 or 3 of the Google Maps API, selectable via the google_api directive in the global.conf file. As of August 2010, only the v3 API is supported since v2 is now officially deprecated by Google. Any old v2 configuration in your installation (assuming you installed prior to August 2010) will be ignored.

Adding rectified overlays
^^^^^^^^^^^^^^^^^^^^^^^^^

You can add layers that include rectified maps by creating serve-able tiles using a tool such as `MapWarper <http://mapwarper.net>`_ and the Google/OSM URL it provides as an export option. The OSM URL will be in the format ``http://mapwarper.net/maps/tile/0001/z/x/y.png``. You will need to change the x, y and z placeholders in ${x}, ${y} and ${z} respectively. The example OSM URL for CollectiveAccess would be ``http://mapwarper.net/maps/tile/3671/${z}/${x}/${y}.png``. This URL should be entered into the "Tile Server URL" option for the metadata element. You should also provide a layer name describing the content of the map. If you wish to allow users to toggle the layer on and off check the "Show layer switcher controls" checkbox.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/geocode_settings.csv

Attribute settings: Url
-----------------------

Accepts a properly formatted URL value.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/url_settings.csv

Attribute settings: Currency
----------------------------

Accepts a currency value composed of a currency specifier and a decimal number.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/currency_settings.csv

Attribute settings: Length
---------------------------

Accepts length measurements in metric, English and typographical points units.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/length_settings.csv

Attribute settings: Weight
---------------------------

Accepts weight measurements in metric and English units.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/weight_settings.csv

Attribute settings: TimeCode
----------------------------

Accepts time offsets in a number of time code formats.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/timecode_settings.csv

Attribute settings: Integer
---------------------------

Accepts a properly formatted integer value.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/integer_settings.csv

Attribute settings: Numeric
---------------------------

Accepts numeric values and strings consisting of optional sign, any number of digits, optional decimal part and optional exponential part.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/numeric_settings.csv

Attribute settings: Numeric
---------------------------

Accepts numeric values and strings consisting of optional sign, any number of digits, optional decimal part and optional exponential part.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/numeric_settings.csv

Attribute settings: LCSH
------------------------

Library of Congress Subject Heading values.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/lcsh_settings.csv

Attribute settings: GeoNames
----------------------------

Represents one or more latitude/longitude coordinates

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/geonames_settings.csv

Attribute settings: Files
-------------------------

Uploaded file

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/file_settings.csv

Attribute settings: Media
-------------------------

Uploaded media (image, sound video).

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/media_settings.csv

Attribute settings: Taxonomy
----------------------------

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/taxonomy_settings.csv

Attribute settings: Entities
----------------------------

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../../_static/csv/entities_settings.csv
