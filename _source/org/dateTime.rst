Date and Time Formats
=====================

CollectiveAccess can process dates and times in a variety of formats. Internally, CA represents date/times as a range with a beginning and an end. This means that your dates can be as precise or imprecise as necessary. For example, 2007, June 2007, June 7 to June 10 2007 and June 7 2007 are all valid dates. They are stored internally as

    - January 1 2007 @ 00:00:00am - December 31 2007 @ 12:59:59pm
    - June 1 2007 @ 00:00:00am - June 30 2007 @ 12:59:59pm
    - June 7 2007 @ 00:00:00am - June 10 2007 @ 12:59:59pm
    - June 7 2007 @ 00:00:00am - June 7 2007 @ 12:59:59pm

respectively.

The actual low-level storage format represents dates as a pair of numbers representing the start and end of a date range rather than text. This allows CA to properly search and sort dates no matter what format and language is used to enter them. It also allows CA to impose a standard display format on dates regardless of their original input format and to re-format and translate dates on the fly without requiring changes to your underlying data.

Languages and Localization
^^^^^^^^^^^^^^^^^^^^^^^^^^

Date/time expressions are output in the users' current locale language. Language specific settings are defined in TimeExpressionParser locale configuration files stored in app/lib/core/Parsers/TimeExpressionParser

Configuration
^^^^^^^^^^^^^

It is possible to configure how dates and times are parsed and displayed using the datetime.conf configuration file

Valid input formats
^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :widths: auto
   :header-rows: 0
   :file: ../_static/csv/valid_input_formats.csv

For numeric dates (eg. 6/7/2007) multiple delimiters are supported. For example, in the US localization the following dates are all valid and equivalent:

 6/7/2007

 6-7-2007

 6.7.2007

 7-JUN-2007

 7-JUN-07

Dates with times
^^^^^^^^^^^^^^^^

You can specify a time for any date by following the date with a time expression. Both 24 hour and 12 hour (AM/PM) times are supported, and you can specify times to the minute or second. For readability you can optionally separate the date and time with a separator. For the US localization allowable separators are:

  at, @


.. csv-table::
   :widths: auto
   :header-rows: 0
   :file: ../_static/csv/dates_with_times.csv

If you omit the time then a time is assumed depending upon whether the date is the beginning, end or both of a date range. For dates at the beginning of a range, the default time is 00:00:00 (midnight). For dates at the end of a range the default time is 11:59:59pm. This means that if you input a date without a time the entire day is encompassed.

The elements of a time specification may be delimited in multiple ways. For the US localization the following delimiters are supported:

.. code-block:: none

   :
   .

Thus the following times are valid and equivalent:

 4.15:05pm

 16.15.05

 4:15:05pm

 16:15:05

You can also enter date/times in ISO 8601 format. Note that CollectiveAccess has no provision for recording time zones. All times are assumed to be in the same time zone and any time zone information in ISO-format dates is currently discarded (this may change in a future release).

Date ranges
^^^^^^^^^^^

You can specify a date range by inputting two dates (with or without times) separated by a range separator. For the US localization, the range separators are:

 to, -, and, .., through

For readability you can also include an optional range indicator before the first date. For the US localization range indicators are:

 from, between

Examples of date ranges:

 June 5, 2007 - June 15, 2007

 Between June 5, 2007 and June 15 2007

 From 6/5/2007 to 6/15/2007

 6/5/2007 @ 9am .. 6/5/2007 @ 5pm

 6/5 .. 6/15/2007  (Note implicit year in first date)

 6/5 at 9am - 5pm (Note implicit date in current year with range of times)

Special expressions
^^^^^^^^^^^^^^^^^^^

There are a number of shorthand expressions for common dates. Examples below are for the English localization, but all localizations support them:

 today (current date to the day)

 yesterday (yesterday's date to the day)

 tomorrow (tomorrow's date to the day)

 now (current date/time to the second)

 1990's (decade)

 199- (AACR2 format decade)

 20th century (century)

 19-- (AACR2 format century)

Uncertain dates
^^^^^^^^^^^^^^^

You can express uncertain dates in two ways:

    Preface the date with a "circa" specifier (in English, use "circa", "c" or "ca").
    Add a question mark ("?") to the end of the date

For example:

 circa 1955

 ca June 1865

 May 2 1921?

As of version 1.1 you can also use "circa" with date ranges:

 circa 1950 - 1956

Imprecise dates
^^^^^^^^^^^^^^^

"Circa" indicates merely that the date is not precisely known. It does not convey an information about the margin of error of the date estimate. If you want to specify a numeric margin of error for a date/time us expressions such as these:

 June 10 1955 ~ 10d (June 10th 1955 plus or minus 10 days)

 1955 ~ 3y (1955 plus or minus 3 years)

Eras
^^^^

All dates are assumed to be in the Common Era (CE) unless otherwise specified. In the English localization you can specify a date before the Common Era by appending "BCE":

 850 BCE

You may also append "CE" for common era dates if you wish. The English localization also supports use of "AD" and "BC" Other localizations may use different modifiers.

Year-less dates
^^^^^^^^^^^^^^^

It is possible to enter dates that lack years if needed. Year-less dates are restricted to delimited date format input and are available at the month and month/day level:

 6/10/????

 6/????

Note that any number of question marks will create a valid date/time.

Seasonal dates
^^^^^^^^^^^^^^

As of version 1.1 of CollectiveAccess, seasonal dates are supported. Simply enter the name of the season optionally followed by a year (the current year is assumed if there is no year input), and CollectiveAccess will convert the date to numbers. In the English locale, valid seasonal input might include:

 Summer 2011

 Fall 2009

These expressons map to specific dates, June 21 2011 to September 20 2011 for Summer for example.

Quarter-century dates
^^^^^^^^^^^^^^^^^^^^^

Ranges of years falling on quarter centuries may be input as century/quarter pairs. For example:

 20 Q3

is equivalent to 1950 - 1975 (3rd quarter of 20th century). Quarter century expressions are always in the Common Era. They cannot be used for BC dates.

Undated
^^^^^^^
You may indicate a date-less item using "undated" or "unknown" (in the standard English translation, at least). "Undated" date expressions imply the absence of date, and are not searchable. They exists only to indicate that no date is known.
