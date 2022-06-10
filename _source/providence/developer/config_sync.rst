Configuration Sync
==================

A feature as of CollectiveAccess Version 1.6.2, **configuration sync** allows for the exporting and importing of partial profiles. These partial profiles can then be used to replicate configuration changes from one system to another, or to a package.

Exporting Partial Configurations
--------------------------------

There are a few options in **app.conf** that control what exactly gets exported. These options are as follows:

* **configuration_export_only_system_displays**: if set to 1, only system displays are exported
* **configuration_export_only_system_search_forms**: if set to 1, only system search forms are exported
* **configuration_export_exclude_lists**: list of list codes to exclude from configuration export

The defaults should work for most setups.

.. note:: It is recommended to ceate backups of the client/target systems before attempting to export.

Exporting Via the Command Line
------------------------------

The export-profile utility now has an additional, optional parameter, **-t/--timestamp.** It can be used to limit the export to configuration elements changed after that timestamp. 

The parameter should be a Unix timestamp, typically a 10 digit number. Find the current unix time by running:

.. code-block: none

   date +%s

in a terminal. Dates can also be easily converted into timestamps:

.. code-block: php

   date -d"2016-01-28T10:00" +%s

Once the timestamp is converted, run the exporter like so:

.. code-block: php

   support/bin/caUtils export-profile -t 1465287584

To redirect the output to a file ~/foo.xml:

.. code-block: php

   support/bin/caUtils export-profile -t 1465287584 -o ~/foo.xml

Exporting Via Web Service
-------------------------

The same functionality is also available via web service:

.. code-block: php

   curl -XGET 'http://administrator:dublincore@localhost/service.php/model/exportConfig?modifiedAfter=1465287584'

For a partial configuration either created by hand or via the export tools described above, apply those changes to existing systems that have data in them. These changes can, in certain cases, cause data loss, or severe configuration issues. Make sure to backup your database before you do this, and verify all the changes before you start entering data again.

Put the partial profile in install/profiles/xml and then run: 

.. code-block: php

   support/bin/caUtils update-installation-profile -n <name_of_your_profile>

The script will not ask for confirmation, so make sure to backup everything before running it. 

How it Works
------------

The script will generally try to find existing records for the profile definitions (lists, list items, UIs, etc.) by idno or code and, if it will update/overwrite them. It is assumed that the whole "surrounding" element is present in the partial profile. To change a single element in a container, the entire container will have to be put in the partial profile. 

For lists, the entire hierarchy path for the changed item must go in the partial profile. The same goes for almost everything else; the partial configuration exporter described above will do all of this automatically. 

If the script can't find an existing record, a new record will be created as if this were the initial installation. New fields, UIs, and lists  can be added. However, idnos should not be re-used. 

Automatically Push or Replicate Configuration Changes to Another System
-----------------------------------------------------------------------

If there are multiple systems running off the same configuration, the two above features together can automatically push configuration changes from one master system, to all other systems. This is another script in caUtils that can be used like this:

.. code-block: php

   support/bin/caUtils push-config-changes -t http://yourclient/ -u configsync -p topsecret -s 1464870539

The options are:

* **Targets (-t)**: Comma- or semicolon separated list of target systems to push changes to.
* **Username (-u)**: User name to use to log into the targets.
* **Password (-p)**: Password to use to log into the targets.
* **Timestamp (-s)**: Timestamp to use to filter the configuration changes that should be exported/pushed. Optional.

This script will utilize the partial configuration exporter and importer described above. All communication is done via HTTP web services.

.. note:: Do not use the administrator login to do this. It's highly recommended to create a separate user account, and only give it access to the Model JSON service.

.. note:: The timestamp is only used for the very first push to that system. After that the master system will store the last push timestamp and use that instead. The -s parameter is a fixed offset/"starting point" of sorts. We assume that you set up all your systems using the same profile at some point. The starting point could be 2 seconds after that setup.





