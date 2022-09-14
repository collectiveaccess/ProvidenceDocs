Access Restrictions Configuration: access_restrictions.conf
===========================================================

* `Syntax`_ 
* `Rules and Arrays`_
* `Example Rules`_ 


CollectiveAccess uses a Model-View-Controller structure that allows one to restrict access to each navigation module, controller or even controller action. Those restrictions are defined in *access_restrictions.conf*. The *access_restrictions.conf* configuration file is part of this structure 

More here

Syntax
------

The beginning of the file features a key that allows you to disable all module, controller, or action-based access control. To not enforce access restrictions, set the following to zero. To enforce access restrictions, set to 1. 

``: enforce_access_restrictions = 1``

The second directive in this file is a big array named "access_restrictions". It consists of an arbitrary number of module, controller, and action-based access restrictions. The key of each array element is either a path to a controller group ("module") in *app/controllers*, or a path to a controller in a controller group: 

Path to controller group (module): ``administrate/setup``

Path to controller in a controller group: ``administrate/setup/RelationshipTypesController``

The key can even feature an action (method) of a particular controller, as follows:

``administrate/setup/RelationshipTypesController/Save``

Rules and Arrays
----------------

A user must pass all applicable restriction checks before access to an action is granted. Each array element (indexed by module/controller/action) can consist of an arbitrary number of access rules. These rules are arrays describing the group of users that are allowed to access the subject. Each rule may consist of the following keys:

.. csv-table:: 
   :header-rows: 1
   :file: access_restrict_table1.csv

Example Rules
-------------

The following example uses most of the features described above: 

.. code-block::

   editor/objects/ObjectEditorController/Save = {
		create = {
			parameters = {
				object_id = {
					value = 0,
					type = int
				}
			},
			actions = { can_create_ca_objects }
		},
		edit = {
			parameters = {
				object_id = {
					value = !0,
					type = int
				}
			},
			actions = { can_edit_ca_objects }
		}
	},
 
This rule restricts access to the "Save" action of the "ObjectEditorController" in the "editor/objects" module. It features two access rules: 

1. Only applies if the parameter "object_id" equals zero. In this case only users that have a role with the user action "can_create_ca_objects" are allowed to perform this action. 

2. Enforced if the parameter doesn't equal zero. In that case a user is trying to save changes to an existing object, and has to be able to perform the action "can_edit_ca_objects". Note that the "operator" directive is omitted in both rules. Since the action lists consist of only 1 item, it doesn't matter if they're connected via AND or OR. 

Below is another example that makes use of the "operator" key: 

.. code-block::

   editor/occurrences/OccurrenceEditorController/Edit = {
		edit_delete = {
			parameters = {
				item_id = {
					value = !0,
					type = int
				}
			},
			operator = OR,
			actions = { can_edit_ca_occurrences, can_delete_ca_occurrences }
		},
		create = {
			parameters = {
				item_id = {
					value = 0,
					type = int
				}
			},
			actions = { can_create_ca_occurrences }
		},
	},

The following example makes use of the type parameter. The usage of this is especially useful in combination with the automatic action expansion feature in User_Actions_Configuration. 

.. code-block::

   editor/objects/ObjectEditorController/Save = {
		photography_create = {
			parameters = {
				object_id = {
					value = 0,
					type = int
				},
				type = photography
			},
			actions = { can_create_ca_objects_type:ca_objects.photography }
		},
		document_create = {
			parameters = {
				object_id = {
					value = 0,
					type = int
				},
				type = document
			},
			actions = { can_create_ca_objects_type:ca_objects.document }
		},
		photography_edit = {
			parameters = {
				object_id = {
					value = !0,
					type = int
				},
				type = photography
			},
			actions = { can_edit_ca_objects_type:ca_objects.photography }
		},
		document_edit = {
			parameters = {
				object_id = {
					value = !0,
 					type = int
				},
 				type = document
			},
			actions = { can_edit_ca_objects_type:ca_objects.document }
		},
	},

 
