Content Caching Configuration
=============================

This configuration file is specific to the Pawtucket public web front-end application, and defines where and how to cache the output of specific controller actions. By capturing and reusing the output of various actions, it is possible to greatly increase the performance of Pawtucket, especially on installations with heavy traffic. 

Since caching simply "replays" previous output, only cache those actions whose output for a given set of inputs is invariant over a predictable period of time. For example, a home page that changes every two hours is a good candidate for caching. A page displaying detailed information for a collection object that changes every few days or months is also a good candidate. A page of randomly selected objects that changes on every load is not. Pages that depend upon user state (the user's previous actions on the site) are also not good candidates for caching, as the cached content cannot take into account the state of different users.

How to Use
----------

For each action you wish to enable caching for, you must define an entry in the cached_actions list below. Each key in cached_actions is a controller path (module path + controller). The value for each controller path is a list of actions, each of which has defined caching settings.

The following caching settings are defined:

* **lifetime**: the number of seconds before cached data expires and is removed from the cache; if you don't define this the default of 120 seconds will be used. See this value to be as large as is possible, but low enough that changes to the page will be reflected in the cache in a reasonable amount of time. For pages that change infrequently a value of 14400 (4 hours) or so is a reasonable value.
* **parameters**: a list of request parameters that will be used to generate the key for the cached content; this list ALL parameters that are required to uniquely identify unique content.

Directives
----------

To Come 
