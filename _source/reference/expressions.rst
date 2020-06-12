.. _expressions:

Expressions
===========

Expressions are statements evaluated by CollectiveAccess to a text, numeric or boolean (`true`/`false`) value. Expressions can be used to conditionally trigger (or not) elements of an import mapping or display template, where the boolean value returned determines what happens. Values may be generated through use of functions (described in more detail below), comparisons and mathematical operations.

At its simplest an expression is a number or text quantity. These are examples of perfectly valid expressions:

* 5
* "Software is great"

You'll notice in the examples above that numbers are just numbers while text must be enclosed in quotes (single or double). Any quantity that is non-empty and non-zero will evaluate to "true" meaning that 5 = `true` while 0 = `false`. -1 is also `true`, as it is a non-zero value. Any strings besides "" (no text at all) is `true`, even " " (a single space).

While single values are valid expressions, they're usually only useful when used in conjunction with `operators`. Operators are symbols that take two operands (values), perform some operation, and return a new value based upon the operands. There are several types of operators available in expressions:

Comparison operators
--------------------

Comparison operators compare two operands and return `true` or `false`. The most common operator is "=", which returns `true` if the operands are exactly the same, false if they are not. For example, "wood" = "wood" is `true` whereas "wood" = "cement" is not. In an import mapping it is possible to use the "=" operator to check if an input field is a certain value.  

Other comparison operators are:

* >		greater than
* <		less than
* >=		greater than or equal
* <=		less than or equal
* <>		not equal
* !=		not equal (alternate form)

Greater than/less than operators only work with numeric values. Equal and not equal work with numbers or text.

Boolean comparison
##################

As of version 1.7.9 values representing boolean `true` and `false` are available for use in comparisons. These allow you to more easily test the return value of an expression of function using the bare, unquoted word "true" or "false". For example, this expression:

.. code-block:: none

	dateIsRange("1950's") = false


Would return `true` when dateIsRange() returns false, which is useful for importer actions and display templates where specific behaviors are triggered by true expressions.

Math operators
--------------

With expressions you can perform mathematical operations on numbers using +, -, * and /. These are addition, subtraction, multiplication and division respectively. The + operator also works on text, and will merge two text values together into a single run-on text value. For example:

.. code-block:: none

	4 + 5 			
			
will return the value `9`

.. code-block:: none

	"Julia" + " plus " + "Allison"
	
will return the value `"Julia plus Allison"`

Logical operators
-----------------

It is also possible to string together many expressions into a larger composite expression using the boolean logic operators "AND" and "OR". "AND" returns `true` if, and only if, both operands evaluates as `true`. "OR" returns `true` if, and only if, at least one operand evaluates as `true`. For example:

.. code-block:: none

	(5 > 10) AND ("seth" = "seth")		
	
is false because 5 is not greater than 10, and both expressions need to be true for the composite AND to be true


.. code-block:: none

	(5 > 10) OR ("seth" = "seth")
	
is true because "seth" = "seth" is true and only one needs to be true for logical OR to return true


.. note:: Prior to version 1.7.9 logical operators were required to be upper-case only. Both upper and lower-case operators are now allowed.

Additional comparison operators
-------------------------------

The comparison operators shown above are useful but limited. There are a couple of additional ones that are really where the action is :-) They are:

The "IN" operator
-----------------
"IN" lets you compare a value to a list of values. It returns true if ANY value in the list matches the value you are comparing. For example:

.. code-block:: none

	"Seth" IN ("Julia", "Allison", "Sophie", "Maria", "Angie", "Seth")

returns `true` while

.. code-block:: none

	"Joe" IN ["Julia", "Allison", "Sophie", "Maria", "Angie", "Seth"]		

returns `false`.

There is also a related "NOT IN" operator which will return `true` if the value is not in the list.

The =~ (regular expression) operator
------------------------------------

You can compare a value against a regular expression using the =~ operator. Regular expressions are a very powerful and very flexible pattern matching syntax.  At its most basic a regular expression is a simple bit of text that is matched anywhere in the value being compared. For example:

.. code-block:: none

	"Software is great" =~ /soft/ 

returns `true`.

Note that the regular expression is on the right side of the operator and is enclosed in "/" characters. This is a traditional notation for regular expressions; they are enclosed in the forward slashes to set them off from normal text.

There is also a related !~ operator which will return `true` when the value does not match the regular expression.

Variables
---------

This is all well and good, but the above examples are not terribly useful with hardcoded values in them. Where things start getting truly useful is variables.  Any source in an import record can be used as a variable by prefixing its name with a "^" character. So if you were importing an Excel spreadsheet and wanted to apply rules when the word "allison" appears anywhere in the value of column 4 you'd write

.. code-block:: none

	^4 =~ /allison/

Similarly, if you want to make sure that the value in the 10th column is equal to "metal" then you use the expression:

.. code-block:: none

	^10 = "metal"

If you wanted to make sure that both conditions applied to a record  then you'd use:

.. code-block:: none

	(^4 =~ /allison/) AND (^10 = "metal")

If either would suffice you could use "OR" rather than "AND"

For XML input data the variable names are the XML paths – the exact same thing used in the source specification but with a "^" tacked onto the front.

Functions
---------

Functions are black-boxes that you put a number of values into in order to get a single value out of. The expression system current allows the following functions:

.. csv-table::
   :widths: 10, 40, 30, 10, 10
   :header-rows: 1
   :file: expressions_functions.csv

To include the function-produced value in your expression just add the function name with a paren-enclosed list of values following. For example:

.. code-block:: none

	random(10) > 5  	

returns `true` if the random number between 0 and 10 is greater than 5.

* ceil(5.2)				returns 6
* floor(5.6)			returns 5
* round(5.2)			returns 5
* round(5.6)			returns 6
* length("hello")			returns 5
* sizeof(1,2,3,4)		returns 4
* age("23 June 1912", "7 June 1954") returns 41
* age("7 June 1954", "23 June 1912") returns 41 (order doesn't matter)
* age("7 June 1954", "9 May 1945", "23 June 1912") returns 41 ('extra' dates don't matter)
* age("28 January 1985") returns something > 29; 30 if you run it before 28 January 2016
* agedays("23 June 1912", "7 June 1954") returns 15324
* agedays("1912/06/23") returns something > 37653
* avgdays("1912/06/23 - 1954/06/07", "1985/01/28 - 2015/07/24") returns 13229
* avgdays("1945/01/02 - 1945/01/03", "1985/01/28 - 1985/01/29") returns 1
* formatdate("1985/01/28") returns 2015-08-05T14* 28* 31-04* 00. Note that this result can vary based on your time zone setting in setup.php!
* formatgmdate("1985/01/28") returns 1985-01-28T05* 00* 00+00* 00. Note that this result can vary based on your time zone setting in setup.php!
* formatgmdate("1985/01/28", "Y") returns 1985
* trim(" this text has spaces at the end   ") returns "this text has spaces at the end"
* join(", ", "Smith", "Bob") returns "Smith, Bob"

Parentheses
-----------

You may have noticed that parens have been sprinkled through some of the examples. You can use matched parens to group elements of an expression. This makes it easier to read and also ensures that operators are applied in the desired sequence in complex expressions. The three things you need to know about parens are: (1) each paren'ed sub-expression is evaluated as a single unit, before being combined with other sub-expressions (2) you must always match each opening paren with a closing paren and (3) parens don't hurt anything, but can improve readability of the expression so you are encouraged to use them liberally.
