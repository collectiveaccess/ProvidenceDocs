Display Template Syntax
=======================

.. contents::
   :local:
   
Display templates are used to format data from bundles (elements of metadata stored in CollectiveAccess) for display on screen, output into reports and presentation in search results. When no display template is defined CollectiveAccess defaults to displaying bundle data in the simplest possible way, typically as a semicolon-delimited list of values. For bundles comprised of a single value (Eg. a simple text metadata element) this is often enough. For complex bundles consisting of several discrete values – a mailing address for example – a template is usually required to adequately format the value. Other cases where bundle display templates are called for:

    - To define styling, such as headings, bold and italics around bundle elements.
    - To format and conditionally include delimiters and suffixes between values in a complex bundle. For example, in a bundle with width, length and height dimensions, "x" delimiters can be placed between each dimension value. A display can be used to output values in a width/length/height order (or any other order). Thus a bundle with length=24", height=8" and width=3" can be output as 3" x 24" x 8" ... or 3"W x 24"L x 8"H ... or 3"W x 8"H if length happens to be undefined (because displays can intelligently omit the delimiter and suffix).
    - To display data attached to related items. For example to display both the name and life dates for related entities a bundle display template can be used to extract and format the data. Any data attached to the related entity can be displayed.
    - To display related data traversing any number of intervening relationships. As a simple example, imagine that you have an object related to a collection, and the collection is related to a donor. It's not necessary to catalog the donor directly on the object in order to display the donor's address there, because it's possible to pull the address through the intervening collection relationship. Another example prevalent in film and performance archives, is that objects can be related to "works" (occurrences) which in turn have entity relationships ("director", "actor", "choreographer"). A display template can display object information alongside entity data related to a work that is related to the object.
    - To apply one of several display formats using expressions conditional on one or more data values.

Display templates are also used extensively by Pawtucket 2.0 for formatting in themes. They are the preferred formatting method in Pawtucket 2.0, although mixed HTML/PHP coding is still supported.

Defining templates
^^^^^^^^^^^^^^^^^^
Default display templates can be defined for metadata elements as part of their configuration. Default formatting can be overridden by additional context-specific templates within a display or user interface.

The default template for a metadata element can be set in the configuration interface. Display and user interface related templates may be set in their respective configuration editors on a per-bundle basis. When a template is defined for a metadata element within a display or editor user interface it will take precedence over templates defined in the element's configuration.

Template syntax
^^^^^^^^^^^^^^^
At their most basic, templates are simply text with placeholders to be replaced by bundle values. Placeholders always start with a caret ("^") character followed by a bundle specifier, an unambiguous identifier for a metadata element. For example, if you have a metadata element in an object record with the element code description and wish to preface the value of the element with the label "Description:" the template would be:

``Description: ^ca_objects.description``

where ca_objects indicates an object record and description is the metadata element code.

If the value of the description metadata element happens to be empty, this template will cause the label "Description:" to be awkwardly displayed without a trailing value. To avoid unwanted blank spaces a display template can be made conditional on the presence of a value within a field. A template for description that only displays something if there's a description available would look like this:

``<ifdef code="ca_objects.description">Description: ^ca_objects.description</ifdef>``

