..  _informationServices:

Information Services
====================

CollectiveAccess supports several external information services to attached metadata to CollectiveAccess records. It does this by performing a lookup operation at the remote service and then allowing you to pick a value from a results list. It stores core information about the referenced piece of data and a reference (URI) to the original resource. 
To configure metadata fields in the user interface, select the InformationService or LCSH *metadata element type*.

InformationService is also a plugin API that makes it easy to add support for other external services. The exact information stored locally differs from plugin to plugin. 

.. contents::
   :local:
   :depth: 1


Library of Congress Plugins (LC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

Example LC installation profile code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: none

	<metadataElement code="lcsh_terms" datatype="LCSH">
   	 	<labels>
       	 <label locale="en_US">
        	  <name>Library of Congress Subject Headings</name>
       	   <description>Library of Congress Subject headings describing this object.</description>
       	 </label>
   	 	</labels>
    	<settings>
     	   <setting name="fieldWidth">80</setting>
      	  <setting name="fieldHeight">1</setting>
      	  <setting name="vocabulary">cs:http://id.loc.gov/authorities/subjects</setting>
   	 	</settings>
   	 	<typeRestrictions>
        	<restriction code="ca_objects">
        	<table>ca_objects</table>
          		<settings>
            		<setting name="minAttributesPerRow">0</setting>
            		<setting name="maxAttributesPerRow">100</setting>
            		<setting name="minimumAttributeBundlesToDisplay">1</setting>
          	</settings>
        	</restriction>
    	</typeRestrictions>
	</metadataElement>


Information Services Plugins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`Getty Vocabularies <http://vocab.getty.edu>`_
##############################################
	AAT (Art and Architecture Thesaurus), TGN (Thesaurus of Geographic Names), and ULAN (The Union List of Artist Names) are all provided via SparqlEndpoint Linked Open Data Service by the Getty Vocabularies. 
	None of these 3 plugins has any custom settings on element level, but they share a more comprehensive configuration in the configuration file :ref:`linked_data.conf`. The default configuration should work for most use cases.
	
`ALA-National Species List <https://api.ala.org.au/apps>`_
##########################################################
	"Open access to the Atlas of Living Australia's biodiversity data" 
	
`CollectiveAccess <https://github.com/collectiveaccess>`_
##########################################################
	This plugin allows you to reference records in remote CollectiveAccess instances. Available settings are as follows: 
		
.. csv-table:: CollectiveAccess Information Service
   :header: "Setting Name", "Description", "Example"
   :widths: 20, 20, 20
  		
   		"service", "Set service setting to 'CollectiveAccess' to use this plugin", 	"CollectiveAccess"
		"baseURL", "URL used to query the information service", 	"http://localhost/admin/"
		"table", "valid CollectiveAccess table name", 	"ca_entities"
		"user_name", "User name to authenticate with on remote system", 	"webservice"
		"password", "Password to authenticate with on remote system", 	"/"
		"labelFormat", "Display template to format query result labels", 	"^ca_entities.preferred_labels"
		"detailFormat", "Display template to format detailed information blocks", 	"^ca_objects.preferred_labels (^ca_objects.idno)" 
		

`Encyclopedia of Life (EOL) <https://eol.org/docs/what-is-eol/data-services/classic-apis>`_
###########################################################################################
	"Global acccess to knowledge about life on Earth"
	
`Iconclass <http://www.iconclass.org/>`_
#########################################
	"A multilingual classification system for cultural content"
	
`ResourceSpace <https://www.resourcespace.com/knowledge-base/api>`_
###################################################################
	"ResourceSpace is a web-based Digital Asset Management software offering a solution for organising and sharing files"
	
`VIAF <https://www.oclc.org/developer/develop/web-services/viaf.en.html>`_
##########################################################################
	"Open access to linked names for the same entity across the world's major name authority files, including national and regional variations in language, character set, and spelling."
	
`Wikipedia <https://www.mediawiki.org/wiki/API:Web_APIs_hub>`_
##############################################################
	This service allows referencing Wikipedia articles. Available settings are:

.. csv-table:: Wikipedia Information Service Installation Profile Settings
   :header: "Setting Name", "Description", "Example"
   :widths: 20, 20, 20
  		
   		"service", "Set service setting to 'Wikipedia' to use this plugin", "Wikipedia"
		"lang", "2- or 3-letter `language code <http://meta.wikimedia.org/wiki/List_of_Wikipedias>`_ for Wikipedia to use. Defaults to en", "en"
		
Wikipedia Display Template Options
**********************************
This plugin can pull in data for local display. For example, both the abstract and preview image are available in bundle displays. Suppose your wikipedia metadata element has the code **wikipedia**. You can reference additional properties about a referenced article like this: 

.. code-block:: none

	ca_objects.wikipedia.<property>	

Where property is one of the following: 

.. csv-table:: Wikipedia Information Service Installation Profile Settings
   :header: "Setting Name", "Description"
   :widths: 20, 50
  		
   		"image_thumbnail", "Image thumbnail URL"
		"image_thumbnail_width", "Width of image thumbnail. Box is capped at 200px by 200px"
		"image_thumbnail_height", "Height of image thumbnail. Box is capped at 200px by 200px"
		"image_viewer_url", "(Valid for v1.5.1) URL for Wikipedia's full screen image viewer"
		"title", "Title of the Wikipedia article"
		"pageid", "Numeric page identifier"
		"fullurl", "URL for the article"
		"canonicalurl", "Canonical URL for the article"
		"extract", "Extract of the article, usually a HTML representation of the full article"
		"abstract", "CollectiveAccess tries to extract the first paragraph from the article to provide a shorter abstract. This is usually the part shown above the table of contents but extraction might fail for poorly formatted articles"
		
`WorldCat <https://www.oclc.org/developer/develop/web-services/worldcat-search-api.en.html>`_
#############################################################################################
	To use WorldCat you'll need either a valid OCLC `Z39.50 login <https://help.oclc.org/Metadata_Services/Z3950_Cataloging>`_ or WorldCat Web Search API key. The two connection method have different technical requirements but offer identical functionality. Note that your OCLC user agreement may prohibit you from using the `Web Search API <https://www.oclc.org/developer/develop/web-services/worldcat-search-api.en.html>`_ for cataloguing activity. Consult your OCLC service representative as to your rights before using the API. Your PHP installation must have `cURL support <https://www.php.net/manual/en/book.curl.php>`_ to use the Web Search API. PHP must be built with `YAZ <https://www.php.net/manual/en/book.yaz.php>`_ support to use Z39.50. YAZ is available as a standard package on many Linux distributions and installation is generally straightforward.

Specify your Web Search API key or Z39.50 login in App.conf. The entries are:

   - worldcat_api_key
   - worldcat_z39.50_user
   - worldcat_z39.50_password
	
	
WorldCat Options
****************
	You can use WorldCat as a metadata element type "information service", but you can also use it to import bibliographic data from WorldCat directly into your CollectiveAccess system using the WorldCat import interface, available in the "Import" menu. The importer works much as the general data importer, but with a specialized interface for interactively locating and retrieving one or more entries from WorldCat. For more information, read the <PLACE LINK HERE> Importer documentation.

Example Information Service installation profile code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: none

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


Implementing new plugins
^^^^^^^^^^^^^^^^^^^^^^^^

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

.. code-block:: none

	public function getDataForSearchIndexing($pa_settings, $ps_url);

Returns a list of strings that are added to the search index for the record associated with this attribute. This allows you to add additional data points that can be used to find the CollectiveAccess record but are not necessarily available for display. Note that the data returnd by getExtraInfo() is not indexed for search, so you might have to add the same data twice.

.. code-block:: none

	public function getDisplayValueFromLookupText($ps_text);

The default behavior is to use the (selected) label returned by the lookup() function as display value for attribute values. That can be undesirable for use cases like the AAT where one the one hand you want a lot of identifying information in the lookup dropdown but on the other you probably don't care about all that info once the "relationship" has been created because the keyword is doing its job in the background (making the associated record findable). Maybe you just want a simple and short label instead to save space.

This function allows you to mangle the lookup text to create a different display value. The lookup text usually has the URL in it, so you could even look up additional info to pull in here if you wanted. An example can be found in the `AAT implementation <https://github.com/collectiveaccess/providence/blob/master/app/lib/core/Plugins/InformationService/AAT.php>`_, where we do some regular expression magic to convert lookup texts:

.. code-block:: none

	before: [300025342] swordsmiths [people in crafts and trades by product, people in crafts and trades]
	after: swordsmiths
	