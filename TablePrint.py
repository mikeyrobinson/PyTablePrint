try:
    # try to import for Python 2.7
    from cStringIO import StringIO
except ImportError:
    # else import for Python 3.x
    from io import StringIO

from sys import stdout
'''
TablePrint provides a formated table view of a dictionary.
An ordered list of dictionary keys are the column headers
for the dictionary, which identifies which keys in dictionary
to display.

See TablePrintTest.py for example usage.
See TestTablePrint.py for library tests.

Tested with Python versions 2.7.10 and 3.5.2.

Author: Mike Robinson
Version: 1.0.0
Last Update:  01/31/2017
'''


class TablePrintHeader:
    # keep the header string so only calculated once
    __headers = None
    # count used by iterator
    __count = 0

    def add(self, key, column_name, header_align='center',
            column_align='center'):
        '''
        Add new header based to be displayed
        :param key: Key inside the dictionary. Supports option separator ':'
        for multiple keys if nested inside dictionaries
        :param column_name: Printable column header name
        :param header_align: Header alignment [right, center, left]
        :param column_align: Column data alignment [right, center, left]
        :return: NA
        '''
        index = len(self.__headers)
        self.__headers[index] = {"key": key,
                                 "column_name": column_name,
                                 "header_align": header_align.lower(),
                                 "column_align": column_align.lower()}

    def __init__(self):
        self.__headers = {}

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self):
        return self.__next_item__()

    def next(self):
        return self.__next_item__()

    def __next_item__(self):
        self.__count += 1
        if self.__count > len(self.__headers):
            raise StopIteration
        return self.__headers[self.__count - 1]


