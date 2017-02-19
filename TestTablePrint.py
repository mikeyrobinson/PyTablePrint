import unittest
from TablePrint import TablePrint, TablePrintHeader


class TestHeaders(unittest.TestCase):
    def test_header_defaults(self):
        index = 0
        header_key = ["header_1", "header_2", "header_3"]
        header_val = ["Header 1", "Header 2", "Header 3"]
        tph = TablePrintHeader()
        tph.add(header_key[0], header_val[0])
        tph.add(header_key[1], header_val[1])
        tph.add(header_key[2], header_val[2])
        for header in tph:
            self.assertEqual(header["key"], header_key[index])
            self.assertEqual(header["column_name"], header_val[index])
            self.assertEqual(header["header_align"], "center")
            self.assertEqual(header["column_align"], "center")
            index += 1

    def header_tester(self, align):
        index = 0
        header_key = ["header_1", "header_2", "header_3",
                      "header_4", "header_5", "header_6"]
        header_val = ["Header 1", "Header 2", "Header 3",
                      "Header 4", "Header 5", "Header 6"]
        tph = TablePrintHeader()
        tph.add(header_key[0], header_val[0], align.capitalize(),
                align.lower())
        tph.add(header_key[1], header_val[1], align.lower(),
                align.capitalize())
        tph.add(header_key[2], header_val[2], align.capitalize(),
                align.capitalize())
        tph.add(header_key[3], header_val[3], align.lower(),
                align.lower())
        tph.add(header_key[4], header_val[4], align.upper(),
                align.lower())
        tph.add(header_key[5], header_val[5], align.lower(),
                align.upper())
        for header in tph:
            self.assertEqual(header["key"], header_key[index])
            self.assertEqual(header["column_name"], header_val[index])
            self.assertEqual(header["header_align"], align.lower())
            self.assertEqual(header["column_align"], align.lower())
            index += 1

    def test_header_left(self):
        self.header_tester("left")

    def test_header_right(self):
        self.header_tester("right".capitalize())

    def test_header_center(self):
        self.header_tester("center".capitalize())

    def test_header_mixed(self):
        index = 0
        header_key = ["header_1", "header_2", "header_3",
                      "header_4", "header_5", "header_6"]
        header_val = ["Header 1", "Header 2", "Header 3",
                      "Header 4", "Header 5", "Header 6"]
        header_align = ["center", "left", "right", "left", "right", "center"]
        column_align = ["left", "right", "left", "center", "center", "right"]
        tph = TablePrintHeader()
        tph.add(header_key[0], header_val[0],
                header_align[0].capitalize(), column_align[0].lower())
        tph.add(header_key[1], header_val[1],
                header_align[1].lower(), column_align[1].capitalize())
        tph.add(header_key[2], header_val[2],
                header_align[2].capitalize(), column_align[2].capitalize())
        tph.add(header_key[3], header_val[3],
                header_align[3].lower(), column_align[3].lower())
        tph.add(header_key[4], header_val[4],
                header_align[4].upper(), column_align[4].lower())
        tph.add(header_key[5], header_val[5],
                header_align[5].lower(), column_align[5].upper())
        for header in tph:
            self.assertEqual(header["key"], header_key[index])
            self.assertEqual(header["column_name"], header_val[index])
            self.assertEqual(header["header_align"],
                             header_align[index].lower())
            self.assertEqual(header["column_align"],
                             column_align[index].lower())
            index += 1


if __name__ == '__main__':
    unittest.main()
