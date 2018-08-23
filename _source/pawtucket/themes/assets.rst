.. _assets:

Assets
======

The assets folder contains any external files, including graphics, stylesheets, fonts and javascript libraries, that you may need to customize your Pawtucket installation.  By default, the assets folder contains subfolders for css and graphic files, but you can create as many folders as you wish for other types of assets.

Loading New Assets
^^^^^^^^^^^^^^^^^^

Pawtucket will automatically load your js and css assets throughout the installation, but first they must be configured in the assets.conf file (note that new graphics in your graphics folder are excluded from this requirement).  

By default, your list of assets might look like this:  

.. code-block:: none

	themePackages = {
		# -----------------------
		pawtucket = {
			css = css/main.css:100, 
			fonts = css/fonts.css,
			fontAwesome = css/Font-Awesome/css/font-awesome.css,
			themecss = css/theme.css:200
		}
		# -----------------------
	}
	
To add a new js file, you can create 	

