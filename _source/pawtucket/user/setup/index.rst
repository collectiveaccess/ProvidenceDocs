What is Pawtucket2?
~~~~~~~~~~~~~~~~~~~

`Pawtucket2` is general purpose public-access publishing tool for CollectiveAccess. It provides an easy way to create web sites around data entered into CollectiveAccess using the Providence cataloguing tool. Pawtucket2 provides many features for displaying, finding and interacting with collections information, including:

* Responsive, mobile-friendly interface based upon [http://getbootstrap.com Bootstrap].
* Full text search
* Highly configurable search and browse interfaces for all record types
* Ability to browse within search results (aka. "refine your search")
* Configurable detail displays for collection objects and all authorities- you can show as much or as little information from your database as you want
* Built-in support for "galleries" - simple online exhibitions using curator-defined sets.
* Built-in support for user-created tags, comments, ratings, image annotations and presentations
* Export search and browse results to formatted PDFs, Excel and PowerPoint

The current version is available on GitHub at https://github.com/collectiveaccess/pawtucket2/releases

Pawtucket2 is meant to be customized. The base installation includes a default theme that supports all functionality in a plain white design. By simply editing the CSS stylesheets and system header and footer templates you can have Pawtucket2 fit into most any existing design scheme. More complex customization can be achieved by editing Pawtucket2 configuration, modifying its templates and extending its functionality through theme-specific controllers, helpers and views.

Getting Started
===============

Pawtucket2 is designed to work with an existing Providence database. If you have not already Providence you must do so before trying to set up Pawtucket2.

Before attempting an installation, verify that your server meets the basic requirements for running Pawtucket2. They are the same as those of Providence.

Software requirements
=====================

The core software requirements for Pawtucket2 are the same as for Providence: a web server (Apache 2.4 or nginx), MySQL database (version 5.7 or 8.0) and the PHP programming language (version 7.4).

You should also try to have the same media processing software installed as for Providence (of course, if you are running both on the same server this will not be a problem), but this is not required as Pawtucket2 does not currently accept media uploads.

Configuring PHP prior to installation
=====================================

Once you have the core software requirements installed on your server you're almost ready to install Pawtucket2. But first you will need to take a look at your PHP configuration file and possible adjust a few options.

Your PHP configuration file is usually named php.ini. On Linux systems the php.ini file is often in /etc/php.ini or /usr/local/lib/php.ini. If you cannot find your php.ini file, look for its location in the output of phpinfo(), either by running the PHP command line interpreter with the -i option (eg. `php -i`) or running a PHP script that looks like this: `<?php phpinfo(); ?>`  The output from phpinfo() will include the precise location of the php.ini file used to configure PHP.

Once you've found your php.ini file, open it up and verify and, if necessary, change the following values:

* `memory_limit`  - sets the maximum amount of memory a PHP script may consume. The default is 128 megabytes which should be more than enough. If you don't want to leave it that high, you should be able to run with the limit set as low as 32 megabytes. If you received memory limit exceeded errors, you should increase this limit.
* `display_errors` - determines whether errors are printed to the screen or not. In some installation this is set to "off" by default. While this is a good security decision for public-facing systems, it can make debugging installation problems almost impossible. It is therefore suggested that while installing and testing Pawtucket2 you set this option to "On"

Installing Pawtucket2
=====================

Now that you've got all the requirements in place it's time to set up Pawtucket2. You will need to perform the following steps. Note that these instructions assume that you are installing Pawtucket2 in a subdirectory called "pawtucket" located in the server root of an existing Providence installation. You can also install Pawtucket2 in a completely separate server root, or make Providence a sub-directory of your Pawtucket2 installation. You can even install Pawtucket2 on a completely different server than Providence. All of these options are permutations of the process outlined below.

To install Pawtucket2 in a sub-directory of an existing Providence installation:

* Make sure you have a working Providence installation. 
* Copy the contents of the Pawtucket2 software distribution to a directory called `pawtucket` within the Providence server root. If you are to obtain Pawtucket2 from the project's GitHub repository then run the following command from the parent of the directory into which you want to install Pawtucket2: `git clone http://github.com/collectiveaccess/pawtucket2.git pawtucket` where the trailing "pawtucket" is the name of the directory you want your installation to be in. Git will create the directory for you.
* Copy the setup.php-dist file in your `pawtucket` directory to a file named setup.php in the same directory. Edit setup.php, changing the various directory paths and database login parameters to reflect your server setup. `Note: you must specify a valid login to the same MySQL database used by your Providence installation.` It doesn't have to be the same login, but it must have full access to the same database.
* Make sure the permissions on the `pawtucket/app/tmp` directories are such that the web server can write to them. This will allow Pawtucket2 to generate caches, improving performance. 
* By default Pawtucket2 will serve media uploaded in Providence out of the `media` directory in the root of its installation directory. To ensure that Pawtucket2 can find your media create a symbolic link called `media` from the media directory in your Providence installation to the root of your Pawtucket2 installation.  (If you can't create a symbolic link, either because you're running on Windows or running Pawtucket2 on a different server than Providence see the next section)
* In a web browser navigate to the `pawtucket` subdirectory. (If your login to CollectiveAccess/Providence is `http://localhost/ca/` then your access to Pawtucket2 should be `http://localhost/ca/pawtucket/`)
 
That's it! There is no installer for Pawtucket2. It should run directly.

Dealing with symlink troubles
=============================

Pawtucket2 is by default configured to serve media uploaded in Providence out of its own `media` folder in the Pawtucket2 root directory. If you're using a Unix-based operating system (including Mac OS X where they are called 'aliases') and running both Providence and Pawtucket2 on the same server, the simplest and most efficient way to ensure that Pawtucket2 can "see" all of the media in Providence is to create a symbolic link from the Pawtucket2 `media` directory to the Providence `media` directory. 

If you're running on an operating system that doesn't support symbolic linking such as Windows versions prior to Vista, or are running Providence and Pawtucket2 on different servers then things get a bit more complicated.

For Windows servers your options are:

* Copy the entire Providence `media` directory to Pawtucket2. This will work but you'll double your storage requirements and have to keep the Pawtucket2 copy of `media` in sync with the Providence original.
* Add a third party symbolic linking utility. 

For users running Providence and Pawtucket2 on different servers:

* Copy the entire Providence `media` directory to Pawtucket2. This will work but you'll double your storage requirements and have to keep the Pawtucket2 copy of `media` in sync with the Providence original. This may not be a bad thing if you are running completely separate installations (including database) as it allows you to present a snapshot of your system the public without exposing your Providence system.
* Mount the Providence media directory on the Pawtucket2 server using a network file system such as NFS.

If you happen to be running Pawtucket2 in a subdirectory within the Providence installation you can also edit your Pawtucket2 `app/conf/global.conf` to point directly to the Providence media directory.  Edit `ca_media_url_root` setting to point to the `media` folder in Providence. If your Providence install is in `/ca` and your Pawtucket2 install is in `/ca/pawtucket` then you'd want to change the line to read:

`ca_media_url_root = /ca/media/<app_name>`

The `ca_media_root_dir` setting will also need a direct path to the media subfolder in PROVIDENCE written all the way from the root `such as` (remember: you'll need to add YOUR Windows path all the way down to the media directory in Providence):

`ca_media_root_dir = d:/Apache2/htdocs/ca/media/<app_name>`

What to do if something goes wrong?
===================================

If your Pawtucket2 installation fails look at the error messages, if any. If you get a blank white screen, odds are error messages are being suppressed in your PHP php.ini configuration file. Try changing the `display_errors` option to "On" and then try accessing Pawtucket2 again.

If you are totally stumped on an installation issue you can post your questions on the CA support forum at https://support.collectiveaccess.org. Please include a full description of your problem as well as the operating system you are running, the text of any error messages and the output of phpinfo(). We will try our best to resolve your problems quickly.