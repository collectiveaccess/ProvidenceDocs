.. _import_mappings_mappingOptions:

Mapping Options
===============

* `Full List of Mapping Options`_
* `Option: applyRegularExpressions`_ 
* `Option: prefix`_ 
* `Option: suffix`_ 
* `Option: skipIfEmpty`_
* `Transform Values Using Worksheet`_ 

Options allow you to set additional formatting and conditionals on data during import. Some Options are designed to actually set parameters on the mapping behavior, such as the skip options. **skipGroupIfEmpty**, for example, allows you to prevent the import of certain fields, depending on the presence of data in another related field. Other Options simply format data, such as **formatWithTemplate**, **suffix**, and **convertNewlinesToHTML**. 

Full List of Mapping Options
----------------------------

A full list of mapping options is listed below.

.. csv-table::
   :header-rows: 1
   :file: mapping_options.csv


Option: applyRegularExpressions
'''''''''''''''''''''''''''''''

This option allows the user to effectively rewrite messy and problematic source data using Perl compatible regular expressions as supported in the PHP programming language. Let's say you are mapping duration data to a TimeCode element, and the source data syntax is invalid. See the :doc:`regex` page for useful regular expressions.
     
     Invalid timecode format:
     ``7.30.``

     Should be transformed to valid timecode format:
     ``7:30``

The invalid data can be transformed using the applyRegularExpressions option with the proper regular expressions.

.. code-block:: none

    {
       "applyRegularExpressions": [
           {
               "match": "([0-9]+)\\.([0-9]+)",
                "replaceWith": "\\1:\\2"
           },
            {
               "match": "[^0-9:]+",
               "replaceWith": ""
           }
        ]
    }
 
match: A regular expression applied to source data values.
replaceWith: If a match is found, it will be replaced with whatever is contained in "replaceWith".

In this example, the first regular expression matches <number>.<number> and replaces it with <number>:<number>. In other words, "7.30." becomes "7:30.". The [0-9]+ string matches sequences of 1 or more numbers. Since they’re in parenthesis they can be “back referenced” into the replaceWith part using the \\1 and \\2 placeholders. The second regular expression matches any character that is not a number or a colon (the first one having reformatted any period between numbers as a colon) and replaces it with nothing – removing it in other words. This regular expression takes care of the erroneous period at the end of the invalid data."7:30." is transformed into "7:30" - a valid TimeCode input.

     .. note:: The only deviation from the standard regular expressions language are the backslashes. Wherever you would use a single backslash in a regular expression, you need to use two in our mapping because JSON treats backslashes specially and demands that a literal ``\`` be encoded as ``\\``
    

Option: prefix
'''''''''''''''''''''''''''''''

With the **prefix** option, text can be added to prepend to values prior to import. This option can be particularly useful when importing currency values; using this option can prepend a currency symbol that will display upon import. 

.. code-block::

   {"prefix": "$"}

Option: suffix
'''''''''''''''''''''''''''''''

Using the **suffix** option allows text to be added to append to values prior to import.



.. code-block::

   {"suffix": "cm"}''

Option: skipIfEmpty
'''''''''''''''''''

When set to 1, **skipIfEmpty** will skip the mapping if the data value being mapped is empty. This option is useful for when data has empty values. 

.. code-block::

   {"skipIfEmpty": 1}


.. note:: Remember that 1 = yes, and 0 = no. Setting skipIfEmpty to 1 (yes) will ensure that the mapping is skipped if the data value is empty. 

**skipIfEmpty** can be used in conjunction with other Options as well. 

.. code-block::

   {"skipIfEmpty":1, "prefix": "$"}
   

.. _transformValuesUsingWorksheet:

Transform Values Using Worksheet 
''''''''''''''''''''''''''''''''
       
Using `Original Values and Replacement Values <file:///Users/charlotteposever/Documents/ca_manual/providence/user/import/orig_replace_example.html#import-orig-replace-example>`_ is sufficient for transforming a small range of values. But for large transformation dictionaries, use the option `transformValuesUsingWorksheet <file:///Users/charlotteposever/Documents/ca_manual/providence/user/import/mappings/mappingOptions.html#transformvaluesusingworksheet>`_ instead. You can use this option to reference a list of values in a separate worksheet within the mapping document. The formatting of the sheet should place original values in the first column, and replacement values in the second column.

When this option is set, any values in the "original values" and "replacement values" columns of the mapping worksheet are ignored, even if the "transformValuesUsingWorksheet" worksheet is empty or does not exist. You refer to the sheet by name:

.. code-block:: none

   {"transformValuesUsingWorksheet":"Worksheet Title"}
