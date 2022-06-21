Cookbook: Configuration files
=============================

This section provides some real examples of common challenges that may arise during the set up of configuration files. This section is aimed at developers who can configure code and set up configuration files in the installation profile for CollectiveAccess.

Each scenario begins with a “problem,” describing a certain challenge or question that may occur during installation. There is an accompanying “solution” provided for each problem, which outlines how to carry out the necessary steps to reach a specific outcome. 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online `Support Forum <https://collectiveaccess.org/support/>`_, `Online Chat <https://gitter.im/collectiveaccess/support>`_, `Slack Channel for Developers <https://collectiveacc-uye7574.slack.com/join/signup#/domain-signup>`_, and `Back-end <https://github.com/collectiveaccess/providence>`_ and `Front-end <https://github.com/collectiveaccess/pawtucket2>`_ GitHub Repositories.  

Contents
--------

* `Browsing on a Metadata Element`_
*

Browsing on a Metadata Element 
------------------------------

**Problem**: You need to set up the browse function in CollectiveAccess so users are able to browse on a particular metadata element, such as a list.

**Solution**: In the *browse.conf* file, configure a browsing facet of type:Attribute for whichever primary type you need to browse for. You should only configure browsing on metadata elements that have a relatively small range of possible values; for example, browsing on List elements works quite well. Attributes with narrative text content will not work well.

Determine the primary table for which you are configuring a browse (Objects, Entities, Collections, etc.). For example, all the browse facets for Objects are preceded by the following code:

.. code-block::

   # Configuration for object browse
   ca_objects = {
   facets = {

Then, enter the following:

.. code-block::

   name_your_facet = {
   type = attribute,
   element_code = your_metadata_element_code,

   group_mode = none,

   label_singular = _("Enter a Label Here"),
   label_plural = _("Enter a Label Here")
   },

Where **"your_metadata_element_code"** would be replaced by the element code for your chosen field. Be sure to name_your_facet uniquely, and assign the appropriate labels for the facet as well.

Browsing on Related Authorities
-------------------------------

**Problem**: You need to set up the browse function in CollectiveAccess so that users can browse for Objects by related authorities, such as Occurrences.

**Solution**: In browse.conf, Authority facets allow for browsing on cataloging applied to the browsed item from a related authority. If you want to browse for objects by place name, you'd set up a facet of type authority with options to cover the places authority. Here is an example of the code you would enter to browse by Related Occurrences:

.. code-block::

   occurrence_facet = {
			type = authority,
			table = ca_occurrences,
			generate_facets_for_types = 1,
			relationship_table = ca_objects_x_occurrences,
			restrict_to_types = [],
			restrict_to_relationship_types = [],			
			
			groupings = {
				label = _("Name"), 
				type = _("Type"),
				relationship_types = _("Role"),
				ca_attribute_dates_value:years = _("Years"),
				ca_attribute_dates_value:decades = _("Decades")
			},
			
			group_mode = alphabetical,
			
			label_singular = _("occurrence"),
			label_plural = _("occurrences")
		},

Note that if there are multiple Occurrence types, and you wish for a unique browsing facet to be generated for each type, you can use the following setting:

.. code-block::

   generate_facets_for_types = 1,

On the other hand, if there are multiple Occurrence types, and you wish to restrict the browse to a particular type or types, or if you wish to restrict the browse to particular relationship types, enter the List Identifier, or Relationship Type identifier, in the following brackets:

.. code-block::

   restrict_to_types = [],
   restrict_to_relationship_types = [],

Changing Currency Settings
--------------------------


