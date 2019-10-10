System Requirements
===================

What is Providence?
-------------------

**Providence** is the core of CollectiveAccess. It includes a schema modeling framework, a database, a media system framework capable of manipulating and converting digital images, video, audio and documents, and a web-based user interface application for cataloguing, searching and managing your collections. If you are starting out with CollectiveAccess, **Providence** is the first (and most important) component you need to install. All other CollectiveAccess components are add-ons to Providence and require a functional Providence installation.

Getting Started
-------------------

Providence is a web-based application that runs on a designated server computer. Users access the server from their own computers over a network using standard :ref:`web browser software <Supported_web_browsers>`. As with any web-based application, Providence is designed to be accessed via the internet, enabling collaborative cataloguing of collections by widely dispersed teams. However, you do **not** have to make your Providence installation accessible on the internet. It will function just as well on a local network with no internet connectivity, or even on a single machine with no network connectivity at all. Who gets to access your system is entirely up to you and your network administrator.

The first step, before attempting an installation, is to verify that your server meets the basic requirements for running Providence:


.. csv-table::
   :widths: 20, 80
   :header-rows: 1
   :file: server_requirements.csv

Core software requirements
--------------------------

Providence requires three core open-source software packages be installed prior to installation. Without these packages Providence cannot run:

.. csv-table::
   :widths: 20, 80
   :header-rows: 1
   :file: software_packages.csv

.. _PHP: http://php.net/
.. _Apache HTTPD version 2.0 or 2.2: http://httpd.apache.org/
.. _MySQL: http://dev.mysql.com/

All of these should be available as pre-compiled packages for most Linux distributions and as installer packages for Windows. Apache and PHP come standard with recent versions of Mac OS X (desktop and server versions) - you should not have to install them yourself. MySQL comes standard with Mac OS X Server but not desktop, so you will have to install MySQL yourself if you are using the desktop version of Mac OS X. For Macs, `Brew`_ is a highly recommended way to get all of CA's prerequisites up and running.

A step-by-step recipe for installing Apache, PHP, ImageMagick and MySQL on a Windows host is also available on this wiki.

If setting up Apache, MySQL or PHP is daunting, you may want to consider pre-configured Apache/MySQL/PHP environments available for Windows and Macintosh such as `MAMP`_ and `XAMPP`_. These can greatly simplify setup of CollectiveAccess and its' requirements and are useful tools for experimentation and prototyping. They are not recommended for hosting live systems, however.


.. _Brew: http://brew.sh/
.. _MAMP: http://www.mamp.info/
.. _XAMPP: https://www.apachefriends.org/index.html

Required and Suggested Software Packages By Distribution
--------------------------------------------------------

**CentOS 7**

Some packages used by CollectiveAccess are available only from 3rd party repositories. Packages recommended here are from the following repositories:

- Nux: http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
- Remi: http://rpms.remirepo.net/enterprise/remi-release-7.rpm
- EPEL: https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

**Required:**
	
- mariadb-server		[Database server]
- httpd				[Web server]
- redis-server 			[Cache server]
- php php-mcrypt php-cli php-gd php-curl php-mysqlnd php-zip php-fileinfo php-devel php-gmagick php-opcache php-process php-xml php-mbstring php-redis			[Runtime environment] (Remi, EPEL)

**Suggested:**
- GraphicsMagick-devel	[Image processing]
- ghostscript-devel		
- ffmpeg-devel			[Audio and video processing] (Nux)
- libreoffice			[Microsoft Office file processing] (EPEL) 
- dcraw				[RAW image format support] 
- mediainfo			[Media metadata extraction] 
- exiftool			[Media metadata extraction] 
- xpdf				[Media metadata extraction] 

When installing a tool for media metadata extraction, you need only install one, although having multiple installed will not cause issues.

**Ubuntu 16.04**

Some packages used by CollectiveAccess are available only from 3rd party repositories. Packages recommended here are from the following repositories:

- ondrej/php: ppa:ondrej/php
- PECL: https://pecl.php.net

**Required:**

