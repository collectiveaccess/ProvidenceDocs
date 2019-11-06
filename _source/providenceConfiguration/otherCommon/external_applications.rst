External_applications.conf
==========================

Several components of CollectiveAccess employ external applications to perform various tasks. Typically these tasks relate to conversion and reformatting of uploaded media (images, video, audio, etc.) and indexing of text embedded in uploaded files.

The *external_applications.conf* file defines the locations of these applications on your server. If an application location is set incorrectly or the application is not installed then the functionality provided by the application will not be available within CollectiveAccess.

The locations you set should be absolute paths to the directory or executable (as specified below) in the standard format for your OS (Unix paths or Windows paths).

Directives
----------
The following entries may be defined in this configuration file. Note that there are no default values for entries in *external_applications.conf*. You must define a value for all applications you wish to use.

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: External_applications.csv