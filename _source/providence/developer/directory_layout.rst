Directory Layout 
================

The Providence installation package is a single directory designed to be "droppable" onto a web server for easy installation. The default directory structure is:

* **/app**: contains much of the code that implements Providence, with the exception of the views that define what the user interface looks like (these are housed in the /themes directory further described below). **/app** contains the following sub-directories:
    * **/app/conf:** contains stock versions of all application configuration files with the exception of the bootstrap *setup.php* file located in the Providence root directory.
    * **/app/conf/local:** contains locally modified configuration files.
    * **/app/helpers:** function libraries implementing various helpful functions used internally by Providence.
    * **/app/locale:** contains GetText-format .po and .mo message catalogues used to localize the Provider user interface.
    * **/app/models:** contains classes defining interfaces to most database tables (which generally correspond on a 1-to-1 basis with data entities) in the Providence schema. These classes are used to manipulate data in the database - virtually all write operations on the database take place through these classes.
    * **/app/controllers:** contains all action controllers - the classes that actually handle requests, invoke library and model methods and load views for display. All controller classes are organized into subdirectories under 
    */controllers* that mirror the structure of the URLs used to invoke them.
    * **/app/lib:** contains code libraries used by Providence. It is divided into two subdirectories:
        * **/app/lib/core:** contains "core" libraries implementing generally useful functions in a manner not specific to Providence. (Or to put it another way, core libraries are reusable across applications and make few, if any, assumptions specific to Providence).
        * **/app/lib/ca:** contains libraries implementing Providence-specific functionality.
    * **/app/plugins:** contains modules implementing various types of add-on functionality.
    * **/app/printTemplates:** contains templates for generating printable PDFs
    * **/app/tmp:** a temporary directory used for queuing media for background processing, for housing of cache files, and for processing of uploaded batches of media. This directory **must be write-able by the user the web server runs under**, otherwise errors will occur.
* **/install:** contains the Providence installer. This should be deleted once Providence is successfully installed.
* **/js**: contains all Javascript libraries.
* **/media:** contains all uploaded media (images, audio, video, PDF documents, etc.)and files derived from that media.
* **/support:** contains various support files and useful administrative utilities in the following subdirectories:
* **/support/sql:** contains the Providence database schema and migrations. Useful for developers.
* **/support/icons:** contains graphics used as default icons for uploaded media in cases where a thumbnail image cannot be derived (for audio files, for example).
* **/support/import:** contains utilities for importing specific types of data from external sources into Providence. This directory includes, for instance, a script for importing the Getty Art & Architecture Thesaurus.
* **/support/bin:** contains the caUtils and caTools command-line utilities.
* **/support/utils:** contains a few administrative utilities retained for compatibility reasons.
* **/themes:** contains the "views" defining what various parts of the Providence user interface look like. You can have multiple views defining different look-and-feels for the software. Each theme is contained in its own subdirectory. The standard Providence package ships with a single default theme contained in */themes/default.* Each theme contains multiple view directories.
* **/viewers:** contains web-based viewing software for various types of media.

It also contains the following files (not including informational README and licensing text files:

* **index.php:** the "front controller" of the system; all requests go through this PHP script and are subsequently dispatched to action controllers in /app/controllers using information specified in the URL.
* **setup.php-dist**: the distribution copy of the bootstrap configuration file used by the application to find its components and configuration files. The distribution copy is meant to be copied to *setup.php,* and modified to suit the installation.

