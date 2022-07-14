Inspector Display Flags
-----------------------

As of CollectiveAccess version 1.5, optional flags, or alerts, are supported based on record metadata in the Inspector window of a record’s editor screen. 

For example, to alert users when a yes/no checkbox is checked “yes,” a directive can be set in **/app/conf/app.conf**. Setting this will enable a visual indication in the Inspector window. 

The configuration follows the following syntax:

.. code-block:: php

   <table_name>_inspector_display_flags 

The directive should be set to an associative array where each key is an expression and each value is the content to print if the expression is true. For example:

.. code-block:: php

   "(^ca_objects.legalRestriction = \"yes\")" = <strong>Legal Restriction</strong><br/>

The expression must be put in quotes. Any sort of expression will work including regular expressions. For example: 

.. code-block:: php
   
   ca_objects_inspector_display_flags = {
 	"(^ca_objects.preferred_labels.name =~ /place/)" = <strong>Has the word place in the title!</strong>
   }

The default delimiter between flags is set to a semi-colon ";". If you would like to configure how multiple flags appear in the inspector panel, use this setting in app.conf:

.. code-block:: php
   
   ca_objects_inspector_display_flags_delimiter = <br/>

In this case, the delimiter is set to a line break so that the flags appear stacked on top of each other. The " can be replaced with any arbitrary string.

