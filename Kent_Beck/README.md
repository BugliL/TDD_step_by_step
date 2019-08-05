# Multi concurrency problem

Starting again the problem once the python version is finished.  
Trying to have the whole things to do and starting again.  
We have a DB with prices of things and we want to add a different currency.

For example something like this (same as the book)
<pre>
=================+=====================================
|    Instrument  |   Shares  |   Prices  |   Total    |
==================+====================================
|    IBM         | 1000      | 25        | 25,000     |
+-----------------------------------------------------+
|    GE          | 400       | 100       | 40,000     |
+-----------------------------------------------------+
                             | Total     | 65,000     |
                             +------------------------+
</pre>

This is the result when adding different currencies
<pre>
=================+=====================================
|    Instrument  |   Shares  |   Prices  |   Total    |
==================+====================================
|    IBM         | 1000      | 25 USD    | 25,000 USD |
+-----------------------------------------------------+
|    GE          | 400       | 150 CHF   | 60,000 CHF |
+-----------------------------------------------------+
                             | Total     | 65,000 USD |
                             +------------------------+
</pre>

Doing this, we need to define a change rate of money
<pre>
=================+===================
|   From    |   To      |   Rate    |
==================+==================
|    CHF    |   USD     |   1.5     |
+-----------------------------------+
</pre>

## TODO LIST
  - Add amount of different values
  - Money rounding

  - equals
    - Equal null
    - Equal object
  - hashCode
  - $5 + 10CHF = $10 if rate is 2:1

  * $5 + $5 = $10
  * Multiply amounts Dollars
  * Multiply amounts Franc
  * Amount private
  * Check side effects
  * equals
    * common equal
  * compare dollars and francs
  * $5 * 2 = $10
  * Dollar / Franc duplication

