Cookbook: Installation
======================

This section provides some real examples of common challenges that may arise during the installation of CollectiveAccess software. 

Each scenario begins with a “problem,” describing a certain challenge or question that may occur during installation. There is an accompanying “solution” provided for each problem, which outlines how to carry out the necessary steps to reach a specific outcome. 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online Support Forum, Online Chat, Slack Channel for Developers, and Back- and Front-end GitHub Repositories. 

Contents
--------
* `Performing a Quick Installation of CollectiveAccess for Evaluation`_
* `Meeting Basic Server Requirements`_
* `Core Software Requirements`_
* `Configuring PHP`_ 
* `Installing CollectiveAccess From Git`_ 
* `Installing CollectiveAccess on Shared Servers`_ 
* `Media Upload Issues on Shared Servers`_

Performing a Quick Installation of CollectiveAccess for Evaluation
------------------------------------------------------------------

**Problem**: You want to install CollectiveAccess quickly, without worrying about server configuration, for evaluation purposes.

**Solution**: Try the quick start installation package for Mac or Windows: http://collectiveaccess.org/download

Meeting Basic Server Requirements
---------------------------------

**Problem**: You want to make sure your server meets the basic CollectiveAccess requirements.

**Solution**: The basic server requirements include:
    -Operating system: Linux, Windows (Server 2003, Server 2008, Windows XP and Windows 7 verified to work), Solaris 9+, Mac OS X 10.5+.
    -Server memory: For typical uses and small media (eg. 10 meg TIFF images or 2 meg JPEG images) 1gig of memory is usually adequate to ensure reasonable performance.
    -Data storage: A simple formula for estimating storage requirements requires an expected number of media items to be catalogued and an average size for those media items. Once these quantities are known an estimate can be derived using some simple multiplication: <storage required> = <# of media items> * <average storage requirements per media item> * 1.5. The factor 1.5 is used to take into account the overhead of storing derivatives.
    -Processor: Any modern CPU should provide adequate performance.
    -Read Installing Providence for more details. 

Core Software Requirements
--------------------------

**Problem**: You are configuring a server to run CollectiveAccess, and are checking that all the software requirements are in place.

**Solution**: The core requirements include:
    -MySQL version 5.0, 5.1 or 5.5. Make sure your MySQL installation supports InnoDB tables.
    -PHP version 5.3.6 or better is required. 5.4 is supported. You will need to make sure your PHP installation includes the following extensions: ZIP, libXML, DOM, mbstring, iconv, EXIF, JSON, MySQL, and posix
    -Apache HTTPD version 2.0 or 2.2 is recommended. Other web servers that support the PHP programming language will work as well.

Core Media processing software for type-specific media handling includes:
    -ImageMagick version 6.5 or better
    -ffmpeg 
    -Ghostscript
    -and more, depending on media type
	-See Software Requirements. 

Configuring PHP
---------------

**Problem**: You are configuring PHP prior to installation.

**Solution**: Your PHP configuration file is usually named php.ini. Check the following settings:
    -post_max_size: the default value is 8 megabytes. If you are uploading large media files (and most CollectiveAccess users are) you will need to raise this to a value larger than the largest file size you are likely to encounter.
    -upload_max_filesize: set this to the same value you set post_max_size.
    -memory_limit: the default is 128 megabytes which should be enough for many systems, unless you are (a) uploading large images or (b) reindexing the search index of a large database. If you received memory limit errors, you should increase this limit.
    -display_errors: in some installations, this is set to "off" by default. It is suggested that while installing and testing CA you set this option to "On.”
    -See Configuring PHP. 

Installing CollectiveAccess From Git
------------------------------------

**Problem**: Your server is configured and you want to pull from git to install CollectiveAccess.

**Solution**: Set up an empty MySQL database for your installation. Run the following command from the parent of the directory into which you want to install CA:

git clone http://github.com/collectiveaccess/providence.git providence 

where the trailing "providence" is the name of the directory you want your installation to be in. Git will create the directory for you.

Copy the setup.php-dist file (in the root directory of the CA distribution) to a file named setup.php. Edit setup.php, changing the various directory paths and database login parameters to reflect your server setup. Make sure the permissions on the app/tmp, app/lib/core/Parsers/htmlpurifier/standalone/HTMLPurifier/DefinitionCache and server root directories are such that the web server can write to them. In a web browser navigate to the web-based installer (http://www.myCollectiveaccessSite.org/install). Enter your email address and select the installation profile that best fits your needs. Then click on the "begin" button. For more, see Installing Providence.

Installing CollectiveAccess on Shared Servers
---------------------------------------------

**Problem**: You want to install CollectiveAccess on a cheap, shared server.

**Solution**: Look for a host that can provide support for InnoDb tables for MySQL, such as: 
    -PHP 5.3.6+ 
    -Git
    -Ffmpeg
    -Image Magick.
    -See Installing on Cheap Shared Servers

Media Upload Issues on Shared Servers
-------------------------------------

**Problem**: You're having issues uploading media after installing on a cheap, shared server.

**Solution**: Take a look at Manage > Administration > Configuration Check. You may need to increase the values of some of the Suhosin configurations (PHP). On a shared server, you'll need to set this in the php.ini or phprc file.

Also see Installing on Cheap Shared Servers. 

