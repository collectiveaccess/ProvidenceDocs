.. _defining:

Defining Your Own Theme
=======================

In order to display custom metadata, graphics and styling to your Pawtucket installation, you'll need to define a custom theme.  A custom theme selectively overrides the areas of the :ref:`defaulttheme` that you'd like to tailor to your project.  Nearly all custom themes will use at least some views from default theme to function.  In fact, it is to your advantage to override *only* the views that are necessary for customization, as this will allow you to easily update your theme with future improvements to the Pawtucket base code as they become available.

Creating a theme
^^^^^^^^^^^^^^^^

At it's most basic, a custom theme needs only to have folders for :ref:`assets` (such as graphic, javascript and css files), :ref:`conf` (these contain the options you'll need to set to customize your search and other site functions), and :ref:`views` (these control the layout and output of your data).  

A blank theme named **copyme** comes pre-installed with your Pawtucket system - this consists of the basic theme folder structure and can be used as a template to get you started.  To create your custom theme, simply copy the **copyme** folder and its contents and name it what you like.  For the purposes of this tutorial, we'll assume a theme name of **mytheme**.  To complete the creation of your new theme, copy the contents of themes/default/conf into the **conf** folder in your theme.  

Next, you'll need to tell Pawtucket to use your theme instead of the default.  This setting can be found on line 77 of the setup.php file in Pawtucket's root directory.  Change the theme setting to your theme's folder name, like this:

.. code-block:: none
  
	$_CA_THEMES_BY_DEVICE = array(
		'_default_' 	=> 'mytheme'	// use the 'default' theme for everything else
	);

Now that you've created your new theme, your Pawtucket site will look... exactly the same!  This is because you have not begun overriding files or settings yet.  As a result, your custom theme is falling back entirely on content being generated from the default theme.

Customizing your theme
^^^^^^^^^^^^^^^^^^^^^^

To begin overriding default theme views, you need only to copy them from the default theme into the appropriate folder in your custom theme.  As an example, let's replace the default CollectiveAccess logo in your theme.  The logo graphic is declared on line 100 of themes/default/views/pageFormat/pageHeader.php, so you'll want to copy this view file into themes/mytheme/views/pageFormat (do not change the filename).  Once the file is copied, you can edit the code to your liking.  Since we are reference a new graphic, you'll also want to upload your new logo to the assets folder in themes/mytheme/assets/pawtucket/graphics/.

.. tip::
	Only copy the views from the default theme that are needed for your customized design.  This will make updates more efficient by ensuring that your Pawtucket system draws on the default theme wherever possible, and reduces the need to manually update code in your views.

If you navigate to themes/mytheme/assets/pawtucket/css, you'll notice that it contains one blank css stylesheet, named **theme.css**.  This is where you can add any css needed to customize your site and override any styles employed by the default theme.  Simply add the styles you'd like to override to this file and the changes will be reflected in your Pawtucket site.  You can also add any additional css files you'd like to use to this css folder - just follow the instructions for loading additional :ref:`assets`.

A great deal of common configuration options are available simply by editing :ref:`conf`.  Please check the documentation for these files individually for a guide to the options available.

Advanced Customization
^^^^^^^^^^^^^^^^^^^^^^

Most themes will limit their customization to the three areas listed above.  However, the latest version of Pawtucket allows developers to create theme-specific Controllers in addition to the above.  To create a theme specific controller, simply create a folder named **controllers** in your theme directory and copy the Controller you'd like to edit.  This is helpful if you want to pass new or custom variables to existing views, or create new site areas that are not included in the default Pawtucket.