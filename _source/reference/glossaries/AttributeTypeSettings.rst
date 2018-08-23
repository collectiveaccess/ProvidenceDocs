Attribute Types Settings
========================

.. contents::
   :local:

Attribute settings: Containers
------------------------------
Unlike all other attribute types, containers do not represent data values. Rather their sole function is to organize attributes into groups for display. In a multi-attribute value set (for example an address with separate attributes for street number, city, state, country and postal code), there will be at least one container serving as the "root" (or top) of the attribute hierarchy. Other containers may serve to further group items in the multi-attribute set into sub-groups displayed on separate lines of a form.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/19R8gl5bko1iP8sa6jb29UMEIv158mXyyhwQlgQ971V4/pub?gid=0&single=true&output=csv
   

Attribute settings: Text
------------------------

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/19dQHtOADh3QZHr1EdDGfLBAY6kskyiM4lGHPS5fI8SA/pub?gid=0&single=true&output=csv   

 
Attribute settings: DateRange
-----------------------------

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/12r07gn1GLx2apB1B8WvOQDDCBWw32WSbYyY1boR-658/pub?gid=0&single=true&output=csv
   
   
Attribute settings: Lists
-------------------------

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1mHHKv8D4vRfApHB6avhTwkIR1n9EKRtwvwYwNh7pDO4/pub?gid=0&single=true&output=csv
   
Attribute settings: Geocode
---------------------------

The Geocode attribute type represents one or more coordinates (latitude/longitude pairs) indicating the location of an item (collection object, geographic place, storage location or whatever else you want to place on a map).

Coordinates can be entered as decimal latitude/longitude pairs (ex. 40.321,-74.55) or in degrees-minutes-seconds format (ex. 40° 23' 10N, 74° 30' 5W). Multiple latitude/longitude coordinates should be separated with semicolons (";"). `UTM <https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system>`_ format coordinates is also supported.

Non-coordinate entries are converted to coordinates using the Google Maps Geocoding service, which works well for most full and partial addresses worldwide. To unambiguously distinguish coordinate data from address data to be geocoded, it is strongly suggested that coordinate lists be enclosed in square brackets (ex. [40.321,-74.55; 41.321,-74.55;41.321,-75.55;40.321,-75.55;40.321,-74.55].

Google Maps integration
^^^^^^^^^^^^^^^^^^^^^^^

The Google Maps mapping service is used to produce maps displaying your coordinates. The Geocode attribute used to support either version 2 or 3 of the Google Maps API, selectable via the google_api directive in the global.conf file. As of August 2010, only the v3 API is supported since v2 is now officially deprecated by Google. Any old v2 configuration in your installation (assuming you installed prior to August 2010) will be ignored.

Adding rectified overlays
^^^^^^^^^^^^^^^^^^^^^^^^^

You can add layers that include rectified maps by creating serve-able tiles using a tool such as `MapWarper <http://mapwarper.net>`_ and the Google/OSM URL it provides as an export option. The OSM URL will be in the format ``http://mapwarper.net/maps/tile/0001/z/x/y.png``. You will need to change the x, y and z placeholders in ${x}, ${y} and ${z} respectively. The example OSM URL for CollectiveAccess would be ``http://mapwarper.net/maps/tile/3671/${z}/${x}/${y}.png``. This URL should be entered into the "Tile Server URL" option for the metadata element. You should also provide a layer name describing the content of the map. If you wish to allow users to toggle the layer on and off check the "Show layer switcher controls" checkbox.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1walOLd6yjOblWNK9vIF0S9VVILgUD1pjMTTyK35S8Vg/pub?gid=0&single=true&output=csv
   
Attribute settings: Url
-----------------------

Accepts a properly formatted URL value.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1hSg3jy8xyNCslEbjgKpJn4ztmtpz4Dhq93xBpVYGbTk/pub?gid=0&single=true&output=csv
   
Attribute settings: Currency
----------------------------

Accepts a currency value composed of a currency specifier and a decimal number.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1UNkKWyfnBv3xTFbzkDb0IwmidA0kloo3_RPeno-fG3A/pub?gid=0&single=true&output=csv
   
Attribute settings: Length
---------------------------

Accepts length measurements in metric, English and typographical points units.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1fwltFPwcV1W_Z99o9V2_ZSZxr9_-hpOD4PIHrVB9O_k/pub?gid=0&single=true&output=csv


Attribute settings: Weight
---------------------------

Accepts weight measurements in metric and English units. 

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/15hGedU4G7pZ4xlOoHw-O1Bsu8FWgJ48vw8mAHmq475s/pub?gid=0&single=true&output=csv
   

Attribute settings: TimeCode
----------------------------

Accepts time offsets in a number of time code formats.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1KvJZ-4wmotCjzjHOT6tBQ4pnqZuIaQWpLkMfp_N0Qk0/pub?gid=0&single=true&output=csv
   
Attribute settings: Integer
---------------------------

Accepts a properly formatted integer value.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/13jYM5u20Uor0ePuP94-uz66waxVQnpc1leDwA6IeAyI/pub?gid=0&single=true&output=csv
   
Attribute settings: Numeric
---------------------------

Accepts numeric values and strings consisting of optional sign, any number of digits, optional decimal part and optional exponential part.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1UX7ljYR3KZcBMrE1n-LlA268OhHj95TsL1ffJX6IHUI/pub?gid=0&single=true&output=csv
   
Attribute settings: Numeric
---------------------------

Accepts numeric values and strings consisting of optional sign, any number of digits, optional decimal part and optional exponential part.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1UX7ljYR3KZcBMrE1n-LlA268OhHj95TsL1ffJX6IHUI/pub?gid=0&single=true&output=csv
   
Attribute settings: LCSH
------------------------

Library of Congress Subject Heading values.

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1pZS12JxBTTLR7JkJ5LT70jk1ejF8OFJkxU-a-UF1glw/pub?gid=0&single=true&output=csv
   
Attribute settings: GeoNames
----------------------------

Represents one or more latitude/longitude coordinates

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1zEZbJO-qlGYwdHJZFlm9sLvc69lIRqJRgGofH7jBVj4/pub?gid=0&single=true&output=csv
   
Attribute settings: Files
-------------------------

Uploaded file

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1rWqINtQoXLlxtSbmqdPCdQcYf8uo8ShOcvC8nzHdiMs/pub?gid=0&single=true&output=csv
   
   
Attribute settings: Media
-------------------------

Uploaded media (image, sound video).

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1ZGJZymdym55r03RV8MxyhgdY_dwjWHh4fHWYH0S9wI4/pub?gid=0&single=true&output=csv
   


Attribute settings: Taxonomy
----------------------------

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1Dn50FG8fm0JOh1d20cn9NquSvgROdKJTUDhJHNAXQyg/pub?gid=0&single=true&output=csv

Attribute settings: Entities
----------------------------

.. csv-table::
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/1ed9x012bbw3LhdAF3f9IOZZHJ4WJi13PJJGMmlCn3Qk/pub?gid=0&single=true&output=csv