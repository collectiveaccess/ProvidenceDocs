Browse.conf
===========

CollectiveAccess includes a configurable *Browse Engine* that powers all faceted browse and search features. The engine is capable of browsing for, and returning sets of, any of the primary item types: objects, object lots, entities, places, occurrences, collections and storage locations. The engine automatically caches both results and generated facet content to improve performance. If two users perform the same browse, results for the second browse will be picked up from the cache saving time. Similarly, facet content, which is often costly to generate, is shared across similar browses increasing responsiveness.

Current use
-----------
Faceted browse is currently used in the Providence (back-end) "Find" interfaces for all primary item types. It is also used to provide browse services in the Pawtucket public-access front-end.

Configuration
-------------
Any intrinsic field (ie. a field that is always part of an item such as extent and extent_units in object lots), metadata attribute or related authority may be used for browsing. Since every deployment of CA is different, and the metadata schema varies from one installation to another, you must tell the browse engine what sorts of information you want to be browse-able and how that data should be displayed to the user. This is done by modifying the browse configuration file in *app/conf/browse.conf.* As with all other CA configuration files, *browse.conf* is written using the standard CA configuration syntax.

.. csv-table::
   :widths: 12, 32
   :header-rows: 1
   :file: ../_static/csv/browse1.csv

For each item type you want to be browse-able, you must define a top-level key with the item's table name (eg. ca_objects for objects) and a associative array value. The array must contain a facets key whose value is in turn an associative array defining each available browse facet for the item type. The keys of the facets array are arbitrary code name for the facets – it doesn't matter what they are so long as they are unique within the facet list. The values are yet another associative array which actually defines the characteristics of the facet.

Each facet has a type and some (but not all) of the facet definition keys are dependent upon this type. The follow types of facets are currently supported:

.. csv-table::
   :widths: 12, 32
   :header-rows: 1
   :file: ../_static/csv/configuration_browse_conf_supported_facets_table.csv

For all types of facets the following configuration keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/browse3.csv

For facets of type **authority** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/browse4.csv

For facets of type **field** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/browse5.csv

For facets of type **fieldList** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/browse6.csv

For facets of type **normalizedDates** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/configuration_browse_conf_normalizedDates_table.csv

For facets of type **attribute** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/browse8.csv

For facets of type **label** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/browse9.csv

For facets of type **has** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/browse10.csv

For facets of type **dupeidno** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/configuration_browse_conf_dupeidno_table.csv

For facets of type **location** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/configuration_browse_conf_locations_table.csv


For facets of type **violations** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/configuration_browse_conf_violations_table.csv

For facets of type **checkouts** these additional keys are defined:

.. csv-table::
   :widths: 12, 32, 12
   :header-rows: 1
   :file: ../_static/csv/configuration_browse_conf_checkouts_table.csv

Browse results when no criteria are defined
-------------------------------------------
By default the browse will not return results if you attempt to execute a browse with no criteria defined. In principle, a criteria-less browse should return all possible results – every item in your database. However, for most data sets such a result set would be of limited use and slow to render. In most CA Providence and Pawtucket implementations, a special "start browsing" display is used when no criteria are defined.

If you really do want all results returned when no criteria are defined you can force it on a per-table basis by setting show_all_for_no_criteria_browse in the table-level block (the one that must contain the facets list). See the ca_objects block in the example below to see how this is done.

Avoiding Cache Confusion
------------------------
Browse results are cached for a period of time defined by the cache_timeout value in your browse configuration. Once cached, a browse result will be reused until it expires, even if you change your browse configuration in the meantime. This has the effect of making it almost impossible to experiment with browse configuration while caching is enabled. If you are developing or debugging a browse configuration, be sure to set cache_timeout to zero while you're working. Once your browse is working as you want it to re-enable the cache by setting the timeout to a reasonable value. Caching significantly improves overall performance so you'll probably want it enabled for every day use.

Example Configuration
---------------------
A working browse.conf should look something like this:

