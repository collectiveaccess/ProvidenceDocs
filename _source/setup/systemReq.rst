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
   :header: "Server Requirements", "Notes"
   :widths: 20, 80

   "Operating System", "Linux, Windows (Server 2003, Server 2008, Server 2012, Windows XP and Windows 7, Windows 8 verified to work), Solaris 9+, Mac OS X 10.5+. See the operating system specific notes for additional information on specific operating systems"
   "Server Memory", "For typical uses and small media (eg. 10 meg TIFF images or 2 meg JPEG images) 1gig of RAM is usually adequate to ensure reasonable performance. If you intend to have CA handle large image image files then your server should ideally have three times the size of the largest image when uncompressed. If you don't have this much memory media processing still work, but will be much slower for large files. Processing of video and audio is much less memory intensive but can still benefit from additional memory when present. In general more memory is always better, and 4gigs of RAM is a good baseline assuming it is not cost prohibitive or otherwise impractical." 
   "Data storage", "This is largely project dependent. Collections with quantities of high-quality video, for example, can quickly use up hundreds of gigabytes of storage while lower-resolution image catalogues may require only a few megabytes of space. A simple formula for estimating storage requirements requires an expected number of media items to be catalogued and an average size for those media items. Once these quantities are known an estimate can be derived using some simple arithmetic: <storage required in mb> = (<# of media items> * <average storage requirements per media item in mb>) + (<# of media items> * 5mb). 5mb is estimated overhead of storing derivatives (small JPEG, TilePic pan-and-zoom version, etc.); if is often lower but shouldn't exceed this unless you're storing truly huge images or change the standard media processing configuration. Unless cost-ineffective, it is recommended to double the calculated storage requirements when acquiring hardware. Storage requirements for your metadata and database indices, even if your database is quite large, are usually negligible compared to the storage required for media." 
   "Processor", "Any modern CPU should provide adequate performance. Multiprocessor/multicore architectures are desirable for the improved scalability they provide, and well as the capability to speed the processing of uploaded media. Media processing is often CPU-bound (as opposed to database operations which are often I/O bound) and lends itself to multiprocessing. It is advisable to to obtain at least a 2-way and, if possible, 4-way machine. The extra processor cores are usually not an expensive add-on and often prove valuable in production environments." 

Core software requirements
--------------------------

Providence requires three core open-source software packages be installed prior to installation. Without these packages Providence cannot run:

.. csv-table::
   :header: "Software Package", "Notes"
   :widths: 20, 80

   "Webserver", "`Apache HTTPD version 2.0 or 2.2`_ is recommended. Other web servers that support the `PHP`_ programming language will work as well."
   "MYSQL Database", "`MySQL`_ Version 5.1, 5.5 and 5.6 are supported. Make sure your MySQL installation supports InnoDB tables. CollectiveAccess requires InnoDB support to function properly." 
   "PHP programming language", "`PHP`_ version 5.3.15 or better is required. 5.4 or better are strongly recommended. CollectiveAccess version 1.5 will be the last version to support PHP 5.3. You will need to make sure your PHP installation includes the following extensions: ZIP, libXML, DOM, mbstring, iconv, EXIF, JSON, MySQL, posix and OpenSSL or mcrypt. All of these are configurable options included in the standard PHP distribution and are usually (but not always) enabled in packaged binaries." 

.. _PHP: http://php.net/
.. _Apache HTTPD version 2.0 or 2.2: http://httpd.apache.org/
.. _MySQL: http://dev.mysql.com/

All of these should be available as pre-compiled packages for most Linux distributions and as installer packages for Windows. Apache and PHP come standard with recent versions of Mac OS X (desktop and server versions) - you should not have to install them yourself. MySQL comes standard with Mac OS X Server but not desktop, so you will have to install MySQL yourself if you are using the desktop version of Mac OS X. For Macs, `Brew`_ is a highly recommended way to get all of CA's prerequisites up and running.

A step-by-step recipe for installing Apache, PHP, ImageMagick and MySQL on a Windows host is also available on this wiki.

If setting up Apache, MySQL or PHP is daunting, you may want to consider pre-configured Apache/MySQL/PHP environments available for Windows and Macintosh such as `MAMP`_ and `XAMPP`_. These can greatly simplify setup of CollectiveAccess and its' requirements and are useful tools for experimentation and prototyping. They are not recommended for hosting live systems, however.


.. _Brew: http://brew.sh/
.. _MAMP: http://www.mamp.info/
.. _XAMPP: https://www.apachefriends.org/index.html

