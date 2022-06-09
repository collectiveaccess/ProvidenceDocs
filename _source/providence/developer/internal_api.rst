.. developer_internal_api:

Internal APIs
=====================

Writing Dashboard Widgets
-------------------------

Widgets are mini-applications that run within the dashboard in Providence. Users can select and freely arrange widgets on their dashboard to create a custom system management interface. 

The functionality that is encapsulated in a widget is only limited by space – they must fit within a single dashboard column (approximately 350 pixels wide). While widgets will typically provide simple, focused functionality, they have full access to the CollectiveAccess database and programming APIs, as well as their own configuration files and views. Widgets can interact with other CollectiveAccess plugins and external systems. See the Dashboard for a list of widgets included in the standard installation of CA.

Layout
------

Widgets are similar in structure to Application plugins, as each widget has a directory in **app/widgets**. The name of this directory must be the name of the widget (for example, Clock). Within this directory, a PHP class must exist with the widget's name and the **suffix Widget.php**. For a widget, Clock, the class is named **ClockWidget.php**.

Any widget must consist of a widget class and at least one view (named, by convention, main_html.php). It can also have, if required, additional views, graphics and configuration files. By convention, these are located in directories within the widget directory with the following layout: 

.. code-block:: php

   app/widgets/Clock app/widgets/Clock/ClockWidget.php [widget class]

   app/widgets/Clock/conf [directory containing widget's configuration file(s)]

   app/widgets/Clock/views [directory containing views for the widget; you must define at least one view]

   app/widgets/Clock/graphics [directory containing graphic elements; only needed if the widget needs its own graphics]

The Widget Class
----------------

The widget class (**ClockWidget.php**) must define two methods, two properties and a single data structure. The required methods are:

1. checkStatus(): returns information about the widget and whether it is available for use or not. The return value for checkStatus() is an array with four keys:
        * **Description**: a description of the widget
        * **Errors**: an array of text error messages relating to the initialization of the widget. This should be an empty array if there are no errors. If the widget is not available the reason why should be expressed in the errors array.
        * **Warnings**: an array of text warning messages relating to the initialization of the widget. Should be a list of warnings about anything that will limit the functionality of the widget. Should be an empty array if there are no warnings.
        * **Available**: set to true if widget is loaded and available for use, false if it cannot load for some reason.

2. If initialization of the widget fails, or the widget is not be available in the current context (eg. some requirement for running is not met) then return false for the available value.

3. renderWidget: is called when the widget needs to be displayed. This is where most of your widget code will live. The method is passed several parameters:
       * **$ps_widget_id**: 32 character MD5 hash widget unique identifying the widget instance
       * **$pa_settings**: an array of widget settings in a key-value format corresponding to the settings structure defined in the BaseWidget::$s_widget_settings entry for the widget (see below for further discussion)

The widget must also set the *$title* and *$description* properties, inherited from the base widget class. The *$title* property should be set to a single line description of the widget. The *$description* property should be set to a short narrative description of the plugin. Both are intended for display to end-users, and should be written in plain and accessible language.

If the widget defines per-user settings, then your widget class must also define an entry in the **BaseWidget::$s_widget_settings** array. The entry should have an array key equal to the **widget name + 'Widget' (eg. 'ClockWidget')**, and an array value that defines each setting. 

Per-user settings are distinct from any configuration file settings the widget may have. The latter are intended for definition of system-wide widget behavior by system administrators while the former are meant for on-the-fly configuration by widget users. Since a user may place multiple instances of a single widget on their dashboard at the same time, per-user settings also provide a means to differentiate the copies.

If the widget needs to load its own configuration files or do other initialization, include a constructor in the class. The constructor is passed an absolute file path to the widget's directory, which is needed to load widget-specific configuration files (or anything else in the widget directory for that matter).

.. note:: CollectiveAccess will only invoke the getDescription() and renderWidget() methods.

Rendering Widget Content
------------------------

The dashboard will call the renderWidget() method of each widget that needs display. The renderWidget() method should perform all of the work needed to generate content for display, and then render that content using a view in the widget views directory. 

The widget must have at least one view, and may have more if needed. The rendered view will be automatically passed, in addition to whatever you pass into the view in your own code, with the following values:

.. csv-table:: 
   :header-rows: 1
   :file: api_writing_dash_widtable1.csv

These variables can be accessed from within the view using **$this->getVar('<variable name>')**; from within the controller you can access the view via the **$opo_view** property. For example, to pass a custom into the view from within the controller, use the code:

.. code-block:: php

   $this->opo_view->render('main_html.php');

.. note:: The specification for the view to be rendered is simply the name of the view, because the view in question resides in the root of the widget's views directory. If it was in a subdirectory, then a root-relative path would be required.

The *BaseWidget::$s_widget_settings* Array
------------------------------------------

The widget can define settings to be set by end-users. These settings may be set at any time using a web interface built into the dashboard itself and are attached to a specific instance of the widget. That is, if there is more than one copy of the same widget on a users' dashboard, the settings are attached to the specific widget that was selected, not all copies of the widget.

The settings form for the widget is created by the dashboard, so there is no need to define a view for the settings. Simply specify what settings are required by the widget, and what kind of values those settings should take in the **BaseWidget::$s_widget_settings** static array.


To specify widget settings, define an entry in **BaseWidget::$s_widget_settings**, whose key is:
   * The name of the widget + 'Widget' (eg. 'ClockWidget') 
   * The value is an array listing each setting 

The settings array for the clock example looks like this:

.. code-block:: php

   BaseWidget::$s_widget_settings['ClockWidget'] = array(		
		'display_mode' => array(
			'formatType' => FT_TEXT,
			'displayType' => DT_SELECT,
			'width' => 40, 'height' => 1,
			'takesLocale' => false,
			'default' => 'standard',
			'options' => array(
				_t('Analog') => 'retro',
				_t('Digital') => 'standard'
			),
			'label' => _t('Display mode'),
			'description' => _t('Determines how to display information when it exceeds the maximum length.')
		),
		'display_format' => array(
			'formatType' => FT_TEXT,
			'displayType' => DT_SELECT,
			'width' => 40, 'height' => 1,
			'takesLocale' => false,
			'default' => 'h:i a',
			'options' => array(
				_t('Yes') => 'h:i:s a',
				_t('No') => 'h:i a'
			),
			'label' => _t('Show seconds?'),
			'description' => _t('Determines how to display information when it exceeds the maximum length.')
		)
	);

Each setting in the settings list has an alphanumeric code that uniquely identifies the setting within the context of the widget. The formatType and displayType values for the setting determine the type of data stored and the form the editing element will take for it in the settings form. The constants used for these two values are the same as those used in model definitions, as defined in **app/lib/core/BaseModel.php**. 

The dashboard settings form generator only supports a subset of the full list of format and displayType values, including: FT_TEXT for formatType (only text values are currently allowed) and DT_FIELD, DT_SELECT and DT_CHECKBOXES for displayType.

The *takesLocale* value should be set to true if the setting needs to be customized for each supported cataloguing language, otherwise false. Some values, such as options are only required when using specific form editing elements, such as DT_SELECT (and HTML <select> drop-down menu). The 'default' value should be chosen with care since it will be used when the user has not yet set a value. This means that the defaults you specify will help determine what the widget looks like when it is first added to the dashboard.
