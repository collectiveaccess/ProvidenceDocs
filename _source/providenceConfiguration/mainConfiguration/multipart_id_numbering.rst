Multipart numbering
===================

The MultiPartIDNumber plug-in provides a flexible means to generate structured numbering systems such as accession numbers within CollectiveAccess. For most numbering schemes employed by museums and archives it should be possible to configure a convenient user interface and adequate validation rules using only the plug-in and without any custom programming.

The MultiPartIDNumber plug-in requires an ID number *format* for each item in CollectiveAccess that supports ID numbers. A format is composed of *elements* joined together by a *separator*. Each element in a format has settings specified that determine what input is valid for it and how it will behave in the user interface. An ID number is constructed by stringing together the individual elements using separators. By combining various types of elements you can create arbitrarily complex numbering systems.

The multipart_id_numbering.conf configuration file
--------------------------------------------------

The file defines the formats used by the MultiPartIDNumber plug-in. It is a standard CollectiveAccess configuration file using the :ref:`common configuration syntax <configuration_file_syntax>`.

CollectiveAccess supports ID numbers for the following items:

- objects (*ca_objects*)
- lots (*ca_object_lots*)
- entities (*ca_entities*)
- places (*ca_places*)
- collections (*ca_collections*)
- occurrences (*ca_occurrences*)
- loans (*ca_loans*)
- movements (*ca_movements*)
- storage locations (*ca_storage_locations*)
- representations (*ca_object_representations*)
- list items (*ca_list_items*)
- content managed site pages (*ca_site_pages*)
- tours (*ca_tours*)
- tour stops (*ca_tour_stops*)

You may specify numbering formats for any type of item listed above in multipart_id_numbering.conf. The format name for each must be identical to the item code (italicized in the list above). CollectiveAccess will use the format to generate an ID number entry interface and validate input for the ID number field of the respective data item. For lots this is the 'idno_stub' field; for objects and other items it is the 'idno' field.

The following sample multipart_id_numbering.conf configuration is for an organization employing a lot numbering scheme based upon the year of acquisition and an automatically assigned incrementing lot number. Object numbers are based upon the lot number format but with an additional automatically assigned incrementing item number. In both number formats, elements are separated with periods ("."). The file specifies a two part number for entities: the first element is a code taken from a drop-down list of three allowable values and the second element is an automatically assigned incrementing number. For both place names and vocabulary terms an automatically assigned incrementing number is specified.

.. code-block:: none

	formats = {
		ca_objects = {
	# This is a default numbering format for object type for which a format has not been explicitly specified
			__default__ = {
				separator = .,
	# sorting of id numbers will be in reverse of display order (eg. if display is 2011.52.1, sort will be on 1.52.2001); remove sort_order altogether if you want sort to consider elements in display order

				sort_order = [item_num, lot_num, acc_year],

				elements = {
					acc_year = {
						type = YEAR,
						width = 6,
						description = Year,

						editable = 1
					},
					lot_num = {
						type = NUMERIC,
						width = 6,
						description = Lot number,

						editable = 1
					},
					item_num = {
						type = SERIAL,
						width = 6,
						description = Item number,

						editable = 1
					}
				}
			},
	# Here's a specialized number format for objects of type "video" (where "video" is the idno of the object_type)
			video = {
				separator = .,

				elements = {
					acc_year = {
						type = YEAR,
						width = 6,
						description = Year,

						editable = 1
					},
					typecode = {
						type = LIST,
						values = [8MM, DV, BETASP],
						default = ORG,
						width = 6,
						description = Type code,
						editable = 1
					},
					item_num = {
						type = SERIAL,
						width = 6,
						description = Item number,

						editable = 1
					}
				}
			}
		},

		ca_object_lots = {
			__default__ = {
				separator = .,

				elements = {
					acc_year = {
						type = YEAR,
						width = 6,
						description = Year,

						editable = 1
					},
					lot_num = {
						type = SERIAL,
						width = 6,
						description = Lot number,

						editable = 1
					}
				}
			}
		},

		ca_entities = {
			__default__ = {
				separator = .,

				elements = {
					code = {
						type = LIST,
						values = [PER, ORG, GRP],
						default = ORG,
						width = 6,
						description = Entity code,
						editable = 1
					},
					num = {
						type = SERIAL,
						width = 8,
						description = Entity number,
						editable = 1
					}
				}
			}
		},
		ca_places = {
			__default__ = {
	# Note the blank separator -- the comma is part of the config file, not the separator value
				separator = ,

				elements = {
					num = {
						type = SERIAL,
						width = 8,
						description = Place number,
						editable = 0
					}
				}
			}
		},

		ca_collections = {
			__default__ = {
	# Note the blank separator -- the comma is part of the config file, not the separator value
				separator = ,

				elements = {
					num = {
						type = SERIAL,
						width = 8,
						description = Collection number,
						editable = 0
					}
				}
			}
		},

		ca_occurrences = {
			__default__ = {
	# Note the blank separator -- the comma is part of the config file, not the separator value
				separator = ,

				elements = {
					num = {
						type = SERIAL,
						width = 8,
						description = ID number,
						editable = 0
					}
				}
			}
		}
	}

All formats in the configuration file are located in an associative list named *formats* The keys of this list are table names for which format are specified. Each table name key has as its value an associative list keyed on type. Use the special *__default__* type to specify a format for use with any type not declared with a specific format. 

Each type key has as its value an associative list specifying the format. The following keys may be placed in the list:

.. csv-table::
   :widths: 12, 32, 12, 12
   :header-rows: 1
   :file: multipartid_conf_general_settings.csv

The keys of the *element* associative list are element names. These names are only used for reference during configuration and to name HTML form elements and are not presented to the user. They should use only alphanumeric characters and underscores. Do not include spaces or punctuation in the names.

The value for each element name in the elements list is another associative list, this one containing a list of settings declaring the characteristics of the element. The most important setting to set for an element is its type which defines the general range of allowable values and user interface behaviors. The plug-in supports the following types:

.. csv-table::
   :widths: 12, 32
   :header-rows: 1
   :file: multipartid_conf_types.csv

Beyond type, there are a number of other settings that can be set for an element. Some are common to all element types and others are specific to certain types.

Settings applicable to all types of elements are:

.. csv-table::
   :widths: 12, 32
   :header-rows: 1
   :file: multipartid_conf_field_settings.csv

Type-specific settings are:

.. csv-table::
   :widths: 12, 12, 32
   :header-rows: 1
   :file: multipartid_conf_setting_options.csv

Problems with SERIAL elements
-----------------------------
To generate unique values for SERIAL elements the plug-in must query your CollectiveAccess database. If the database operation fails you may see the word 'ERR' instead of the expected numeric value. In versions prior to 1.7.9 the underlying database table and fields used to derive the next number in sequence had to be manually configured for each SERIAL element using the *table*, *field* and *sort_field* settings. If you are running an older version and receive an ERR value verify that the table, field and sort_field element settings are set correctly. 

The automatically issued SERIAL values should always be one more than the largest extant value in your database. If you are getting values that are less than the maximum try *reloading sort values*, using the option under the administrative *Maintenance* menu or the command line :ref:`caUtils <ca_utils>` command using the *rebuild-sort-values* option.
