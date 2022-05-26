import unittest
import codon_optimization


class CodonOptimizationTest(unittest.TestCase):
    def test_reverse_transcription(self): # return after reverse transcription
        opt = codon_optimization.CodonOptimizer("homo_sapiens", "escherichia_coli_K12")
        dna = opt.reverse_transcription("UUGCUCGCAUCAAAGgNNNN")
        self.assertEqual("AACGAGCGTAGTTTCCNNNN", dna)

    def test_transcription(self):
        opt = codon_optimization.CodonOptimizer("homo_sapiens", "escherichia_coli_K12")
        rna = opt.transcription("AACGAGCGTAGTTTCcNN")
        self.assertEqual("UUGCUCGCAUCAAAGGNN", rna)

    def test_optimization_rna(self):
        opt = codon_optimization.CodonOptimizer("homo_sapiens", "escherichia_coli_K12")
        print()
        seq = opt.optimize("UCU", isDNA=False)
        self.assertEqual("UCG", seq)

    def test_optimization_dna(self):
        opt = codon_optimization.CodonOptimizer("homo_sapiens", "escherichia_coli_K12")
        print()
        seq = opt.optimize("TCATCATCATCA", isDNA=True)
        self.assertEqual("UCAUCAUCAUCA", seq)


if __name__ == '__main__':
    unittest.main()
