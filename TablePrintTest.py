#!/usr/bin/python

from TablePrint import TablePrint, TablePrintHeader

'''
TablePrintTest provides a formated table view of a dictionary.
An ordered list of dictionary keys are the column headers
for the dictionary, which identifies which keys in dictionary
to display.

Tested with Python 2.7.10 and 3.5.2.

Author: Mike Robinson
Version: 1.0.0
Last Update:  02/04/2017
'''


def test_defaults():
    data = []
    data.append({"total_misses": 10, "total_hits": 115, "who_cares": 42,
                 "short_name": "short", "marketing_source": "The Best"})
    data.append({"total_misses": 150,
                 "short_name": "A very long value goes here",
                 "who_cares": 1977,
                 "sometimes_name": "present and accounted for sir",
                 "total_hits": 15, "marketing_source": "The Worst"})
    data.append({"total_misses": 20,
                 "short_name": "Something",
                 "who_cares": 1977,
                 "sometimes_name": "Here",
                 "total_hits": 10, "marketing_source": "Shorty"})

    tp = TablePrint()
    tph = TablePrintHeader()

    # Add headers in order from left to right
    tph.add("marketing_source", "Marketing Source")
    tph.add("total_hits", "Total Hits")
    tph.add("short_name", "Short Name")
    tph.add("missing_name", "Missing Name")
    tph.add("sometimes_name", "Sometimes Name")

    print("\nTest defaults (centered) results:\n")
    tp.print_table(data, tph)


def test_right():
    data = []
    data.append({"total_misses": 11, "total_hits": 116, "who_cares": 42,
                 "short_name": "short", "marketing_source": "The Best"})
    data.append({"total_misses": 151,
                 "short_name": "A very long value goes here",
                 "who_cares": 1978,
                 "sometimes_name": "present and accounted for sir",
                 "total_hits": 16, "marketing_source": "The Worst"})
    data.append({"total_misses": 20,
                 "short_name": "Something",
                 "who_cares": 1977,
                 "sometimes_name": "Here",
                 "total_hits": 10, "marketing_source": "Shorty"})

    tp = TablePrint()
    tph = TablePrintHeader()

    # Add headers in order from left to right
    tph.add("marketing_source", "Marketing Source", "right", "right")
    tph.add("total_hits", "Right Hits", "right", "right")
    tph.add("short_name", "Short Name", "right", "right")
    tph.add("missing_name", "Missing Name")
    tph.add("sometimes_name", "Sometimes Name", "right", "right")

    print("\nTest right results:\n")
    tp.print_table(data, tph)


def test_left():
    data = []
    data.append({"total_misses": 12, "total_hits": 117, "who_cares": 42,
                 "short_name": "short",
                 "marketing_source": "The Best"})
    data.append({"total_misses": 152,
                 "short_name": "A very long value goes here",
                 "who_cares": 1979,
                 "sometimes_name": "present and accounted for sir",
                 "total_hits": 17, "marketing_source": "The Worst"})
    data.append({"total_misses": 20,
                 "short_name": "Something",
                 "who_cares": 1977,
                 "sometimes_name": "Here",
                 "total_hits": 10, "marketing_source": "Shorty"})

    tp = TablePrint()
    tph = TablePrintHeader()

    # Add headers in order from left to right
    tph.add("marketing_source", "Marketing Source", "left", "left")
    tph.add("total_hits", "Left Hits", "left", "left")
    tph.add("short_name", "Short Name", "left", "left")
    tph.add("missing_name", "Missing Name")
    tph.add("sometimes_name", "Sometimes Name", "left", "left")

    print("\nTest left results:\n")
    tp.print_table(data, tph)


def test_center():
    data = []
    data.append({"total_misses": 13, "total_hits": 118,
                 "who_cares": 42, "short_name": "short",
                 "marketing_source": "The Best"})
    data.append({"total_misses": 153,
                 "short_name": "A very long value goes here",
                 "who_cares": 1977,
                 "sometimes_name": "present and accounted for sir",
                 "total_hits": 18, "marketing_source": "The Worst"})
    data.append({"total_misses": 20,
                 "short_name": "Something",
                 "who_cares": 1977,
                 "sometimes_name": "Here",
                 "total_hits": 10, "marketing_source": "Shorty"})

    tp = TablePrint()
    tph = TablePrintHeader()

    # Add headers in order from left to right
    tph.add("marketing_source", "Marketing Source")
    tph.add("total_hits", "Center Hits")
    tph.add("short_name", "Short Name", "center", "center")
    tph.add("missing_name", "Missing Name")
    tph.add("sometimes_name", "Sometimes Name", "center", "center")

    print("\nTest center results:\n")
    tp.print_table(data, tph)


