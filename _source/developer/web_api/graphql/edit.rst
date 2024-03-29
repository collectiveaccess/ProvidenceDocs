.. _developer_api_graphql_edit:

Editing (endpoint name ``Edit``)
================================

The Edit service provides mutations to create new records, and modify or delete existing records.

Creating new records
~~~~~~~~~~~~~~~~~~~~

The ``add`` mutation is used to create new records. To create a record three bits of information are needed: the :ref:`table <primary_tables>` the record will reside in, the ``type`` for the new record, and an ``idno`` (a unique user-provided identifier) value. Other data elements (or "bundles") can be set by listing them in the ``bundles`` parameter of the query. For example:

.. code-block:: text

	mutation { 
		add(
			table: "ca_objects", 
			idno: "test.101", 
			type: "artifact",
			bundles: [
				{ name: "preferred_labels", value: "My first record"},
				{ name: "description", value: "This is a new record!"},
				{ name: "date", value: "April 3 1984"}
			]
		) { 
			id, 
			table, 
			identifier, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		} 
	} 
 
This mutation will create a new artifact object record with the provided values for idno, title (aka. preferred label), description and date. Note that that format for the ``idno`` value, valid values for ``type`` and available bundles are system-specific. The values used here are examples. 

The ``bundles`` parameter takes a list of bundle value specifications. Each specification requires, at a minimum, a bundle ``name`` and ``value`` to set. For bundles that repeat, specifications with the same bundle name may be set. For example, to set multiple dates on an object (assuming the schema is configured to allow repeating dates):

.. code-block:: text

	mutation { 
		add(
			table: "ca_objects", 
			idno: "test.101", 
			type: "artifact",
			bundles: [
				{ name: "preferred_labels", value: "My first record"},
				{ name: "description", value: "This is a new record!"},
				{ name: "date", value: "April 3 1984"},
				{ name: "date", value: "June 8 1984"},
				{ name: "date", value: "July 26 1984"}
			]
		) { 
			id, 
			table, 
			identifier, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		} 
	} 

If your system supports multiple cataloguing locales, the locale for each bundle value may be specified using ``locale`` and an ISO code:

.. code-block:: text

	{ name: "description", value: "Hier ist ein neuer Rekord", locale: "de_DE" },
	
If you omit the locale value for a bundle, the system default locale is used.

For container bundles – fields that contain sub-fields, set ``values`` for the bundle specifier with a list of sub-field specifiers. For example:

.. code-block:: text

	mutation { 
		add(
			table: "ca_objects", 
			idno: "test.101", 
			type: "artifact",
			bundles: [
				{ name: "preferred_labels", value: "My first record"},
				{ name: "description", value: "This is a new record!"},
				{ name: "address", values: [
					{ name: "address1", value: "1000 Surf Avenue" },
					{ name: "city", value: "Brooklyn" },
					{ name: "state", value: "NY" },
					{ name: "postal_code", value: "11224" },
					{ name: "country", value: "USA" }
				]}
			]
		) { 
			id, 
			table, 
			identifier, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		} 
	} 

Similarly, for preferred and non-preferred labels that take multiple sub-values, such as entities, ``values`` may be set on the bundle to specific sub-field values:

.. code-block:: text

	mutation { 
		add(
			table: "ca_entities", 
			idno: "E.1", 
			type: "individual",
			bundles: [
				{ name: "preferred_labels", values: [
					{ name: "forename", value: "David" },
					{ name: "surname", value: "Lowery" },
					{ name: "middlename", value: "Alan" },
					{ name: "prefix", value: "Mr" }
				]},
				{ name: "biography", value: "He was born in Brooklyn in 1914... etc etc"},
				{ name: "lifedates", value: "February 13, 1914 - March 6, 1981"}
			]
		) { 
			id, 
			table, 
			idno, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		} 
	} 

For non-preferred labels, which take an option label `type` value, you may also pass ``type`` in the bundle specification. If it is omitted the default type will be used.

Note that all bundles are assumed to be bound to the table to which you are adding the record. To manage relationships between records use the ``addRelationship``, ``editRelationship``, ``deleteRelationship`` and ``deleteAllRelationships`` `mutations <#creating-relationships>`_ described below. You may also create relationships within the ``add`` mutation using the ``relationships`` parameter described below.

