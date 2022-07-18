.. _import_mappings_regex:

Regular Expressions
===================

.. contents::
   :local:




Remove All Spaces
`````````````````
Changes "1982 .  30001" into "1982.30001"

.. code-block:: none

  " {
   ""applyRegularExpressions"":
   [{
        ""match"": ""(\\s)+"",
        ""replaceWith"": """"
    }]
   }"
    
