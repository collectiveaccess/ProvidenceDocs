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

The ``parseDate`` query parse text dates into a numeric interval and a normalized text representation. The interval can be returned in CA's internal "historic" floating point format, or as Unix timestamps. Note that Unix timestamps can only be created for dates on or after January 1, 1970. Historic values are used by default. Set the ``format`` parameter to "unix" to return Unix timestamps. The format of the normalized text date can be controlled using the ``displayFormat`` parameter. Possible values are ``text`` (localized text), ``delimited`` (a date in the format 1/1/2020), ``iso8601``, ``yearOnly`` (only the year no matter how specific the input date is) and ``ymd`` (a date in the form 20200101). By default ``text`` is used. To specify the language of returned text dates set the ``locale`` parameter, as in this query:
	
.. code-block:: text
	
	query { 
		parseDate(
			date: "january 1950", 
			locale: "de_DE"
		) { 
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
			"parseDate": {
				"start": 1950.0101,
				"end": 1950.0131235959,
				"text": "Januar 1950"
			}
		}
	}