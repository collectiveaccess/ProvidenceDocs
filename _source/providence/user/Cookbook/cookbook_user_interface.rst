Cookbook: User Interface
========================

This section provides some real examples of common challenges that may arise relating to the CollectiveAcces user interface.

Each scenario in this section begins with a “problem,” describing a certain challenge or question that may occur. There is an accompanying “solution” provided for each problem, which outlines how to carry out the necessary steps to reach a specific outcome. 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online `Support Forum <https://collectiveaccess.org/support/>`_, `Online Chat <https://gitter.im/collectiveaccess/support>`_, `Slack Channel for Developers <https://collectiveacc-uye7574.slack.com/join/signup#/domain-signup>`_, and `Back-end <https://github.com/collectiveaccess/providence>`_ and `Front-end <https://github.com/collectiveaccess/pawtucket2>`_ GitHub Repositories. 

See also: `User Interface Administration <file:///Users/charlotteposever/Documents/ca_manual/providence/user/editing/interfaces.html?highlight=user+interface>`_ and `User Interface Settings <file:///Users/charlotteposever/Documents/ca_manual/providence/user/reference/settings/userInterfaceSettings.html?highlight=user+interface>`_. 

Contents
--------

* `Auto-Generated ID numbers are stuck`_
* `Using Summaries`_
* `Including an ID Number (idno) in a Display`_
* `Adding WYSIWYG Editor to Text Fields`_
* `Keeping Track of an Item's Changes`_
* `Match a Batch Media Import through a Relationship`_
* `Batch Editing Records`_
* `Batch Deleting Records`_
* `Searching on a Specific Metadata Element`_
* `Changing the Layout of "Quick Search" Results`_
* `Creating a "Researcher" Access Role`_
* `Disabling a User Login`_
* `Adding or Removing Elements from an Editor UI Doesn't "Stick"`_
* `Viewing Search Results as a Spreadsheet`_
* `Keeping Track of the Path via the “Breadcrumb Trail”`_
* `Grouping Records Using Sets`_
* `Navigating to Individual Records from Within a Set`_
* `Creating a Display through the User Interface`_
* `Searching on Specific Metadata`_
* `Browsing by Current Location (Object Use History)`_
* `Adding List Items Through the UI`_
* `Creating a New Vocabulary Through the UI`_
* `Creating a New Metadata Element Through the UI`_
* `Downloading Search Results to Excel`_
* `Enable Spell Correction`_
* `Set Defaults for "delete/transfer" Prompt`_

Auto-Generated ID numbers are stuck
-----------------------------------

**Problem**: Your auto-generated ID numbering system is stuck on a value that is already in use, or the numbers are not sorting or being generated properly.

**Solution**: If you notice values such as titles and identifiers are sorting incorrectly, you may need to reload sort values from your data. The internal format of sort values can vary between versions of CollectiveAccess, causing erroneous sorting behavior after an upgrade. To rebuild sort values, navigate to Manage -> Administration -> Maintenance -> Rebuild Sort Values from the Global Navigation.

Note that depending upon the size of your database, reloading sort values can take from a few minutes to an hour or more.

Using Summaries
---------------

**Problem**: You want to use the "Summary" screen to view a record, but it seems to be blank.

**Solution**: You must configure a display that includes all of the metadata you want to see summarized. To do this through the UI, navigate to Manage > My Displays. Then, to create a new display, choose the table for which the display is relevant, go to "Display List," and then drag and format the elements you wish to include. For tips on formatting, see Bundle Display Templates. Then, when you are in the Summary screen, you can choose the appropriate Display from the drop-down in the top-right corner.

Including an ID Number (idno) in a Display
-----------------------------------

**Problem**: You want a display to include the field "Object ID," but you're not sure which bundle to use when you're setting the display up in "My Displays."

**Solution**: Choose the bundle with the code "ca_objects.idno." Don't confuse this with ca_objects.object_id, which is the internal ordering that CollectiveAccess uses to number records, and is not the same thing as the Object Identifier that your organization uses. Note that If you're creating a display for Lots, use the bundle with the code "ca_objects.idno_stub."

Adding WYSIWYG Editor to Text Fields
------------------------------------

**Problem**: You realized that you wanted a certain "description" field to have a rich-text editor after your installation profile was fully installed.

**Solution**: Go to *Manage > Administration > Metadata Elements* and find the field in question. As long as it is a text field, there will be a checkbox entitled "use rich text editor." Check this and save.

