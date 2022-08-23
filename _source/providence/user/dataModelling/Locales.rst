Locales
=======

* `Locale-specific Information in CollectiveAccess`_ 
* `How Locales are Selected`_ 
* `Translating CollectiveAccess into a New Language`_ 

CollectiveAccess supports localizations of its user interface. It also supports multi-lingual metadata - you can add information translated into many languages to a object or authority record. Whenever a language must be specified, either to indicate how the UI should be localized or what language metadata is in, a locale code is used.

Locale codes are comprised of a two or three character country code taken from the `ISO 639 <http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_ standard and a two character language code taken from the `ISO 3166-1 <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ standard joined together by an underscore ("_") character. For example, English as spoken in the United States is indicated by **en_US**. German as spoken in Germany is indicated by **de_DE**. An optional dialect specifier may also be added following the country and separated with an underscore when sub-divisions of languages must be taken into account. (Note: the dialect specification may be dropped in the future; if you think this should stay let us know.)

**Locale-specific Information in CollectiveAccess**
---------------------------------------------------


Locale-related information is stored into three places within CollectiveAccess:


* The list of locales for which CollectiveAccess can accept cataloguing is stored in the *ca_locales* table in the database. *ca_locales&* records simply contain the language, country and dialect codes along with a unique, compact integer identifier that is used internally to represent the locale.
* Localized text for the user interface is stored in `GNU GetText <http://www.gnu.org/software/gettext/>`_ -compatible .po files in the *app/locale/<locale_code>* directory (for example: *app/locale/en_US*). Note that not all locales present in the *ca_locales* table will have localization files in *app/locale*, but that all locales *'with*' localization files will have a corresponding record in *ca_locales*.
* Configuration specifying how date/time expressions are parsed and presented for a given locale are stored in *app/lib/core/Parsers/TimeExpressionParser* When creating a new locale it is best to clone an existing locale file and alter it to suit the new locale.
* CollectiveAccess uses Zend_Locale (from the `Zend Framework <http://framework.zend.com/>`_) to manage other localization data (number formats, country and language names and the like). The data is stored in *app/lib/core/Zend/Locale/Data* in files using standard locale codes.

**How Locales are Selected**
----------------------------

Each CollectiveAccess user may select a preferred locale for their user interface; the list of locales is limited to those for which a user interface translation exists in *app/locale*. The selected locale is used not only for the user interface but also, when possible, for displayed content. That is, CollectiveAccess will always try to display catalogued data in the user's preferred UI locale. If catalogue data is not available in the user's selected language then CollectiveAccess will attempt to display the data using one of the system default locales, as set in the global.conf configuration file. The default locales will be used in order of listing until catalogue data is found. If no catalogue data exists for the default locales, CollectiveAccess will display data in whatever locale *does* exist.

**Translating CollectiveAccess into a New Language**
----------------------------------------------------

For information on how to translate CollectiveAccess into a language for which a translation does not yet exist, see the the page on creating `Translations <file:///Users/charlotteposever/Documents/ca_manual/providence/developer/translation.html?highlight=translations>`_.
