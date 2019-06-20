import csv


class CSVUtils:
    """This class simplifies the process of working with CSV files."""

    def __init__(self):
        pass

    def get_headers(self, infile):
        """
        Get a dictionary where k = header name, v = column index.
        :param infile: CSV file to read from
        :return: dictionary where k = header name, v = column index
        """
        headers_map = {}
        with open(infile) as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                for i in range(len(line)):
                    headers_map[line[i]] = i
                break
        return headers_map

    def read_csv(self, infile, has_headers=True, selected_columns=None):
        """
        Read all lines in a CSV file to a list of lists.
        :param infile: CSV file to read from
        :param has_headers: whether or not the CSV file has a header line; default is True
        :param selected_columns: list of selected columns by either header name or index
        :return: tuple -- contents of CSV file as list of lists, headers dictionary
        """
        headers_map = None
        l1 = False
        if has_headers:
            headers_map = self.get_headers(infile)
            l1 = True
        lines = []
        with open(infile) as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                if l1:
                    # skip reading header line
                    l1 = False
                    continue
                # make sure this line has contents
                if len(line):
                    # pull only selected columns
                    if selected_columns:
                        l = []
                        for c in selected_columns:
                            if isinstance(selected_columns[0], str):
                                # pull selected columns by header
                                l.append(line[headers_map[c]])
                            else:
                                # pull selected columns by index
                                l.append(line[c])
                        if len(l):
                            lines.append(l)
                    else:
                        if len(line):
                            lines.append(line)
        return lines, headers_map