Everything between the <ifdef> and </ifdef> is only output for the corresponding bundle (specified without the ^ in the <ifdef> tag because it's a code, not a placeholder in this context) when it actually has a value.

Conditional output can be used for more than just labels. For dimensions and other collections of quantities, conditional output can be used to deal with variations when not all values are available in all cases. For example, let's say you have a metadata container on an object record named "dimensions" with three sub-elements: width, height and depth, all of which are elements of type Length. Displaying the container ca_objects.dimensions without a template would result in three values separated with semicolons, which are the default delimiter:

    ``12"; 6"; 9"``

(we assume here that we're displaying in English units)

To make it clearer we can format the container using this template:

``^ca_objects.dimensions.width W x ^ca_objects.dimensions.height H x ^ca_objects.dimensions.depth D``

This will display:

    ``12" W x 6" H x 9" D``

As you can see, a special syntax is used to articulate container elements. It is no longer just ^ca_objects.dimensions in our example, but rather the code for the parent container along with the specific sub-element you've chosen to display.

If the depth value happens to be blank in some cases then the output would sometimes be like this:

    ``12" W x 6" H x D``

To rectify this we can use conditional output:

.. code-block:: none

	<ifdef code="ca_objects.dimensions.width">^ca_objects.dimensions.width W x</ifdef> <ifdef code="ca_objects.dimensions.height">
	^ca_objects.dimensions.height H x</ifdef> <ifdef code="ca_objects.dimensions.depth">^ca_objects.dimensions.depth D</ifdef>

Note that we can also use conditionals to close up the space between ^ca_objects.dimensions.width and the "W", ^ca_objects.dimensions.height and "H" and ^ca_objects.dimensions.depth and "D". Normally space is required between the placeholder and any non-placeholder text to make clear where the placeholder ends. With a conditional you can keep the placeholder separate from other text without resorting to spaces, as in this example:

.. code-block:: none

	^ca_objects.dimensions.width<ifdef code="ca_objects.dimensions.width">W x</ifdef> ^ca_objects.dimensions.height
	<ifdef code="ca_objects.dimensions.height">H x</ifdef> ^ca_objects.dimensions.depth<ifdef code="ca_objects.dimensions.depth">D</ifdef>

If you need to make part of your template conditional upon more than one value being set simply list the placeholder names in the "code" value separated by commas:

.. code-block:: none

	<ifdef code="ca_objects.dimensions.width,ca_objects.dimensions.height,ca_objects.dimensions.depth">Dimensions are: </ifdef>
	^ca_objects.dimensions.width<ifdef code="ca_objects.dimensions.width">W
	x</ifde> ^ca_objects.dimensions.height<ifdef code="ca_objects.dimensions.height">
	H x</ifdef> ^ca_objects.dimensions.depth<ifdef code="ca_objects.dimensions.depth">D</ifdef>

"Dimensions are:" will only be output if width, height and depth all have values. The text can be output if any of the values in the code list are set by separating the placeholder names with "|" (aka. "pipe") characters:

.. code-block:: none

	<ifdef code="ca_objects.dimensions.width|ca_objects.dimensions.height|ca_objects.dimensions.depth">Dimensions are: </ifdef>
	^ca_objects.dimensions.width<ifdef code="ca_objects.dimensions.width">W x</ifdef>
	^ca_objects.dimensions.height<ifdef code="ca_objects.dimensions.height">H x</ifdef>
	^ca_objects.dimensions.depth<ifdef code="ca_objects.dimensions.depth">D</ifdef>

There are some cases in which you may need to make part of a template conditional upon a value or values not being defined. The <ifnotdef> tag will do this in an analogous manner to <ifdef>. For example, if you want to output a "No dimensions" message when no values are defined:

.. code-block:: none

	<ifnotdef code="ca_objects.dimensions.width,ca_objects.dimensions.height,ca_objects.dimensions.depth">No dimensions are set</ifnotdef>
	^ca_objects.dimensions.width<ifdef code="ca_objects.dimensions.width">W x</ifdef> ^ca_objects.dimensions.height
	<ifdef code="ca_objects.dimensions.height">H x</ifdef> ^ca_objects.dimensions.depth<ifdef code="ca_objects.dimensions.depth">D</ifdef>

Placeholder options
^^^^^^^^^^^^^^^^^^^
Placeholder values may be modified by options appended as a series of named parameters. Options are separated from the placeholder with a "%" character and listed in <name>=<value> pairs delimited by "&" or "%" characters.(("&" are used in older templates, but now may be used interchangeably with "%"). For example:

``^ca_objects.hierarchy.preferred_labels.name%maxLevelsFromBottom=4&delimiter=_➜_``

will output a list of hierarchical object titles consisting of the bottom-most four titles separated by arrows. If those options were not set they would revert to defaults, in this case the entire hierarchy delimited by semicolons.

Any number of options may be appended to a placeholder.

Note that spaces are not allowed in options as they are used to separate placeholders. You can use URL encoding (eg. %20 for a space) or a underscores in place of spaces.

The following options may be used to format the text value of any placeholder:

.. csv-table::
   :widths: 25, 75
   :header-rows: 1
   :file: ../_static/csv/placeholder_options.csv

For simple true/false options such as toUpper you may omit the "=" and value. These two templates are the same:

``^ca_objects.preferred_labels.name%trim=1``

and

``^ca_objects.preferred_labels.name%trim``

Pulling metadata through a relationship
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the previous examples, data displayed is always from a particular object record at hand – the "primary" record. Templates are always processed relative to to the primary record. If you are formatting object search results, for example, your template will be repeatedly evaluated for each object in the result set, with each object taking its turn as primary. It's obvious but still worth stating: placeholders referring directly to data in the primary (^ca_objects.idno for example) derive their values from the primary. If a bundle repeats for a record, you may get multiple values, but all values referring to the primary will always be taken from the primary. Any record can be primary. Primary-ness is simply the context is which a template is processed.

It is often necessary to display metadata from records related to the primary. For example, you might want to display entities related to an object (the primary) displaying each entity's lifespan and birthplace next to their name. Or a display the related collections, with name, access restrictions and availability information. Or perhaps a display of objects related to the current primary object.

For simple cases displaying related data is similar to primary data. For placeholders that refer to non-primary data CollectiveAccess will look for records of that kind directly related to the primary. For a ^ca_entities.preferred_labels.displayname placeholder in a display for object results, CollectiveAccess will pull the names of all entities directly related to the primary object. Using our sample data:

``^ca_entities.preferred_labels.displayname``

will result in a list of display names for related entities, separated by semicolons (the default delimiter):

``George Tilyou; Elmer Dundy``

To pull data from related records of the same kind as the primary (Ex. objects related to an object) add "related" to the bundle specifier:

``^ca_objects.related.preferred_labels.displayname``

With our sample data this will result in the title of the object related to the primary being returned. You can include "related" in specifiers for any kind of related record but it is only required when things would otherwise be ambiguous without it.

You may pull any data in the related entity records using similarly constructed placeholders. For example, this template:

``^ca_entities.preferred_labels.displayname (Life dates: ^ca_entities.life_span)``

will return

``George Tilyou; Elmer Dundy; (Life dates: 1865 - 1914; 1862 - 1907)``

Each placeholder is evaluated separately and a list of values returned in its place. To format several related data elements in a block, as well as to display indirectly related data (such as the related entity's birthplaces), set custom delimiters and other options a new template directive, the <unit> tag, is needed.

Formatting templates with <unit>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
<unit> tags allow you to break your templates into sub-templates that are evaluated independently and then reassembled for final output. Using the <unit> relativeTo attribute, the primary record of the template may be transformed into one or more related records, repeating values from the primary (e.g. values in a repeating container) or a set of hierarchical values, and the sub-template evaluated for each.

<unit>'s and relativeTo enable a host of useful (and often complex) formatting transformations:

- When a record has repeating containers. Say you have a repeating address container on an entity record to accommodate multiple address changes. If you format your display template without specifying that each instance of the container needs to be displayed as a unit the result will be a single address in return, no matter how many addresses are entered, and each placeholder will contain the values for all of the addresses - a nonsensical way to display an address list. Wrapping the address portion of the template in <unit> tags and specifying that it be evaluated relative to the repeating address element, rather than the primary record itself, will force the template contained within to be evaluated once per repeating address value, resulting in an independently formatted value for each address. Ex.

.. code-block:: none

	<unit relativeTo="ca_entities.address">
	^ca_entities.address.street_address<br/>^ca_entities.address.city, ^ca_entities.address.state ^ca_entities.address.zip_code<br/>
	</unit>

The relativeTo option in the <unit> tag forces the sub-template to be evaluated once per address value in the primary record.

- When you need to present more than one data element from related records side-by-side. In the previous section we saw how different placeholders referencing the same related records always return separate lists, one per placeholder. When displayed side-by-side the result is a series of lists rather than the discrete blocks of output for each related item that are more typically desired. <unit> tags make it possible to define sub-templates that are evaluated repeatedly, as many times as there are related records. Our example in the previous section reformatted with <unit> tags like this:

``<unit relativeTo="ca_entities">^ca_entities.preferred_labels.displayname (Life dates: ^ca_entities.life_span)</unit>``

results in this output:

``George Tilyou (Life dates: 1865 - 1914); Elmer Dundy (Life dates: 1862 - 1907)``

Here the relativeTo option in the <unit> tag shifts the primary record to be each related entity in turn, in the sub-template defined by the <unit> only.

- When you need to set display options for part of a template. <unit> tags provide options to modify output for sub-templates. You can set the delimiter for repeating values using the delimiter option, or restrict the related items displayed by relationship type or related item type using restrictToRelationshipTypes and restrictToTypes respectively (or their counterparts excludeRelationshipTypes and excludeTypes). (You can also set options on individual placeholders, but declaring options on <unit> tags is usually more convenient and always more readable). Ex.

.. code-block:: none

	<unit relativeTo="ca_entities" restrictToRelationshipTypes="actor, director, producer">
	^ca_entities.preferred_labels.displayname (Life dates: ^ca_entities.life_span)
	</unit>

- When you need to display metadata relating to hierarchical records. Without the <unit> tag, there's no way to individually list child records and accompanying metadata in a display. With the <unit> tag you can display parent and/or child records and hierarchical paths as discrete, complex units, by making the unit relativeTo the hierarchical record set. Ex.

``<unit relativeTo="ca_list_items.hierarchy"><p>^ca_list_items.preferred_labels.name_plural (ca_list_items.idno)</p></unit>``

Here the relativeTo option in the <unit> tag shifts the primary record to be each related list item in the hierarchy in turn, in the sub-template defined by the <unit> only.

- When you need to pull metadata through an indirect relationship. Without the <unit> tag only metadata from records directly related to the primary can be displayed in a template. In our sample data, this means only the entities related to the primary object can be displayed. The birthplace data related to each entity cannot. By using <unit> tags nested within one another and specifying the relativeTo option we can shift the primary record for a sub-template across any number of relationships. We might call this "Six Degrees of Kevin Bacon for CollectiveAccess" where A is related to B which is related to C. For example, if the primary is an object, and you need to display place data from entities related to objects (not places related directly to the object), the following template would do the job:

.. code-block:: none

	Object is ^ca_objects.preferred_labels.name;
	Entities are: <unit relativeTo="ca_entities">^ca_entities.preferred_labels.displayname
	(Birthplace: <unit relativeTo="ca_places">^ca_places.preferred_labels.name</unit></unit>

Each unit shifts the primary by one relational "jump." Nesting <units> allows shifts to accumulate because they are always evaluated relative to their context. Thus entities related to objects are grabbed, and then places related to those entities.

<unit> tags may take any of the following attributes:

.. csv-table::
   :widths: 25, 25, 25, 25
   :header-rows: 1
   :file: ../_static/csv/unit_attributes.csv

The <unit> tag presents many opportunities for complex display formatting which are explained in more detail, along with examples, here.

You can limit the number of values returned from a <unit> operating on a repeating value using the start and limit unit attributes described previously. You can display text indicating how many values were not shown using the <whenunitomits> tag following a <unit>. For example, to show the first 5 related entities and then a message with the total number:

.. code-block:: none

	<code>
	<unit relativeTo="ca_entities" delimiter=", " start="0" length="5">^ca_entities.preferred_labels.displayname</unit><whenunitomits> and ^omitcount more</whenunitomits>
	</code>

The ^omitcount placeholder can be used within the <unit> or <whenunitomits> tag. The <whenunitomits> tag always refers to the number of values omitted in the <unit> before it in the template and will be suppressed when no values from the previous <unit> are hidden.

Contextual tags: <more> and <between>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Templates using <ifdef> and <ifnotdef> can get long and unruly when they include many elements dependent on the state of multiple placeholders. To help make such templates more manageable two tags are available that control output based solely upon their position in a template, obviating the need for long lists of placeholder names.

The <more> tag will output content if any placeholders following it have a value. Thus this template:

``^ca_objects.description <more><br/>The source for this was: </more>^ca_objects.description_source``

will output this (assuming both description and description_source are set to "A metal pan" and "1978 auction catalogue" respectively):

.. code-block:: none

	A metal pan
	The source for this was: 1978 auction catalogue

If description_source was empty the output would be:

``A metal pan``

The <between> tag will output content if any placeholders before it in the template and the placeholder directly following it in the template have values. This makes delimiting lists of values more compact than options using <ifdef>:

``^ca_objects.dimensions.width <between>x</between> ^ca_objects.dimensions.height <between>x</between> ^depth``

The output of this would be the defined dimensions with a single "x" delimiter between each pair.

Conditional tags: <ifdef>, <ifnotdef>, <ifcount>, <if>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As mentioned earlier you can make display of portions of your template contingent upon specified conditions by surrounding part of the template with <ifdef> and <ifnotdef> tags. Both tags take a "code" attribute containing one or more bundle specifiers. If the value for the bundle is not empty <ifdef> will display the portion of the template it encloses. Conversely, if the value is empty <ifnotdef> will display the content it encloses.

For example:

``Title: ^ca_objects.preferred_labels.name <ifdef code="ca_objects.description">Description: ^ca_objects.description</ifdef>``

Note that the specifier in the code attribute is not a placeholder and therefore does not take a "^" prefix.

You can make <ifdef> and <ifnotdef> contingent upon more than one bundle by listing them in the code attribute separated by commas or pipes ("|"). When separated by commas, all of the bundles must be defined (<ifdef>) or not defined (<ifnotdef>) for the tag to display content. When separated by pipes, any of the bundles defined (<ifdef>) or not defined (<ifnotdef>) will cause the tag to display content.

The <ifcount> tag controls display of content based upon the number of values available from the bundle specifier in code. It is useful when you wish to only show content when the number of values a bundle has is within a range. For example, if you wish to show a list of related entities only when there are between 2 and 5 relationships:

``<ifcount code="ca_entities.related" min="2" max="5">Related entities: ^ca_entities.preferred_labels.displayname</ifcount>``

You can show content whenever the count is greater than a number by omitting the max attribute:

``<ifcount code="ca_entities.related" min="2">Related entities: ^ca_entities.preferred_labels.displayname</ifcount>``

If the min attribute is omitted it is assumed to be zero.

To only show content when the count is a specific number set both min and max to the same number:

``<ifcount code="ca_entities.related" min="1" max="1">Related entity: ^ca_entities.preferred_labels.displayname</ifcount>``

The <if> tag provides maximum control by using expressions to determine when content is displayed. For example, to output the display only if "current" is selected from the type drop-down in a repeating credit line container:

.. code-block:: none

	<unit relativeTo="ca_objects.credit_line"><if rule=\"^credit_type =~ /current/\">^ca_objects.credit_line.credit_text
	(^ca_objects.credit_line.credit_type)</if></unit>

The rule attribute must be set to a valid expression, which can use any valid placeholder available in the template, and must be enclosed in escaped (prepended "\") quotes to ensure that it is evaluated correctly.

Both <ifcount> and <ifdef> include blank values in their evaluation. From version 1.7.9 blank values may suppressed by setting the optional "omitBlanks" to a non-zero value. This is often useful when formatting data for display.  If "omitBlanks" is set, <ifcount> will return the number of non-blank values; <ifdef> will evaluate as true only if the bundle has at least one non-blank value. Note that <if> does not support the "omitBlanks" option. You must filter blank values in the expression.

Even more conditional: the <case> tag
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sometimes you need to to choose from one of several templates based upon varying criteria. For instance, when listing entities related to an object you might want to vary the text before the list with respect to the number of entities being listed. There are ways to do this with display templates, but the cleanest way is with a <case> tag:

.. code-block:: none

	<case>
		 <ifcount code="ca_entities.related" max="0">No related entities</ifcount>
		 <ifcount code="ca_entities.related" min="1" max="1">Related entity: ^ca_entities.preferred_labels.name</ifcount>
		 <ifcount code="ca_entities.related" min="2">Related entities: ^ca_entities.preferred_labels.name%delimiter=,_</ifcount>
	</case>

The <case> tag evaluates each <ifcount> tag in order and stops at the first one that results in output. You can include templates beginning with <ifdef>, <ifnotdef> and <if> as well as <ifcount>. If a <unit> tag is included as the last template in a <case> it will be used as the default in case no other template results in output.

Because <case> tags stop evaluating as soon as they find a template with output they are generally the best performing way to choose a template from a list of possibilities.

Expressions
^^^^^^^^^^^
It's also possible to output the result of expressions as-is. A use case for this is making certain statistics about your metadata searchable. For instance, you could use Prepopulate to always keep the current number of entity relationships for your objects in a hidden (but searchable and sortable) field.

Usage of the expression tag is simple: Anything inside the tag is treated as expression (see expressions for more info). You can use your typical caret-prefixed bundle placeholders and even unit tags. Unit tags get evaluated/replaced first when CollectiveAccess runs display templates, so you can use the result of a unit tag in your expression. Here are a few basic examples:

``<expression>5 + 4</expression>``
``<expression>length(^ca_objects.preferred_labels)</expression>``

This one outputs related entity names and their string lengths:

``<unit relativeTo="ca_entities">^ca_entities.preferred_labels, <expression>length(^ca_entities.preferred_labels)</expression></unit>``

The following counts the number of entity relationships for the current record. We use a unit tag to generate the parameters for the sizeof function.

``<expression>sizeof(<unit relativeTo="ca_entities" delimiter=",">^ca_entities.entity_id</unit>)</expression>``

This one calculates the age of Alan Turing:

``<expression>age("23 June 1912", "7 June 1954")</expression>``

Formatting hierarchical displays
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Many types of records can be arranged hierarchically. To get some or all of the hierarchy for display use a hierarchical bundle specifier. This is just a normal specifier with a hierarchical modifier (hierarchy, parent, children) added.

For example, for an object primary, a ^ca_objects.hierarchy.preferred_labels.name placeholder will return the names of all objects in the hierarchy from top to bottom. You'll probably want to set a delimiter between each item in the hierarchy. You can do so by adding a placeholder option: append a percent sign and delimiter=<my delimiter> to the bundle specifier, like so:

``^ca_objects.hierarchy.preferred_labels.name%delimiter=_➔_``

When setting the delimiter, underscores are used in place of spaces. Spaces are used to delimit individual bundle specifiers, so you can't have the delimiter floating out past a space associated with the specifier. The underscores will be converted to spaces for display.

You can get more control over hierarchy displays using a <unit> set relative to a hierarchy. For our object primary:

``<unit relativeTo="ca_objects.hierarchy">^ca_objects.preferred_labels.name (^ca_objects.idno)</unit>``

will evaluate the <unit> for each record in the hierarchy in turn set to primary. Related data can be accessed as well, and additional <unit>'s can be specified within.

The parent and children modifiers work similarly to hierarchy but return the immediate parent of a record or its immediate children respectively.

There are a number of placeholder options that can be used to modify how hierarchical data is displayed:

.. csv-table::
   :widths: 25, 75, 25
   :header-rows: 1
   :file: ../_static/csv/hierarchical_placeholders.csv

Making links to other records
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The <l> tag may be used to create links within the template. The links will always point to the primary record. In Providence the link will lead to the editing interface for the record; in Pawtucket the link will be to the detail display for the record. It is possible to write plugins that override this behavior and create other sorts of links.

Any stretch of the template may be made into a link. For example, assuming the primary is an entity:

.. code-block:: none

	<l>^ca_entities.preferred_labels.displayname</l> <ifdef code="ca_entities.address.address1">(</ifdef>^ca_entities.address.address1
	<ifdef code="ca_entities.address.address1">)</ifdef>

Clicking on the entity name in Providence would take a cataloguer to the editor for the entity record; in Providence it leads to the detail for the entity.

Links always point to the primary record. If you use <l> tags within a <unit> the links will be to the primary within the <unit>.

Using HTML
^^^^^^^^^^
You can freely use HTML tags for formatting within your templates, so long you follow the rules and use well-formed markup. Be sure to close any tag you open. The special template tags such as <ifdef> count in terms of well-formedness even though they don't display. This, for instance, is not correct and will render unpredictably:

.. code-block:: none

	<l>^ca_occurrences.preferred_labels.names</l> <ifdef code="ca_occurrences.exhibit_date"><b>(Dates: </ifdef>^ca_occurrences.exhibit_date
	<ifdef code="ca_occurrences.exhibit_date">)</b></ifdef> ^ca_occurrences.description

Notice that the <b> tag in the first <ifdef> is not closed before the closing </ifdef>, producing invalid markup. There is a </b> tag later on but this too is taken on its own due to the enclosing <ifdef> tags. The correct way to write this template is:

.. code-block:: none

	<l>^ca_occurrences.preferred_labels.names</l> <ifdef code="ca_occurrences.exhibit_date"><b>(Dates: ^ca_occurrences.exhibit_date
	</b></ifdef> ^ca_occurrences.description

Special placeholders
^^^^^^^^^^^^^^^^^^^^
There are a few placeholders that have special meanings for certain kinds of primary records:

.. csv-table::
   :widths: 25, 75
   :header-rows: 1
   :file: ../_static/csv/special_placeholders.csv
   
Splitting apart a date range into separate data points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Single date values that are expressed as ranges (e.g. 2000-2018) can be parsed into separate data points for start and end dates. For example, if you wish to export to MS Excel and would like distinct columns for the first and last dates in the range. You can do so with the following syntax:

.. code-block:: none

	^ca_objects.your_date_element_code%start_as_iso8601=1
	^ca_objects.your_date_element_code%end_as_iso8601=1
