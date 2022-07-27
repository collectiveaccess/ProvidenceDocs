Translation
===========

* `Components of a Translation`_ 
* `Editing User Interface Text`_ 
* `Legacy Way`_
* `Creating a Localization File for the date/time Parser`_ 
* `Localizing an Installation Profile`_ 
* `Installation-Specific Translations`_ 
* `Translating Pawtucket`_ 
* `Sharing Your Translation`_ 

Modern  versions of CollectiveAccess, version 1.0 and later are designed to be fully localizable.
We are working to get CA translated for use in as many languages and locales as possible.
If you wish to help us translate CA into your language,  email us at info@collectiveaccess.org

To learn more about the mechanics of creating a new translation, read on.

Components of a translation
###########################

Translating CollectiveAccess into your own language requires that you translate three distinct sets of text:

* **User interface text**: like other localizable applications, CollectiveAccess has a list of text messages ("strings") that require translation. These messages are presented to users while the application runs and do not vary from installation to installation and configuration to configuration. Therefore **all** users of CollectiveAccess who speak a given language can benefit from a user interface text translation for that language.
* **Date/time parser settings**: the date and time parser – the piece of code that interprets and outputs dates – has its own language specific settings that must be defined in a translation. These settings include not only translations of the months of the year and other date-related text, but also locale-specific values that affect the formatting and presentation of dates. As with user interface text, these settings are generally useful to all speakers of a language. They do not vary between configurations.
* **Installation profiles**: profiles contain installation-specific configuration information about every data element in your system, as well as controlled lists, relationship qualifiers and more. The names, descriptions and values of these configuration elements are translated into your target language within the profile, and then loaded into the database at installation time. Since configuration profiles are often specific to a single user (or group of users), they usually contain only the language(s) used by the author. This means that even if there already exists user interface and data/time parser translations for your target language, it is likely you will still have to translate your desired installation profile.

The default language used in CollectiveAccess code is English, so all user interface text translations are from English to the target language. Similarly date/time parser settings are usually translated using the English settings file as a starting point. Pre-made installation profiles are in the preferred language of the author. All standards-based profiles created by the CollectiveAccess project use English.

Editing user interface text
###########################

CollectiveAccess uses the `Gnu GetText <http://www.gnu.org/software/gettext/>`_ system for managing translations of user interface text. GetText stores both original English-language messages as well as translations in an editable file with the **.po** extenson. Using a special utility one can convert the **.po** file for use in the running application as an **.mo** file. Note that only **.po** files are editable. **.mo** files are derivatives designed for optimal performance.

User interface translations are stored in the *app/locale* directory. Each specific locale (a "locale" is the combination of a language and a culture) is represented with a directory. Inside each directory are two files: **messages.po** and **messgages.mo**

For editing translations, we are using online tool `Transifex <https://www.transifex.com/collectiveaccess/collectiveaccess-providence/app-locale-messages-pot--develop/>`_, where you can submit translations (and later review them).
If your language or language variant is not enabled on Transifex, write us to info@collectiveaccess.org and we will create it.
After translation completion contact us, and  we will copy translation to application sources.

Legacy way
**********

You can also create translation without usin online tools.
If you are starting a new translation you need to do the following:

#. Decide what the locale code of your translation is. For example, if you are writing a translation specifically for use in Flemish-speaking Belgium then you would probably want to use the locale nl_BE. If it is a more general Dutch translation, then nl_NL is probably more appropriate (of course, an nl_NL translation already exists!) Note that the language always comes first and is lower case. The country comes second and is always upper-case. The language codes should adhere to the ISO-639-1 standard.
#. Create a directory in *app/locale* for your new locale.
#. Copy the *messages.po* file from the en_US directory to your new locale directory.
#. Correct settings for language variant - language name, & plural forms.
#. Open and edit *messages.po* using a GetText-compatible editor such as `Poedit <http://www.poedit.net>`_ and translate each English string into your target language. If using POEdit, the *.mo* file will be automatically created or updated every time you save your *.po* file.


Creating a localization file for the date/time parser
#####################################################

The next step is to localize the date/time parser. To do so copy the English language date/time parser settings file in *app/lib/core/Parsers/TimeExpressionParser/en_US.lang* to a file with your locale in the name in *app/lib/core/Parsers/TimeExpressionParser* and edit to suit. The file includes comments describing the meaning and format of various settings.

Localizing an installation profile
##################################

At this point you have a translated application. You still need a translated configuration, however. If you decide to use an existing [[installation_profile]] as the basis of your system then you will likely need to edit the profile adding localized text as needed. All display text in a profile is tagged with a locale string and supports specification of multiple locales. Simply add your translation alongside the existing text tagged with your selected locale.

Installation-specific translations
##################################

In some cases the terminology used in the translations in *app/locales* are not quite what you want. Naturally, you can modify the terms used in the locale files to suit your purposes. However, this approach comes with a problem: you risk losing your changes when updating your CollectiveAccess installation, as the standard locale files in the update will overwrite your changes.

To avoid this problem, CollectiveAccess supports installation-specific locale files. Simply create a directory for your locale in *app/locales/user* and use it to house your custom *messages.po* and *messages.mo*. CollectiveAccess will always use an installation-specific locale, when present, in preference to the standard locale files.

Translating Pawtucket
#########################

Pawtucket uses a similar system for localization. It has locale files in *app/locale* and date/time parser settings in *app/lib/core/Parsers/TimeExpressionParser*.

Sharing your translation
########################

We invite you to submit your translations for inclusion in the CollectiveAccess software distribution! If you wish to contribute please contact us at support@collectiveaccess.org, or create Pull Request on `github <https://github.com/collectiveaccess/providence>`_.
