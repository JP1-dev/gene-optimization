import unittest
import loading


class LoadingTest(unittest.TestCase):
    def test_1(self):
        loader = loading.Loader(amino_acid_file="amino_acids.json")
        table1 = loader.load_codon_usage_table("codon_usages/codon_usage_homo_sapiens.csv")
        self.assertEqual(len(table1.keys()), 23)

    def test_2(self):
        loader = loading.Loader(amino_acid_file="amino_acids.json")
        table = loader.load_codon_usage_table("codon_usages/codon_usage_escherichia_coli_K12.csv")
        loader.usage_table_to_percentage(table)
        print(table.get("proline"))
        for i in table.keys():
            s = 0
            for j in table[i].keys():
                s += table[i][j]
            self.assertAlmostEqual(s, 100)
            break


if __name__ == '__main__':
    unittest.main()
