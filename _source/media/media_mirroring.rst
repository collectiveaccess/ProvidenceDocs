Media Mirroring
===============


Mirroring media uploaded to CollectiveAccess via FTP
----------------------------------------------------

All media uploaded to CollectiveAccess are stored locally in web-accessible locations defined in the media_volumes.conf configuration file. This is usually all you need, but there are a few cases where being able to automatically copy – or mirror - media to another server can come in handy:

You want to manage audio or video files in CollectiveAccess locally but stream them from a dedicated audio/video host externally, to save local bandwidth or take advantage of features only streaming hosts can provide.

You want to provide high-availability to media files using multiple servers.

You want to make real-time backups of your media.

CollectiveAccess supports mirroring via FTP ("File Transfer Protocol"). FTP is a standard for moving files between servers on the Internet. When FTP mirroring is enabled, every time you upload a new media file the file and its derivatives will be automatically copied using FTP to one or more remote servers. The copying happens in the background so you need not wait for the file transfers to complete before continuing your work. Files of any size (subject to disk space limitations of the mirror servers, of course) may be mirrored.

.. note::
   The media mirroring system is very old. It was actually part of the 0.5x code
   base and was originally intended to move files to Adobe Flash Streaming Server.

   At the time everyone still used FTP to move files. Now, you'd never do that.
   It's obsolete and should be removed.

Additionally, CA can be configured to automatically use a mirror to serve media internally, if one is available. In this case when a media file is first uploaded it will be served from the local location. Once mirroring is complete (for large files or limited bandwidth connections, this can take a while) CA will automatically shift over to using the mirror.

Note that the CA mirroring system will automatically remove media from mirrors if they are removed from the local system. This prevents waste of disk space on mirror servers. You should not rely upon mirrors for backups of accidentally deleted files. Use a traditional data backup solution instead.

Configuring mirroring
#####################

Mirroring is configured on a per-volume basis. All media written to a mirrored volume are mirrored. If you want to mirror a specific type of file then you should create a separate volume for that type of file and configure the media processing system (in media_processing.conf) to use the volume. The default CA configuration has definitions for media-specific volumes that should work fine for most installations.

Within a given volume, to enable mirroring add a "mirrors" list directive. The mirrors list should contain a series of "mirror codes" (unique alphanumeric identifiers for the mirror that you define), each of which has a list of configuration values for the mirror. A typical mirror setup to mirror all media added to the "images" volume (taken from the CA default configuration) looks like this:

.. code-block:: text

    images = {
        hostname = <site_hostname>,
        protocol = <site_protocol>,
        urlPath = <ca_media_url_root>/images,
        absolutePath = <ca_base_dir>/<ca_media_url_root>/images,
        writeable = 1,
        description = Images,

        accessUsingMirror = my_mirror,

        mirrors = {
            my_mirror = {
                method = ftp,
                hostname = ftp.mysite.org,
                username = my_ftp_login_name,
                password = my_password,
                directory = /usr/home/mysite/public_html/images,
                passive = 1,
                accessProtocol = http,
                accessHostname = www.mysite.org,
                accessUrlPath = /images
            }
        }
    }

Note the ``accessUsingMirror`` directive. This tells CA what mirror to use locally if it
is available. If you omit this directive the mirror will receive files from CA but
will not actually be used by CA to serve media.

For further details about the mirror configuration see
:ref:`FTP Mirror configuration <providenceConfiguration/developer/media_volumes.conf:FTP Mirror configuration>`.

