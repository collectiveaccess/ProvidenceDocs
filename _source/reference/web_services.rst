Web Services
============

CollectiveAccess supports several external web services as metadata attached to CollectiveAccess records. It does this by performing a lookup operation at the remote service and then allowing you to pick a value from a results list. It then stores some core information about the referenced piece of data and a reference (URI) to the original resource. InformationService and LCHS are *metadata elements types* that allow these web services to be configured as fields in the User Interface.

InformationService is also a plugin API that makes it easy to add support for other external services. The exact information stored locally differs from plugin to plugin. 

Available plugins
------------------

**LCSH**
	- `LC subject headings <http://id.loc.gov/authorities/subjects.html>`_
	- `LC Name Authority file <http://id.loc.gov/authorities/names.html>`_	
	- `LC subject headings for children <http://id.loc.gov/authorities/childrensSubjects.html>`_
	- `LC Genre/Forms File <http://id.loc.gov/authorities/genreForms.html>`_
	- `Thesaurus of Graphic Materials <http://id.loc.gov/vocabulary/graphicMaterials.html>`_
	- `Preservation Events <http://id.loc.gov/vocabulary/preservation.html>`_
	- `Preservation Level Role <http://id.loc.gov/vocabulary/preservation/preservationLevelRole.html>`_
	- `Cryptographic Hash Functions <http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions.html>`_
	- `MARC Relators <http://id.loc.gov/vocabulary/relators.html>`_
	- `MARC Countries <http://id.loc.gov/vocabulary/countries.html>`_
	- `MARC Geographic Areas <http://id.loc.gov/vocabulary/geographicAreas.html>`_
	- `MARC Languages <http://id.loc.gov/vocabulary/languages.html>`_
	- `ISO639-1 Languages <http://id.loc.gov/vocabulary/iso639-1.html>`_
	- `ISO639-2 Languages <http://id.loc.gov/vocabulary/iso639-2.html>`_
	- `ISO639-5 Languages <http://id.loc.gov/vocabulary/iso639-5.html>`_

**InformationService**
	- `AAT <http://vocab.getty.edu>`_
	- `ALA-National Species List <https://api.ala.org.au/apps>`_
	- `CollectiveAccess <https://github.com/collectiveaccess>`_
	- `Encyclopedia of Life (EOL) <http://eol.org/api>`_
	- `Iconclass <http://www.iconclass.org/>`_
	- `ResourceSpace <https://www.resourcespace.com/knowledge-base/api>`_
	- `SparqlEndpoint <http://vocab.getty.edu>`_
	- `TGN <http://vocab.getty.edu/>`_
	- `ULAN <http://vocab.getty.edu/>`_
	- `VIAF <https://www.oclc.org/developer/develop/web-services/viaf.en.html>`_
	- `Wikipedia <https://www.mediawiki.org/wiki/API:Web_APIs_hub>`_
	- `WorldCat <https://www.oclc.org/developer/develop/web-services/worldcat-search-api.en.html>`_
	
Implementing new plugins
------------------------

InformationService implementations reside in *app/lib/core/Plugins/InformationService* and should implement `IWLPlugInformationService <https://github.com/collectiveaccess/providence/blob/master/app/lib/core/Plugins/IWLPlugInformationService.php>`_ and extend `BaseInformationServicePlugin <https://github.com/collectiveaccess/providence/blob/master/app/lib/core/Plugins/InformationService/BaseInformationServicePlugin.php>`_. The class name must be "WLPlugInformationService<Service>" and the file name "<Service>.php".

It can provide additional settings using the static $s_settings variable, usually derived from $g_information_service_settings_<Service>. It should set the "NAME" property of the info array in the constructor.

The `Wikipedia implementation <https://github.com/collectiveaccess/providence/blob/master/app/lib/core/Plugins/InformationService/Wikipedia.php>`_ is relatively simple and uses most of the available features (except getDataForSearchIndexing()) so you could use that as a template.

**Core functions**

The core functions you must implement are:

.. code-block:: none

	public function lookup($pa_settings, $ps_search, $pa_options=null);

where $pa_settings is an array containing the settings for this particular element (including the ones you provided) and $ps_search is the search expression provided by the user. The function should return an array with the "results" key being a list results for the given search expression. Each result should have a label, url and idno.

.. code-block:: none

	public function getExtendedInformation($pa_settings, $ps_url);

This should return an array with the "display" key set to an HTML representation of the given record (identified by the URL/URI). You can either go and look the detailed data up remotely or, for instance, call getExtraInfo() to get locally stored data (see below).

**Optional functions**

The functions listed below are optional and have default (empty) implementations in `BaseInformationServicePlugin <https://github.com/collectiveaccess/providence/blob/master/app/lib/core/Plugins/InformationService/BaseInformationServicePlugin.php>`_ so it doesn't hurt to leave them out of your plugin entirely. They can be used to provide useful features though.

.. code-block:: none

	public function getExtraInfo($pa_settings, $ps_url);

Returns an array of key=>value pairs containing extra information to be stored locally, alongside the id, the display label and the URL. This data can be accessed using SearchResult::get(), so you should keep the keys alphanumeric, lowercase and without spaces.

public function getDataForSearchIndexing($pa_settings, $ps_url);

Returns a list of strings that are added to the search index for the record associated with this attribute. This allows you to add additional data points that can be used to find the CollectiveAccess record but are not necessarily available for display. Note that the data returnd by getExtraInfo() is not indexed for search, so you might have to add the same data twice.

public function getDisplayValueFromLookupText($ps_text);

The default behavior is to use the (selected) label returned by the lookup() function as display value for attribute values. That can be undesirable for use cases like the AAT where one the one hand you want a lot of identifying information in the lookup dropdown but on the other you probably don't care about all that info once the "relationship" has been created because the keyword is doing its job in the background (making the associated record findable). Maybe you just want a simple and short label instead to save space.

This function allows you to mangle the lookup text to create a different display value. The lookup text usually has the URL in it, so you could even look up additional info to pull in here if you wanted. An example can be found in the `AAT implementation <https://github.com/collectiveaccess/providence/blob/master/app/lib/core/Plugins/InformationService/AAT.php>`_, where we do some regular expression magic to convert lookup texts:

.. code-block:: none

	before: [300025342] swordsmiths [people in crafts and trades by product, people in crafts and trades]
	after: swordsmiths
	