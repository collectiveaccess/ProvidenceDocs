Media Watermarking
==================

CollectiveAccess can automatically add a visible watermark to image derivatives. The watermark pattern is a graphic provided by you: it can be a logo, text or anything else than can be expressed in a bitmap. Watermarking is applied as derivatives are created. The watermarks are part of the image and cannot be easily removed. (They can be cropped out or Photoshop'ed away, of course, just like anything else in an image).

Requirements
------------

Watermarking is only supported for image formats processed by the ImageMagick, GraphicsMagick
Gmagick, and IMagick media processing plugins. Watermarking is not supported
with GD. If you are having trouble getting watermarking to work make sure your
system is actually using a supported media processing plugin.

Getting started
---------------

Watermarking works by superimposing your watermark image over the image being processed. You can specify the location, size and transparency for the watermark, which gives you some control over how obviously visible the watermark is. If you need to mark images in a way that is detectable but not distracting then a small mostly transparent logo in a corner of the image is probably sufficient. If you want to render images completely unusable for anything but sample purposes a relatively opaque watermark the size of the image itself may be called for.

How the watermark image is defined will greatly affect how well it performs. An effective watermark will be detectable no matter what the image it sits on looks like. As you can imagine, if your watermark image is black text and you superimpose it on a dark region it won't be very noticeable. In practice, simple black text or logo watermarks will be virtually undetectable to all viewers, including you, on dark backgrounds.

To ensure visibility on all backgrounds make sure your watermark image contains both black and white. One effective technique is to take a simple black outline of text or a logo (or both) and give it a white "halo." If you have access to Photoshop you can do this easily by:

1. Open the original outline in Photoshop and select only the content (ie. create a selection that includes only the text or logo, not the white background)/
2. Copy and paste the selection into a new layer behind the original one.
3. Invert the new layer so what was black is now white.
4. Move the new layer down 1 or 2 pixels and to the left 1 or two pixels. (Vary the movement amount and directions to suit your taste).
5. Save this resulting image as a JPG, PNG or TIFF.

Configuration
-------------

Once you have your watermark image ready, the next step is to configure CollectiveAccess to use it. To do so you must edit the media_processing.conf configuration file in app/conf.

You can add watermarking to specific derivatives (or "versions" as they are referred to in the configuration file) by adding a WATERMARK rule to their processing rules.


You should add WATERMARK rule with the appropriate values to each version you want to watermark. A watermark configuration for the "small" version (default 240x240 pixel image) might look like this:


.. code-block:: text

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

See :ref:`Watermarking configuration <media_processing_rule_watermarking>` for details on the configuration options.

.. note::

   WATERMARKing is not supported for ``tilepic`` versions of  images.

