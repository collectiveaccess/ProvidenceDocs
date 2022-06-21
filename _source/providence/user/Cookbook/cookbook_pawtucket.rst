Cookbook Pawtucket
==================

This section provides some real examples of common challenges that may arise during the configuration of Pawtucket in CollectiveAccess (front-end software). 

Click on a scenario below in the Contents to view problems and solutions. For more support, please see the online `Support Forum <https://collectiveaccess.org/support/>`_, `Online Chat <https://gitter.im/collectiveaccess/support>`_, `Slack Channel for Developers <https://collectiveacc-uye7574.slack.com/join/signup#/domain-signup>`_, and `Back-end <https://github.com/collectiveaccess/providence>`_ and `Front-end <https://github.com/collectiveaccess/pawtucket2>`_ GitHub Repositories. 

Contents
--------

* `Adding Elements to a "Detail" Page`_
* `Adding a List Element to a “Detail” Page`_
* `Adding a Relationship to a “Detail” Page`_
* `Adding a Relationship to a “Detail” Page with Additional Metadata`_
* `Managing Visibility for Sets of Objects in Pawtucket`_

Adding Elements to a "Detail" Page
----------------------------------

**Problem**: You want to add fields (or metadata elements) to the display on a "Detail" page in Pawtucket.

**Solution**: To place metadata elements in the left column of a Detail page, navigate to app.conf. Set the following codes to a list of metadata elements you would like to appear on the Detail page: 

.. code-block::

   ca_objects_detail_display_attributes
   ca_entities_detail_display_attributes
   ca_places_detail_display_attributes
   ca_occurrences_detail_display_attributes, and/or 
   ca_collections_detail_display_attributes 

Note that these codes all share _detail_display, indicating that setting these codes will affect what is displayed in the Detail page. 

Adding a List Element to a “Detail” Page
----------------------------------------

**Problem**: You want to add a list element to the display on a "Detail" page in Pawtucket..

**Solution**: Pass the convertCodesToDisplayText option to get() in the Detail view on your detail page (/themes/default/views/Detail). For example: 

.. code-block::

   if($vs_material = $t_object->get("ca_objects.material" , array('convertCodesToDisplayText' => true))){
			print "<div class='unit'><b>".$t_object->getDisplayLabel("ca_objects.material").":</b> {$vs_material}</div><!-- end unit -->";
			}

Adding a Relationship to a “Detail” Page
----------------------------------------

**Problem**: You want to display a relationship on a record's "Detail" page in Pawtucket.

**Solution**: You'll need to add the relationship(s) in the file for the specific detail page (i.e. ca_collections_detail_html.php) at themes/(your_theme)/views/Detail.
Below shows Related Entities on a Collection detail page: 

.. code-block::

   $va_entities = $t_collection->get("ca_entities", array("returnAsArray" => 1, 'checkAccess' =>$va_access_values)); if(sizeof($va_entities) > 0){	?><div class="unit"><h2><?php print _t("Related")." ".((sizeof($va_entities) > 1) ? _t("Entities") : _t("Entity")); ?></h2>
    <?php
   foreach($va_entities as $va_entity) {print "<div>".(($this->request->config
   >get('allow_detail_for_ca_entities')) ? caNavLink($this->request, $va_entity["label"], '', 'Detail', 'Entity', 'Show', array('entity_id' => $va_entity["entity_id"])) : $va_entity["label"]).(".$va_entity['relationship_typename'].")</div>\n";
				}
    ?>
				</div><!-- end unit -->
    <?php
			}

Adding a Relationship to a “Detail” Page with Additional Metadata
-----------------------------------------------------------------

**Problem**: You want to display a relationship on a record's "Detail" page in Pawtucket, but also pull metadata from the related record, to display on that page in Pawtucket. 

**Solution**: You'll need to add the relationship(s) in the file for the specific detail page (i.e. ca_objects_detail_html.php) at themes/(your_theme)/views/Detail, just like above. 
Additional syntax is required to display the related record's metadata. Below shows Related Occurrences on an object detail page, where the Occurrence Date is displayed along with the Occurrence itself. To configure metadata in your relationship bundle, swap out "Date" for the element code of the data you wish to display: 

.. code-block::

   <code>
   get("ca_occurrences", array("returnAsArray" => 1, 'checkAccess' =>$va_access_values)); if(sizeof($va_occurrences) > 0){	 ?>
   1) ? _t("Occurrences") : _t("Occurrence")); ?>

   <!--T:20-->
   ".(($this->request->config->get('allow_detail_for_ca_occurrences')) ? caNavLink($this->request, $va_occurrence["label"], '', 'Detail', 'Occurrence', 'Show', array('occurrence_id' => $vn_occurrence_id)) : $va_occurrence["label"])." (".$va_occurrence['relationship_typename'].")
   \n"; print "
   "._t("Occurrence Date").": ".$t_occurrence->get('ca_occurrences.DATE')."
   "; } ?>

   <!--T:21→

   </code>

Managing Visibility for Sets of Objects in Pawtucket
----------------------------------------------------

**Problem**: You need to set the "access" value for a set of objects to "public" to allow display in Pawtucket.

**Solution**: Use the Batch Editor tool to set the access values of a set of objects. Prior to CollectiveAccess version 1.7, the only way to batch-set access levels for representations is by writing a script, or by enabling representation editing (set ca_object_representations_disable = 0 in app.conf), then using the batch editor on a set of representations. 

As of CollectiveAccess Version 1.7, a new batch editor bundle is available that allows setting of access on related representations while batching objects.
