Multipart id numbering.conf
===========================

The MultiPartIDNumber plug-in provides a flexible means to generate structured numbering systems such as accession numbers within CollectiveAccess. For most numbering schemes employed by museums and archives it should be possible to configure a convenient user interface and adequate validation rules using only the plug-in and without any custom programming.

The MultiPartIDNumber plug-in requires an ID number "format" for each data item in CollectiveAccess that supports ID numbers. A format is composed of "elements" joined together by a "separator." Each element in a format has parameters specified that determine what input is valid for it and how it will behave in the user interface. An ID number is constructed by stringing together the individual elements using separators. By combining various types of elements you can create arbitrarily complex numbering systems.

The multipart_id_numbering.conf configuration file
--------------------------------------------------

The id_numbering.conf file defines the formats used by the MultiPartIDNumber plug-in. It is a standard CollectiveAccess configuration file using the common configuration syntax.

CollectiveAccess supports ID numbers for the following data items:

- objects ("ca_objects")
- lots ("ca_object_lots")
- entity authority items ("ca_entities")
- place name authority items ("ca_places")
- collection authority items ("ca_collections")
- items in user-defined authorities (aka "occurrences") ("ca_occurrences")
- loans ("ca_loans")
- movements ("ca_movements")
- tours ("ca_tours")
- tour stops ("ca_tour_stops")

You must specify a format for each type of data item listed above in id_numbering.conf. The format name for each must be identical to the data item name (quoted in the list above). CollectiveAccess will use the format to generate an ID number entry interface and validate input for the ID number field of the respective data item. For objects, this is the 'idno' field; for lots this is the 'idno_stub' field; for the authorities and for vocabularies it is the 'idno' field.

The following sample id_numbering.conf configuration is for an organization employing a lot numbering scheme based upon the year of acquisition and an automatically assigned incrementing lot number. Object numbers are based upon the lot number format but with an additional automatically assigned incrementing item number. In both number formats, elements are separated with periods ("."). The file specifies a two part number for entities: the first element is a code taken from a drop-down list of three allowable values and the second element is an automatically assigned incrementing number. For both place names and vocabulary terms an automatically assigned incrementing number is specified.

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
				
						editable = 1,
					
						table = ca_objects,
						field = idno,
						sort_field = idno_sort,
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
				
						editable = 1,
					
						table = ca_objects,
						field = idno,
						sort_field = idno_sort,
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
				
						editable = 1,
					
						table = ca_object_lots,
						field = idno_stub,
						sort_field = idno_stub_sort
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
						editable = 1,
					
						table = ca_entities,
						field = idno,
						sort_field = idno_sort
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
						editable = 0,
					
						table = ca_places,
						field = idno,
						sort_field = idno_sort
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
						editable = 0,
				
						table = ca_collections,
						field = idno,
						sort_field = idno_sort
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
						editable = 0,
				
						table = ca_occurrences,
						field = idno,
						sort_field = idno_sort
					}
				}
			}
		}
	}
	
All formats in the configuration file are located in an associative list named 'formats' The keys of this list are table names for which format are specified. Each table name key has as its value an associative list keyed on type (you should use the idno of types for the table, not numeric type_ids). If you want to specify a format valid for all types, a common case, use __default__ instead of a valid type code.

Each type key has as its value an associative list specifying the format. The following keys may be placed in the list:

.. csv-table::
   :widths: 12, 32, 12, 12
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTLSaX5Jk_mKE1HC0l33YFmFSLTYAf0S-VaTgK2GEW7n0D34Y4mfE6LNmW5ELG83wQZTSOB2bv02ZeH/pub?output=csv

The keys of the element associative list are element names. These names are only used for reference during configuration and to name HTML form elements and are never output to the user. They should use only alphanumeric characters and underscores. Do not put spaces or punctuation in the names.

The value for each element name in the elements list is yet another associative list, this one containing a list of parameters defining the characteristics of the element. The most important parameter to set for an element is its type which defines the general range of allowable values and user interface behaviors. The plug-in supports the following types:

.. csv-table::
   :widths: 12, 32
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/e/2PACX-1vQgPg2G_Zn_aDSV5d_NEAn6xK2SvkQkJ-RovR_FV0YFCmv1b1PjrSOjXtu3ebRR88zL3WqsSihMHcyt/pub?output=csv

Besides type, there are a number of other parameters that can be set for an element. Some are common to all element types and others are specific to certain types.

Parameters applicable to all types of elements are:

.. csv-table::
   :widths: 12, 32
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTjHLw4FlKONhAn-NvdJ7VmlMEtAd1z1YhQMOtb9vFW7ONrxZJUS7NO9nVfBX2C_QdG0SUhYUzuLk-M/pub?output=csv

Type-specific parameters are:

.. csv-table::
   :widths: 12, 12, 32
   :header-rows: 1
   :url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTC2_tsng93HEvNiiyktqU-TGvk6HZZPAsP_aH9Y_y7W-20t0PkNoXd6nC8PblpWr_WWu066KbEFyUO/pub?output=csv

Problems with SERIAL elements
-----------------------------
To generate unique values for SERIAL elements the plug-in must query your CollectiveAccess database. If the database operation fails you may see the word 'ERR' instead of the expected numeric value. If you get an ERR value, verify that the table, field and sort_field element parameters are correct.

The automatically issued SERIAL values should always be one more than the largest extant value in your database. If you are getting values that are less than the maximum check that the sort_field element parameter is correct. The plug-in relies upon this field to properly sort the existing numbers in order to choose the largest existing value.
