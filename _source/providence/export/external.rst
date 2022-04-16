.. _external_exports:

External Export Framework
=========================

.. note:: This feature is available from CollectiveAccess version 1.8.

CollectiveAccess can interact with other external systems, including digital preservation and data backup platforms, using the external export framework. The framework provides a pipeline for assembly, packaging and transmission of CollectiveAccess-managed metadata and media to other applications. A variety of standard formats and protocols are supported and may be mixed and matched to facilitate interoperation.

The framework operates at the record level, creating packages incorporating metadata, media (images, audio, video, documents) and documentation such as checksums and use statements for individual objects, collections and other record types. Record metadata may be generated in any format supported by the :ref:`metadata export system <export_mappings>`, including XML, tab, CSV and MARC, and can include metadata from related records. Multiple metadata exports may be included in a single package, as well as any available versions of associated media.

Package formats include interchange standards such as `BagIT <https://en.wikipedia.org/wiki/BagIt>`_ and widely used container formats such as ZIP. Once packages are created, the framework can transfer them to external systems using protocols such as Secure FTP.

The framework is designed to be extensible. It is possible to add support for additional package formats or data transport protocols by creating software plugins.

Configuration
-----------------------------------

Behavior of the external export framework is controlled using `targets`. A target is a set of configuration defining what data is to be exported, how that data is to be packaged, what criteria trigger creation of a package and where packages are ultimately sent. You can configure as many targets as required, each with its own packaging, destinations and other characteristics.

Targets are defined in the `external_exports.conf` configuration file. Each target has a unique code and a dictionary of configuration values. Within the dictionary, a few top-level settings define basic parameters:

.. csv-table::
   :header-rows: 1
   :widths: 30, 45, 25
   :file: external_basic_settings.csv
   
Detailed configuration is contained in three blocks:

* `triggers` defines the criteria that will trigger export of a record to this target.
* `output` defines the data to be exported  


.. code-block:: none

    targets = {
        mods_export_to_sftp_server = {
            label = MODS export,
            enabled = 1,

            table = ca_objects,
            checkAccess = [1],

            triggers = {
                lastModified = {
                    from_log_timestamp = 4/1/2020,
                    #from_log_id = 20000,
                    #query = cooking
                }
            },

            output = {
                format = BagIT,
                name = "EXPORT_^ca_objects.idno",
                content = {
                    mods.xml = {
                        type = export,
                        exporter = mods_exporter_with_guid
                    },
                    . = {
                        type = file,
                        files = {
                            ca_object_representations.media.original = {
                                delimiter = .,
                                components = {^original_filename }
                            }
                        }
                    }
                },
                options = {
                    file_list_template = "^ca_objects.idno, ^filename, ^filesize_for_display, ^mimetype",
                    file_list_delimiter = ";"
                }
            },

            destination = {
                type = sFTP,
                hostname = my-sftp-server@example.net,
                user = my_user,
                password = my_password,
                path = "path/to/where/packages/are/uploaded"
            }
        }
    }


Running an export
-----------------------------------

How to run an export here.

Extending the framework
-----------------------------------

Overview of plugin system here