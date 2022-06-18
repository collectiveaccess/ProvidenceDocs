.. _system_requirements:
System Requirements
===================

What is Providence?
-------------------

**Providence** is the core of CollectiveAccess. It includes a data modeling framework, a database, a media handling framework capable of manipulating and converting digital images, video, audio and documents, and a web-based user interface application for cataloguing, searching and managing your collections. If you are starting out with CollectiveAccess, **Providence** is the first (and most important) component you need to install. All other CollectiveAccess components are add-ons to Providence and require a functional Providence installation.

Getting Started
-------------------

Providence is a web-based application that runs on a server. Users access the server from their own computers over a network using standard web browser software. As with any web-based application, Providence is designed to be accessed via the internet, enabling collaborative cataloguing of collections by widely dispersed teams. However, you do **not** have to make your Providence installation accessible on the internet. It will function just as well on a local network with no internet connectivity, or even on a single machine with no network connectivity at all. Who gets to access your system is entirely up to you.

Before attempting an installation verify that your server meets the basic requirements for running Providence:


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

.. _PHP: https://php.net/
.. _Apache: https://httpd.apache.org/
.. _nginx: https://httpd.apache.org/ or https://nginx.org
.. _MySQL: https://dev.mysql.com/
.. _MariaDB: https://mariadb.org/

All of these should be available as pre-compiled packages for most Linux distributions and as installer packages for Windows. For Macs, `Brew`_ is a highly recommended way to get all of CA's prerequisites quickly up and running.

If setting up Apache, MySQL or PHP is daunting, you may want to consider pre-configured Apache/MySQL/PHP environments available for Windows and Macintosh such as `MAMP`_ and `XAMPP`_. These can greatly simplify setup of CollectiveAccess and its requirements and are useful tools for experimentation and prototyping. They are not recommended for hosting live systems, however.


.. _Brew: https://brew.sh/
.. _MAMP: https://www.mamp.info/
.. _XAMPP: https://www.apachefriends.org/index.html

Required and Suggested Software Packages By Distribution
--------------------------------------------------------
**CentOS 8**

Some packages used by CollectiveAccess are available only from 3rd party repositories. Packages recommended here are from the following repositories:

- Remi: https://rpms.remirepo.net/enterprise/remi-release-8.rpm
- EPEL: https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
- RPMFusion: https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm

**Required:**
	
- mysql-server or mariadb-server		[Database server]
- httpd					[Web server]
- redis 				[Cache server]
- php:remi-7.4 php-cli php-gd php-curl php-mysqlnd php-zip php-fileinfo php-gmagick php-opcache php-process php-xml php-mbstring php-redis			[Runtime environment] (Remi, EPEL)

**Suggested:**
- GraphicsMagick-devel	[Image processing]
- ghostscript-devel		
- ffmpeg			[Audio and video processing]
- libreoffice			[Microsoft Office file processing] (EPEL) 
- dcraw				[RAW image format support] 
- mediainfo			[Media metadata extraction] 
- perl-Image-ExifTool			[Media metadata extraction] 
- Poppler				[Media metadata extraction] 


**CentOS 7**

Some packages used by CollectiveAccess are available only from 3rd party repositories. Packages recommended here are from the following repositories:

- Nux: http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
- Remi: http://rpms.remirepo.net/enterprise/remi-release-7.rpm
- EPEL: https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

**Required:**
	
- mysql-server or mariadb-server		[Database server]
- httpd					[Web server]
- redis 				[Cache server]
- php php-pecl-mcrypt php-cli php-gd php-curl php-mysqlnd php-zip php-fileinfo php-devel php-gmagick php-opcache php-process php-xml php-mbstring php-redis			[Runtime environment] (Remi, EPEL)

**Suggested:**
- GraphicsMagick-devel	[Image processing]
- ghostscript-devel		
- ffmpeg			[Audio and video processing] (Nux)
- libreoffice			[Microsoft Office file processing] (EPEL) 
- dcraw				[RAW image format support] 
- mediainfo			[Media metadata extraction] 
- perl-Image-Exifool [Media metadata extraction] 
- xpdf				[Media metadata extraction] 

Each metadata extraction tool is useful for specific types of media. MediaInfo provides the most information when used with audio/video files. ExifTool is best with images. 

**Ubuntu 18.04**

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

**Ubuntu 20.04**

**Required:**

- mysql-server 
- apache2 
- redis-server
- php php-cli php-common php-gd php-curl php-mysqlnd php-zip php-fileinfo php-gmagick php-opcache php-process php-xml php-mbstring php-gmagick

**Suggested:**

- graphicsmagick libgraphicsmagick-dev [Image processing]
- ffmpeg 	[Audio and video processing]
- ghostscript 	[PDF processing] 
- libreoffice 	[Microsoft Office file processing]
- dcraw		[RAW image format support] 
- mediainfo 	[Media metadata extraction]
- poppler 		[Media metadata extraction]
- perl-Image-ExifTool	[Media metadata extraction]


Directories
-----------

If you are running Apache on Linux, the root of your CollectiveAccess installation will usually be located in **/var/www/html.**

Software requirements for media processing
------------------------------------------
Depending upon the types of media you intend to handle with CA you will also need to install various supporting software libraries and tools. None of these is absolutely required for CA to install and operate but without them specific types of media may not be supported (as noted below).

.. csv-table::
   :widths: 20, 20, 60
   :header-rows: 1
   :file: software_requirements.csv

Most users will want at a minimum GraphicsMagick installed on their server, and should install other packages as needed. For image processing you need only one of the following: GraphicsMagick, ImageMagick, libGD.

PHP extensions for media processing (optional)
----------------------------------------------

CA supports two different mechanisms to employ GraphicsMagick or ImageMagick. The preferred option is a PHP extensions that, when installed, provide a fast and efficient way for PHP applications such as CA to access GraphicsMagick or ImageMagick functionality. Alternatively GraphicsMagick or ImageMagick can be invoked as a command-line program directly without any PHP extension.

In general you should try to use a PHP extension rather than the command-line mechanism. The extensions provide **much** better performance. Unfortunately, the extensions have proven to be unstable in some environments and can be difficult to install on Windows systems. If you are running the PHP GMagick (for GraphicsMagick) or IMagick (for ImageMagick) extension and are seeing segmentation faults or incorrect image encoding such as blank images you should remove the extension, let the command-line mechanism take over and see if that improves things. Avoid installing both GMagick and IMagick on the same server. Simultaneous installation of both extensions has been associated with crashes and general instability.

.. note:: GraphicsMagick version 1.3.32 and better break certain functions in the PHP GMagick extension API and cause all media processing to fail in CollectiveAccess in versions prior to 1.7.9. Upgrade to the current version of CollectiveAccess if you are seeing failed processing with later versions of GraphicsMagick from 1.3.32.

Both `Gmagick`_ and `Imagick`_ are available in the PHP PECL repository and often available as packages for various operating systems. They should be easy to install on Unix-y operating systems like Linux and Mac OS X. Installation on Windows can be challenging.


.. _Gmagick: http://pecl.php.net/gmagick
.. _Imagick: http://pecl.php.net/imagick

