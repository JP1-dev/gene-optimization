import json


class Loader:
    def __init__(self, amino_acid_file):
        self.amino_acid_file = amino_acid_file
        with open(self.amino_acid_file, 'r') as file:
            self.triplet_codes = json.loads(file.read())

    def load_codon_usage_table(self, file_name: str, delim=")  ") -> dict:
        raw = []
        data = {}

        with open(file_name) as file:
            for line in file:
                if line == '\n':
                    continue
                raw.append(self.remove_parenthesis(line.split(delim)))

        for row in raw:
            for element in row:
                element = element.split(' ')
                triplet = element[0]
                counter = float(element[-1])
                amino_acid = self.triplet_codes['RNA'].get(triplet)[0]
                if data.get(amino_acid) is None:
                    data[amino_acid] = {triplet: counter}
                else:
                    data[amino_acid][triplet] = counter

        return data

    @staticmethod
    def remove_parenthesis(lst: list) -> list:
        new_lst = []
        for i in lst:
            new_lst.append(i.split('(')[0])
        return new_lst

    @staticmethod
    def usage_table_to_percentage(table: dict):
        for acid in table.keys():
            sum = 0.0000000001
            for codon in table[acid]:
                sum += table[acid][codon]

            for codon in table[acid]:
                table[acid][codon] = (table[acid][codon] / sum) * 100
