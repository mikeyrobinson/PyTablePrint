# PyTablePrint
Python library to print dictionaries in a formatted table.

Tested with python versions 2.7.10 and 3.5.2 and pep8 version 1.7.0.

### Files:
~~~
   TablePrint.py     - library file with TablePrintHeader and TablePrint classes.
   TestTablePrint.py - unittests for the utility.
   TablePrintTest.py - test examples for library.
~~~

### The library provides the following features:
~~~
1) Header text alignment per column - Center (default), Right, Left
2) Column text alignment per column - Center (default), Right, Left
3) Table format character which can be configured:
   a) Column (default "|")
   b) Header (default "-")
   c) Joint of header and column (default "+")
4) Column headers display text and be confiured
5) Select which dictionary items to diplay
6) Dictionary items with dictionaries can be displayed
~~~

### Examples
~~~
Right-justified headers and columns:
+------------------+------------+-----------------------------+--------------+-------------------------------+
| Marketing Source | Right Hits |                  Short Name | Missing Name |                Sometimes Name |
+------------------+------------+-----------------------------+--------------+-------------------------------+
|         The Best |        116 |                       short |              |                               |
|        The Worst |         16 | A very long value goes here |              | present and accounted for sir |
|           Shorty |         10 |                   Something |              |                          Here |
+------------------+------------+-----------------------------+--------------+-------------------------------+


Left-justified headers and columns:
+------------------+-----------+-----------------------------+--------------+-------------------------------+
| Marketing Source | Left Hits | Short Name                  | Missing Name | Sometimes Name                |
+------------------+-----------+-----------------------------+--------------+-------------------------------+
| The Best         | 117       | short                       |              |                               |
| The Worst        | 17        | A very long value goes here |              | present and accounted for sir |
| Shorty           | 10        | Something                   |              | Here                          |
+------------------+-----------+-----------------------------+--------------+-------------------------------+


Center-justified headers and columns:
+------------------+-------------+-----------------------------+--------------+-------------------------------+
| Marketing Source | Center Hits |          Short Name         | Missing Name |         Sometimes Name        |
+------------------+-------------+-----------------------------+--------------+-------------------------------+
|     The Best     |     118     |            short            |              |                               |
|    The Worst     |      18     | A very long value goes here |              | present and accounted for sir |
|      Shorty      |      10     |          Something          |              |              Here             |
+------------------+-------------+-----------------------------+--------------+-------------------------------+


Mixed justified headers and columns:
+-----------------+------------+-----------------------------+--------------+-------------------------------+
| Marketing Right | Total Left |          Short Name         | Missing Name |          Sometimes Name Right |
+-----------------+------------+-----------------------------+--------------+-------------------------------+
|        The Best | 118        |            short            |              |                               |
|       The Worst | 18         | A very long value goes here |              | present and accounted for sir |
|          Shorty | 10         |          Something          |              |                          Here |
+-----------------+------------+-----------------------------+--------------+-------------------------------+


Override default table format characters:
*~~~~~~~~~~~~~~~~~~*~~~~~~~~~~~~*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*~~~~~~~~~~~~~~*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
! Marketing Source ! Total Hits !          Short Name         ! Missing Name !         Sometimes Name        !
*~~~~~~~~~~~~~~~~~~*~~~~~~~~~~~~*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*~~~~~~~~~~~~~~*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
!     The Best     !    115     !            short            !              !                               !
!    The Worst     !     15     ! A very long value goes here !              ! present and accounted for sir !
!      Shorty      !     10     !          Something          !              !              Here             !
*~~~~~~~~~~~~~~~~~~*~~~~~~~~~~~~*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*~~~~~~~~~~~~~~*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
~~~

