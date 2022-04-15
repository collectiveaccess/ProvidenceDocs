**WorldCat**
========
CollectiveAccess supports WorldCat as a bibliographic authority in any given system. `Worldcat <https://www.worldcat.org/ >`_ is the world’s largest digital database of library content and operates as an OCLC. WorldCat houses publications from all over the world, and incorporates various editions, volumes, languages, and media relating to specific titles. Citations can be linked to records, and automated citations enhance retrieval in searches within CollectiveAccess. 

WorldCat can be used in two modes in CollectiveAccess: as a **bibliographic authority** referenced in metadata elements from any record in your CollectiveAccess system, or, as a **data source** from which to import bibliographic data into CollectiveAccess. Note that when WorldCat is used as an authority within CollectiveAccess, only references between CollectiveAccess records and WorldCat are created; nothing is actually imported.

Bibliographic data that is directly imported into any CollectiveAccess system uses the WorldCat import interface, which works with a specialized interface for interactively locating and retrieving one or more entries from WorldCat. A WorldCat lookup field can also be included in any record in a given system.

To use WorldCat, either a valid OCLC Z39.50 `login <https://help.oclc.org/Metadata_Services/Z3950_Cataloging>`_ or a `WorldCat Web Search API <https://www.oclc.org/developer/api/oclc-apis/worldcat-search-api.en.html>`_ key is required. These two connection methods have different technical requirements but offer identical functionality. Note that your OCLC user agreement may prohibit you from using the Web Search API for cataloging activity; consult your OCLC service representative as to your rights before using the API. 

Your PHP installation must have `cURL support <https://www.php.net/manual/en/book.curl.php>`_ to use the Web Search API. PHP must be built with `YAZ support <https://www.php.net/manual/en/book.yaz.php>`_ to use Z39.50. YAZ is available as a standard package on many Linux distributions and installation is generally straightforward. 

Users who wish to incorporate WorldCat into a Collective Access system must have a subscription. To read more about installation, terms of use, and other supported external information services, please see `Information Services <https://manual.collectiveaccess.org/dataModelling/metadata/informationServices.html>`_. 
