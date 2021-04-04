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

For each table, there is an associative array, with the following keys:

* :ref:`MEDIA_ACCEPT <providenceConfiguration/mainConfiguration/media_processing.conf:MEDIA_ACCEPT>`: Relates mimetypes and media types. Each type of media (Ex. ``image``) may have multiple mimetypes associated with it.
* :ref:`MEDIA_TYPES <providenceConfiguration/mainConfiguration/media_processing.conf:MEDIA_TYPES>`: Describes queueing and available representation versions in different sizes and flavours.
* :ref:`MEDIA_TRANSFORMATION_RULES <providenceConfiguration/mainConfiguration/media_processing.conf:MEDIA_TRANSFORMATION_RULES>`: Describes the rules to apply to transform a representation file.

This is an example of a media processing file:

.. code-block:: text

  ca_object_representations = {
    MEDIA_METADATA = "media_metadata",
    MEDIA_CONTENT = "media_content",

    MEDIA_ACCEPT = {
        image/jpeg     = image,
        image/gif      = image,
        image/png      = image,
        image/tiff     = image,
        image/x-bmp    = image,
        image/x-dcraw  = image,
        image/x-psd    = image,
        image/x-exr    = image,
        image/jp2      = image,

        application/octet-stream = binaryfile
    },
    # ---------------------------------------------------------
    MEDIA_TYPES = {
        image = {
            QUEUE = mediaproc,
            QUEUED_MESSAGE =  _("Image is being processed"),
            QUEUE_USING_VERSION = original,
            VERSIONS = {
                thumbnail = {
                    RULE = rule_thumbnail_image, VOLUME = images,
                    QUEUE_WHEN_FILE_LARGER_THAN = <queue_threshold_in_bytes>
                },
                preview = {
                    RULE = rule_preview_image, VOLUME = images,
                    QUEUE_WHEN_FILE_LARGER_THAN = <queue_threshold_in_bytes>
                },
                original = {
                    RULE = rule_original_image, VOLUME = images,
                    USE_EXTERNAL_URL_WHEN_AVAILABLE = <use_external_url_when_available>
                },
                tilepic = {
                    RULE = rule_tilepic_image, VOLUME = tilepics,
                    QUEUE_WHEN_FILE_LARGER_THAN = <queue_threshold_in_bytes>
                }
            },
            MEDIA_VIEW_DEFAULT_VERSION = tilepic,
            MEDIA_PREVIEW_DEFAULT_VERSION = small
        },
        binaryfile = {
            QUEUE = mediaproc,
            QUEUED_MESSAGE =  _("Image is being processed"),
            QUEUE_USING_VERSION = original,
            VERSIONS = {
                thumbnail = {
                    RULE = rule_thumbnail_image, VOLUME = images, BASIS = large,
                    QUEUE_WHEN_FILE_LARGER_THAN = <queue_threshold_in_bytes>
                },
                preview = {
                    RULE = rule_preview_image, VOLUME = images, BASIS = large,
                    QUEUE_WHEN_FILE_LARGER_THAN = <queue_threshold_in_bytes>
                },
                original 	= {
                    RULE = rule_original_image, VOLUME = images,
                    USE_EXTERNAL_URL_WHEN_AVAILABLE = <use_external_url_when_available>
                }
            },
            MEDIA_VIEW_DEFAULT_VERSION = large,
            MEDIA_PREVIEW_DEFAULT_VERSION = small
        }
    },
    MEDIA_TRANSFORMATION_RULES = {
        # ---------------------------------------------------------
        # Image rules
        # ---------------------------------------------------------
        rule_thumbnail_image = {
            SCALE = {
                width = 120, height = 120, mode = bounding_box, antialiasing = 0
            },
            SET = {quality = 75, format = image/jpeg}
        },
        rule_preview_image = {
            SCALE = {
                width = 180, height = 180, mode = bounding_box, antialiasing = 0
            },
            SET = {quality = 75, format = image/jpeg}
        },
        rule_original_image = {},
        rule_tilepic_image = {
            SET = {quality = 40, tile_mimetype = image/jpeg, format = image/tilepic}
        }
        # ---------------------------------------------------------
    }
  }


MEDIA_ACCEPT
************

One entry per mimetype. Each type of media (Ex. ``image``) may have multiple mimetypes associated with it.

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

Each key is a version descriptor, containing an associative array, with a pointer to
media transformation :ref:`rules <providenceConfiguration/mainConfiguration/media_processing.conf:MEDIA_TRANSFORMATION_RULES>`
that help building a new derivative version of a media file.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: media_processing_versions.csv


MEDIA_TRANSFORMATION_RULES
**************************

Rules that describe how to build a derivative version of a media file. There are
:ref:`operations <media_rules_operations>` on the image and also :ref:`filters <media_rules_filters>`.

It is an associative array of operation keys.

.. _media_rules_operations:

Here it is a listing of available **operations**:

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: media_processing_operation_rules.csv

.. _media_rules_filters:

Here it is a listing of available **filters**.

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: media_processing_operation_filters.csv

