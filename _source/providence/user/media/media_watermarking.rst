Media Watermarking
==================

* `Creating a Watermark`_
* `Configuring a Watermark in CollectiveAccess`_ 

Watermarks are usually a transparent stamp, logo, or or signature that has been superimposed onto an existing image. Thus, they are considered part of an image, and cannot be easily removed (they can be cropped out or Photoshopped away). CollectiveAccess can automatically add a visible watermark to image derivatives. The watermark pattern is a graphic provided by the user; it can be a logo, text or anything else that can be expressed in a bitmap format. Watermarking is applied as derivatives are created. 

Watermarking is only supported for image formats processed by the ImageMagick and IMagick media processing plugins. Watermarking is not supported with GD. 

Creating a Watermark
---------------

Watermarking works by superimposing a watermark image over the image being processed. The location, size, and transparency of the watermark can be customized. Watermarks work for a variety of image purposes: to mark images in a detectable, but not distracting, way; or, to render sample images with more opaque watermarks. 

How the watermark image is defined will greatly affect how well it performs. An effective watermark will be detectable no matter what the image it sits on looks like. To ensure visibility on all backgrounds, make sure your watermark image contains **both black and white**. One effective technique is to take a simple black outline of text or a logo (or both) and give it a white "halo." If you have access to Photoshop you can do this easily by:

1. Open the original outline in Photoshop and select only the content (ie. create a selection that includes only the text or logo, not the white background). 
2. Copy and paste the selection into a new layer behind the original one.
3. Invert the new layer so what was black, is now white.
4. Move the new layer down 1 or 2 pixels and to the left 1 or two pixels. (Vary the movement amount and directions to suit your taste).
5. Save this resulting image as a JPG, PNG or TIFF.

Configuring a Watermark in CollectiveAccess
-------------------------------------------

To configure a watermark in CollectiveAccess, use the `media_processing.conf <https://manual.collectiveaccess.org/providence/user/configuration/mainConfiguration/media_processing.conf.html>`_ configuration file in **app/conf**.

Add watermarking to specific image derivatives (or "versions" as they are referred to in the configuration file) by adding a WATERMARK rule to their processing rules.

The WATERMARK rule takes the following parameters:

.. csv-table:: 
   :header-rows: 1
   :file: watermarking_newtable1.csv

Add a WATERMARK rule, with the appropriate values, to each version that will contain a watermark. A watermark configuration for the "small" version (default 240x240 pixel image) might look like this:

.. code-block:: php

    rule_small_image = {
        SCALE = {
             width = 240, height = 240, mode = bounding_box
        },
        WATERMARK = {
             image = <ca_app_dir>/watermarks/my_watermark_logo.png,
             width = 72, height = 85, position = south_east, opacity = 0.4
        },
        SET = {quality = 75, format = image/jpeg}
    }

The non-WATERMARK rules are just the default rules; only WATERMARK is new. The configuration above assumes that the **my_watermark_logo.png** image file is located in a directory called **watermarks** in the CollectiveAccess *app/directory*.

.. note::

   WATERMARKing is not supported for ``tilepic`` versions of  images.

