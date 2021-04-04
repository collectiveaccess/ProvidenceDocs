Search.conf
===========

Serching  can be enhanced using PCRE - Perl Compatible Regular Expressions. On https://www.php.net/manual/en/regexp.introduction.php you can find more syntax samples.


Indexing Tokenizer Regex
------------------------
This is the Regex character class used when indexing saved text; values matched will be used as token delimiters (in other words, the search expression will be broken into words wherever the matched characters are). Note that the default class, as displayed in the example below, starts with a caret ("^"), which has the effect of negating the class. In other words, the class defines what characters will not be treated a token delimiters.

.. code-block:: none

	indexing_tokenizer_regex = ^\pL\pN\pNd/_#\@\&\.

Search Tokenizer Regex
----------------------
This is the Regex character class used when searching; values matched will be used as token delimiters (this is the same thing as indexing_tokenizer_regex except that it's used when to break user searches into words rather than text to be indexed).

.. code-block:: none

	search_tokenizer_regex = ^\pL\pN\pNd/_#\@\&\.

"As Is" Regex Matching for Accession Numbers
--------------------------------------------
Here you may enter a list of regular expressions that if matched cause search input to be treated "as-is," or searched without being broken up into tokens. This is useful for preventing tokenization of accession numbers and other values that rely upon punctuation being kept intact when being searched.

.. code-block:: none

	asis_regexes = [
		"^[\d]+[\.\-][A-Za-z0-9\.\-]+$"
	]

Changing the layout of quicksearch results
------------------------------------------
With the following format:

.. code-block:: none

	ca_<table>_<type>_quicksearch_result_display_template = 

or

.. code-block:: none

	ca_<table>_quicksearch_result_display_template = 
	
The format of the quick search results can be altered. The value of the template uses the same syntax as bundle displays. The below is an example for adding "artists" to an "artwork" search result layout:

.. code-block:: none

	ca_objects_artwork_quicksearch_result_display_template = 
	<unit relativeTo='ca_entities' restrictToRelationshipTypes='artist'><u>^ca_entities.preferred_labels.surname, ^ca_entities.preferred_labels.forename</u>:</unit>
	<em>^ca_objects.preferred_labels.name</em> (<l>^ca_objects.idno</l>) [^ca_objects.type_id]

SqlSearch Plugin Configuration
------------------------------
Set to 0 if you don't want search input stemmed (ie. suffixes removed) prior to search

The plugin uses the English Snoball stemmer (http://snowball.tartarus.org/) and can give poor results with non-English content. If you are cataloguing non-English material you will probably want to turn this off.

search_sql_search_do_stemming = 1


ElasticSearch Plugin Configuration
----------------------------------
enter the elastic search base url here (without any index names) search_elasticsearch_base_url = http://localhost:9200/

This is the name of the ElasticSearch index used by CollectiveAccess. You probably don't need to change this unless you're using a single ElasticSearch setup for multiple CollectiveAccess instances and/or other applications. search_elasticsearch_index_name = collectiveaccess
