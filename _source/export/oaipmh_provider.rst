OAI-PMH Provider
================

CollectiveAccess features an implementation of the `OAI Protocol for Metadata Harvesting <http://www.openarchives.org/pmh/>`_ that serves database records using virtually arbitrary XML-based formats. It supports all requests `defined in the protocol <http://www.openarchives.org/OAI/openarchivesprotocol.html#ProtocolMessages>`_ and is made possible through the Data_Exporter framework.

In order to make your data available via OAI-PMH you first have to create at least one XML mapping for the data exporter. Data providers are required to provide at least `Dublin Core <https://en.wikipedia.org/wiki/Dublin_Core>`_ so we suggest you start with that. You can, however, provide any number of formats so long as you create the corresponding export mappings in CollectiveAccess.

For now we assume that you created a mapping with the code 'oai_dc' that describes how your data is mapped to Dublin Core XML. 

oai_provider.conf configuration
-------------------------------

This is the core configuration file for this feature. If you want to provide only one the Dublin Core mapping you just created, you're pretty much good to go with the stock configuration. Just fill in the mapping code. The interesting part of the configuration is under the 'providers' key. Here you can define an arbitrary number of endpoints where harvesters can go and gather your data. You could, for instance, define 1 endpoint for your object/item records and one for your collections. Each of those is a full-fledged standalone OAI-PMH provider accessible via the following URL pattern:

.. code-block:: none

	http://www.mydomain.org/service.php/OAI/<provider_key>

In the default config there's only one provider with the code 'dc'. It can be accessed like so:

.. code-block:: none

	http://www.mydomain.org/service.php/OAI/dc

Within each provider configuration you have a number of available settings. They are described in the table below. 

.. csv-table::
   :header-rows: 1
   :widths: 25, 75, 25
   :file: ../_static/csv/oaipmh_provider_settings.csv

Format Definition
-----------------
The definition of a single format used by a provider configures the exporter mapping that should be used for this format as well as some metadata about the format itself. The type of records served (objects, entities, ...) is defined by the exporter mapping. We strongly recommend not to mix mappings for different types in one provider. If you want to provide, say, your objects and your collections, you should configure 2 separate providers to do this, otherwise harvesters could get inconsistent results for the same identifiers.

The key of the format definition is the so called `metadataPrefix <http://www.openarchives.org/OAI/openarchivesprotocol.html#MetadataNamespaces>`_. It is used to address these formats in OAI-PMH requests (and also for the 'default_format' setting). 

.. csv-table::
   :header-rows: 1
   :widths: 25, 75, 25
   :file: ../_static/csv/oaipmh_format_definition.csv

An example configuration with only one format (metadataPrefix: oai_dc) served by the provider could look like this:

.. code-block:: none

		formats = {
		oai_dc = {
			mapping = ca_objects_oai_dc,
			schema = http://www.openarchives.org/OAI/2.0/oai_dc.xsd,
			metadataNamespace = http://www.openarchives.org/OAI/2.0/oai_dc/,
		}
	},

Testing your setup
------------------
To explore your collection using the OAI-PMH provider you just set up, you can for instance use the `OAI Repository Explorer <http://re.cs.uct.ac.za/>`_ maintained by the University of Cape Town. This tool obviously only works if your provider is accessible online. You can also test the results by accessing provider via the following:

.. code-block:: none

	https://mydomain.com/service.php/OAI/dc?verb=ListRecords&metadataPrefix=oai_dc

Be sure to change out the metadataPrefix if it something other than oai_dc.

DPLA
----
Partner hubs of the `Digital Public Library of America <https://dp.la/>`_ can provide metadata to the DPLA by setting up an OAI-PMH provider servicing data in either DublinCore, MARC, or MODS. Consult with the DPLA for other supported formats, or refer to the DPLA metadata specification crosswalk `here <https://docs.google.com/spreadsheets/d/1BzZvDOf4fgas3TD21xF40lu2pk2XW0k2pTGJKIt6438/edit#gid=1453046017>`_. 