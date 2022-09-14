Information Services
====================

* `Configuration in an Installation Profile`_ 
* `Available Plugins`_ 
* `Implementing New Plugins`_ 

InformationService is a `metadata element type <file:///Users/charlotteposever/Documents/ca_manual/providence/user/dataModelling/metadata/informationServices.html>`_ that allows for the referencing of external web services as metadata attached to CollectiveAccess records. 

InformationService is also a plugin API that makes it easy to add support for other external services. The exact information stored locally differs from plugin to plugin.

This metadata element type references specific external web services by performing a lookup operation at the remote service, and then allowing the user to pick a value from a result list. Core information about the referenced piece of data and a reference (URI) to the original resource is then stored. 

For a full list of supported external web services supported by CollectiveAccess, please see `Information Services`_. 

Configuration in an Installation Profile
----------------------------------------

A basic configuration of InformationService in an installation profile might look like: 

.. code-block::

   <metadataElement code="my_element" datatype="InformationService">
      <labels>
        <label locale="en_US">
          <name>My InformationService Element</name>
        </label>
      </labels>
      <settings>
        <setting name="service"><!-- enter service here --></setting>
      </settings>
      <typeRestrictions>
        <restriction code="r1">
          <table>ca_objects</table>
          <settings>
            <setting name="minAttributesPerRow">0</setting>
            <setting name="maxAttributesPerRow">255</setting>
            <setting name="minimumAttributeBundlesToDisplay">1</setting>
          </settings>
        </restriction>
      </typeRestrictions>
    </metadataElement>

Note that the **service setting** is mandatory, and defines the plugin used for that element. A list of available plugins is below. 

Available Plugins
-----------------

Below is a list of existing plugins and available settings: 

CollectiveAccess
^^^^^^^^^^^^^^^^

This plugin allows you to reference records in remote CollectiveAccess instances. Available settings are as follows:

.. csv-table::
   :header-rows: 1
   :file: info_service_table1.csv

uBio
^^^^

uBio is an initiative within the science library community to join international efforts to create and utilize a comprehensive and collaborative catalog of known names of all living (and once-living) organisms. Available settings for this implementation are:

.. csv-table::
   :header-rows: 1
   :file: info_service_table2.csv

Getty Linked Open Data Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Getty LOD Services are technically 3 different plugins that share a common code base. They allow referencing concepts in Getty's AAT, TGN and ULAN vocabularies via their SPARQL Linked Open Data web service. Set the service setting to AAT, TGN or ULAN to use corresponding services. The plugin uses Getty's SPARQL endpoint and their full text indexes for fast lookups and the full RDF representation (example here) of the concepts to display more detailed info and also to make additional data available for search.

None of the 3 plugins has any custom settings on element level, but they share a more comprehensive configuration in the configuration file linked_data.conf. The default configuration should work for most use cases. The file has 3 large blocks, one for each of the plugins (tgn, aat, ulan). 

Their format is identical and consists of 3 settings:

.. csv-table::
   :header-rows: 1
   :file: info_service_table3.csv

Wikipedia
^^^^^^^^^

This service allows referencing Wikipedia articles. Available settings are:

.. csv-table::
   :header-rows: 1
   :file: info_service_table5.csv

This plugin also tries to pull in an abstract and a preview image for local display. Both the abstract and preview image are available in bundle displays. Suppose your wikipedia metadata element has the code wikipedia. You can reference additional properties about a referenced article like this:

``ca_objects.wikipedia.<property>``

Where property is one of the following:

.. csv-table::
   :header-rows: 1
   :file: info_service_table4.csv

Implementing New Plugins
------------------------

InformationService implementations reside in */app/lib/Plugins/InformationService* and should implement IWLPlugInformationService and extend BaseInformationServicePlugin. The class name must be "WLPlugInformationService<Service>" and the file name "<Service>.php".

It can provide additional settings using the static $s_settings variable, usually derived from $g_information_service_settings_<Service>. It should set the "NAME" property of the info array in the constructor.
The Wikipedia implementation is relatively simple, and uses most of the available features (except getDataForSearchIndexing()) so you could use that as a template.

Core Functions
^^^^^^^^^^^^^^

The core functions you must implement are:

``public function lookup($pa_settings, $ps_search, $pa_options=null);``

where $pa_settings is an array containing the settings for this particular element (including the ones you provided) and $ps_search is the search expression provided by the user. The function should return an array with the "results" key being a list of results for the given search expression. Each result should have a label, url and idno:

``public function getExtendedInformation($pa_settings, $ps_url);``

This should return an array with the "display" key set to an HTML representation of the given record (identified by the URL/URI). You can either go and look the detailed data up remotely or, for instance, call getExtraInfo() to get locally stored data (see below).

Optional functions
^^^^^^^^^^^^^^^^^^

The functions listed below are optional, and have default (empty) implementations in BaseInformationServicePlugin, so it doesn't hurt to leave them out of your plugin entirely. However, they can be used to provide useful features. 

``public function getExtraInfo($pa_settings, $ps_url);``

Returns an array of key=>value pairs containing extra information to be stored locally, alongside the id, the display label and the URL. This data can be accessed using SearchResult::get(), so you should keep the keys alphanumeric, lowercase and without spaces.

``public function getDataForSearchIndexing($pa_settings, $ps_url);``

Returns a list of strings that are added to the search index for the record associated with this attribute. This allows you to add additional data points that can be used to find the CollectiveAccess record but are not necessarily available for display. Note that the data returned by getExtraInfo() is not indexed for search, so you might have to add the same data twice.

``public function getDisplayValueFromLookupText($ps_text);``

The default behavior is to use the (selected) label returned by the lookup() function as display value for attribute values. That can be undesirable for use cases like the AAT where one the one hand you want a lot of identifying information in the lookup dropdown but on the other you probably don't care about all that info once the "relationship" has been created because the keyword is doing its job in the background (making the associated record findable). Maybe you just want a simple and short label instead to save space.

This function allows you to mangle the lookup text to create a different display value. The lookup text usually has the URL in it, so you could even look up additional info to pull in here if you wanted. An example can be found in the AAT implementation, where we do some regular expression magic to convert lookup texts:

before: ``[300025342] swordsmiths [people in crafts and trades by product, people in crafts and trades]``

after: ``swordsmiths``
