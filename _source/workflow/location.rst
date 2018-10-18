Tracking current object location
================================

.. contents::
   :local:   
   
Overview
--------
Prior to version 1.5 collection object location and use history were tracked using standard metadata elements and relationships, in the same ways as other object-level information. Storage locations could be defined hierarchically and objects could be related to specific locations. Additional metadata could be recorded in the object and/or location records. For simple tracking this arrangement worked well enough, but it proved problematic for users seeking to maintain location histories, record complex per-move data (packing, insurance, etc.) or tracking usage across different classes of activity records (eg. loans, exhibitions, conservation, as well as movement). Starting with version 1.5, the available options have been expanded, with specialized tools for tracking location and use history of collection objects. (Of course, existing systems can continue to use the pre-1.5 location tracking methods if they wish.)

One size does not fit all when it comes to location tracking. To handle the range of tracking methodologies required by different types of museum and archival collections CollectiveAccess now offers three different mechanisms to track the location of collection objects:

    - **Direct object-location references.** Location is recorded using relationships between object and storage location records. Relationships are dated, with the most recent date considered "current". This allows construction of simple location histories and is similar to the pre-1.5 method save for the dating.
    - **Movement-based location tracking.** Location is recorded for objects in related movement records. Each movement record records details about a specific change in location for one or more objects. The current location for an object is considered to be the location referred to by the most recent movement by date. Movement of entire storage locations within the location hierarchy can be configured to record a movement, allowing current location tracking based upon individual object moves as well as movements of containers or other storage units.
    - **Workflow-based location tracking.** Location is recorded for an object across a range of record types representing various related activities, including loans, movements, occurrences (typically recording exhibitions), deaccession and location relationships. Locations recorded using direct object-location or movement-based location tracking can be part of the range of data used by to derive current location.

Although it is possible to simultaneously employ more than one of these mechanisms in your system, in general you should choose only one to use.

Which method should I use?
--------------------------
**Direct object-location** reference is the simplest option and is suitable for collections that have fairly uniform location reporting requirements. If everything in your collection has a standard location and there are relatively informal movements of items between locations use this option. Many archives, historical societies and house museums and the like will find this an effective and easy to deploy option.

**Movement-based location tracking** records detailed information about how one or more objects are transferred between locations, in addition to the location history. This option is intended for collections where documenting chain of custody, insurance and packing are critical. This additional documentation comes at the expense of added complexity and additional required data entry. Every movement of an object or group of objects to a new location requires completion of a full movement record. Collections that routinely move valuable, sensitive or fragile materials (fine art museums, artists studios, archives with privacy concerns) may find this option preferable.

**Workflow-based location tracking** is designed for institutions with a robust notion of location and expands upon either of the preceding two options. In contrast with other methods, which all record relationships between objects and locations (with or without movements), workflow-based location tracking takes into consideration several types of records to determine the current location of an object, including direct object-location or movement-based tracking. With this method location can be based upon a combination of reported storage location, occurrence (often an exhibition or event), loan, movement or deaccession. For institutions that often loan or exhibit objects workflow-based tracking can reduce redundant data entry by using the loan or exhibition record itself as documentation of location, rather than requiring hacky double entry and pseudo "loan" or "on exhibit" storage locations. This flexibility comes at the cost of more complex configuration and, potentially, additional required data entry.

For most users direct object-location tracking should be sufficient. Movement-based or workflow-based location tracking should only be considered if you require the specific functionality they provide.