The ``add`` mutation can return the internal CollectiveAccess ``id`` value for the newly created record, the ``table`` of the record (always the same as the table parameter passed in the mutation), the idno value (which may be calculated using a server-side policy and differ from the passed value) and a list of errors, warnings and informational messages related to the add operation. Errors indicate failures and include an error code, the idno of the affected record, a descriptive message and the name of the bundle the error affects. Non-bundle-specific errors will have a bundle code of ``GENERAL``. Warnings indicate possible error conditions and issues, and are purely advisory. Informational messages (``info``) provide details about processing stages of the mutation, including how existing records may or may not have been matched, and if related records may have been created. Both ``warnings`` and ``info`` messages have a simliar structure to ``error``.

Multiple adds and hierarchies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple records may be created in single request using the ``records`` parameter. Each record includes an ``idno``, ``type`` and ``bundles`` list. The ``insertMode`` parameter controls how records are created. Setting ``insertMode`` to `FLAT` (the default) will create individual records. Setting ``insertMode`` to `HIERARCHICAL` will arrange the newly created records in a hierarchy, with the first listed record as the hierarchical root. This example will create three levels in the storage location hierarchy:

.. code-block:: text

	mutation {
		add(
			table: "ca_storage_locations",
			insertMode: "HIERARCHICAL",
			existingRecordPolicy:"IGNORE",
			ignoreType: true,
			records:[{
				idno: "s.1",
				type: "building",
				bundles: [
					{ name: "preferred_labels", value: "Hibbens Hall", replace: true}
				]
			 },{
				idno: "f.1",
				type: "floor",
				bundles: [
					{ name: "preferred_labels", value: "Floor 1"}
				]
			 },{
				idno: "r.123",
				type: "room",
				bundles: [
					{ name: "preferred_labels", value: "Room 123"}
				]
			 } ]
		) {
			id,
			table,
			idno,
			changed,
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		}
	}
	
The ``existingRecordPolicy`` parameter controls behavior when a record with the specified `idno` value (or other specified criteria, as described in the next section) is already present.

.. csv-table:: `existingRecordPolicy` values
   :header: "Value", "Description"
   :widths: 20, 20

   "IGNORE", "Ignore existing records and attempt to create a new record."
   "REPLACE", "Delete the existing record and insert a new record."
   "MERGE", "Merge bundles into existing record. Essentially the same as editing the existing record."
   "SKIP", "Skip add if record with idno already exists."
   
If you do not set and existing record policy, `SKIP` is assumed.

By default, existing records must match on idno, type and parent (when using ``HIERARCHICAL`` insert mode). The type matching requirement can be relaxed by passing the ``ignoreType`` option as in the previous example. The parent matching requirement when in ``HIERARCHICAL`` insert mode can be relaxed by passing the ``ignoreParent`` option.


Adding relationships to a new record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Relationships may be established between an added record and existing records using the ``relationships`` list parameter. Each item in the relationships list contains keys for ``target`` (the table to relate to) and ``relationshipType`` (a valid relationship type code for the relationship to be created). The record to relate to must be specified using one of the following: ``targetId`` (the database ID of the record to relate to), ``targetIdno`` (the idno of the related record), or ``targetIdentifer`` (the idno or database ID). You may also set interstitial data on the relationship by passing an optional ``bundles`` parameter within a ``relationships`` item. For example:

.. code-block:: text

	mutation {
		add(
			table: "ca_objects",
			idno: "2020.11.1",
			type: "artifact",
			bundles: [
				{ name: "preferred_labels", value: "Thimble Folk"},
				{ name: "description", value: "Highly collectible felt dolls."}
			],
			replaceRelationships: false,
			relationships: [
				{
					target:"ca_entities",
					targetIdentifier: "E.100",
					relationshipType:"donor",
					bundles: [
						{ "effective_date": "1961 - 1965" }
					]
				}
			]
		) {
			id,
			table,
			idno,
			changed,
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		}
	}

Any number of relationships may be added to a record in this way. If the ``add`` mutation is for a record that already exists in the database, relationships will be added to the existing record with relationships matching existing ones skipped. To force the relationships on existing records to conform those specified in the mutation set the ``replaceRelationships`` parameter to true (the default is false). This will cause all existing relationships to be removed before the relationships specified in the mutation are added.