def test_mixed():
    data = []
    data.append({"total_misses": 13, "total_hits": 118,
                 "who_cares": 42, "short_name": "short",
                 "marketing_source": "The Best"})
    data.append({"total_misses": 153,
                 "short_name": "A very long value goes here",
                 "who_cares": 1977,
                 "sometimes_name": "present and accounted for sir",
                 "total_hits": 18, "marketing_source": "The Worst"})
    data.append({"total_misses": 20,
                 "short_name": "Something",
                 "who_cares": 1977,
                 "sometimes_name": "Here",
                 "total_hits": 10, "marketing_source": "Shorty"})

    tp = TablePrint()
    tph = TablePrintHeader()

    # Add headers in order from left to right
    tph.add("marketing_source", "Marketing Right", "right", "right")
    tph.add("total_hits", "Total Left", "left", "left")
    tph.add("short_name", "Short Name", "center", "center")
    tph.add("missing_name", "Missing Name")
    tph.add("sometimes_name", "Sometimes Name Right", "right", "right")

    print("\nTest mixed results:\n")
    tp.print_table(data, tph)


def test_table_chars():
    data = []
    data.append({"total_misses": 10, "total_hits": 115,
                 "who_cares": 42, "short_name": "short",
                 "marketing_source": "The Best"})
    data.append({"total_misses": 150,
                 "short_name": "A very long value goes here",
                 "who_cares": 1977,
                 "sometimes_name": "present and accounted for sir",
                 "total_hits": 15, "marketing_source": "The Worst"})
    data.append({"total_misses": 20,
                 "short_name": "Something",
                 "who_cares": 1977,
                 "sometimes_name": "Here",
                 "total_hits": 10, "marketing_source": "Shorty"})

    tp = TablePrint()
    tph = TablePrintHeader()
    tp.set_column_char("!")
    tp.set_header_char("~")
    tp.set_joint_char("*")

    # Add headers in order from left to right
    tph.add("marketing_source", "Marketing Source")
    tph.add("total_hits", "Total Hits")
    tph.add("short_name", "Short Name")
    tph.add("missing_name", "Missing Name")
    tph.add("sometimes_name", "Sometimes Name")

    print("\nTest Table Chars results:\n")
    tp.set_data(data, tph)
    tp.display_table()


def test_table_dict():
    data = []
    data.append({"misses": 10, "hits": 115,
                 "villan": {"name": "Freddy", "age": 40},
                 "director": {"name": "Craven",
                              "sequels":
                                  {"first":
                                      {"name": "Seq1", "year": 1985}}},
                 "victim": {"name": "Mary", "age": 20},
                 "short_name": "short"})
    data.append({"misses": 150,
                 "director":
                     {"name": "Carpenter",
                              "sequels":
                                  {"first":
                                      {"name": "Sq1",
                                          "fans":
                                              {"name": "mike, one"
                                                       " eyed pirate"}}}},
                 "short_name": "A very long value goes here",
                 "villan": {"name": "Jason", "age": 30},
                 "sometimes_name": "present and accounted for sir",
                 "hits": 15})
    data.append({"misses": 20,
                 "short_name": "Something",
                 "sometimes_name": "Here",
                 "hits": 10,
                 "director": {"name": "Donner",
                              "sequels":
                                  {"first":
                                      {"name": "Sq1", "year": 1987,
                                       "fans": {"name": "dave"}}}},
                 "victim": {"name": "Jane", "age": 25}})

    tp = TablePrint()
    tph = TablePrintHeader()

    # Add headers in order from left to right
    tph.add("hits", "Total Hits")
    tph.add("villan:name", "Villan Name")
    tph.add("misses", "Total Misses")
    tph.add("short_name", "Short Name")
    tph.add("victim:age", "Victim Age")
    tph.add("victim:not_here", "Victim Not Here")
    tph.add("director:sequels:first:year", "Sequel Year")
    tph.add("director:sequels:first:fans:name", "Fan Name")

    print("\nTest dictionary entry results:\n")
    tp.print_table(data, tph)


def test_iter():
    data = []
    data.append({"total_misses": 10, "total_hits": 115, "who_cares": 42,
                 "short_name": "short", "marketing_source": "The Best"})
    data.append({"total_misses": 150,
                 "short_name": "A very long value goes here",
                 "who_cares": 1977,
                 "sometimes_name": "present and accounted for sir",
                 "total_hits": 15, "marketing_source": "The Worst"})
    data.append({"total_misses": 20,
                 "short_name": "Something",
                 "who_cares": 1977,
                 "sometimes_name": "Here",
                 "total_hits": 10, "marketing_source": "Shorty"})

    tp = TablePrint()
    tph = TablePrintHeader()

    # Add headers in order from left to right
    tph.add("marketing_source", "Marketing Source")
    tph.add("total_hits", "Total Hits")
    tph.add("short_name", "Short Name")
    tph.add("missing_name", "Missing Name")
    tph.add("sometimes_name", "Sometimes Name")

    print("\nTest table iterator results:\n")
    tp.set_data(data, tph)
    for row in tp:
        print(row)


if __name__ == "__main__":
    test_defaults()
    test_right()
    test_left()
    test_center()
    test_mixed()
    test_table_chars()
    test_table_dict()
    test_iter()

    print("\n*****\nDone\n*****\n")
