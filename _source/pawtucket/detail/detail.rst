detail.conf
===========

The detail.conf configuration file defines all available detail views for a theme. Details 
are, as their name implies, detailed metadata displays for a specific item – a *subject*. 
At a minimum, a detail will be bound to a table. A detail may be designed to display data for 
one of the following tables: objects, entities, occurrences, places, or collections.

You may define any number of details. Each will have a unique code that is used in Pawtucket 
URLs to reference the detail. 

------------------
Top-level settings
------------------

The primary top-level setting is *detailTypes*, a dictionary that contains definitions for
each detail. Other top-level settings control download of media.

.. csv-table::
   :widths: 20, 35, 30, 5, 5, 5
   :header-rows: 1
   :file: detail_conf_table.csv

--------------------------
Settings for *detailTypes* 
--------------------------

Keys in the *detailTypes* dictionary are used as unique detail codes. Values control 
detail display and functionality.

.. csv-table::
   :widths: 20, 35, 30, 5, 5, 5
   :header-rows: 1
   :file: detailTypes_conf_table.csv
  
----------------------------------
Settings for *detailTypes* options
----------------------------------

Many display settings for a detail are set in the *options* dictionary. 

.. csv-table::
   :widths: 20, 35, 30, 5, 5, 5
   :header-rows: 1
   :file: detailTypes_options_conf_table.csv
   
-----------
Detail URLs
-----------

Unique codes are used in URLs to select a detail for display. The URL format is:

\https://<your-hostname>/Detail/<code>/<identifier> where <code> is the detail's code
and <identifier> is the numeric row id or alphanumeric record identifier to display.