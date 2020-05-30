.. _external_exports:
External Export Framework
=========================

CollectiveAccess can interact with other external systems, including digital preservation and data backup platforms, using the external export framework. The framework provides a pipeline for assembly, packaging and transmission of metadata and media to other applications. A variety of standard formats and protocols are supported and may be mixed and matched to facilitate interoperation.

The framework operates at the record level, creating packages incorporating metadata, media (images, audio, video, documents) and documentation such as checksums and use statements for individual objects, collections and other record types. Record metadata may be generated in any format supported by the :ref:`metadata export system <export_mappings>`, including XML, tab, CSV and MARC. Multiple metadata exports may be included in a single package, as well as all available versions of associated media.

Package formats include interchange standards such as `BagIT <https://en.wikipedia.org/wiki/BagIt>`_ and widely used container formats such as ZIP. Once packages are created, the framework can transfer them to external systems using protocols such as Secure FTP.

The framework is designed to be extensible. It is possible to add support for additional package formats or data transport protocols by creating software plugins.

external_exports.conf configuration
-----------------------------------

Config file details go here