``relationships`` and ``replaceRelationships`` may be specified at the top level of the mutation when the mutation is for a single new record (as shown above). For multiple adds, the parameters must be specified for each record in the ``records`` list.


Matching using other fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Matching of existing records is typically done with ``idno`` values, but other data may be used as well. To toggle between matching on ``idno`` or preferred label use the ``matchOn`` parameter set to a list containing one or both of the values "idno" or "preferred_labels" in the order of precedence. Setting ``matchOn`` to 

.. code-block:: text

	matchOn: ["preferred_labels", "idno"]

will result in matching on preferred labels, falling back to idno if there are no label matches. Setting a single value will result in matching on only the specified field.


Arbitrary matching criteria may be specified using the ``match`` parameter. ``match`` offers two sub-parameters: ``search``` matches records using a query string; ``criteria`` matches records using field-level search criteria. The two sub-parameters are analogous to the ``search`` and ``find`` queries in the :ref:`search endpoint <developer_api_graphql_search>`, taking identical input and employing the same methods to locate matches. 

``match`` and ``matchOn``` may be used in conjunction with ``existingRecordPolicy`` to implement useful data migration patterns that might otherwise require several separate queries and mutations. One common data migration pattern occurs when importing a data set that includes references to related records (a set of artworks with related artists, for example). In this case, one would process each object record in turn, creating related entity records for artists that don't already exist, and then establishing object-artist relationships. Without ``match`` or ``matchOn`` the process would require these steps:

1. Create the object
2. Perform a ``search`` query for each artist related to the object
3. Create entity records for all artists that did not return a match
4. Create relationships between the entities and newly created object

By using an ``add`` mutation with ``relationships`` set to the relevant object, ``match`` > ``criteria`` set to the artist's name and an ``existingRecordPolicy`` of ``MERGE``, steps 2-4 can be consolidated into a single mutation that finds matching artist records based upon name, creates a new record for an artist if there are no matches, and then creates an object-artist relationship between the matched or newly created artist record. The mutation might look like this, if you wanted to match both name and lifedates:

.. code-block:: text

	mutation { 
		add(
			table: "ca_entities", 
			idno: "E.%", 
			type: "individual",
			bundles: [
				{ name: "preferred_labels", values: [
					{ name: "forename", value: "David" },
					{ name: "surname", value: "Lowery" },
					{ name: "middlename", value: "Alan" },
					{ name: "prefix", value: "Mr" }
				]},
				{ name: "biography", value: "He was born in Brooklyn in 1914... etc etc"},
				{ name: "lifedates", value: "February 13, 1914 - March 6, 1981"}
			],
			existingRecordPolicy: "MERGE",
			match: {
				find: [
					{
						name: "ca_entities.preferred_labels.surname", 
						operator: EQ, 
						value: "Lowery"
					},
					{
						name: "ca_entities.preferred_labels.forename", 
						operator: EQ, 
						value: "David"
					},
					{ 
						name: "lifedates", 
						operator: EQ, 
						value: "February 13, 1914 - March 6, 1981"
					}
				]
			},
			relationships: [
				{
					target:"ca_objects",
					targetIdentifier: "2021.004.001",
					relationshipType:"donor"
				}
			]
		) { 
			id, 
			table, 
			idno, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		} 
	} 
	
If only a name match is required, a somewhat simpler mutation using ``matchOn`` might look like this;

.. code-block:: text

	mutation { 
		add(
			table: "ca_entities", 
			idno: "E.%", 
			type: "individual",
			bundles: [
				{ name: "preferred_labels", values: [
					{ name: "forename", value: "David" },
					{ name: "surname", value: "Lowery" },
					{ name: "middlename", value: "Alan" },
					{ name: "prefix", value: "Mr" }
				]},
				{ name: "biography", value: "He was born in Brooklyn in 1914... etc etc"},
				{ name: "lifedates", value: "February 13, 1914 - March 6, 1981"}
			],
			existingRecordPolicy: "MERGE",
			matchOn: ["preferred_labels"],
			relationships: [
				{
					target:"ca_objects",
					targetIdentifier: "2021.004.001",
					relationshipType:"donor"
				}
			]
		) { 
			id, 
			table, 
			idno, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		} 
	} 

