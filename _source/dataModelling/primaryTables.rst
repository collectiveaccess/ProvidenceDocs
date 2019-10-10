.. _primary_tables:

Primary Tables
==============

.. contents::
   :local:
   :depth: 1

CollectiveAccess is structured around several primary tables, with editors that can be enabled (or disabled) depending on project requirements. Each primary table has intrinsic bundles and its own set of preferred and non-preferred labels bundles. Distinct user interfaces can be configured for each table, and within that, a single table can have multiple user interfaces restricted by Type (see Types).

Editors that are not relevant for your system (you don't catalogue places for example) can be disabled in the configuration file app.conf, by setting the various \*_disable directives below to a non-zero value

Here's how it looks in app.conf:

.. code-block:: none

	# Editor "disable" switches
	# -------------------
	ca_objects_disable = 0
	ca_entities_disable = 0
	ca_places_disable = 0
	ca_occurrences_disable = 0
	ca_collections_disable = 0
	ca_object_lots_disable = 0
	ca_storage_locations_disable = 0
	ca_loans_disable = 0
	ca_movements_disable = 1
	ca_tours_disable = 1
	ca_tour_stops_disable = 1
	ca_object_representations_disable = 1

Objects (ca_objects)
^^^^^^^^^^^^^^^^^^^^
Object records represent items or assets in a collection, typically the physical or born-digital items being managed. Every object record has a "type" that determines which fields are relevant for it. The list of types available in your system can be customized to match your specific cataloging requirements.

Object intrinsics (ca_objects)
******************************

.. csv-table::
   :widths: 15, 25, 40, 5, 5
   :header-rows: 1
   :file: intrinsics_objects.csv

Object Lots (ca_object_lots)
^^^^^^^^^^^^^^^^^^^^^
Lots record the accession or acquisition of one or more objects. Lots are commonly used by collecting institutions who may accession more than one unique item per accession. Registrarial information, such as the Deed of Gift, may be recorded in a lot record while  cataloging for each accessioned object remains at the object level. 

Object lot intrinsics (ca_object_lots)
**************************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_object_lots.csv

Entities (ca_entities)
^^^^^^^^^^^^^^^^^^^^^^
Entity records represent specific people and organizations. Relationships can be created between entity and object records (or any other records in any other table) with fully customizable relationship types. For example, an entity record for an individual could be related to an object record as the creator of the object, or the photographer, donor, publisher, performer, etc.

Entity intrinsics (ca_entities)
*******************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_entities.csv

Places (ca_places)
^^^^^^^^^^^^^^^^^^
Place records represent physical locations, geographic or otherwise. Places are inherently hierarchical allowing you to nest more specific place records within broader ones. As with entities, places can be related records in other tables. Places are typically used to model location authorities specific to your system. For cataloguing of common geographical place names consider using CollectiveAccess' built-in support for GoogleMaps, OpenStreetMap, GeoNames and/or the Getty Thesaurus of Geographic Names (TGN).

Place intrinsics (ca_places)
****************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_places.csv

Occurrences (ca_occurrences)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Occurrences are used to represent temporal concepts such as events, exhibition, productions or citations. 

Occurrence intrinsics (ca_occurrences)
**************************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_occurrences.csv

Collections (ca_collections)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Collections represent significant groupings of objects. They may refer to physical collections, symbolic collections of items associated by some criteria, or any other grouping. Collection records are often used to manage formal archival processing and the creation of finding aids, by configuring records to be compliant with the Describing Archives (DACS) content standard.

Collection intrinsics (ca_collections)
**************************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_collections.csv
   
Storage Locations (ca_storage_locations)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Storage location records represent physical locations where objects may be located, displayed or stored. Like place records, storage locations are hierarchical and may be nested to allow notation location at various levels of specificity (building, room, cabinet, drawer, etc.). As with the other primary tables, each storage location may have arbitrarily rich cataloguing, including access restrictions, geographical coordinates, keywords and other information. 

Storage location intrinsics (ca_storage_locations)
**************************************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_storage_locations.csv

Loans (ca_loans)
^^^^^^^^^^^^^^^^
Loan records record details of both incoming and outgoing loans of objects. Loan records, like those in all other tables, is fully customizable and can be used to track alls aspects of a loan, including dates, shipping, and insurance information. 

Loan intrinsics (ca_loans)
**************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_loans.csv

Movements (ca_movements)
^^^^^^^^^^^^^^^^^^^^^^^^
For more complex location tracking needs, movement records can be used to record in precise detail movement of objects between storage locations, while on loan or while on exhibition. Used as part of a location tracking or use history policy, movements can provide a robust record of every movement event in an object's history.

Movements intrinsics (ca_movements)
***********************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_movements.csv

Object Representations (ca_object_representations)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Representations capture representative digital media (images, video, audio, PDFs) for objects. Representation records usually contain only just a media file, but can accommodate  additional cataloguing that is specific to the media file (not to the object the file depicts or represents) if desired. When used. representation metadata often includes captions, credits, access information, rights and reproduction restrictions.

Object representation intrinsics (ca_objects_representations)
*************************************************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_object_representations.csv

Tours (ca_tours)
^^^^^^^^^^^^^^^^
Tour records capture information about on-site or online tours of objects, locations, collections or any other record in the database. 

Tour intrinsics (ca_tours)
**************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_tours.csv

Tour Stops (ca_tour_stops)
^^^^^^^^^^^^^^^^^^^^^^^^^^
Each tour record has any number of ordered "stops". Each tour stop contains metadata about the stop (descriptive text, geographic coordinates, etc.) as well as relationships to relevant objects, entities and more.

Tour stop intrinsics (ca_tour_stops)
************************************

.. csv-table::
   :widths: 20, 15, 40, 10, 10
   :header-rows: 1
   :file: intrinsics_tour_stops.csv
