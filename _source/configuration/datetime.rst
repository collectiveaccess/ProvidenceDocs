Datetime.conf
=============

'''In Progress'''

The output, or display, of dates and times inside dateRange metadata elements can be configured in datetime.conf. For valid <em>input</em> formats for dates and times, please visit [[Date_and_Time_Formats|this page.]]

==Date/time output configuration==

In Datetime.conf, you may define common text expressions you wish to have the date/time parser convert to dates. The text expression on the left side of the equal sign must be *all lowercase*; the date/time expression on the right side must be valid and parsable:

<pre>
expressions = {
	us civil war = 1861 to 1865,
	world war 2  = 1939 to 1945,
	nickel empire = 1920s,
}
</pre>

==Output options for date/times==

{| {{PrettyTable}}
|-
||'''Setting'''||'''Description'''||'''Options'''
|-
||dateFormat || Format to use for dates. "Original" is the date as entered by the user; other values will normalize all date/time input to the selected standard format. || Valid values are text, delimited, iso8601, and original. The default is text.
|-
||timeOmit || You may output or omit the time portion of date time expressions.  || 1 (yes) or 0 (no)
|-
||showCommaAfterDayForTextDates || If set to a non-zero value commas are included after the day in a US-style (month first) text date || Default = 0
|-
||timeFormat || Format to use for times. "12" displays as, for example, 3:15 PM, where "24" would display at 15:15PM. || Valid values are 12 and 24. Default = 24.
|-
||useQuarterCenturySyntaxForDisplay || If true dates ranging over uniform quarter centuries, such as 1900-1925 or 1975-2000 will be output in the format "20 Q1" eg. 1st quarter of 20th century, or 1900-1925.|| 1 (yes) or 0 (no)
|-
||useRomanNumeralsForCenturies || If true century only dates (eg "18th century") will be output in roman numerals like "XVIIIth century". || 1 (yes) or 0 (no)
|-
||timeDelimiter || Delimiter in time display; must be valid for the current language or default will be used; Default is first delimiter in language config file. || :
|-
||timeRangeConjunction || Text to put between times in a range; must be valid for the current language or default will be used; default is first in language config. || -
|-
||rangePreConjunction || Text to place before date/times in a range; must be valid for the current language or default will be used. Default is none. || from 
|-
||rangeConjunction ||  Text to place between date/times in a range; must be valid for the current language or default will be used. || to
|-
|| dateTimeConjunction || Text to put between times in a range; must be valid for the current language or default will be used; default is first in language config. || to
|-
||showADEra || If set to a non-zero value the "AD" era will be show for all dates; default is to only show it in ranges that span era || 1 or 0
|-
|| uncertaintyIndicator || Text to use to indicate date is uncertain; must be valid for the current language or default will be used. || circa
|-
|| dateDelimiter || Text to place before date/times in a range; must be valid for the current language or default will be used. Default is none.|| 
|-
|| circaIndicator || Text to place before date/times to indicate it is a "circa", or uncertain, date. Must be valid for the current language or default will be used. || circa
|-
|| beforeQualifier || Text to place before a date/time to indicate that it is no later than the specified date; must be valid for the current language or default will be used. || before/prior to
|-
|| afterQualifier ||  Text to place before a date/time to indicate that it is no earlier than the specified date; must be valid for the current language or default will be used. || after
|-
|| presentDate || Text that represents the current date; must be valid for the current language or default will be used. || today
|}