.. code-block:: none

	# Browse configuration

	# number of seconds to keep cached browses around
	# set to 0 to disable caching
	cache_timeout = 60

	# Configuration for object browse
	ca_objects = {
			show_all_for_no_criteria_browse = 1,
		facets = {
			entity_facet = {
				# 'type' can equal authority, attribute, fieldList, normalizedDates
				type = authority,
				table = ca_entities,
				relationship_table = ca_objects_x_entities,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [surname, forname],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(entity),
				label_plural = _(entities)
			},
			place_facet = {
				type = authority,
				table = ca_places,
				relationship_table = ca_objects_x_places,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(place),
				label_plural = _(places)
			},
			collection_facet = {
				type = authority,
				table = ca_collections,
				relationship_table = ca_objects_x_collections,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(collection),
				label_plural = _(collections)
			},
			occurrence_facet = {
				type = authority,
				table = ca_occurrences,
				generate_facets_for_types = 1,
				relationship_table = ca_objects_x_occurrences,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(occurrence),
				label_plural = _(occurrences)
			},
			term_facet = {
				type = authority,
				table = ca_list_items,
				relationship_table = ca_objects_x_vocabulary_terms,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(term),
				label_plural = _(terms)
			},
			type_facet = {
				type = fieldList,
				field = type_id,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(type),
				label_plural = _(types)
			},
			object_subtype_facet = {
				type = attribute,
				element_code = object_subtypes,

				requires = type_facet,
				group_mode = alphabetical,

				label_singular = _("Sub-Type"),
				label_plural = _("Sub-Types")
			},
			status_facet = {
				type = fieldList,
				field = status,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(status),
				label_plural = _(statuses)
			},
			access_facet = {
				type = fieldList,
				field = access,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(access status),
				label_plural = _(access statuses)
			},
			date_facet = {
				type = normalizedDates,
				element_code = creation_date,

				# 'normalization' can be: years, decades, centuries
				normalization = years,
				sort_by = [name],
				group_mode = none,

				indefinite_article = a,
				label_singular = _(year),
				label_plural = _(years)
			}
		}
	}

	# Configuration for object lot browse
	ca_object_lots = {
		facets = {
			entity_facet = {
				# 'type' can equal authority, attribute, fieldList, normalizedDates
				type = authority,
				table = ca_entities,
				relationship_table = ca_object_lots_x_entities,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [surname, forname],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(entity),
				label_plural = _(entities)
			},
			place_facet = {
				type = authority,
				table = ca_places,
				relationship_table = ca_object_lots_x_places,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(place),
				label_plural = _(places)
			},
			collection_facet = {
				type = authority,
				table = ca_collections,
				relationship_table = ca_object_lots_x_collections,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(collection),
				label_plural = _(collections)
			},
			occurrence_facet = {
				type = authority,
				table = ca_occurrences,
				relationship_table = ca_object_lots_x_occurrences,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(occurrence),
				label_plural = _(occurrences)
			},
			term_facet = {
				type = authority,
				table = ca_list_items,
				relationship_table = ca_object_lots_x_vocabulary_terms,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(term),
				label_plural = _(terms)
			},
			type_facet = {
				type = fieldList,
				field = type_id,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(type),
				label_plural = _(types)
			},
			status_facet = {
				type = fieldList,
				field = status,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(status),
				label_plural = _(statuses)
			},
			access_facet = {
				type = fieldList,
				field = access,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(access status),
				label_plural = _(access statuses)
			}
		}
	}
	# --------------------------------------------------------------------
	# Configuration for entity browse
	ca_entities = {
		facets = {
			place_facet = {
				type = authority,
				table = ca_places,
				relationship_table = ca_entities_x_places,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(place),
				label_plural = _(places)
			},
			occurrence_facet = {
				type = authority,
				table = ca_occurrences,
				relationship_table = ca_entities_x_occurrences,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(occurrence),
				label_plural = _(occurrences)
			},
			collection_facet = {
				type = authority,
				table = ca_collections,
				relationship_table = ca_entities_x_collections,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(collection),
				label_plural = _(collections)
			},
			term_facet = {
				type = authority,
				table = ca_list_items,
				relationship_table = ca_entities_x_vocabulary_terms,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(term),
				label_plural = _(terms)
			},
			type_facet = {
				type = fieldList,
				field = type_id,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(type),
				label_plural = _(types)
			},
			status_facet = {
				type = fieldList,
				field = status,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(status),
				label_plural = _(statuses)
			},
			access_facet = {
				type = fieldList,
				field = access,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(access status),
				label_plural = _(access statuses)
			}
		}
	}
	# --------------------------------------------------------------------
	# Configuration for collection browse
	ca_collections = {
		facets = {
			entity_facet = {
				# 'type' can equal authority, attribute, fieldList, normalizedDates
				type = authority,
				table = ca_entities,
				relationship_table = ca_entities_x_collections,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [surname, forname],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(entity),
				label_plural = _(entities)
			},
			place_facet = {
				type = authority,
				table = ca_places,
				relationship_table = ca_places_x_collections,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(place),
				label_plural = _(places)
			},
			occurrence_facet = {
				type = authority,
				table = ca_occurrences,
				relationship_table = ca_occurrences_x_collections,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(occurrence),
				label_plural = _(occurrences)
			},
			term_facet = {
				type = authority,
				table = ca_list_items,
				relationship_table = ca_collections_x_vocabulary_terms,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(term),
				label_plural = _(terms)
			},
			type_facet = {
				type = fieldList,
				field = type_id,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(type),
				label_plural = _(types)
			},
			status_facet = {
				type = fieldList,
				field = status,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(status),
				label_plural = _(statuses)
			},
			access_facet = {
				type = fieldList,
				field = access,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(access status),
				label_plural = _(access statuses)
			}
		}
	}

	# --------------------------------------------------------------------
	# Configuration for place browse
	ca_places = {
		facets = {
			entity_facet = {
				# 'type' can equal authority, attribute, fieldList, normalizedDates
				type = authority,
				table = ca_entities,
				relationship_table = ca_entities_x_places,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [surname, forname],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(entity),
				label_plural = _(entities)
			},
			object_facet = {
				type = authority,
				table = ca_objects,
				relationship_table = ca_objects_x_places,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(object),
				label_plural = _(objects)
			},
			occurrence_facet = {
				type = authority,
				table = ca_occurrences,
				relationship_table = ca_places_x_occurrences,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(occurrence),
				label_plural = _(occurrences)
			},
			term_facet = {
				type = authority,
				table = ca_list_items,
				relationship_table = ca_places_x_vocabulary_terms,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(term),
				label_plural = _(terms)
			},
			type_facet = {
				type = fieldList,
				field = type_id,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(type),
				label_plural = _(types)
			},
			status_facet = {
				type = fieldList,
				field = status,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(status),
				label_plural = _(statuses)
			},
			access_facet = {
				type = fieldList,
				field = access,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(access status),
				label_plural = _(access statuses)
			}
		}
	}
	# --------------------------------------------------------------------
	# Configuration for occurrence browse
	ca_occurrences = {
		facets = {
			entity_facet = {
				# 'type' can equal authority, attribute, fieldList, normalizedDates
				type = authority,
				table = ca_entities,
				type_restrictions = [exhibitions],   # if browse for occurrences is type-restricted then only display this facet when browsing for exhibitions

				relationship_table = ca_entities_x_occurrences,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [surname, forname],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(entity),
				label_plural = _(entities)
			},
			object_facet = {
				type = authority,
				table = ca_objects,
				relationship_table = ca_objects_x_occurrences,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(object),
				label_plural = _(objects)
			},
			term_facet = {
				type = authority,
				table = ca_list_items,
				relationship_table = ca_occurrences_x_vocabulary_terms,
				restrict_to_types = [],
				restrict_to_relationship_types = [],
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(term),
				label_plural = _(terms)
			},
			type_facet = {
				type = fieldList,
				field = type_id,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(type),
				label_plural = _(types)
			},
			status_facet = {
				type = fieldList,
				field = status,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(status),
				label_plural = _(statuses)
			},
			access_facet = {
				type = fieldList,
				field = access,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = an,
				label_singular = _(access status),
				label_plural = _(access statuses)
			}
		}
	}

	# --------------------------------------------------------------------
	# Configuration for storage location browse
	ca_storage_locations = {
		facets = {
			type_facet = {
				type = fieldList,
				field = type_id,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(type),
				label_plural = _(types)
			},
			status_facet = {
				type = fieldList,
				field = status,
				sort_by = [name],
				group_mode = alphabetical,

				indefinite_article = a,
				label_singular = _(status),
				label_plural = _(statuses)
			}
		}
	}