.. IMPORTANT::
   In an ``add`` mutation, when a ``search``, ``find`` matches more than one record the first record found is considered the existing record. All other matches are discarded. For predictable results use criteria that will return unique matches. ``matchOn`` only matches using fields that are typically unique (idno and preferred labels), but will exhibit the same behavior should those fields include non-unique values.


Editing records
~~~~~~~~~~~~~~~~~~~~

To edit an existing record, the ``edit`` mutation is used with the target record specified by ``table`` and ``identifier`` parameters. The ``identifier`` parameter may be either an numeric internal CollectiveAccess ID value or the ``idno`` value of a record. Note that ``idno`` values are not guaranteed to be unique (although they typically are). If more than one record matches the identifier, the first match will be edited and additional matches ignored. If the supplied ``identifier`` is numeric it will be matched first as an internal ID, and subsequently as an ``idno`` if no internal ID is found. In cases where ``idno`` values solely contain digits, mismatches may occur. To force matching on internal ID or ``idno`` only use the ``id`` and ``idno`` parameters respectively, rather than ``identifier``.

Edited values are specified in the ``bundles`` parameter, similar to the format used for adding with a few additions. By default each listed bundle will be appended to the record. For bundles supporting repeating values, this means the addition of values. For fields that limited or not repeatability, edits will fail once the limit is reached. To replace a value rather than append to it, a ``replace`` value set to ``true`` may be set in the bundle specification. If a value exists it will be replaced by the new value; if no value exists yet, the new value will be added. 

To target a specific value in a bundle with multiple repeating values a value ``id`` may be set in the bundle specifier. These ``id`` values can be returned alongside their values in ``Item`` service endpoint responses (described above)

To delete a value from a record set a ``delete`` value to ``true`` in the bundle specifier. If ``id`` is also specified the specific value will be removed. If ``id`` is omitted all values will be removed.

An ``edit`` mutation that changes the ``idno``, replaces the description and removes all non-preferred labels:

.. code-block:: text

	mutation { 
		edit(
			table: "ca_objects", 
			identifier: "TEST.1", 
			bundles: [
				{name:"idno", value: "test.101"},
				{ name:"nonpreferred_labels", delete: true },
				{ name: "description", value: "This is a new description", replace: true }
			]
		) { 
			id, 
			table, 
			idno, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		} 
	} 

Note that the response format is identical to that used for ``add``.

Relationships may be specified for edits in the same manner they are for the ``add`` mutation.

Multiple edits
~~~~~~~~~~~~~~

Multiple records may be edited in single request using the ``records`` parameter. Each record includes an ``identifier`` (or ``id`` or ``idno``), ``type`` and ``bundles`` list.  This example will edit the preferred labels of three objects in a single request:

.. code-block:: text

	mutation {
        edit(
			table: "ca_objects",
			records:[{
				identifier: "Test.400",
				bundles: [
					{ name: "preferred_labels", value: "My new title", replace: true}
				]
			 },{
				identifier: "Test.401",
				bundles: [
					{ name: "preferred_labels", value: "Another new title", replace: true}
				]
			 },{
				identifier: "Test.450",
				bundles: [
					{ name: "preferred_labels", value: "A third new title", replace: true}
				]
			 } ]
		) {
			id,
			table,
			idno,
			changed,
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		}
	}

Deleting records
~~~~~~~~~~~~~~~~~~~~

To delete a record, pass the table and an identifier (CollectiveAccess ID value or ``idno`` value):

.. code-block:: text

	mutation { 
		delete(
			table: "ca_objects", 
			identifier: "test.101"
		) { 
			id, 
			table, 
			identifier, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		}
	} 
	
The response will be in the same format as that used for ``add`` and ``edit`` mutations, but ``id`` and ``identifier`` will always be set to null.

As with edits, if the supplied ``identifier`` is numeric it will be matched first as an internal ID, and subsequently as an ``idno`` if no internal ID is found. In cases where ``idno`` values solely contain digits, mismatches may occur. To force matching on internal ID or ``idno`` only use the ``id`` and ``idno`` parameters respectively, rather than ``identifier``.

