Pawtucket2 Site Pages
=====================

.. contents::
   :local:

The site page feature provides users with an easy way to add blog-like functionality to their Pawtuckt2 site through the use of static page templates, which are edited in Providence, and which generate stand-alone pages on their front end. These pages are fully customizable and also allow for media upload through Providence to give users without a background in HTML/CSS the ability to create new pages for their site. This allows for easier editing of About, Contact and other pages that may require occasional updates but which are not part of an organization's digital collections.

There are several components that that provide the design and configuration for these components: the page template(s) (a .tmpl file), your theme's template.conf file in Pawtucket and the Site Page editor in Providence.


General Steps
-------------

    - Create one or more .tmpl files. These provide the HTML markup for each type of site page and contain {{{[field]}}} placeholders for user-supplied values. These pages can use the Bootstrap CSS classes to structure the layout. There are several examples included in the default Pawtucket2 theme.

    - Add and modify a template.conf file to the Pawtucket theme. This file provides title and format instructions how the user-supplied {{{[field]}}} values can be edited, including WYSIWG editor options and others. An example template.conf file is also included in the default Pawtucket2 theme.

    - Run the scan-site-page-templates utility in your Pawtucket's support directory

    - Create site page(s) in Providence using the site page editor

.. note::

    A site page editor must be defined in your configuration file for this to be enabled.


Template (.tmpl) Files
----------------------

These files provide the HTML layout of a site page and include the triple-curly bracketed field placeholders that designate where user-editable text will be included. This layout can be very simple and just provide places for header and body text, or they can provide more structure and customizable fields. A simple example is provided below:

.. code-block:: none

   <h1>{{{title}}}</h1>
   <h3>{{{subtitle}}}</h3>

   <div class="bodytext">
      {{{bodytext}}}
   </div>

template.conf
-------------

This file controls how the user-editable fields defined in your templates (e.g. {{{title}}}) can be edited. This is a fairly short list of options that include the title, description, width and height of the editor that appears in the Providence site page editor. The full list of options is:

.. csv-table::
   :widths: auto
   :header-rows: 1
   :file: ../_static/csv/pawtucket2sitepagestemplate.conf.csv

A simple template.conf file will look like:

::

  fields = {
    title = {
      label = Page title,
      description = Title of page,
      width = 600px,
      height = 1
    },
    bodytext = {
      label = Page text,
      description = Main text for page,
      usewysiwygeditor = 1,
      width = 600px,
      height = 300px
    }
  }

scan-site-page-templates caUtils script
---------------------------------------

Before these pages can be created and/or edited, you must run a caUtils script on the command line in order for Providence to detect the new/changed templates in Pawtucket2. To do so go to the support directory of your pawtucket install and run:

::

    php -f bin/caUtils scan-site-page-templates

Providence Editor
-----------------

.. important::

    If you are implement Site Pages on an older version of Providence it is very likely you have not created an User Interface for editing Site Pages. You must create this interface before you can create/edit these pages (See :ref:`providence-user-interfaces` for more information)

Once you have created the templates and conf file you will be able to create and edit these pages through Manage > Pawtucket > Site Pages. To be made available each page must be assigned a unique URL in the "URL Path" Field. This path '''must''' start with a backslash (e.g. "/About/hours")

The other bundles operate in the same manner as other editors in Providence. Images you upload through the Site Page media bundle are available to embed in any field with WYSIWYG editing enabled. They can be selected by clicking the image icon in the editor's toolbar.

Other Options
-------------

Special placeholders
^^^^^^^^^^^^^^^^^^^^

In your .tmpl files there are several special placeholders that perform specific functions. They are:

.. csv-table::
   :header-rows: 1
   :file: ../_static/csv/pawtucket2sitepagesspecialplaceholders.csv
