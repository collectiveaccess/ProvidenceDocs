.. _installation_guide:
Installation
============

CollectiveAccess can be run in any environment that supports PHP 7.x and MySQL 5.7 or better. (Note that PHP 8 is not yet supported, but will be soon). This includes any recent version of Linux, Mac OS or Windows. User-contributed :ref:`installation instructions for Linux <install_linux>` are available, as are more detailed installation guides for:

* :ref:`Ubuntu Linux 20.04 LTS <install_ubuntu_20_04>`
* :ref:`CentOS/Red Hat Enterprise Linux 8 <install_centos8>`
* :ref:`Mac OS 10.14 <install_macos>`
* :ref:`Windows <install_windows>` (Note: this remains for the time-being rough, user-contributed notes)

General Instructions
=================================

Installing software requirements
-------------------------------------

CollectiveAccess relies upon a number of software packages to manage data and process media. Required software is outlined in the :ref:`system requirements <system_requirements>` list. Instructions for installing requirements is more fully described in the installation guides listed above.

Configuring PHP prior to installation
-------------------------------------

With the core software requirements installed on your server examine the newly installed PHP configuration file. A few settings may need adjustment.

Your PHP configuration file is usually named php.ini. On Linux systems the php.ini file is often in /etc/php.ini or /usr/local/lib/php.ini. If you cannot locate your php.ini file, look for its location in the output of phpinfo(), either by running the PHP command line interpreter with the -i option (eg. **php -i**) or running a PHP script that looks like this: **<?php phpinfo(); ?>**  The output from phpinfo() will include the precise location of the php.ini file used to configure PHP.

Once you've found your php.ini file  verify and, if necessary, change the following values:

1. *upload_max_filesize* - sets the maximum size of an uploaded file. If you are uploading large media files (and most CollectiveAccess users are) you will need to raise this to a value larger than the largest file size you are likely to encounter..
2. *post_max_size* - sets maximum size a POST-style HTTP request can be. The default value is 8 megabytes. You should set this to a value somewhat larger than `upload_max_filesize` or 8mb, whichever is larger.
3. *memory_limit*  - sets the maximum amount of memory a PHP script may consume. The default is 128 megabytes which should be enough for many systems, unless you are (a) uploading large images (b) reindexing the search index of a large database or (c) importing data. Even if you have not received memory limit exceeded errors, you may want to increase this limit to between 256mb and 512mb.
4. *display_errors* - determines whether errors are printed to the screen or not. In some installation this is set to "off" by default. While this is a good security decision for public-facing systems, it can make debugging installation problems difficult. It is therefore suggested that while installing and testing CA you set this option to "On"

Installing Providence 
---------------------

To install CollectiveAccess Providence perform the following steps:

1. Set up an empty MySQL database for your installation. Give the database a name and create a login for it with full read/write access. Note the login information - you'll need it later. You can use the MySQL command line or web-based tools like phpMyAdmin to create the database and login.
2. Copy the contents of the CollectiveAccess software distribution to the root of the web server instance in which your installation will run. You can obtain the latest release version from our `download page`_. If you wish to obtain CollectiveAccess from the project's GitHub repository run the following command from the parent of the directory into which you want to install CA:
   ``git clone https://github.com/collectiveaccess/providence.git providence`` where the trailing "providence" is the name of the directory you want your installation to be in. `Git will create the directory for you`_.
3. Copy the setup.php-dist file (in the root directory of the CA distribution) to a file named setup.php. Edit setup.php, changing the various directory paths and database login parameters to reflect your server setup.
4. Make sure the permissions on the ``app/tmp``, ``app/log``, ``vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache`` and ``media`` directories are such that the web server can write to them. In the next step, the web-based installer will need the access to create directories for uploaded media, and to generate cached files. In most hosted environments these permissions will already be set correctly.
5. In a web browser navigate to the web-based installer. If the URL for your installation server is ``http://www.myCollectiveaccessSite.org`` then the URL to the installer is ``http://www.myCollectiveaccessSite.org/install``. Enter your email address and select the installation profile (a profile is a set of pre-configured values for your system) that best fits your needs. Then click on the "begin" button. If you don't see a profile suitable for your project you may want to ask on the `support forum`_ or look at our `list of contributed profiles`_.
6. The installer will give you login information for your newly installed system when installation is complete. Be sure to note this information in a safe place!

.. _Git will create the directory for you: http://git-scm.com
.. _download page: https://collectiveaccess.org/get-started/
.. _list of contributed profiles: http://www.collectiveaccess.org/configuration
.. _support forum : https://support.collectiveaccess.org

Optional post installation tasks
--------------------------------

Set up for background encoding of media
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, CollectiveAccess will process all uploaded media immediately at time of upload. For large media files this can make the user's browser in unresponsive for an extended period of time while CA performs large and complex media conversions. If you expect to be uploading many large media files you can enable background processing of media by setting the __CA_QUEUE_ENABLED__ setting to 1 in your **setup.php** (it is off by default).

Once background processing is enabled, all media files exceeding a specific size will be queued for later processing. Small sizes will still be run "while you wait" unless you modify the media processing configuration. To actually process the images in the queue you must run the script **support/bin/caUtils process-task-queue**. This script is typically run from a **crontab** (in Unix-like operating systems, at least).

You can run the queue processing script as often as you want. Only a single instance of the script is allowed to run at any given time, so you need not worry about out-of-control queue processing scripts running simultaneously and depleting server resources. Note that the queue processing script should *always* be run under a user with write-access to the CA media directory.

What to do if something goes wrong?
-----------------------------------

.. tip::

   If your CollectiveAccess installation fails, the first thing to do is examine error messages on screen or in the log (written to the app/log directory). If you receive a blank white screen odds are error messages are being suppressed in your PHP php.ini configuration file. Try changing the **display_errors** option to "On" and then attempt to reinstall.


If you are totally stumped after reviewing the error messages and logs you can find help on the online support `forum`_. Please include a full description of your problem as well as the operating system you are running, the version of CA you are running, the text of any error messages, the output of phpinfo() and the output of the CA "Configuration Check" (available in the "Manage" menu under "System Configuration") - assuming you are able to log in. We will try our best to resolve your problems quickly.


.. _forum: https://support.collectiveaccess.org