Keeping Track of an Item's Changes
----------------------------------

**Problem**: You're not finished working on an Object record, but you need to do some other work before you can return to it.

**Solution**: Add the record to the "My Watched Items" list. In the Inspector Window of a record’s user interface, click on a small icon that looks like an eye.  The record will then be stored in the "My Watched Items" list, which is accessible through Manage > My Watched Items. Changes to the record will be tracked here.

Match a Batch Media Import through a Relationship
-------------------------------------------------

**Problem**: You want to import a large set of images relating to an already-catalogued event, but you want them to have their own records.

**Solution**: From **Import > Media**, you can upload the batch of media. Set it to create relationships with a given record type by using the "Relationships" media import tool. You can select the type (in this case "Occurrence") and relationship type (i.e. "depicts"). The relationship will be created based on matching the media file name, with the event record identifier, so make sure the files are properly named.

Batch Editing Records
---------------------

**Problem**: You want to batch edit metadata in a set of records.

**Solution**: The easiest way to batch edit records is to add the target records to a set via search results. Opening the "sets" menu in the search results toolbar will give you controls to add multiple or single records at a time. Once your to-be-edited set is complete, you can open the batch under **Manage > My Sets**. Click the multi-record icon, and you will see the batch edit interface. Custom interfaces can be configured under **Manage > Administration > User interfaces** and set under **Preferences > Batch Editing**.

Batch Deleting Records
----------------------

**Problem**: You want to batch delete a set of records.

**Solution**: The easiest way to batch delete records is to add the target records to a set via search results. Opening the "sets" menu in the search results tool bar will give you controls to add multiple or single records at a time. Once your to-be-deleted set is complete you can open the batch under Manage > My sets. Click the multi-record icon and then chose "More options" in the record inspector on the upper left hand corner of the screen. There you will see options for batch delete.

Searching on a Specific Metadata Element
----------------------------------------

**Problem**: You want to restrict a search to a date in a specific date field.

**Solution**: First, specify the table name and field, separated by a dot:

.. code-block::

   <table>.<field> (ex. ca_objects.date_created)

Then, use an accepted date range format to search for the date you want to return:

.. code-block::

   ca_objects.date_created:8/2/2013

Use the same basic procedure to search on other specific metadata elements, replacing the date value with the desired text.

Changing the Layout of "Quick Search" Results
---------------------------------------------

**Problem**: You want to change the layout of search results returned for a quick search (search box in the upper-right hand corner).

**Solution**: In */app/conf/search.conf*, set the layout for the table/type using display templates. 
For example, to add "artists" to "artwork" search results use this format:

.. code-block::

   ca_objects_artwork_quicksearch_result_display_template = 
   <unit relativeTo='ca_entities' restrictToRelationshipTypes='artist'><u>^ca_entities.preferred_labels.surname, ^ca_entities.preferred_labels.forename</u>:</unit>
   <em>^ca_objects.preferred_labels.name</em> (<l>^ca_objects.idno</l>) [^ca_objects.type_id]

Note that the name of the *search.conf* entry is

.. code-block::

   ca_<table>_<type>_quicksearch_result_display_template = 

It can also be

.. code-block::

   ca_<table>_quicksearch_result_display_template

The former is type-specific. The latter applies to any type. If you define both the type specific one will always be used in preference.

Creating a "Researcher" Access Role
-----------------------------------

**Problem**: You want certain users to log in as researchers with read-only capabilities.

