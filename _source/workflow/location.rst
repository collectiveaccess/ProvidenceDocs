Tracking current object location
================================

.. contents::
   :local:   
   
Overview
--------
By default, Storage locations can be defined hierarchically and objects can be related to specific locations. Additional metadata can be recorded in the object and/or location records. For simple tracking this arrangement works well enough, but it can be limiting for users seeking to maintain location histories, record complex per-move data (packing, insurance, etc.) or tracking usage across different classes of activity records (eg. loans, exhibitions, conservation, as well as movement). Therefore, there are specialized tools for tracking location and use history of collection objects.

One size does not fit all when it comes to location tracking. To handle the range of tracking methodologies required by different types of museum and archival collections CollectiveAccess now offers three different mechanisms to track the location of collection objects:

    - **Direct object-location references.** Location is recorded using relationships between object and storage location records. Relationships are dated, with the most recent date considered "current". This allows construction of simple location histories. It is basically the default functionality of creating relationships between objects and storage locations, but with date tracking built in.
    - **Workflow-based location tracking.** Location is recorded for an object across a range of record types representing various related activities, including loans, movements, occurrences (typically recording exhibitions), deaccession and location relationships. Locations recorded using direct object-location or movement-based location tracking can be part of the range of data used to derive current location. Use this method if your location tracking needs extent to tables beyond simply storage locations - e.g. Loans and Exhibitions.
    - **Movement-based location tracking.** Location is recorded for objects in related movement records. Each movement record records details about a specific change in location for one or more objects. The current location for an object is considered to be the location referred to by the most recent movement by date. Movement of entire storage locations within the location hierarchy can be configured to record a movement, allowing current location tracking based upon individual object moves as well as movements of containers or other storage units. This is the most complicated method to configure and is probably overkill for all but the most complex projects. It is recommended that you use this method only if a) you need to capture complex metadata about a given movement action, beyond simply recording updated locations for objects and b) if several objects at once can be moved within a single "movement" action. 

Although it is possible to simultaneously employ more than one of these mechanisms in your system, in general you should choose only one to use.

Which method should I use?
--------------------------
**Direct object-location** reference is the simplest option and is suitable for collections that have fairly uniform location reporting requirements. If everything in your collection has a standard location and there are relatively informal movements of items between locations use this option. Many archives, historical societies and house museums and the like will find this an effective and easy to deploy option.

**Workflow-based location tracking** is designed for institutions with a robust notion of location. In contrast with other methods, which all record relationships between objects and storage locations (with or without movements), workflow-based location tracking also takes into consideration several different types of records to determine the current location of an object, including occurrences (often an exhibition or event), loans, or deaccessions. For institutions that often loan or exhibit objects, workflow-based tracking can reduce redundant data entry by using the loan or exhibition record itself as documentation of location, rather than requiring hacky double entry and pseudo "loan" or "on exhibit" storage locations. This flexibility comes at the cost of more complex configuration and, potentially, additional required data entry.

**Movement-based location tracking** records detailed information about *how* one or more objects are transferred between locations, in addition to the location history. This option is intended for collections where documenting chain of custody, insurance and packing are critical. This additional documentation comes at the expense of added complexity and additional required data entry. Every movement of an object or group of objects to a new location requires completion of a full movement record. Collections that routinely move valuable, sensitive or fragile materials (fine art museums, artists studios, archives with privacy concerns) may find this option preferable.


For most users direct object-location tracking should be sufficient. Movement-based or workflow-based location tracking should only be considered if you require the specific functionality they provide.
