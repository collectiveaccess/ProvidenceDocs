PDF Output
==========

CollectiveAccess can output data as formatted PDFs in several contexts:

1. As a **Report** presenting formatted data from the results of a search or browse.
2. As a **Summary** of data from an individual item
3. As a set of **Printable Labels** including formatted data from items retrieved from the results of a search or browse.
4. As **formatted letters and documents** (eg. deeds of gift, thank you letters, receipts) for an object or lot. 
5. As a **formatted summary or invoice** from a metadata element, or a specific repeat of a metadata element.

PDF output in CollectiveAccess is generated from an HTML/CSS page layout using templates stored in the app/printTemplates. The HTML output by these templates is converted to PDF using one of several rendering engines. Any PDF output format can be modified or customized by editing or adding templates in app/printTemplates.

The HTML templates are standard views, the same as any other in the CollectiveAccess application. You can use PHP code with the view and include subviews using $this->render(). For label and summary views you can also use the {{{variable}}} tag format to include variables and display templates directly in your HTML – no PHP required. The variables passed to the template view vary by context and are described below.

How PDF Templates are Evaluated
-------------------------------

When a PDF output is requested, CollectiveAccess loads the specified template views and provides them with the data required for display. The view is then evaluated: any executable in the view is run and substitution of curly-brace tags is performed. The transformed HTML text of the view is then passed to dompdf for conversion to a PDF.

The evaluation process varies somewhat by context:

**Report templates** are passed a result set and evaluated as a single page. The template is provided with a search result instance (subclass of SearchResult) and expected to render a full HTML page for the entire result set. This is typically done with embedded PHP code. 

**Summary templates** are similarly evaluated as a single page, but are provided with the model instance (subclass of BaseModel) for the item being summarized rather than a result set. Letter templates work similarly to summaries. 

**Label templates** are evaluated once per label and placed on the page by the PDF generator in the appropriate location for the selected label format. Label templates are passed a model instance for the item for which the label is being produced.

Creating PDF Formats
--------------------

The *app/printTemplates* directory contains subdirectories for each context – results (aka. report), summary, labels, letter and element. Directly within those directories are the standard formats and supporting files for each context. 

Custom, printable templates can be added by creating new files in the local directory contained within. 

.. note:: Although templates placed directly in the context directory will work normally, they may be overwritten during application updates. Always place custom templates in local.

Custom formats must generate a full, freestanding and well-formed HTML document. It also must include a header with basic information about the template and how it is to be used. The header is a collection of named values, with all names beginning with the **@** character. The following values are required:

.. csv-table::
   :header-rows: 1
   :file: pdf_output_table1.csv

For labels the following additional header entries defining the geometry of the label form are also required:

.. csv-table::
   :header-rows: 1
   :file: pdf_output_table2.csv

All measurements require a numeric values followed by a unit specifier. Allowable units are:

.. csv-table::
   :header-rows: 1
   :file: pdf_output_table3.csv


The header should be in an HTML or PHP comment. Here is an example header in a PHP comment:

.. code-block::

    /*
    * Template configuration:
    *
    * @name Avery 8164
    * @type label
    * @pageSize letter
    * @pageOrientation portrait
    * @tables ca_objects
    * @marginLeft 0.125in
    * @marginRight 0.125in
    * @marginTop 0.25in
    * @marginBottom 0.25in
    * @horizontalGutter 0in
    * @verticalGutter 0.25in
    * @labelWidth 4in
    * @labelHeight 3.375in
    */

From CollectiveAccess Version 1.7, you can temporarily disable a template using the @disable header setting. Simply set it to a non-zero value to remove the template from use.

Your template view will be provided with a set of variables to work with that is dependent upon the context. Below is a list of variables by template context:

For all results (browse or search)
----------------------------------

.. csv-table::
   :header-rows: 1
   :file: pdf_output_table4.csv

For search results
------------------

.. csv-table::
   :header-rows: 1
   :file: pdf_output_table5.csv

For browse results
------------------

.. csv-table::
   :header-rows: 1
   :file: pdf_output_table6.csv

For summaries
-------------

.. csv-table::
   :header-rows: 1
   :file: pdf_output_table7.csv

For labels
----------

.. csv-table::
   :header-rows: 1
   :file: pdf_output_table8.csv

Using View Variables
--------------------

The variables provided may be accessed via PHP code within the view by calling the view's setVar() method with the variable name. This code fragment will print out the current search phrase for search result views:

.. code-block::
   <?php print $this->getVar('search'); ?>


For label and summary views, an alternative PHP-free {{{variable}}} syntax can also be used. 
Surrounding the name of the variable with sequences of three curly-braces will cause its value to be substituted into the view. 

.. note:: These curly-brace tags should be placed in the HTML of your view. They are not valid PHP and will cause errors if placed within PHP code. The curly-brace syntax is not available in results views.

In addition to variables, display templates may also be evaluated and output using the curly-brace syntax. For example:

.. code-block:: 
   {{{Identifier is ^ca_objects.idno and titles is ^ca_objects.preferred_labels.name}}}

would cause the text to be output with the ^-prefixed data specifications substituted with values.

Setting the Download File Name
------------------------------

A custom file name for downloaded PDFs can be generated from your view template by setting the @filename header entry.

From CollectiveAccess Version 1.7.6, your template view can also specify the file name for the downloaded PDF by setting the "filename" view variable. Because this value is set using PHP code it can be set dynamically based upon report parameters, user settings or anything else you can access. View variables are set using the view's setVar() method with the variable name ("filename") and the desired filename:

.. code-block:: 
   <?php print $this->setVar('filename', 'my_custom_report_file.pdf'); ?>

If you don't set a file name a default name will be used.

Displaying Barcodes
-------------------

Bar codes may be output in any view using the PHP caGenerateBarcode() helper function. Simply pass it the value to be encoded and an array of options that include the type of barcode and size of the code and a path to a PNG file displaying the bar code is returned. You can then construct and <img> tag within the view or do other processing. It is your responsibility to remove the generated PNG file, any of which will be in the system tmp directory, when you are done.

For example:

.. code-block:: 
   <?php $vs_path = caGenerateBarcode('$ps_identifier, array('checkValues' => $this->opa_check_values, 'type' => 'code128', 'height' => 12)); print "<img src='".$vs_path."'/>"; ?>

For views that support curly-brace syntax, you may also pass a special barcode template in the format barcode:<type>:{size}:template. For example:

.. code-block::

   {{{barcode:code128:12:^ca_objects.idno}}}

Supported Bar Code Formats
--------------------------

.. csv-table::
   :header-rows: 1
   :file: pdf_output_table9.csv

Rendering Engines
-----------------

Conversion of HTML generated by templates to PDF is performed by a rendering engine installed on the server. There are several choices to select from. 

CollectiveAccess comes with plugins that allow the software to use three of the most common rendering engines. Support for other engines can be added by coding additional plugins.

Currently supported rendering engines include:

.. csv-table::
   :header-rows: 1
   :file: pdf_output_table10.csv

If using a non-domPDF renderer, be sure that the path to the command-line render application is set properly in external_applications.conf. Selection of the renderer is automatic, with wkhtmltopdf or PhantomJS if present used in preference to domPDF.

Testing Labels
--------------

When testing your label layouts, setting the add_print_label_borders directive in app.conf to a non-zero value will cause outlines to display on the borders of all printed labels.

