Importing media embedded metadata
=================================

CollectiveAccess can extract and import EXIF, IPTC, XMP and technical metadata embedded in uploaded image, video, audio and document files. Import of embedded metadata can be performed on media uploaded as object representations individually in the record editor interface or in batches using the media importer.

Transformation and import of media embedded metadata employs the import system used for import of data files in various XML and delimited file formats. Crosswalks between embedded metadata extracted from media and CollectiveAccess records are specified using the same import mapping format used for general data import. 

Data is extracted from media using the standard `MediaInfo <https://mediaarea.net/en/MediaInfo>`_ and `ExifTool <https://exiftool.org>`_ applications. When using MediaInfo, extracted metadata is presented for import as `PBCore <https://pbcore.org>`_ version 2.0 XML. When using ExifTool, data is presented as nested value tags. Creation of mappings for the import of output from these tools into CollectiveAccess is described in detail below.

MediaInfo is an excellent tool for extracting embedded descriptive and technical metadata from audio and video files, but returns limited metadata for images and documents. ExifTool returns comprehensive data for images, but may not capture all aspects of time-based media. Therefore you may wish to employ ExifTool for some types of media and MediaInfo for others. CollectiveAccess can be configured to automatically choose one over the other for specific file types, or to let the user decide which to use. You can also specify import mappings for specific media formats.

Installing required software
----------------------------

You will need to have MediaInfo and/or ExifTool installed on your server. Both applications are packaged for easy installation on most Linux distributions and the MacOS. 

To install on RedHat/CentOS 7.x or 8.x:

.. code:: bash

    yum install mediainfo exiftool

On Ubuntu/Debian 18.04lts:

.. code:: bash

    apt install mediainfo exiftool