Software requirements for media processing
------------------------------------------
Depending upon the types of media you intend to handle with CA you will also need to install various supporting software libraries and tools. None of these is absolutely required for CA to install and operate but without them specific types of media may not be supported (as noted below).

.. csv-table::
   :header: "Software package", "Media types", "Notes"
   :widths: 20, 20, 60

   "GraphicsMagick", "Images", "Version 1.3.16 or better is required. GraphicsMagick is the preferred option for processing image files on all platforms and is better performing than any other option. Be sure to compile or obtain a version of GraphicsMagick with support for the formats you need! Support for some image formats is contingent upon other libraries being present on your server (eg. libTiff must be present for TIFF support])."
   "ImageMagick", "Images", "Version 6.5 or better is required. ImageMagick can handle more image formats than any other option but is significantly slower than GraphicsMagick in most situations. Be sure to compile or obtain a version of ImageMagick with support for the formats you need! Support for some image formats is contingent upon other libraries being present on your server (eg. libTiff must be present for TIFF support])."
   "libGD", "Images", "A simple library for processing JPEG, GIF and PNG format images, GD is a fall-back for image processing when ImageMagick is not available. This library is typically bundled with PHP so you should not need to install it separately. In some cases you may need to perform a manual install or use a package provided by your operating system provider. In addition to supporting a limited set of image formats, GD is typically slows than ImageMagick or GraphicsMagick for many operations. If at all possible install GraphicsMagick on your server."
   "ffmpeg", "Audio, video", "Required if you want to handle video or audio media. Be sure to compile to support the file formats and codecs you require"
   "qt-faststart", "Video", "A utility packaged as part of ffmpeg that modifies QuickTime output from ffmpeg for "quick start" (play back starts as soon as possible) during progressive download. If you will be serving video out of CollectiveAccess via progressive HTTP download you will probably want to install this application. If it is not installed QuickTime files may not start playing until completely downloaded."
   "Ghostscript", "PDF Documents", "Ghostscript 8.71 or better is required to generate preview images of uploaded PDF documents. PDF uploads will still work, but without preview images, if Ghostscript is not installed. If you require color management (if you are dealing with color PDF documents you do), then you must install Ghostscript 9.0 or better."
   "dcraw", "Images", "Required to support upload of proprietary CameraRAW formats produced by various higher-end digital cameras. Note that that AdobeDNG format, a newer RAW format, is supported by GraphicsMagick and ImageMagick."
   "PdfToText", "PDF Documents", "A utility to extract text from uploaded PDF files. If present CA will use PdfToText to extract text for indexing. If PdfToText is not installed on your server CA will not be able to search the content of uploaded PDF documents."
   "PdfMiner", "PDF Documents", "A utility to extract text and text locations from uploaded PDF files. If present CA will use PdfMiner to extract text for indexing and locations to support highlighting of search results during PDF display. If PdfMiner is not installed on your server CA will fall back to PdfToText for indexing and highlighting of search results will be disabled."
   "MediaInfo", "Images, audio, video, PDF Documents", "A library for extraction of technical metadata from various audio and video file formats. If present CA can use MediaInfo to extract technical metadata, otherwise it will fall back to using various built-in methods such as GetID3."
   "ExifTool", "Images", "A library for extraction of embedded metadata from many image file formats. If present CA can use it to extract metadata for display and import."
   "WkHTMLToPDF", "PDF Output", "WkHTMLToPDF is an application that can perform high quality conversion of HTML code to PDF files. If present CollectiveAccess can use WkHTMLToPDF to generate PDF-format labels and reports. Version 0.12.1 is supported. Do not use version 0.12.2, which has bugs that impede valid formatting of output. If WkHTMLToPDF is not installed CollectiveAccess will try to use PhantomJS and failing that fall back to a slower built-in alternative."
   "PhantomJS", "PDF Output", "Like WkHTMLToPDF, PhantomJS is an application that can perform high quality conversion of HTML code to PDF files. If present CollectiveAccess can use PhantomJS to generate PDF-format labels and reports. Version 1.9.8 or better is supported. PhantomJS will not be used if WkHTMLToPDF is installed. If neither WkHTMLToPDF nor PhantomJS are installed CollectiveAccess will fall back to a slower built-in alternative."
   "LibreOffice", "Office Documents", "LibreOffice is an open-source alternative to Microsoft Office. CollectiveAccess can use it to index and create previews for Microsoft Word, Excel and Powerpoint document. LibreOffice 4.0 or better is supported."


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

You may also want to look at our list of OS specific :ref:`Installation` notes.


.. _forum: http://www.collectiveaccess.org/support/forum
