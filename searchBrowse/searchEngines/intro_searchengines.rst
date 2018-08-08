Search Engines
==============

Providence features a modular search facility that allows you to choose from several low-level search engines. To support a given search engine you must write a Providence plug-in for it. The plug-in is composed of two classes implementing the IWLPlugSearchEngine and IWLPlugSearchEngineResult interfaces (defined in app/lib/core/Plugins). Each class implments "glue" between Providence and the given search engine. The IWLPlugSearchEngine implementor handles indexing and searches, taking tokens to index and searches to execute, and in the case of executed searches returning the IWLPlugSearchEngineResult implementor.

Query syntax
No matter the back-end search engine, your plug-in is expected to implement the Lucene query syntax. Parsing of this syntax is provided by the Zend PHP implementation of Lucene located in app/lib/core/Zend/Zend_Search.

Available plug-ins
Since all of the available open-source search engines have some disadvantage we want to provide as many options for Providence as possible. The following search engine plugins are in development or planned. Feel free to add your own here!