Cookbook: Media Processing
==========================

This section provides some real examples of common challenges that may arise during media processing in CollectiveAccess. 

Each scenario in this section begins with a “problem,” describing a certain challenge or question that may occur. There is an accompanying “solution” provided for each problem, which outlines how to carry out the necessary steps to reach a specific outcome. 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online `Support Forum <https://collectiveaccess.org/support/>`_, `Online Chat <https://gitter.im/collectiveaccess/support>`_, `Slack Channel for Developers <https://collectiveacc-uye7574.slack.com/join/signup#/domain-signup>`_, and `Back-end <https://github.com/collectiveaccess/providence>`_ and `Front-end <https://github.com/collectiveaccess/pawtucket2>`_ GitHub Repositories. 

See also: `Media <file:///Users/charlotteposever/Documents/ca_manual/providence/user/media/index.html>`_. 

Contents
--------

* `Upload PDFs to CollectiveAccess`_
* `Software to Parse PDF Files in CollectiveAccess`_
* `PDF Preview Icons Won’t Display`_
* `Archive and View Microsoft Word/Excel/Powerpoint Documents`_

Upload PDFs to CollectiveAccess
-------------------------------

**Problem**: Uploads of PDF files fail with the error message "Unknown file type not accepted by media.” 

**Solution**: The error is caused by an inability to identify your uploaded file as a PDF. CollectiveAccess' PDF plugin employs one of three possible identification methods:

1. GraphicsMagick: if GraphicsMagick is installed and configured, it will be used to parse and identify PDF files.
2. ImageMagick: if GraphicsMagick is not installed, and ImageMagick is available, it will be used to parse and identify PDF files.
3. Zend_PDF software will be used to parse PDF files, if neither GraphicsMagick or ImageMagick is available. 

By default, CollectiveAccess will try to use GraphicsMagick, then ImageMagick, and finally Zend_PDF. You can disable GraphicsMagick and/or ImageMagick for identification of PDFs using the *dont_use_graphicsmagick_to_identify_pdfs* and *dont_use_imagemagick_to_identify_pdfs* directives in *app.conf*. 

If you are finding that valid PDFs are being rejected by CollectiveAccess, try disabling one or both of these options. Because there is no ideal processing system for PDFs, CollectiveAccess defaults to a typically ideal usage pattern, while providing a means to override the default behavior.

Software to Parse PDF Files in CollectiveAccess
-----------------------------------------------

Three main software programs are used to parse and read PDF files in CollectiveAccess. Some are more effective than others, while some do not require the installation of additional software. Depending on what version of CollectiveAccess is being used for a collections system, different programs may function more efficiently for you. 

**Zend_PDF** has the advantage of not requiring installation of additional software. It can be used no matter the server setup. Unfortunately, Zend_PDF often fails to identify format PDFs that are used post-CollectiveAccess Version 1.6. It tends to use a relatively large amount of memory to do the job.
**ImageMagick** and **GraphicsMagick** are, in general, more memory efficient and support a wider range of PDFs. Unfortunately, they require additional software installation, are often not available on shared servers, and occasionally crash on specific PDFs.

PDF Preview Icons Won’t Display
-------------------------------

**Problem**: Uploads of PDF files are successful, but instead of preview icons a generic document icon is displayed.

**Solution**: There are a several possible causes:
* You don't have Ghostscript installed on your server.
* Ghostscript is installed, but the path to it in external_applications.conf is incorrect.
* You don't have a graphics processing plugin installed that can support TIFF images. TIFFs are used as an in-process format for previews. GraphicsMagick and ImageMagick can, and usually do, support TIFFs.
* You have GraphicsMagick or ImageMagick installed, but they lack TIFF format support.

Most Linux servers already have Ghostscript installed, and it is readily installed on Mac OS X using Brew. Windows installers are also available.

You can check if the path to Ghostscript is set correctly using the "Configuration Check" screen, available under the Manage > Administration menus. On Unix-like operating systems such as Linux and Mac OS X the path to Ghostscript is most often either */usr/bin/gs* or */usr/local/bin/gs*.

If lack of TIFF support is the issue, then install either GraphicsMagick or ImageMagick with libtiff support. On Mac OS X using Brew to install GraphicsMagick, be sure to use the --with-libtiff option, otherwise the resulting installation will not support TIFFs.

Archive and View Microsoft Word/Excel/Powerpoint Documents
----------------------------------------------------------

**Problem**: You want to include Microsoft Office documents (Word, Excel and/or Powerpoint) in your CollectiveAccess archive.

**Solution**: CollectiveAccess can automatically detect the Office XML formats available, and store the uploaded files for later download. CollectiveAccess cannot index the contents of those files for search or generate page previews for viewing within a web browser.

If you want previews and indexing of content, or you want to upload older non-XML Office files, you will need to install LibreOffice 4.2 or better on your server, and set the *libreoffice_app* in external_applications.conf to the path to the LibreOffice executable (typically *soffice*). Once it's running it will do a very good job rendering Office documents. Installation of LibreOffice under Mac OS X is generally hassle-free.

To install LibreOffice on Linux, try to grab the latest packages for your distribution, taking care to install the LibreOffice "headless" package, if it exists, as well as the LibreOffice core. On Ubuntu it is critical to install the "libreoffice-writer" package as well, otherwise conversions will fail silently, and your day will slip away as you continuously bang your head against a nearby wall.

On many Linux distributions, LibreOffice requires write access to the home directory of the user under which it is run. For a web application like CollectiveAccess, this means making sure that the home directory of the web server user is writeable by the web server user. Omitting this detail can result in frustrating silent failures.

On Mac OS X, simply follow the LibreOffice on Mac installation instructions, and then set the *libreoffice_app* in *external_applications.conf* to 

.. code-block::

   /Applications/LibreOffice.app/Contents/MacOS/soffice. 

