Installing on Windows
=====================

Installation of media handling libraries and delegates such as ffmpeg can be problematic because it is more difficult to build software from source on Windows. See Compiling_ffmpeg for information how to install ffmpeg for Windows.

The format of the `/app/conf/External_Applications.conf` file is different in Windows installations. For example, the correct format for the entry describing the ghostscript application is

``ghostscript_app = E:/prog/gs/gswin32c.exe``

in this case, ghostscript is installed on disk E: in the subdirectory `prog/gs`. The application is the non-windows version of ghostscript.

The `app/helpers/mediaPluginHelpers.php` file must also be updated to function properly in Windows. The entry for ghostscript must be changed from

``exec($ps_path_to_ghostscript." -v 2> /dev/null", $va_output, $vn_return);``

to

``exec($ps_path_to_ghostscript." -v 2> /$null", $va_output, $vn_return);``

Similarly, all other media helper functions to detect the other processors you have installed for CA to used must be updated to change `/dev/null` to ``/$null``.

Other places that have `/dev/null` include

TilePicParser in `\app\lib\core\parsers` CoreImage.php in `\app\lib\core\Plugins\Media ImageMagick.php` in `\app\lib\core\Plugins\Media PDFWand.php` in `\app\lib\core\Plugins\Media`

references to /dev/null must be changed to ``/\$null`` in order for the plugin to work correctly. This is particularly important if you are using ImageMagic. Both ImageMagick.php and TilePicParser.php must be changed for this process to work.

The `external_applications` line for ImageMagick might be

``imagemagick_path = E:/Prog/ImageMagick``

depending on where you have installed ImageMagick. Both the static and dynamic versions of ImageMagick seem to work well.

The ImageMagick process is very slow and libGD is preferred for speed, but it requires much more memory. If you are using it locally where you have control over the memory size, up the memory limit entry of php.ini to

memory_limit = 512M

This will allow must photographs to be handled properly without the tilepic function running out of memory.