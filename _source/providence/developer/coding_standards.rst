Coding Standards
================

* `CSS Standards: Naming Conventions`_ 
* `Indenting`_ 
* `Avoid Inline Styles`_ 
* `Coding Standards`_ 
* `PHP`_ 
* `JS`_ 

CSS Standards: Naming Conventions
---------------------------------

Class and ID names should be written in camelCase, with the first letter of the word lowercase. Use prefixes on class and id names to group classes based on site sections or page area. These styles should be grouped together in the stylesheet, and be preceded by a comment. Be careful reusing id or class names across pages, as changes intended for one page can have adverse effects on another page. For Pawtucket, the following prefixes should be used: 

* Header: head
* Navigation: nav
* Footer: foot
* Home Page: hp
* Light Box: lb
* Results: res
* Detail Pages: dp

If you start using a new prefix, please document it here.
 
Indenting
---------

Unit of indent is the tab. Class/id name declaration and opening curly bracket are on one line, closing curly bracket is on its own line. Style attributes are indented within and on individual lines. For example:

.. code-block::

   #hpContentArea #col1{

   float:left;

   width:250px;

   }

Avoid Inline Styles
-------------------

Styles in CSS files should be as specific as possible. Try to avoid using a bare class name. When styling an object that has a container, the style should reference the container as well as the element being styled. The more verbose the styles are in your CSS, the less likely another element will be influenced on another page accidentally.

The most efficient way to style an element is by styling that type of element inside a container. If only one element needs to be styled in a special way, it should be assigned an id and styled using the id and preferably a container.

See this link for examples: http://en.wikibooks.org/wiki/PHP_Programming/Coding_Standards#CSS_Standards 

Coding Standards
----------------

**HTML: Indenting**

The unit of indent is a tab. For block elements, like <div> and <p>, closing tags should be at the same indent level as the opening tag. Code contained within that block should be indented one level. For example:

.. code-block::
   
   <div>
   This is some text.
   </div>

**Ending Comments**

Put a comment after closing tags to indicate which block is being closed. The comment should reference what the opening tag's class or id is. This is especially important for tags providing structure to the page and unnecessary for most inline elements. For example:

.. code-block::
   <div class="className">

   This is some content <span class="arfClass">arf</span>, <i>meow</i>, <strong>grrrrr</strong>.

   </div><!-- end className -->

PHP
---

**Variable naming**


**Indenting**

Our unit of indent is a tab. In conditional statements, opening curly brackets should be on the same line as the control statement and closing brackets are on their own line, unless followed by an else. The ending brace lines up with the statement it conceptually belongs to and the lines within the brackets are indented one tab. For example:

.. code-block:: 
   
   if($something){
   doSomething();
   }

   if($something){
   doSomething();
   }else{
   doSomethingElse();
   }

This corresponds to The One True Brace Style, 1TBS.

**Commenting**

Use brief, but informative comments to label functions and blocks of code. To make comments visible when quickly scanning a file, format them similar to this:

.. code-block::
   # ---------------------------------------
   # --- this is the comment text
   # ---------------------------------------

JS
--


   
