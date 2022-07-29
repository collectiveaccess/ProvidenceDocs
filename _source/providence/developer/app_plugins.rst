Application Plugins
===================

* `Usage`_ 
* `Layout`_ 
* `The Plugin Class`_ 
* `Hooks`_ 
* `Navigation`_ 
* `Editing (Providence editors)`_
* `Lableable Models (API-Level calls)`_ 
* `Bundleable Models (API-Level calls)`_ 
* `Authorization`_ 
* `Task Queue`_ 
* `User Login Editor`_ 
* `Link Generation`_ 
* `Periodic Tasks`_ 

Application plugins are PHP classes that can be written to add specialized functionality to CollectiveAccess. Custom user interfaces, menu items, and screens are all added to a system with application plugins. 

Each application plugin has its own directory in **app/plugins** which contains all of the code, views, graphics and configuration required for operation. At a minimum, every plugin has a **plugin class**. This class, a subclass of *BaseApplicationPlugin*, defines methods that "hook" various events that may occur during a user request. Plugin classes need only implement methods for the hooks they are interested in. Every time a user request is processed by CollectiveAccess and hookable events triggered, each plugin implementing a method for a given hook will be called.

Information will be passed to your methods by the application plugin interface. The scope and format of this information varies by hook and is described in detail below. 

All plugins have access to the current request object, and by extension, request parameters and the application configuration file via an inherited *getRequest()* method.

Usage
-----

1. Application plugins are particularly useful for: 
2. Adding custom menus
3. Adding completely custom screens with individual controllers, views and database tables
4. Modifying, verifying, or otherwise intercepting data being edited, saved or deleted
5. Modifying the behavior of the CollectiveAccess user interface in specific ways

.. note:: Other application plugins exist to to add support for new media formats, add custom search functionality, implement new attribute types (including attributes that leverage web services), generate custom item identifiers, or support alternative file and media storage (eg. cloud storage, external repositories). For more, please see <link here>

Layout
--------

Every plugin has a directory located in *app/plugins*. The name of this directory should be the name of the plugin (for example *mediaImporter*). Within this directory, create a file with the name of the plugin and the suffix 'Plugin.php' This file should contain a PHP class with the plugin's name suffixed with 'Plugin'.

The plugin can have its own controllers, views, graphics and configuration. These are located in directories within the plugin directory, with the following layout (following our 'mediaImporter' example):

* app/plugins/mediaImporter
* app/plugins/mediaImporter/mediaImporterPlugin.php [plugin class]
* app/plugins/mediaImporter/conf [directory containing plugin's configuration file(s); most plugins define at least one configuration file]
* app/plugins/mediaImporter/controllers [directory containing plugin's controllers; only needed if the plugin generates a full user interface]
* app/plugins/mediaImporter/views [directory containing views for the plugin's controllers; only needed if the plugin generates a full user interface]
* app/plugins/mediaImporter/graphics [directory containing graphic elements; only needed if the plugin generates a full user interface]

The Plugin Class
----------------

Besides implementing a method for each hook the plugin needs to use, a checkStatus() method must also be defined. This returns information about the plugin, and determines whether it is available for use or not. The return value for *checkStatus()* is an array with four keys:

* Description: a description of the plugin
* Errors: an array of text error messages relating to the initialization of the plugin. This should be an empty array if there are no errors. If the plugin is not available the reason why should be expressed in the errors array.
* Warnings: an array of text warning messages relating to the initialization of the plugin. Should be a list of warnings about anything that will limit the functionality of the plugin. Should be an empty array if there are no warnings.
* Available: set to true if the plugin is loaded and available for use, false if it cannot load for some reason.

If initialization of the plugin fails, or for some reason the plugin should not be available in the current context (eg. the user does not have privileges to use the plugin, or some requirement for running is not met) then you must return false for the **available** value.

The plugin must also set the **$description** property, inherited from the base plugin class. This should be set to a short description of the plugin, displayed to the system administrator.

If the plugin needs to load its own configuration files or do other initialization, include a constructor in your class. The constructor is passed an absolute file path to the plugin's directory, which is needed to load plugin-specific configuration files (or anything else in the plugin directory).

Hooks
-----

The following hooks can be used by the plugin by defining a method in the plugin class. To do so, use the hook name prefixed with "hook."
 
If your plugin needs to run every time a user edits an item, define a method in the class like this:

.. code-block::

   public function hookEditItem($pa_params) {
	$item_id = $pa_params['id'];  // The parameter passed to EditItem is a key'ed array of values (see below for details)
	$table_num = $pa_params['table_num'];

	// ... more code here ...
   }

Note that some hooks require you to return a value, while others do not. Use care when writing plugins that modify standard user interface elements such as menu bars; errors in the values the plugin returns for hooks such as *RenderMenuBar* can make the system unusable.

If the plugin returns an array, the contents of that array will be merged with the array that was passed, effectively incorporating any changes. There is one significant exception: if you return an empty the plugin manager will immediately return the null value to the caller and abort processing. Other plugins that may respond to the hook will not be called. This allows the plugin to "short circuit" a call to a hook. Returning any non-array value from the plugin is ignored by the plugin manager. In those cases, the plugin manager will return the parameters passed into the hook unchanged.

Below are several tables with Hooks, descriptions of Hooks, and Hook parameters. 

Navigation
----------

.. csv-table:: 
   :header-rows: 1
   :file: app_plugin_table1.csv

Editing (Providence editors)
----------------------------

These hooks are triggered by specific actions in the Providence object, entity, place, etc. editors.

.. csv-table:: 
   :header-rows: 1
   :file: app_plugin_table2.csv

Labelable Models (API-level calls)
----------------------------------

These hooks are called when your code invokes addLabel(), editLabel() or deleteLabel() on a model inheriting from LabelableBaseModelWithAttributes.

.. csv-table:: 
   :header-rows: 1
   :file: app_plugin_table3.csv

Bundleable models (API-level calls)
-----------------------------------

These hooks are called when your code invokes insert() or update() on a model inheriting from BundleableLabelableBaseModelWithAttributes.

.. csv-table:: 
   :header-rows: 1
   :file: app_plugin_table4.csv

Authorization
-------------

.. csv-table:: 
   :header-rows: 1
   :file: app_plugin_table5.csv

Task Queue
----------

.. csv-table:: 
   :header-rows: 1
   :file: app_plugin_table6.csv

User Login Editor
-----------------

.. csv-table:: 
   :header-rows: 1
   :file: app_plugin_table7.csv


Link Generation
---------------

Available from CollectiveAccess Version 1.4.

.. csv-table:: 
   :header-rows: 1
   :file: app_plugin_table8.csv

Periodic Tasks
--------------

.. csv-table:: 
   :header-rows: 1
   :file: app_plugin_table9.csv
