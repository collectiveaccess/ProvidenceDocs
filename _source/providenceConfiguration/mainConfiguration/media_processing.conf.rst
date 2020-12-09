Media_processing.conf
=====================

The file defines the media processing rules to transform media representations to
different media transformations.

It is a standard CollectiveAccess configuration file using the :ref:`common configuration syntax <configuration_file_syntax>`.

CollectiveAccess supports media processing configuration for representations of
the following items:

- representations (*ca_object_representations, ca_object_representation_multifiles*)
- attribute values (*ca_attribute_value_multifiles*)
- icons (*ca_icons*)
- user comments media (*ca_item_comments_media*)
- representation annotation previews (*ca_representation_annotation_previews*)

You may specify accepted media types, and different versions for the transformations, using rules.

Common configuration
--------------------

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: media_processing_top_level.csv


Organization
------------

At the top level, media_processing.conf is structured as a series of blocks,
one for each type of item to be processed:

- representations (*ca_object_representations, ca_object_representation_multifiles*)
- attribute values (*ca_attribute_value_multifiles*)
- icons (*ca_icons*)
- user comments media (*ca_item_comments_media*)
- representation annotation previews (*ca_representation_annotation_previews*)

There is an associative array per table, with the following keys:

* MEDIA_ACCEPT: Relates mimetypes and media types.
* MEDIA_TYPES: Describes queueing and available representation versions in different sizes and flavours.
* MEDIA_TRANSFORMATION_RULES: Describes the rule to apply to transform a representation file.

MEDIA_ACCEPT
************

One entry per mimetype.

.. code-block:: text

    mimetype = media_type


MEDIA_TYPES
***********

Each key is a media type descriptor, containing an associative array with queueing and
representation version descriptions.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: media_processing_media_type.csv

VERSIONS
********

Each key is a version descriptor, containing an associative array.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: media_processing_versions.csv

