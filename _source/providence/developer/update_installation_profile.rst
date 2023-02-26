Updating the Installation Profile
=================================

Using the existing installer, it is possible to update a "live" Providence configuration of CollectiveAccess with additions or changes to the profile configuration using a  partial, or "mini," profile. As of CollectiveAccess Version 1.5, an existing configuration can be updated with the mini profile, incorporating the needed additions.

In previous versions of CollectiveAccess, if a profile was reinstalled, the instance of Providence would be entirely overwritten with the new profile. Currently, this function is only accessible via the command line, in `CaUtils <https://manual.collectiveaccess.org/providence/user/administration/caUtils.html?highlight=cautils>`_.

``update-installation-profile``: Updates the installation profile to match a supplied profile name. This function only creates new values and is useful for appending changes from one profile onto another. 

The new profile must exist in a directory that contains the profile.xsd schema and must validate against that schema in order for the update to apply successfully. The directory must also contain base.xml, or whichever base profile is in use.

Options for **update-installation-profile**: 
--------------------------------------------

.. csv-table:: 
   :header-rows: 1
   :file: install_prof_table1.csv