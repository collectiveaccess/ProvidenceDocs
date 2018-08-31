Configuration File Syntax
=========================

A configuration file can contain any number of key-value pairs. Keys are simple alphanumeric text expressions. Values may be one of three types:

- **Scalar**: a string or number. Strings are always unquoted and may contain any character.
- **List**: a list of strings or numbers separated by commas and enclosed in square brackets ([ and ]). A string must be enclosed in double quotes if it contains a comma. You may not place the double quote character in a list item. Lists are retrievable as indexed PHP arrays. Lists may not be nested.
- **Associative array**: a list of key-value pairs. Both keys and values must be enclosed in double quotes if they contain commas. Neither may contain double quotes. Associative arrays are enclosed with curly brackets ({ and }). Separate keys from values with "=" Separate key-value pairs from each other using commas. Values may be strings, numbers or nested associative arrays. Associative arrays may be nested to any depth.
- **Keys** are always separated from values by "=" You may place as many spaces as you like on either side of the "=" character. Both lists and associative array may span as many lines as necessary.

Any line starting with a pound ("#") sign is considered a comment and ignored. It is ok to put leading spaces or tabs before a comment.

Note that if you begin a scalar value with a '[' or '{' character it will be parsed as a list or associative array respectively, which is not what you want. Be sure to precede the '[' or '{' with an exclamation point ('!') to indicate to the parser that you really want a scalar value.

An example configuration file, illustrating all three value types is below:

.. code-block:: none

	# 'email' is a simple scalar value
	# all it does is set 'email' equal to the email address
	#
	email = support@collectiveaccess.org

	# 'locales' is a list value
	# The values in the list are available to CA as a simple '''ordered''' list.
	#
	locales = [en_US, de_DE, sp_AR]

	# 'search_indexes' is an associative array (aka. a 'hash' in Perl-speak or a 'map' in other languages)
	# Each key in the array has associated with it a value, which can be either a simple scalar (as in the case of the "sortable = yes" lines below) or a nested associative array. You can nest arrays to any depth.
	#
	search_indexes = {
	   objects = {
			 title = {
				  sortable = yes,
				  searchable = yes
			 },
			 description = {
				  sortable = no,
				  searchable = yes
			 }
	   }
	}

Substituting values
Scalar values, once set, can subsequently be used, or substituted, in other locations in the configuration file. This allows you to set frequently used values at the beginning of a configuration file for use later in the file. If you need to change the value, you need only change it in one place - the place where it is defined.

Substituted values are simple scalar keys enclosed in "pointy" brackets (< and >), as in this example:

.. code-block:: none

		protocol = http
		hostname = www.collectiveaccess.org
	
		url = <protocol>://<hostname>
    
Here, we set the URL protocol (HTTP) and the hostname of the URL (www.collectiveaccess.org), then substitute the two values into the url key to create a valid URL.

The global.conf file
--------------------
The global.conf file is a special configuration file that can be used to define values for substitution into other configuration files. It is provides a central location in which to define sets of values shared across multiple configuration files. All configuration files in the same directory share a common global.conf file.

When a configuration file is loaded, CA looks first for a file named global.conf in the same directory as the requested file. If it finds one, it loads global.conf before any other file. This means that any values defined in global.conf are available for substitution in all configuration files located in the same directory. It also means that any value, scalar or not, in global.conf is available to CA in all configuration files.

Translating values into the user's current language
---------------------------------------------------
Any scalar values can be tagged for translation into the user's preferred language by enclosing them in a translation marker, like so: _("... my text ..."). Text so tagged with be passed to the GNU `GetText <http://www.gnu.org/software/gettext/>`_ translation function _t(), which is defined in *app/helpers/utilityHelpers.php*.