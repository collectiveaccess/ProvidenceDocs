Running an Import
=================

**Running an import from the UI**

You can execute a data import from your web browser within the Providence user interface. If you're not comfortable with using terminal, this is a good option. However, for larger imports it's recommended to use the command line, so your import is not tied up by a web browser. Remember to always back up your database before running an import, as you will likely have to tweak imports multiple times. 

From the Providence navigation, go to "Import - Data."  Drag and drop your import mapping XLSX to the importer list, or add the Google Drive link to your import mapping. 

.. note::  Google Drive links you must have sharing settings turned on to "Any User With Link Can View". The advantage of using a Google Drive link for your mapping document is that as you tweak and edit the Google Sheet, you can update the importer by clicking the "Refresh" button in Providence. When using Excel docs, you must delete and re-upload, or change the filename to upload a new version.

Once the mapping document is loaded, you will select it to run an import on the "run import" page, where there are several settings.


=====================    =======================================================================================================
**Setting**              **Description**                                                                       
Importer                 This menu contains all import mappings that are loaded in the importer list. By default, this will be set to whatever mapping you chose on the previous screen.       
Data format              This menu will automatically contain the input format value you set in the import mapping itself. If the data format does not actually correspond to the source data to be imported, change the inputFormat setting in the mapping document.
Data file                This is where you set the data file (or files) that are to be imported. The first option allows you to upload the data file from your machine. The second option allows you to select the file from the import directory. Use the latter option if you are importing a directory of multiple data files at once. The Third option allows you to import data from a Google Drive link, which again needs to have Share settings turned on to work.
Log level                This setting allows you to control the level of detail in the log. The log can capture errors, warnings, alerts, informational messages, and debugging messages. Use the latter for the most comprehensive log.
Testing options          Selecting "dry run" will run the import and generate a log, including errors and debugging messages, without actually creating any records in the system. It's a great way to test an import mapping without actually running an import.
=====================    =======================================================================================================

**Running an import from the terminal**

Before you begin it’s a good idea to make an area for your import mappings and data that’s easily accessible without an inconveniently-long file path. For the sake of this example our import material will live in a Providence directory at:

/support/project/mappings and

/support/project/data

1. *Backup your data*: Before importing, you'll maybe want to back-up your database

         ``mysqldump -u#name -p#password project > ~/project_date.dump``

2. *Define an import*: This is done using *load-import-mapping* option of caUtils:

         ``cd /path_to_Providence/support``

        ``bin/caUtils load-import-mapping --file=project/mappings/mapping1.xlsx``

Once these commands have been run, the new mapping defined in mapping1.xlsx should have been added to imports list. If an existing mapping with the same name as defined in settings section of mapping file already existed, it has been updated.

3. *Run the import*: Once the import have been created, you'll be able to use it. For that you’ll be using the utility import-data, giving the correct name to --mapping parameter.

As you’ll see from:

       ``bin/caUtils help import-data``

there are several options that allow you to designate the format, data source, log preferences, etc.

To run the import:

        ``bin/caUtils import-data --format=XLSX --mapping=mapping1 --source=project/data/Data.xlsx --log=project/log``

With the PHP ncurses extension installed a display will provide moving status indicators including import progress and recent errors.

4. If something gone wrong, it's time to fix mapping or data and import again. To modify your import and rerun the utility, simply restore your database

        ``mysql -u#name -p#password project < ~/project_date.dump``

and start the process again