**Solution**: Navigate to Manage > Access Control > Access Roles > New Role. Set all relevant "Actions" to allow the user to view, but not edit, different tables. Then, create a login and password for your user under "User Logins," and make sure you click "Roles > Researcher" (or whatever you've named your read-only access role). Make sure that you have displays configured, because this is the only way that a read-only login will be able to view information (through the Summary screen).

Disabling a User Login
----------------------

**Problem**: A staff member has left your organization, and you want to deactivate their login without deleting all of their information for legacy purposes.

**Solution**: Rather than deleting the login, go to Manage > Access Control > User logins, and navigate to the "User Class" drop-down. Choose "deleted."

Adding or Removing Elements from an Editor UI Doesn't "Stick"
-------------------------------------------------------------

**Problem**: You want to add or remove elements from a screen in an editor user interface, but upon saving your changes, the screen configuration reverts to its previous state.

**Solution**: Your server is probably configured with limits that prevent the changes from fully saving. This is especially common when editing a screen with many elements already configured. There are two PHP server settings to examine:

1. The Suhosin PHP extension can interfere with saving of large CA forms. If it is installed on your server try setting the suhosin.simulation directive to On
2. You may need to increase the value of max_input_vars. It is set by default in most PHP installations to 1000. Try increasing it to 3000 or more.

Viewing Search Results as a Spreadsheet
---------------------------------------

**Problem**: You've realized that there are mistakes in multiple records, and you want to be able to view and correct them without having to open each individual record.

**Solution**: Use the "editable" layout with your search results to view metadata in a simple, editable spreadsheet format. Note that you must have a display configured in order to dictate which metadata will be included in the spreadsheet, and you won't be able to edit repeating or complex data.

Keeping Track of the Path via the “Breadcrumb Trail”
----------------------------------------------------

**Problem**: You're going back and forth between record types and working within hierarchies, and you're having trouble keeping track of your location in the database. 

**Solution**: Turn on the "breadcrumb trail" in Preferences. To do so, navigate to **Manage > My Preferences > General**. Under “Show current location as 'breadcrumb' trail,” choose “yes.” This will display your current path within the system in a laundry-list format. 

Grouping Records Using Sets
---------------------------

**Problem**: You need to group certain records together in order to share them with other members of your team.

**Solution**: Use "Sets" to create groups of records that you can share and easily return to. This is distinct from Collections, because it's an ad-hoc collection of records for purposes such as slideshows, lessons, or shared work. Sets are often temporary groupings. 

To create a set, navigate to **Manage > My Sets** and choose the type of set you would like to create (Public Presentation or User Set). Then, to begin adding items to the set, type the first few letters of a record's preferred label into the type-ahead field. To make the set accessible to a work group, first create the group in **Manage > Administration**, and then set Group Access on the Set itself.

Navigating to Individual Records from Within a Set
--------------------------------------------------

**Problem**: You've successfully created a set, but now you want to be able to visit one of the records within that set without leaving "my sets" and performing a search.

**Solution**: Click on the editing icon next to the Object's title in the "set items" list. This will open a record in which you can edit the "set item record," or metadata about the record as it applies to the set. To then enter the original record, look in the Inspector Window (the box in the upper left hand corner of the screen). Next to the words "Is Object" you should see a link to the record.

Creating a Display through the User Interface
---------------------------------------------

**Problem**: You need to print out a report for a given record, but none of the pre-configured displays contain the proper metadata.

**Solution**: Navigate to **Manage > My Displays**, choose the relevant table from the drop-down at the top-right of the screen, and click the small "+." Then, navigate to the "Display List" editor (click "Display List" from the left-hand navigation) and drag and drop the metadata bundles to configure your display.

Searching on Specific Metadata
------------------------------

**Problem**: You want to be create a sensitive Object search that includes, for example, Object ID, Title, Dimensions, and Copyright Date.

**Solution**: Create an Advanced Search form. Go to **Manage > Search Tools** and look at the top right of the page. You'll see a drop-down that says "New search form for ___." Choose the appropriate table from the drop-down and then click the small "+" next to it. You will then be able to enter some basic information for your new search form - a title, a unique identifier, etc. To choose which fields will appear in the form, scroll down to "Search Form Contents" and drag and drop the bundles on which you wish to search. Once you've saved, you can navigate to **Find > Objects**, go to the Advanced Search tab from the left-hand navigation, and choose the form you've just created.

Browsing by Current Location (Object Use History)
-------------------------------------------------

**Problem**: You've enabled the Object Use History (aka Location Tracking) feature, and now you want to be able to browse by "current location." Current location is the value that matches the date on the server, based on the use history dates as defined by the bundle.

**Solution**: There are three steps to set up the Current Location browse:

1. Set up the browse facet in browse.conf. Here's an example configuration:

   current_location = {
			type = location,
			restrict_to_types = [],
			
			group_mode = none,
			
			collapse = {
				ca_loans = On loan,
				ca_occurrences = On exhibition,
				ca_movements/movement = In transit,
				ca_movements/condition = Condition
			},
			
			display = {
				ca_storage_locations = {
					location = { template = ^ca_storage_locations.hierarchy.preferred_labels.name%delimiter=_➔_ (storage) }
				},
			},
			
			include_none_option = No location specified,
			
			label_singular = _("current location"),
			label_plural = _("current location")
		},

Collapse will bucket all of the current location values into top level categories such as "On Loan," rather than listing out all of the active loans as unique values. Any table listed under Display will break out into individual values.

Under collapse, the table name is followed by the type code (i.e. ca_movements/condition) and the term on the right side of the equals sign is what will display to users. The only exception to this format is storage locations, which use the relationship type name rather than a record type name (i.e. location above).

2. Next, you'll need to set up *app.conf*:

   current_location_criteria = {
	ca_storage_locations = {
		location = { template = ^ca_storage_locations.hierarchy.preferred_labels.name%delimiter=_➔_ }
	},
	ca_movements = {
		movement = { date = pickup_date },
		condition = { date = pickup_date }
	},
	ca_loans = {
		venue = { date = loan_period }
	},
	ca_occurrences = {
		exhibition = { date = exh_dates }
	}
   }

The values are type ids, except in the case of storage locations which use the relationship type. The dates are set using the metadata element codes.

3. The last step is to run a command using caUtils to load the locations. From the providence/support directory the command is:

.. code-block::

   bin/caUtils reload-object-current-locations

Adding List Items Through the UI
--------------------------------

**Problem**: You have a new employee whose name you need to add to a drop-down list.

**Solution**: Add a list item by navigating to **Manage > Lists and Vocabularies**. From the Hierarchy viewer on that screen, click on the dark gray arrow next to the list you want to change (for example, "Employees.") The list items will appear in a column next to the list names. To add to these list items, click the small "+" next to: “Add under [name of parent list] new [choose from drop-down list]," located above the Hierarchy viewer. You will then see a basic editing screen for your list item, where you can define plural and singular forms and give the list item a unique identifier.

Creating a New Vocabulary Through the UI
----------------------------------------

**Problem**: You've realized that in order to have a table of contents on your public website, you need to add a whole new vocabulary that you can use to tag Objects.

**Solution**: Create a new list in Lists and Vocabularies, and then restrict the bundle ca_list_items to that list on your Object UI. Go to Manage > List and Vocabularies, and choose "add new list" from the top-right of your screen. Make sure you choose the option "use as Vocabulary." Add concepts to the list as described above. Then, go to **Manage > Administration > User Interfaces**. Choose the appropriate UI (in this case, Objects) and drag the ca_list_items (Related Vocabulary Terms) bundle from "Available editor elements" to "Elements to display on this screen." Edit the bundle to customize features such as the Vocabulary's label, and choose the appropriate list to restrict it to.

Creating a New Metadata Element Through the UI
----------------------------------------------

**Problem**: Your system is already all set-up and contains lots of records that you don't want to override, but you've realized you need to add a whole new field.

**Solution**: Go to **Manage > Administration** and click "Metadata Elements" on the left-hand navigation. On the top-right, click the plus-sign labeled "new." Give your field a name, description (if necessary), and unique code. Choose the datatype - is it simple text? A date range? A container that will hold other elements? Then, depending on which type you choose, fill out the datatype-specific options (roll over each for a description). At the bottom of the screen, click "Add type restriction" to bind your new element to the appropriate table. Once all of this has been taken care of, you can add it to the appropriate user interface. Click on the "edit" icon to the right of your chosen interface, and scroll down to "Screens." Click the editing icon next to the appropriate screen (such as "Basic Info") and drag your new element bundle from the list of "Available editor elements'' to the list of "Elements to display on this screen."

Downloading Search Results to Excel
-----------------------------------

**Problem**: You want to download a selection of records to an Excel spreadsheet.

**Solution**: Perform a search for the records you wish to download to Excel. Make sure that you have configured and chosen a display that includes all of the metadata you wish to include in the spreadsheet. When the search is complete, Choose "tools" (one of the choices directly above your search results). 

Then, choose the option "Download Results As." You will see a variety of choices, including options for PDF and XLSX downloads. Choose Tab Delimited, Comma Delimited (CSV), or Spreadsheet with Media Icons (XLSX). If you choose Tab Delimited or Comma Delimited, you can simply open the file with Excel to create a spreadsheet. 

Enable Spell Correction
-----------------------

**Problem**: You want to enable spell correction.

**Solution**: On the command line, cd into the /support directory of Providence. Run bin/caUtils create-ngrams. Spelling corrections will then appear in your basic searches.

Set Defaults for "delete/transfer" Prompt
-----------------------------------------

**Problem**: You want to change which settings defaults for the delete or transfer prompt that appears when you delete a record.

**Solution**: There's a preference per user under **Manage > My preferences > Editing**. You can also set a system default in *app.conf* at */app/conf/app.conf*.


