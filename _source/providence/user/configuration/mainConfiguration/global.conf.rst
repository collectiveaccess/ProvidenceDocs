Global.conf
===========

The global.conf file is a special configuration file that can be used to define values for substitution into other configuration files. It provides a central location to define sets of values shared across multiple configuration files. All configuration files in the same directory share a common global.conf file.

When a configuration file is loaded, CA looks first for a file named global.conf in the same directory as the requested file. If it finds one, it loads global.conf before any other file. This means that any values defined in global.conf are available for substitution in all configuration files located in the same directory. It also means that any value, scalar or not, in global.conf is available to CA in all configuration files.

  