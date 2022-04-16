Backing up a CollectiveAccess installation
==========================================

.. contents::
   :local:
   
Three types of data need to be backed up on a regular basis:

- The database
- Digital media
- Configuration files

All of the procedures outlined in this document assume that you're using a tool that backs up files - something that copies files on your system to some other archival medium, and can restore them from that medium as needed. This could be a program such as BRU (http://www.tolisgroup.com/), AMANDA (http://www.amanda.org/) or Bacula (http://www.bacula.org/) archiving your files to digital tape or a command-line Unix program such as rsync mirroring files from your server to another server or an external hard drive.

Backing up your database
------------------------

To back-up your CollectiveAccess database, you need to have MySQL "dump" it to a file and then have your back-up tool archive that file. MySQL comes with a command-line program called mysqldump that can create a complete snapshot of a database in a single file. The snapshot file will contain SQL commands to restore both the structure of the database and all of the data. A typical command-line invocation of mysqldump would look something like this:

.. code-block:: none

   mysqldump -udb_login_name -pdb_login_password database_name > /path/ to/dumpfile/my_database_backup.dump
	
where the *db_login_name*, *db_login_password* and *database_name* reflect the settings on your system, and *my_database_backup.dump* is the name of the newly created file. 

You can automate the execution of mysqldump by adding an invocation to your **crontab** (on Unix- like systems) or equivalent on Windows. A more featureful solution is a MySQL backup automation script such as AutoMySQLBackup which can take care of naming and compression of snapshots, and can easily handle multiple databases.

Backing up your digital media
-----------------------------

CollectiveAccess stores all uploaded and derived digital media in a series of sub-directories under /media in the root of your installation. Simply backing up the entire contents of media is sufficient in most cases.

Backing up your configuration files
-----------------------------------

CollectiveAccess configuration files are stored in a sub-directory named conf under app (aka. **app/conf**). This entire directory should be backed up. Your **setup.php** file, located in the root of your installation and which contains some basic configuration information such as the locations of the application configuration file, should also be backed up.

Summary
-------

For a typical CollectiveAccess installation where media and configuration files are stored in the typical (and pre-configured) locations, and assuming that you are writing database snapshots into a "dumps" directory in a location outside of the web server root, you should be backing-up, at a minimum, the following directories: 

- /path/to/mysql/dumps
- /path/to/collectiveaccess/app/conf
- /path/to/collectiveaccess/media
- /path/to/collectiveaccess/setup.php

Depending upon the setup and size of your CollectiveAccess installation, server and back-up system you may elect to simply back-up the entire CollectiveAccess directory structure including the application code and supporting directories, rather than specifically selecting the directories above. This has the advantage of providing a complete ready-to-run backup and is the preferred option if it is possible. If you cannot do this, you can always download the CollectiveAccess application code at CollectiveAccess.org.
