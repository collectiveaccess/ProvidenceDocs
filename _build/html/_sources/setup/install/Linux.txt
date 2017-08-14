Installing on Linux
===================

Ubuntu 9.10
-----------

The PHP package for Ubuntu 9.10 defaults to a memory limit of 16megs per process, which is usually too low a ceiling for the installer to operate under. What compounds this minor problem is that, for some reason, no error message is issued when the memory limit is hit. The installer is silently and randomly aborted despite the PHP display_errors directive being set to "On." This has caused no end of confusion.

As of SVN r4129 the installer attempts to set the memory limit to 128megs before starting the actual install. This will only work if you are not running PHP in safe mode or with Suhosin. If the installer cannot up the memory limit on its own then you will get a warning prior to installation advising you to up the memory limit by modifying the php.ini file by hand.

Red Hat Enterprise Linux/CentOS 5
---------------------------------

The Perl Compatible Regular Expression (PCRE) library that ships with some (all?) versions Red Hat/CentOS 5 does not include support for the UTF-8 character set. However the Zend Framework Lucene library that CA uses to parse search expressions requires that PCRE support UTF-8. The result is an error every time you attempt to search.

One solution: grab the latest PCRE source code from `pcre.org <http://www.pcre.org>`_ and build your own version that includes UTF-8 support.


PCLinuxOS 10
------------

.. note::
   Note that the PHP packaged with PCLinuxOS10 has "display_errors" set to Off, which means any errors thrown by CA are not visible. This can be very confusing when trying to debug an installation, so be sure to change it to "On" first thing if you are experiencing problems.

The standard PHP packages shipped with this Linux distribution have two issues when running CA:

The PHP Iconv module, which is required by CA, is not loaded by default. You can fix this by installing the PHP-iconv package using apt-get.
The standard PHP package includes the Suhosin security patches for PHP. Suhosin is a great product, but it introduces some default constraints than can prevent CA from saving information entered into forms. To fix these issues edit the Suhosin configuration file in /etc/php5.d, setting the following directives to these values:
   - suhosin.post.max_name_length: 256
   - suhosin.request.max_varname_length: 256
   - suhosin.post.max_totalname_length: 5012
   - suhosin.request.max_totalname_length: 5012

.. note::
   Note that you can also get CA to work under Sushosin by setting the "suhosin.simulation" directive to "On" This will negate most of the security benefits of having Suhosin installed, however. Note that on some servers (shared hosting) you may not have access to /etc/php5.d. In that case you can make these changes in php.ini for the same result. (You will have to add these values.)