- mysql-server 
- apache2 
- redis-server
- php7.x libapache2-mod-php7.x php7.x-common php7.x-mbstring php7.x-xmlrpc php7.x-gd php7.x-xml php7.x-intl php7.x-mysql php7.x-cli php7.x-mcrypt php7.x-zip php7.x-curl php7.x-posix php7.x-dev php-pear php7.x-
- pecl.php.net/gmagick-2.0.5RC1 [pecl install channel://pecl.php.net/gmagick-2.0.5RC1]

**Suggested:**

- graphicsmagick libgraphicsmagick-dev [Image processing]
- ffmpeg 	[Audio and video processing]
- ghostscript 	[PDF processing] 
- libreoffice 	[Microsoft Office file processing]
- dcraw		[RAW image format support] 
- mediainfo 	[Media metadata extraction]
- xpdf 		[Media metadata extraction]
- exiftool	[Media metadata extraction]


Directories
-----------

If you are running Apache on Linux, by default the root of your CollectiveAccess installation will likely be in **/var/www/html.**

Software requirements for media processing
------------------------------------------
Depending upon the types of media you intend to handle with CA you will also need to install various supporting software libraries and tools. None of these is absolutely required for CA to install and operate but without them specific types of media may not be supported (as noted below).

.. csv-table::
   :widths: 20, 20, 60
   :header-rows: 1
   :file: software_requirements.csv

Most users will want at a minimum GraphicsMagick and ffmpeg installed on their server, and should install other packages as needed. For image processing you need only one of the following: GraphicsMagick, ImageMagick, libGD.

PHP extensions for media processing (optional)
----------------------------------------------

CA supports two different mechanisms to employ GraphicsMagick or ImageMagick. The preferred option is a PHP extensions that, when installed, provide a fast and efficient way for PHP applications such as CA to access GraphicsMagick or ImageMagick functionality. The option option invokes the GraphicsMagick or ImageMagick command-line program directly without any PHP extension.

In general you should try to use a PHP extension rather than the command-line mechanism. The extensions provide **much** better performance. Unfortunately, the extensions have proven to be unstable in some environments and can be difficult to install on non-Linux systems (and in particular Windows). If you are running the PHP GMagick (for GraphicsMagick) or IMagick (for ImageMagick) extension and are seeing segmentation faults or incorrect image encoding such as blank images you should remove the extension, let the command-line mechanism take over and see if that improves things.

Both `Gmagick`_ and `Imagick`_ are available in the PHP PECL repository and often available as packages for various operating systems. They should be easy to install on Unix-y operating systems like Linux and Mac OS X. Installation on Windows is a waking nightmare.


.. _Gmagick: http://pecl.php.net/gmagick
.. _Imagick: http://pecl.php.net/imagick

Configuring PHP prior to installation
-------------------------------------

Once you have the core software requirements installed on your server you're almost ready to install CA. But first you will need to take a look at your PHP configuration file and possibly adjust a few options.

Your PHP configuration file is usually named php.ini. On Linux systems the php.ini file is often in /etc/php.ini or /usr/local/lib/php.ini. If you cannot locate your php.ini file, look for its location in the output of phpinfo(), either by running the PHP command line interpreter with the -i option (eg. **php -i**) or running a PHP script that looks like this: **<?php phpinfo(); ?>**  The output from phpinfo() will include the precise location of the php.ini file used to configure PHP.

Once you've found your php.ini file open it up and verify and, if necessary, change the following values:

1. *post_max_size* - sets maximum size a POST-style HTTP request can be. The default value is 8 megabytes. If you are uploading large media files (and most CollectiveAccess users are) you will need to raise this to a value larger than the largest file size you are likely to encounter.
2. *upload_max_filesize* - sets the maximum size of an uploaded file. Set this to a slightly smaller value that that set for post_max_size.
3. *memory_limit*  - sets the maximum amount of memory a PHP script may consume. The default is 128 megabytes which should be enough for many systems, unless you are (a) uploading large images (b) reindexing the search index of a large database or (c) importing data. Even if you have not received memory limit exceeded errors, you may want to increase this limit to 196 or 256 megabytes.
4. *display_errors* - determines whether errors are printed to the screen or not. In some installation this is set to "off" by default. While this is a good security decision for public-facing systems, it can make debugging installation problems difficult. It is therefore suggested that while installing and testing CA you set this option to "On"

Installing Providence (finally!)
--------------------------------

Now that you've got all the requirements in place it's time to set up CollectiveAccess. You will need to perform the following steps:

1. Set up an empty MySQL database for your installation. Give the database a name and create a login for it with full read/write access. Note the login information - you'll need it later. You can use the MySQL command line or web-based tools like phpMyAdmin to create the database and login.
2. Copy the contents of the CollectiveAccess software distribution to the root of the web server instance in which your installation will run. You can obtain the latest release version from our `download page`_. If you are to obtain CollectiveAccess from the project's GitHub repository then run the following command from the parent of the directory into which you want to install CA:
   ``git clone https://github.com/collectiveaccess/providence.git providence`` where the trailing "providence" is the name of the directory you want your installation to be in. `Git will create the directory for you`_.
3. Copy the setup.php-dist file (in the root directory of the CA distribution) to a file named setup.php. Edit setup.php, changing the various directory paths and database login parameters to reflect your server setup.
4. Make sure the permissions on the ``app/tmp``, ``vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache`` and ``media`` directories are such that the web server can write to them. In the next step, the web-based installer will need the access to create directories for uploaded media, and to generate cached files. In most hosted environments these permissions will already be set correctly.
5. In a web browser navigate to the web-based installer. If the URL for your installation server is ``http://www.myCollectiveaccessSite.org`` then the URL to the installer is ``http://www.myCollectiveaccessSite.org/install``. Enter your email address and select the installation profile (a profile is a set of pre-configured values for your system) that best fits your needs. Then click on the "begin" button. If you don't see a profile suitable for your project you may want to ask on the `support forum`_ or look at our `list of contributed profiles`_.
6. The installer will give you login information for your newly installed system when installation is complete. Be sure to note this information in a safe place!

.. _Git will create the directory for you: http://git-scm.com
.. _download page: http://www.collectiveaccess.org/download
.. _list of contributed profiles: http://www.collectiveaccess.org/configuration
.. _support forum : http://collectiveaccess.org/support/forum

Optional post installation tasks
--------------------------------

Set up for background encoding of media
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, CollectiveAccess will process all uploaded media immediately upon receipt. For large media files this can make the user's browser in unresponsive for an extended period of time while CA performs large and complex media conversions. If you expect that you will be uploading many large media files you can enable background processing of media by setting the __CA_QUEUE_ENABLED__ setting to 1 in your **setup.php** (it is off by default).

Once background processing is enabled, all media files exceeding a specific size will be queued for later processing. Small sizes will still be run "while you wait" unless you modify the media processing configuration. To actually process the images in the queue you must run the script **support/utils/processTaskQueue.php** This script is typically run from a **crontab** (in Unix-like operating systems, at least) with the hostname of your install as the first parameter. The hostname is needed in case you are running several instances of CA within the same install. If you are only running a single instance (just about everyone is) then you can just pass "default" as the parameter.

You can run the **processTaskQueue.php** script as often as you want. Only a single instance of the script is allowed to run at any given time, so you need not worry about out-of-control queue processing scripts running simultaneously and depleting server resources. Note that the **processTaskQueue.php** should *always* be run under a user with write-access to the CA media directory.

What to do if something goes wrong?
-----------------------------------

.. tip::

   If your CollectiveAccess installation fails, the first thing to do is look at the error messages, if any. If you receive a blank white screen odds are error messages are being suppressed in your PHP php.ini configuration file. Try changing the **display_errors** option to "On" and then attempt to reinstall.


If you are totally stumped after reviewing the error messages and logs, ask us for help! You can post your questions on the CA support `forum`_. Please include a full description of your problem as well as the operating system you are running, the version of CA you are running, the text of any error messages, the output of phpinfo() and the output of the CA "configuration check" (available in the "Manage" menu under "System Configuration") - assuming you are able to log in. We will try our best to resolve your problems quickly.

You may also want to look at our list of OS specific :ref:`Installation <installation_guide>` notes.


.. _forum: http://www.collectiveaccess.org/support/forum
