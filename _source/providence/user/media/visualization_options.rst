Visualization Options
=====================

​​Collections with time or place-based data may benefit from the ability to see records represented on an interactive map or timeline. Visualization options allow a user to plot, search and browse results in a variety of ways based on contextual metadata (i.e. dates, or coordinates). Settings are handled in a configuration file called **visualization.conf**. Currently there are two visualization plugins supported: Maps and Timelines.

Maps
----

Multiple map visualizations can be created if the system has multiple geolocation fields. The name setting allows you to uniquely reference each one in the Visualization drop-down menu.

.. code-block:: PHP

   basic_map = {
		name = _("Map"),

Set data to the metadata element code where your location information is stored.

.. code-block:: PHP
   
    plugin = Map,
		sources = {
			georef = {
				data = ca_objects.georeference,

Set the formatting for the metadata that will display on each mapped coordinate. Enter as **table_name.elementCode**.

.. code-block:: PHP

   display = {
					title_template = <l>^ca_objects.preferred_labels.name</l>  (^ca_objects.idno),
					description_template = <div style='float:right; margin-left: 8px;'>^ca_object_representations.media.preview</div>^ca_objects.description

Set screen size options.

.. code-block:: PHP

   	}
			}
		},

		options = {
			width = 100%,
			height = 100%

Timelines
---------

Just like with Maps, multiple timeline visualizations can be created if your system has multiple date fields. The name set here will appear in the visualization drop-down menu.

.. code-block:: PHP

   basic_timeline = {

		name = _("Timeline")

Set data to the metadata element code where your dates are stored. Must be a DateRange datatype field.

.. code-block:: PHP

   plugin = Timeline,
		sources = {
			lifespan = {
				data = ca_entities.lifespan,

Set the formatting for the metadata that will display on each entry of the timeline. Enter as **table_name.elementCode**. For containers, enter as **table_name.containerElementCode.subElementCode**.

.. code-block:: PHP

   display = {
					title_template = ca_entities.preferred_labels.name,
					description_template = ca_entities.biography
Set screen size options.
			}
			}
		},
		options = {
			width = 100%,
			height = 100%
		}
	}
}

The appearance of the timeline can be customized. For example, to color code a certain time period to see which objects fall into a certain era: 

.. code-block:: php

   options = {
			width = 100%,
			height = 100%,
			highlightSpans = {
				confederation = {
					label = Confederation,
					range = 9/13/1759 to 7/1/1867,
					startLabel = 1759,
					endLabel = Confederation,
					color = #FFC080
 
