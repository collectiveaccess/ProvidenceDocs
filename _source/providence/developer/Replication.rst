Replication
===========

* `Usage`_ 
* `Settings for Targets`_ 
* `Running the Replicator`_ 
* `Protocol`_ 
* `Replication Service`_ 
* `Implementation Details`_ 

Replication, available from CollectiveAccess Version 1.7, allows for the replication of data from one CollectiveAccess system to another. To do so, CollectiveAccess will use a specialized version of the `Web Service API <https://manual.collectiveaccess.org/providence/developer/web_service_api.html>`_. 

Usage
-----

The replicator can be run on either the source or target system, or even on a "neutral" third system. All communication is done via RESTful HTTP web services. The configuration for the replicator is **replication.conf.** Essentially, it has two big arrays: "sources" and "targets". 

.. note:: Unlimited sources and targets can be configured. To understand the implications, please take a look at the "Protocol" section below.

An example for a working configuration could look like this:

.. code-block:: php
   
   sources = {
	test = {
		url = http://sync.dev/,
		service_user = admin,
		service_key = dublincore,
		from_log_timestamp = 2016-03-29,

		skipIfExpression = {
			ca_objects = "^ca_objects.type_id !~ /image/",
		}
	}
   }

   targets = {
	test = {
		url = http://providence.dev/,
		service_user = admin,
		service_key = dublincore,

		setIntrinsics = {
			__default__ = {
				ca_objects = {
					source_id = external
				}
			},
			29f91051-3833-4e45-892e-7e833d9af4f0 = {
				ca_objects = {
					source_id = internal
				}
			}
		}
	}
   }

Typically, exactly one source and one target will be defined; however, the syntax allows defining several of each. 
Individual settings are described in the table below; both example systems below have the name/code **"test"**. 

.. csv-table:: 
   :header-rows: 1
   :file: replication_table1.csv


.. note:: For the push_media setting to work, the source needs a copy of the same **replication.conf** that's being used by the replicator (which can be anywhere). This is so that we don't have to send target login credentials from the replicator to the source. The target is being identified by its code in replication.conf. With this feature enabled, source(s) could potentially be used for denial of service attacks. Only enable this if you're sure you need it.

Settings for Targets
--------------------

For the replication process to pull media through, set **allow_fetching_of_media_from_remote_urls** to 1 in **app.conf**. The default is 0.

.. csv-table:: 
   :header-rows: 1
   :file: replication_table2.csv

Running the Replicator
----------------------

Once replication.conf is set up, the replicator can be run. It is recommended to keep a backup of the target system(s) at hand while you play around with the configuration. Selectively rolling back changes made by the sync is not possible at the moment.

The replicator is a simple script in caUtils:

``support/bin/caUtils replicate-data``

It will create a log file in the location specified in replication.conf.

Protocol
--------

The rough protocol outline is as follows. For each combination (sources and targets), adhere to the following:

* Get the system guide for source
* Get the last replicated log id for source at target, if any
* Determine log start point for source and target (take into account "from_log_timestamp" or "from_log_id" settings
* Get log from s.getlog -- taking into account both skipIfExpression and the above log start point
* If no (new) log entries found, abort
* Forward that log to t.applylog -- also passing s.guid and setIntrinsics for that system
* Check over results 

Replication Service
-------------------

All communication is done via the newly implemented replication service. It facilitates both the "source" and the "target" functionality through these endpoints. Note that all the names are case-insensitive. Their CamelCase equivalents will work just as well.

``GET getlog``

returns the change log for that system. Parameters are:

.. code-block:: php

   from (int) = log_id to start from
   limit (int) = limit to this many entries
   skipIfExpression (string) = json-encoded skipIfExpression config fragment (see above)

The response body is the JSON-encoded change log

``GET getsysguid``

Returns the system GUID for this target or source. the response body will have the GUID under the "system_guid" key. 

.. code-block:: php

   GET getlastreplicatedlogid

Returns the last replicated log ID for a given source at that particular target system. this parameter is mandatory:

.. code-block:: php

   system_guid (string) = system GUID for the source system

The log id will be under under the "replicated_log_id" key in the response body 

.. code-block:: php
   
   GET getlogidfortimestamp

Translates a given timestamp into a log id for that system. this facilitates the functionality for the "from_log_timestamp" (see above). There is one mandatory parameter:

.. code-block:: php

   timestamp (int) = the Unix timestamp to translate

The log id will be under the "log_id" key in the response body.

.. code-block:: php

   POST applylog

Apply the given log at the target system. takes the log (in the exact format returned by "getlog" as request body. Also has: 

.. code-block:: php

   system_guid (string) = system GUID of the source system, mandatory
   setIntrinsics (string) = JSON-encoded config fragment for the setIntrinsics functionality (see above)

Will return the last replicated log_id under the "replicated_log_id" key in the response body and any warnings as array under the "warnings" key. 

.. code-block:: php

   POST dedup

Run deduplication for a given list of tables. There is one mandatory parameter:

.. code-block:: php

   tables (string) = JSON-encoded config list of tables to run deduplication on, mandatory

Implementation Details
----------------------

The main functionality of the feature is in the **getlog** and **applylog** functions. 

**Getlog**

The actual implementation is not in the ReplicationService, but in *ca_change_log::getLog()*. For the most part, it just gets the change log from the given start point, and pulls in *ca_change_log_snapshots* and *ca_change_log_subjects* for each of the resulting rows. It then goes through some lengths to make these records useful for sync by adding GUIDs for all system-specific *_id columns.

It also processes the skipIfExpression rules. They're applied to the change log subjects for each change log entry. The whole change log entry is skipped if the expression (and the table) matches for one of the subjects.

**Applylog**

The ReplicationService will pull the log out of the request body and apply some basic sanity checks. It'll also figure out if setIntrinsics was set and prepare that as an option to pass to the change log entry implementations.
It then loops through the log entries and calls *CA\Sync\LogEntry\Base::getInstance()* for each of the entries. That class method will return one of the Implementations of *CA\Sync\LogEntry\Base*, based on what kind of record that log entry represents:

.. code-block:: php

   Attribute -- ca_attributes
   AttributeValue -- ca_attribute_values
   Bundleable -- something like ca_objects
   Label -- something like ca_object_labels
   Relationship -- something like ca_objects_x_occurrences

It will then call apply() on the log entry object. Each row is processed in a transaction, which is rolled back if the log entry object throws an Exception. Because of the interdependencies between the log entries, not everything will be processed at once. 


