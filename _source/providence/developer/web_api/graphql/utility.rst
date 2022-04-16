.. _developer_api_graphql_utility:

Utility (endpoint name ``Utility``)
====================================

The utility service offers miscellaneous queries for parsing and validating data. 

The ``splitEntityName`` query exposes CollectiveAccess' internal entity name processing system, providing conversion of text names into field-level components compatible with CA's entity record label format.

This query takes a text name and splits it into prefix, surname and forename. The ``displaynameFormat`` controls how the display text version is formatted. By default display text is the same as the input text, but can be normalized with to ``surnameCommaForename``, ``forenameCommaSurname``, ``forenameSurname``, ``forenamemiddlenamesurname``, or a :ref:`display template <display_templates>`.

.. code-block:: Text
	
	query { 
		splitEntityName(
			name: "Mr. George Tilyou", 
			displaynameFormat: "surnamecommaforename"
		) { 
			surname, 
			forename, 
			middlename, 
			displayname, 
			suffix, 
			prefix  
		}
	}

The ``parseDate`` query parses text dates into numeric intervals and normalized text representations. The interval can be returned in CA's internal "historic" floating point format, or as Unix timestamps. Note that Unix timestamps can only be created for dates on or after January 1, 1970. Historic values are used by default. Set the ``format`` parameter to "unix" to return Unix timestamps. The format of the normalized text date can be controlled using the ``displayFormat`` parameter. Possible values are ``text`` (localized text), ``delimited`` (a date in the format 1/1/2020), ``iso8601``, ``yearOnly`` (only the year no matter how specific the input date is) and ``ymd`` (a date in the form 20200101). By default ``text`` is used. To specify the language of returned text dates set the ``locale`` parameter, as in this query:
	
.. code-block:: text
	
	query { 
		parseDate(
			dates: ["1/1950", "7/20/1969", "1960's"], 
			locale: "en_US"
		) { 
			date,
			start, 
			end, 
			text  
		} 
	}
	
which returns 

.. code-block:: text

	{
		"ok": true,
		"data": {
			"parseDate": [
				{
					"date": "1/1950",
					"start": 1950.0101,
					"end": 1950.0131235959,
					"text": "January 1950"
				},
				{
					"date": "7/20/1969",
					"start": 1969.072,
					"end": 1969.0720235959,
					"text": "July 20 1969"
				},
				{
					"date": "1960's",
					"start": 1960.0101,
					"end": 1969.1231235959,
					"text": "1960s"
				}
			]
		}
	}
	
A single date may be passed as a string using the ``date`` option, if desired.