On MacOS (assuming you have the `Homebrew <https://brew.sh>`_ package manager installed:

.. code:: bash

    brew install mediainfo exiftool
    
Once installed, make sure the installed paths to the applications are set in your :ref:`external_applications.conf <external_applications_conf>` configuration file.

The metadata extraction process
-------------------------------

When a media file is uploaded to CollectiveAccess a sequence of processing steps are performed that result in the originally uploaded media file and a series of derivatives included in the database. Once processing is complete, extraction of embedded metadata is performed, if configured, on the originally uploaded media. Depending upon the mapping specified for the uploaded media, either MediaInfo or ExifTool are run on the uploaded media file.

When MediaInfo is used, the command-line ``mediainfo`` command is used with options to output extracted metadata as PBCore v2.0 XML. The command used is ``mediainfo --Output=PBCore2 <filename>``, where <filename> is the path to a media file to analyze. You can use this command on the server command-line with selected files to get an idea of the format and structure of the data to be mapped.

Typical MediaInfo PBCore XML output will resemble this example:

.. code:: bash

    <?xml version="1.0" encoding="UTF-8"?>
    <!-- Generated at 2020-04-20T19:43:25Z by MediaInfoLib - v19.09 -->
    <pbcoreInstantiationDocument
        xsi:schemaLocation="http://www.pbcore.org/PBCore/PBCoreNamespace.html https://raw.githubusercontent.com/WGBH/PBCore_2.1/master/pbcore-2.1.xsd"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns="http://www.pbcore.org/PBCore/PBCoreNamespace.html">
        <instantiationIdentifier source="File Name">Self_Portrait_1969_sRGB.tif</instantiationIdentifier>
        <instantiationDate dateType="file modification">2020-04-06T17:56:20Z</instantiationDate>
        <instantiationDimensions unitsOfMeasure="dpi">800.000x800.000</instantiationDimensions>
        <instantiationDigital>image/tiff</instantiationDigital>
        <instantiationStandard>TIFF</instantiationStandard>
        <instantiationLocation>Self_Portrait_1969_sRGB.tif</instantiationLocation>
        <instantiationMediaType>Static Image</instantiationMediaType>
        <instantiationFileSize unitsOfMeasure="byte">42993144</instantiationFileSize>
        <instantiationTracks>1</instantiationTracks>
        <instantiationEssenceTrack>
            <essenceTrackType>Image</essenceTrackType>
            <essenceTrackIdentifier source="StreamKindID (MediaInfo)">0</essenceTrackIdentifier>
            <essenceTrackEncoding annotation="endianness:Big compression_mode:Lossless">Raw</essenceTrackEncoding>
            <essenceTrackBitDepth>8</essenceTrackBitDepth>
            <essenceTrackFrameSize>3200x4475</essenceTrackFrameSize>
            <essenceTrackAnnotation annotationType="Title">&quot;Steve McQueen / Self-Portrait, 1969 / Oil on canvas (in artist&apos;s frame) / 34 x 24 in. (86.3 x 60.9 cm) / Studio #: / Studio binder: Paintings 1969-1970  / Date of photography: / Original photography: 4x5 Transparency&quot;</essenceTrackAnnotation>
            <essenceTrackAnnotation annotationType="ColorSpace">RGB</essenceTrackAnnotation>
        </instantiationEssenceTrack>
        <instantiationAnnotation annotationType="Image_Codec_List">Raw</instantiationAnnotation>
        <instantiationAnnotation annotationType="Encoded_Application_CompanyName">EPSON</instantiationAnnotation>
        <instantiationAnnotation annotationType="Encoded_Application_Name">Adobe Photoshop 21.0 (Macintosh)</instantiationAnnotation>
    </pbcoreInstantiationDocument>

ExifTool is run with the command-line ``exiftool`` command and the ``-json`` (output in JSON format), ``-g1`` (group data under headings), ``-a`` (include all data) options. To simulate this on the server command-line use the command ``exiftool -json -a -g1 <filename>`` where <filename> is the path to a media file to analyze.

Typical ExifTool output with these options should resemble this example:

.. code:: bash

    [{
      "SourceFile": "/Users/ca/Desktop/images/Self_Portrait_1969.tif",
      "ExifTool": {
        "ExifToolVersion": 11.85
      },
      "System": {
        "FileName": "Self_Portrait_1969.tif",
        "Directory": "/Users/ca/Desktop/images",
        "FileSize": "41 MB",
        "FileModifyDate": "2020:04:06 13:56:02-04:00",
        "FileAccessDate": "2020:04:06 13:56:41-04:00",
        "FileInodeChangeDate": "2020:04:06 13:56:41-04:00",
        "FilePermissions": "rw-r--r--"
      },
      "File": {
        "FileType": "TIFF",
        "FileTypeExtension": "tif",
        "MIMEType": "image/tiff",
        "ExifByteOrder": "Big-endian (Motorola, MM)",
        "CurrentIPTCDigest": "bfdbbc3492d748bae59a045d52eedeb8"
      },
      "IFD0": {
        "SubfileType": "Full-resolution Image",
        "ImageWidth": 3200,
        "ImageHeight": 4475,
        "BitsPerSample": "8 8 8",
        "Compression": "Uncompressed",
        "PhotometricInterpretation": "RGB",
        "ImageDescription": "Self-Portrait, 1969\nOil on canvas (in artist's frame)\n34 x 24 in. (86.3 x 60.9 cm)\nStudio #:\nStudio binder: Paintings 1969-1970 \nDate of photography:\nOriginal photography: 4x5 Transparency",
        "Make": "EPSON",
        "Model": "Expression 12000XL",
        "StripOffsets": 26316,
        "Orientation": "Horizontal (normal)",
        "SamplesPerPixel": 3,
        "RowsPerStrip": 4475,
        "StripByteCounts": 42960000,
        "XResolution": 800,
        "YResolution": 800,
        "PlanarConfiguration": "Chunky",
        "ResolutionUnit": "inches",
        "Software": "Adobe Photoshop 21.0 (Macintosh)",
        "ModifyDate": "2020:04:06 12:11:15",
        "Copyright": "Permission to reproduce photography must be obtained from the Artist"
      },
      "XMP-x": {
        "XMPToolkit": "Adobe XMP Core 5.6-c148 79.164036, 2019/08/13-01:06:57        "
      },
      "XMP-xmp": {
        "CreatorTool": "Adobe Photoshop 21.0 (Macintosh)",
        "MetadataDate": "2020:04:06 12:11:15-04:00",
        "CreateDate": "2020:02:05 10:46:06-05:00",
        "ModifyDate": "2020:04:06 12:11:15-04:00"
      },
      "XMP-xmpMM": {
        "DocumentID": "adobe:docid:photoshop:da4cff7b-7f92-de48-9b5a-715bbdf53797",
        "OriginalDocumentID": "4F5F926FB3F7A36F7B9C01E4FE4BDF17",
        "InstanceID": "xmp.iid:d8d49b93-b505-47f1-ae50-1c6197730444",
        "HistoryAction": ["saved","saved","saved","saved","saved","saved","saved"],
        "HistoryInstanceID": ["xmp.iid:67850da4-0379-454a-a635-93c142bcbae3","xmp.iid:77751899-131d-4f7e-a84f-f104200b29ad","xmp.iid:5a1611bc-1e40-488b-b6cd-29a4dd54c2e8","xmp.iid:967f9e41-0541-4afb-9907-5a9f41452a94","xmp.iid:be011035-f7b0-49d9-a712-e25b503e07f4","xmp.iid:90d2ed31-ee25-4fd5-b2a4-0ad3a1ee1b92","xmp.iid:d8d49b93-b505-47f1-ae50-1c6197730444"],
        "HistoryWhen": ["2020:02:05 11:27:06-05:00","2020:02:05 11:28:12-05:00","2020:02:13 16:42:20-05:00","2020:02:13 16:53:13-05:00","2020:04:02 10:24:09-04:00","2020:04:06 12:11:15-04:00","2020:04:06 12:11:15-04:00"],
        "HistorySoftwareAgent": ["Adobe Photoshop Camera Raw 12.1","Adobe Photoshop Camera Raw 12.1 (Macintosh)","Adobe Photoshop 21.0 (Macintosh)","Adobe Photoshop 21.0 (Macintosh)","Adobe Bridge 2020 (Macintosh)","Adobe Photoshop 21.0 (Macintosh)","Adobe Photoshop 21.0 (Macintosh)"],
        "HistoryChanged": ["/metadata","/metadata","/","/","/metadata","/","/"]
      },
      "XMP-dc": {
        "Format": "image/tiff",
        "Description": "Self-Portrait, 1969\nOil on canvas (in artist's frame)\n34 x 24 in. (86.3 x 60.9 cm)\nStudio #:\nStudio binder: Paintings 1969-1970 \nDate of photography:\nOriginal photography: 4x5 Transparency",
        "Subject": ["Painting","Self-Portrait"],
        "Title": "Self-Portrait, 1969",
        "Rights": "Permission to reproduce photography must be obtained from the Artist"
      },
      "XMP-photoshop": {
        "Credit": "© The Artist",
        "Source": "The Studio",
        "ColorMode": "RGB",
        "ICCProfileName": "Adobe RGB (1998)",
        "CaptionWriter": "Willie Mays",
        "History": "2020-04-06T12:03:13-04:00\tFile Self_Portrait_1969.tif opened\n2020-04-06T12:11:15-04:00\tFile Self_Portrait_1969.tif saved\n"
      },
      "XMP-xmpRights": {
        "Marked": true
      },
      "IPTC": {
        "CodedCharacterSet": "UTF8",
        "ApplicationRecordVersion": 4,
        "Caption-Abstract": "Self-Portrait, 1969\rOil on canvas (in artist's frame)\r34 x 24 in. (86.3 x 60.9 cm)\rStudio #:\rStudio binder: Paintings 1969-1970 \rDate of photography:\rOriginal photography: 4x5 Transparency",
        "Writer-Editor": "Willie Mays",
        "Credit": "© The Artist",
        "Source": "The Studio",
        "ObjectName": "Self-Portrait, 1969",
        "Keywords": ["Painting","Self-Portrait"],
        "CopyrightNotice": "Permission to reproduce photography must be obtained from the Artist"
      },
      "Photoshop": {
        "IPTCDigest": "bfdbbc3492d748bae59a045d52eedeb8",
        "XResolution": 800,
        "DisplayedUnitsX": "inches",
        "YResolution": 800,
        "DisplayedUnitsY": "inches",
        "PrintStyle": "Centered",
        "PrintPosition": "0 0",
        "PrintScale": 1,
        "GlobalAngle": 30,
        "GlobalAltitude": 30,
        "CopyrightFlag": true,
        "URL_List": [],
        "SlicesGroupName": "Self_Portrait_1969",
        "NumSlices": 1,
        "PixelAspectRatio": 1,
        "PhotoshopThumbnail": "(Binary data 3973 bytes, use -b option to extract)",
        "HasRealMergedData": "Yes",
        "WriterName": "Adobe Photoshop",
        "ReaderName": "Adobe Photoshop 2020"
      },
      "ExifIFD": {
        "ExifVersion": "0231",
        "ColorSpace": "Uncalibrated",
        "ExifImageWidth": 3200,
        "ExifImageHeight": 4475
      },
      "ICC-header": {
        "ProfileCMMType": "Adobe Systems Inc.",
        "ProfileVersion": "2.1.0",
        "ProfileClass": "Display Device Profile",
        "ColorSpaceData": "RGB ",
        "ProfileConnectionSpace": "XYZ ",
        "ProfileDateTime": "2000:08:11 19:51:59",
        "ProfileFileSignature": "acsp",
        "PrimaryPlatform": "Apple Computer Inc.",
        "CMMFlags": "Not Embedded, Independent",
        "DeviceManufacturer": "none",
        "DeviceModel": "",
        "DeviceAttributes": "Reflective, Glossy, Positive, Color",
        "RenderingIntent": "Perceptual",
        "ConnectionSpaceIlluminant": "0.9642 1 0.82491",
        "ProfileCreator": "Adobe Systems Inc.",
        "ProfileID": 0
      },
      "ICC_Profile": {
        "ProfileCopyright": "Copyright 2000 Adobe Systems Incorporated",
        "ProfileDescription": "Adobe RGB (1998)",
        "MediaWhitePoint": "0.95045 1 1.08905",
        "MediaBlackPoint": "0 0 0",
        "RedTRC": "(Binary data 14 bytes, use -b option to extract)",
        "GreenTRC": "(Binary data 14 bytes, use -b option to extract)",
        "BlueTRC": "(Binary data 14 bytes, use -b option to extract)",
        "RedMatrixColumn": "0.60974 0.31111 0.01947",
        "GreenMatrixColumn": "0.20528 0.62567 0.06087",
        "BlueMatrixColumn": "0.14919 0.06322 0.74457"
      },
      "Composite": {
        "ImageSize": "3200x4475",
        "Megapixels": 14.3
      }
    }]


.. _import_mediaembeddedmetadata:

Creating mappings
-----------------

Import of media embedded metadata is managed through the same `import mapping <file:///Users/charlotteposever/Documents/ca_manual/providence/user/import/c_creating_mapping.html>`_ system used for import of stand-alone datasets. All standard options are available when performing an import of embedded metadata. Embedded imports are always performed in the context of ``ca_object_representations`` records, and any relationships generated will be relative to the object representation record housing the imported media.

MediaInfo
*********

PBCore XML data generated by MediaInfo is passed verbatim to the data importer. The required mapping is identical in format to that used for import of stand-alone PBCore v2.0 XML documents. As with all  :ref:`XML-based formats <import_formats>` XPath is used reference to specific elements within the XML. Note that XPath expressions should omit the ``pbcoreInstantiationDocument`` root tag. For example, to reference the ``essenceTrackType`` value in the example above use ``/instantiationEssenceTrack/essenceTrackType``.

Mappings for MediaInfo-based metadata extraction must include ``mediainfo`` in their ``inputFormats`` setting.

:download:`Sample MediaInfo mapping <mediainfo.xlsx>`


ExifTool
********

JSON output generated by ExifTool is converted by CollectiveAccess into a pseudo XML file using group headers ("IPTC", "XMP-photoshop" and others in the example above) as top-level tags and sub-entries as second-level tags. For example, to reference the XMP Dublin Core description value in the example above use ``/XMP-dc/Description``.

Mappings for ExifTool-based metadata extraction must include ``exif`` in their ``inputFormats`` setting.

:download:`Sample ExifTool mapping <exiftool.xlsx>`

Common EXIF fields and their importer source references:

.. csv-table::
   :widths: 20, 20, 25, 35
   :header-rows: 1
   :file: exiftool_source_reference_list.csv

CollectiveAccess configuration
------------------------------

User interface and logging aspects of the import process can be configured using directives in the :ref:`app.conf <app_conf>` configuration file.

Users can select the import mapping they wish to use at the time of upload in the editing
and batch media importer interfaces when ``allow_user_selection_of_embedded_metadata_extraction_mapping`` is set to
a non-zero value. 

When allowing user selection of mappings, ``allow_user_embedded_metadata_extraction_mapping_null_option`` can be set to
include a "no import" option. Setting this option to zero effectively forces import of embedded metadata in all cases.

If it often desirable to have CA automatically select import mappings based upon the format of the uploaded file. 
The ``embedded_metadata_extraction_mapping_defaults`` setting can be used to map  media file MIME types to mappings. MIME types may be
specific (Ex. image/tiff for TIFF format images) or cover entire classes using wildcards (Ex. image/* for images of any type).

.. code-block:: none

    embedded_metadata_extraction_mapping_defaults = {
        video/* = example_mediainfo_mapping,
        image/* = example_exif_tool_mapping,
        application/pdf = pdf_metadata_import
    }

The values are the right side of the map must be valid data import mapping codes, as defined in the ``code`` setting of a mapping worksheet.

How much information is logged when performing an embedded metadata import can be controlled using the ``embedded_metadata_extraction_mapping_log_level``
setting. Valid values are DEBUG, NOTICE, INFO, WARN, ERR, CRIT and ALERT, where DEBUG logs the most (sometimes too much) information, and levels beyond ERR log only
the most critical errors. It is generally best to leave this setting on DEBUG when testing and use NOTICE or INFO if DEBUG is providing too much information. 