Datetime.conf
=============

The output, or display, of dates and times inside dateRange metadata elements can be configured in datetime.conf. For valid *input* formats for dates and times, please visit the **Date and Time Formats** page.

Date/time output configuration
------------------------------

In Datetime.conf, you may define common text expressions you wish to have the date/time parser convert to dates. The text expression on the left side of the equal sign must be *all lowercase*; the date/time expression on the right side must be valid and parsable:

.. code-block:: none

	expressions = {
		us civil war = 1861 to 1865,
		world war 2  = 1939 to 1945,
		nickel empire = 1920s,
	}

Output options for date/times
-----------------------------

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/e/2PACX-1vQsZ2Tigx07LC0JcH-aHA98B3nQ5TMuwlXS80ukxsKGzVD_TPmFjc98dmZ2sFLzXEFUVdDB3U5ZtL9f/pub?output=csv