class TablePrint:
    # re-use header line once set
    __header_line = None

    # array to hold each printable row
    __table_print = None

    # default table characters
    __column_char = "|"
    __header_char = "-"
    __joint_char = "+"

    def __init__(self):
        self.__header_line = None
        self.__table_print = None

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self):
        return self.__next_item__()

    def next(self):
        return self.__next_item__()

    def __next_item__(self):
        self.__count += 1
        if self.__count > len(self.__table_print):
            raise StopIteration
        return self.__table_print[self.__count - 1]

    def __get_char(self, val):
        if len(val) == 0:
            return " "
        else:
            return val[:1]

    def set_column_char(self, ch):
        '''
        Set the table column character
        :param ch: Character for the table column
        :return:
        '''
        self.__column_char = self.__get_char(ch)

    def set_header_char(self, ch):
        '''
        Set the table header/footer character
        :param ch: Character for the table header/footer
        :return: None
        '''
        self.__header_char = self.__get_char(ch)

    def set_joint_char(self, ch):
        '''
        Set the table row/column joint character
        :param ch: Character for the table joint
        :return: None
        '''
        self.__joint_char = self.__get_char(ch)

    def __append(self, row):
        '''
        Append formatted row string to table
        :param row:
        :return: None
        '''
        if not self.__table_print:
            self.__table_print = []
        self.__table_print.append(row)

    def __add_header_line(self, header_lens, filters):
        '''
        Print the header line based on max length of string in column
        such as: "+-----------+------+-----------+"
        Store the header line in header_line for reuse.
        :param header_lens: Title and max length of title
        :param filters: Contains column names and order of columns
        :return: None
        '''
        if not self.header_line:
            self.header_line = StringIO()
            self.header_line.write("%s" % self.__joint_char)
            for name in filters:
                self.header_line.write(
                    str(self.__header_char*(header_lens[name["key"]] + 2)))
                self.header_line.write("%s" % self.__joint_char)

        self.__append(self.header_line.getvalue())

    def __format_data(self, val, length, alignment):
        '''
        Format data for table cell with length and alignment,
        ending with column char
        :param val: value in the table cell
        :param length: length of table cell
        :param alignment: align right, left or center
        :return: table cell string with formatting ending with column char
        '''
        if alignment == "right":
            return str(" %s %s" % (str(val).rjust(length),
                                   self.__column_char))
        elif alignment == "left":
            return str(" %s %s" % (str(val).ljust(length),
                                   self.__column_char))
        else:
            return str(" %s %s" %
                       (str(val).center(length), self.__column_char))

    def __add_headers(self, header_lens, filters):
        '''
        Print header values formatted for max length of string in column
        :param header_lens: Title and max length of title
        :param filters: Contains column names key and order of columns
        :return: None
        '''
        headers = StringIO()
        headers.write(self.__column_char)
        for filter in filters:
            data_cell = self.__format_data(filter["column_name"],
                                           header_lens[filter["key"]],
                                           filter["header_align"])
            headers.write(data_cell)
        self.__append(headers.getvalue())

    def __add_rows(self, data, hdr_lens, filters):
        '''
        Add row values from data dict formatted for column max length
        :param data: Dictionary to print
        :param hdr_lens: Title and max length of title
        :param filters: Ordered list of keys to print from dictionary
        :return: None
        '''
        for row in data:
            row_data = StringIO()
            row_data.write(self.__column_char)
            # Add values for column headers
            for filter in filters:
                # If data_cell not set then add blank cell
                data_cell = None

                # check for keys and add value if found
                if filter["key"] in row:
                    data_cell = self.__format_data(row[filter["key"]],
                                                   hdr_lens[filter["key"]],
                                                   filter["header_align"])
                elif ":" in filter["key"]:
                    # check value in dict object separated by 1 or more ":"
                    dict_val = self.__get_dict_val(row, filter["key"])
                    if dict_val:
                        data_cell = self.__format_data(
                            dict_val,
                            hdr_lens[filter["key"]],
                            filter["header_align"])

                # add formated cell data or blank
                if data_cell:
                    row_data.write(data_cell)
                else:
                    # nothing to print so print blank
                    data_cell = self.__format_data(
                        " ",
                        hdr_lens[filter["key"]],
                        filter["header_align"])
                    row_data.write(data_cell)

            # Add the row of cells
            self.__append(row_data.getvalue())

    def get_table_row(self, row):
        '''
        Get row of table as formatted string (includes alignment)
        :param row: Row number to get
        :return: None
        '''
        if row >= 0 and row < len(self.__table_print):
            return self.__table_print[row]
        return ""

    def display_table(self):
        '''
        Display the table
        :return: None
        '''
        if self.__table_print:
            for row in self.__table_print:
                print(row)

    def set_data(self, data, filters):
        '''
        Store header and width so we know largest width for column key
        :param data: Dictionary values for table data
        :param filters: TablePrintHeader for filtering table data
        :return: None
        '''
        header_lens = {}
        self.header_line = None

        # Default column header width to header title
        for filter in filters:
            header_lens[filter["key"]] = len(filter["column_name"])

        # From row data check greatest width in column data
        for row in data:
            for name in header_lens:
                # header found in filter so process
                if name in row and row[name]:
                    if len(str(row[name])) > header_lens[name]:
                        header_lens[name] = len(str(row[name]))
                elif ":" in name:
                    # check value in dict object separated by 1 or more ":"
                    item = self.__get_dict_val(row, name)
                    if item and len(str(item)) > header_lens[name]:
                        header_lens[name] = len(str(item))

        # add rows
        self.__add_header_line(header_lens, filters)
        self.__add_headers(header_lens, filters)
        self.__add_header_line(header_lens, filters)
        self.__add_rows(data, header_lens, filters)
        self.__add_header_line(header_lens, filters)

    def __get_dict_val(self, dict_val, dict_names):
        '''
        Get dictionary value for from several keys
        :param dict_val: The dict from which to grab value
        :param dict_names: The keys in the dict separated by ':'
        :return: The value of the dict item, else None
        '''
        vals = dict_names.split(":")
        dict_val = dict_val
        while (vals):
            key = vals.pop(0)
            if key in dict_val:
                dict_val = dict_val[key]
            else:
                # Item not found do nothing
                dict_val = None
                break

        return dict_val

    def print_table(self, data, filters):
        '''
        Print formatted table data
        :param data: Dictionary values for table data
        :param filters: TablePrintHeader for filtering table data
        :return: None
        '''
        self.set_data(data, filters)
        self.display_table()
