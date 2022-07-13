Other customizations
====================

You can make some easy customizations of your installation beyond conf changes.

Cascade Style Sheets
--------------------

You can create new file *themes/default/css/local.css* and use it to restyle page elements or change used fonts etc.


Theme
-----

In *themes* folder you can create your custom theme, where you can redefine page templates and more. Users can easily switch between themes.


Print & export templates
------------------------

In *app/printTemplates/* there are folders *bundles*, *labels*, *results*, *sets* and *summary*. 
These folders contain print  and export templates. You can override them by copying them to *local* subfolder and editing. There, you can also define your own templates.

You can use it for redefining fonts used in exported templates and more.


Plugins
-------

You can write custom plugins implementing custom integrations or data manipulation. You can find more info in   :doc:`Plugins <../developer/plugins>` chapter