SQL Search
==========

SQLSearch is an engine that employs regular MySQL tables to create an inverted index stored. This technique was used in the 0.5x version of CollectiveAccess and provided reasonable performance and scalability combined with easy deployment (zero-configuration is required). For version 0.6 and 1.0 alternative engines were explored that leveraged existing code (eg. PHP Lucene, MySQL FULLTEXT, SOLR, etc.). While ultimately workable, none of the other options combine the deployment and performance characteristics of the inverted index approach. Thus, a new Unicode-friendly "SQL Search" plugin has been implemented, as of version 1.1, as an alternative to PHP Lucene and MySQL Fulltext, the other "easy deploy" options. As of version 1.1, SqlSearch is the default search engine option and as of version 1.3 the only supported "easy deploy" option.

Pros: Performance and scalability are generally good; deployment is effortless

Cons: Indexing can be slow; disk space requirements for indices can be large

Status: Implemented