ElasticSearch
=============
ElasticSearch is a simple, fast and increasingly popular search engine.

Pros: Performance and scalability are very good

Cons: Requires you to run an ElasticSearch installation, which means running a Java application stack. This is often not an option for installations with limited IT resources.

About ElasticSearch
ElasticSearch is an an Open Source (Apache 2), Distributed, RESTful, Search Engine built on top of Apache Lucene. CollectiveAccess added support in v1.3 and completely overhauled the plugin again in v1.6. It now uses the official ElasticSearch PHP API and no longer requires running a script to maintain the field mapping for the search engine.

Note that CollectiveAccess v1.6 only supports ElasticSearch 2.0 or higher!

Setup
Please refer to the ElasticSearch website for installation and setup notes. Prebuilt packages are available for apt/dpkg on Debian/Ubuntu, yum on CentOS/RedHat or homebrew on Mac OS X, and probably your favorite package manager too!

Once you have ElasticSearch set up, you will have to set aside an index for CollectiveAccess to use. By default that index is called "collectiveaccess" but that can be changed in the search.conf configuration file if you want to use one ElasticSearch setup for multiple CollectiveAccess instances. You also have to configure the communication endpoint you want CollectiveAccess to use. If you're running ElasticSearch locally with the default settings, the default values in the config file should work as is: localhost and port 9200.

search_elasticsearch_base_url = http://localhost:9200/
search_elasticsearch_index_name = collectiveaccess
Interaction with the CollectiveAccess Providence Installer
CollectiveAccess will try to maintain the mapping automatically and it uses a few local caches to do so. When running the installer, these cache interactions can get a little wonky and lead to seemingly random exceptions and errors. Try to make sure you delete your ElasticSearch index and clear all local caches (by deleting the contents of app/tmp) before you run the installer if you have CollectiveAccess configured to use ElasticSearch before you install.

You could also run the installer using SqlSearch and then switch to ElasticSearch later. Remember to reindex your database contents after you switch.

Operation
The v1.6 implementation of the ElasticSearch Plugin should take care of mapping maintenance automatically. If you see mapping exceptions piling up in the ElasticSearch log, that's probably because you've changed things in search_indexing.conf.

One common problem is having different analyzer/tokenizer settings for the same field in different contexts. For instance, you could have ca_object_lots.idno_stub indexed for ca_objects with no additional settings but then use INDEX_AS_IDNO and BOOST when indexing it for ca_object_lots. ElasticSearch doesn't like that. Try streamlining these settings so that they're the same for every occurrence of a field in search_indexing.conf. The default config that ships with Providence should be fine but if you have local changes, keep an eye on the ElasticSearch log and change your indexing config accordingly.