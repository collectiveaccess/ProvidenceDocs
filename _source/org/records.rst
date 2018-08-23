Primary Tables
==============

CollectiveAccess is structured around several primary tables with editors that can be enabled (or disabled) depending on project requirements. Distinct User Interfaces can be configured for each table, and within that, a single table can have multiple user interfaces restricted by Type (see Types).

If you're not using certain editors in your system (you don't catalogue places for example), you can disable the menu items for them in the configuration file app.conf, by setting the various *_disable directives below to a non-zero value

Here's how it looks in app.conf:

.. code-block:: none

	#Editor "disable" switches
	#-------------------
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
Object records represent the items or assets in a collection, typically the physical or born-digital items you are managing. Objects can refer to anything - historical artifacts, photographs, film, video, documents, and artwork. Every object record is by definition, of a "Type." The types themselves can be customized to match your own cataloging requirements.

Entities (ca_entities)
^^^^^^^^^^^^^^^^^^^^^^
Entity records represent the authority file for specific people and organizations. When Entity records are created, relationships can be created between them and specific Object records (or any other Table) with fully customizable relationship types. For example, an Entity authority record for an individual could be related to an Object record as the creator of the Object, the photographer, donor, publisher, performer, or anything else. 

Places (ca_places)
^^^^^^^^^^^^^^^^^^
Physical locations, geographic or otherwise. Places are inherently hierarchical allowing you to nest more specific Place records within broader ones. As with Entities, once a Place is created it can be related to any other kind of record.

Occurrences (ca_occurrences)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Events or “things.” An Occurrence is a catch-all term used by CollectiveAccess to refer to contextual items that may require complex cataloguing but are not Entities, Places, Collections or Storage Locations. You can use Occurrences to support structured authorities for virtually any kind of item. Typically, Occurrences are used to support entries for historical events, exhibitions, works, productions, and bibliographies.

Collections (ca_collections)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Collections contain a defined group of objects. Collections can represent physical collections, symbolic collections of items associated by some criteria, or any other arbitrary grouping. This table can also be used to manage formal archival processing and the creation of finding aids, by configuring the Collection User Interface to be compliant with the Describing Archives (DACS) content standard.

Lots (ca_object_lots)
^^^^^^^^^^^^^^^^^^^^^
Lots represent the accession or acquisition of one or more assets. The details and terms of a gift, purchase, or bequest are recorded here. This table is most commonly used by collecting institutions who may accession more than one unique item per Accession. At the Lot level, all of the registrarial information, such as the Deed of Gift, may be recorded, while individual cataloging of the accessioned items can remain at the Object level. And, as always, the Lot record can be related to each Object.

Storage Locations (ca_storage_locations)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Physical locations where Objects are stored. Like Places, Storage Locations are hierarchical – you can nest Locations to allow notation at any level of specificity (building, room, cabinet, drawer). Each Storage Location can take arbitrarily complex cataloguing, including access restrictions, map coordinates and other information. Storage Locations can be linked to both Objects and Lots, either directly, or through Movements.

Loans (ca_loans)
^^^^^^^^^^^^^^^^
Loans are used to track objects that are on loan to or from other institutions. The Loan table, like all other tables, is fully customizable, and can be used to track every aspect of either an incoming or outgoing loan's dates, shipping, and insurance information. Objects included in the Loan are related to the Loan record in the same manner as Collections, Entities, Lots, etc.

Movements (ca_movements)
^^^^^^^^^^^^^^^^^^^^^^^^
For more complex workflow needs, this table can be used to Movements of Objects (e.g., temporary locations, storage rehousing, transport for exhibition, etc). Used in conjunction with Location Tracking and Object Use History, Movements can enable a robust record of every movement event in an object's lifecycle.

Tours (ca_tours)
^^^^^^^^^^^^^^^^

Tour Stops (ca_tour_stops)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Representations (ca_object_representations)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This table captures the Media (images, video, audio, PDFs) that represents an Object. While Representations most often consist of just the media file itself, they can take additional cataloguing that is specific to the media file (and not necessarily to the Object the file depicts or represents). This allows the addition of captions, credits, access information, rights and reproduction restrictions or any other type of information on a Representation-specific basis, if needed.

