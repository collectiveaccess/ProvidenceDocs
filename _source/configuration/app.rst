App.conf
===========

General configuration of CollectiveAccess is controlled by the *app.conf* configuration file. 

Structure
-----------
To make editing app.conf a bit more manageable the file is broken up into several sections grouping related options: menus, disable switches, hierarchies, titles and identifiers, search, features, access control, styling, mapping, defaults, media, administration and esoterica (things you probably won't ever need to change). For sections where a separate configuration file is also available (Eg. search.conf and the search section) the app.conf section controls only high-level options, while the  file handles detailed configuration.


**hierarchies** section:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: configuration_app_conf_hierarchies_table.csv