To delete multiple records with in single request, pass a list of identifiers using the ``identifiers`` parameter. To force matching on internal ID or ``idno`` use the ``ids`` and ``idnos`` parameters respectively.


Truncating tables
~~~~~~~~~~~~~~~~~~~~

When developing or debugging a data import process it is often useful to quickly delete some or all of the records in a table. The ``truncate`` mutation can remove all records in a table, or selected records based upon last modification date and/or record types. 

This mutation would delete all entities of type ``ind`` modified after July 21 2021 at 5pm:

.. code-block:: text
        mutation {
            truncate(
                    table: "ca_entities",
                    date: "after 7/21/2021 @ 5pm",
                    types: ["ind"], 
                    fast: true
            ) { 
                    id
                    table,
                    idno,
                    changed,
					errors { idno, code, message, bundle },
					warnings { idno, code, message, bundle },
					info { idno, code, message, bundle }
            }
        }
        
The ``fast`` option will remove records as quickly as possible by skipping update of the change log and search index. When truncating tables with large numbers of records, this can result in significant time savings. For development systems, the lack of consistent change logging and indexing for deleted records is usually not an issue. The ``fast`` option should not be used in production systems.

.. IMPORTANT::
	Use of this GraphQL service requires authentication with an account having the ``can_truncate_tables_via_graphql`` action privilege.
	
Specific lists may be truncated using the ``list`` parameter. The ``date`` and ``types`` parameter may be set to restrict which items in the list are removed. If ``list`` is set ``table`` is ignored:

.. code-block:: text

	    mutation {
            truncate(
                    list:"chemical_deterioration", fast: true
            ) { 
                    id
                    table,
                    idno,
                    changed,
					errors { idno, code, message, bundle },
					warnings { idno, code, message, bundle },
					info { idno, code, message, bundle }
            }
        }

        
.. _creating_relationships:

Creating relationships
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

	mutation { 
		addRelationship(
			subject: "ca_objects", 
			target: "ca_entities", 
			subjectIdentifier: "test.1", 
			targetIdentifier:"51", 
			relationshipType: "creator"
		) { 
			id, 
			idno, 
			table, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		} 
	} 
	
Returns:

.. code-block:: Text

	{
		"ok": true,
		"data": {
			"addRelationship": {
				"id": 1,
				"idno": null,
				"table": "ca_objects_x_entities",
				"errors": [],
				"warnings": [],
				"idno": []
			}
		}
	}
	
If the supplied ``subjectIdentifier`` or ``targetIdentifier`` values are numeric they will be matched first as internal IDs, and subsequently as ``idno`` if no internal ID is found. In cases where ``idno`` values solely contain digits, mismatches may occur. To force matching on internal ID or ``idno`` only use the ``subjectId`` (or ``targetId``) and ``subjectIdno`` (or ``targetIdno``) parameters respectively, rather than ``subjectIdentifier`` and ``targetIdentifier``.
	
Editing relationships
~~~~~~~~~~~~~~~~~~~~~~	

.. code-block:: text
	
	mutation { 
		editRelationship(
			subject: "ca_objects", 
			subjectIdentifier: "test.1", 
			target:"ca_entities",
			targetIdentifier: "55", 
			relationshipType: "creator", 
			bundles: [
				{name: "effective_date", value: "1960"}, 
				{name: "relationship_type", value: "creator"}, 
				{name: "description", value: "hello world???", replace: true}
			]) { 
				id, 
				table, 
				idno, 				
				errors { idno, code, message, bundle },
				warnings { idno, code, message, bundle },
				info { idno, code, message, bundle }
			}
		} 

Deleting relationships
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
	
	mutation { 
		deleteRelationship(
			subject: "ca_objects", 
			id: 1, 
			target:"ca_entities"
		) { 
			id, 
			table, 
			idno, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		}
	} 

Deleting all relationships:
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

	mutation { 
		deleteAllRelationships(
			subject: "ca_objects", 
			subjectIdentifier: "test.1", 
			target:"ca_entities", 
			relationshipType: "related"
		) { 
			id, 
			table, 
			idno, 
			errors { idno, code, message, bundle },
			warnings { idno, code, message, bundle },
			info { idno, code, message, bundle }
		} 
	} 