Installing on Mac OS
====================

.. note::
    Note: these instructions have been tested on MacOS 10.14 (Mojave). They may or may not work on earlier versions of MacOS.

CollectiveAccess relies on a number of open-source software packages to run, such as MySQL (database server), PHP (programming lanaguage) and Apache or nginx (web server) to name just a few. The simplest way to install these required packages on Mac OS is to use the `Homebrew <https://brew.sh>`_ package manager. Homebrew can be installed by opening a Mac OS Terminal window and pasting this command:

.. code:: bash

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Once installed most required software can be installed using the `brew` command.

Mac OS 10.14 comes with the Apache web server preinstalled. It's tricky to get PHP installed by Homebrew to work with the preinstalled Apache though, so it's best to use Homebrew-managed installation. Before we install Apache with Homebrew, first shutdown the preinstalled server and disable it from starting automatically in the future using these Terminal commands:

.. code:: bash

    sudo apachectl stop
    sudo launchctl unload -w /System/Library/LaunchDaemons/org.apache.httpd.plist 2>/dev/null
    
Now install Apache by typing in Terminal:

.. code:: bash
    
    brew install httpd
    
Next, set Apache to start itself automatically every time you reboot the Mac:

.. code:: bash
    
    sudo brew services start httpd
    
You should now be able to connect to the web server on port 8080 (the default when installing with Brew) by going to the URL `http://localhost:8080` in a web browser running on the Mac. The message "It works!" should display.

.. tip::

    If you want to run Apache on the standard port 80 you'll need to open the Apache configuration file located at `/usr/local/etc/httpd/httpd.conf`, find the line `Listen 8080` and change it to `Listen 80`. Then restart the server with the Terminal command `sudo apachectl -k restart`
    
Next install PHP version 7.2 running in the Terminal:

.. code:: bash
    
    brew install php@7.2
    
Then edit the Apache configuration file located at `/usr/local/etc/httpd/httpd.conf`, adding the line:

.. code:: 

    LoadModule php7_module /usr/local/opt/php@7.2/lib/httpd/modules/libphp7.so

Next, look for this configuration in the Apache configuration file:

.. code:: 

    <IfModule dir_module>
        DirectoryIndex index.html
    </IfModule>
    
and replace it with this:

.. code:: 

    <IfModule dir_module>
        DirectoryIndex index.php index.html
    </IfModule>

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

Restart the server with the Terminal command `sudo apachectl -k restart`. You should now have PHP enabled within your Apache web server.

In order to use the PHP on the Terminal command line (which can be handy) you'll need to add the Homebrew PHP installation directory into your command PATH. Do this by entering in the Terminal:

.. code:: bash

    echo 'export PATH="/usr/local/opt/php@7.2/bin:$PATH"' >> ~/.bash_profile
    echo 'export PATH="/usr/local/opt/php@7.2/sbin:$PATH"' >> ~/.bash_profile
    
Close the current Terminal window and open a new one. Typing `php -v` in the Terminal should return output similar to:

.. code::

    PHP 7.1.23 (cli) (built: Feb 22 2019 22:08:13) ( NTS )
    Copyright (c) 1997-2018 The PHP Group
    Zend Engine v3.1.0, Copyright (c) 1998-2018 Zend Technologies
    
Now let's install MySQL

Next we install various packages to support processing of media: ffmpeg, ghostscript, GraphicsMagick, mediainfo, xpdf, libreoffice

Finally, we need to pull the CollectiveAccess code:

git clone