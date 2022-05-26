import unittest
import sequence_validation


class SequenceValidationTest(unittest.TestCase):
    def test_max_length(self):
        validator = sequence_validation.SeqValidator('DNA', True, True, 6)
        seq = 'AGGTTACAG'
        result = validator.validate(seq)
        self.assertEqual(result, False)

    def test_valid_letters1(self):
        validator = sequence_validation.SeqValidator('RNA', True, True, 200)
        seq = 'TGGGACTAGTGACACTTATTCCCAACCCATCGGAGCTCACCATTAACGGATCTGCCGTAG'
        result = validator.validate(seq)
        self.assertEqual(result, False)

    def test_valid_letters2(self):
        validator = sequence_validation.SeqValidator('RNA', True, False, 200)
        seq = 'TGGGACTAGTGACACTTATTCCCAACCCATCGGAGCTCACCATTAACGGATCTGCCGTAG'
        result = validator.validate(seq)
        self.assertEqual(result, True)

    def test_valid_letters3(self):
        validator = sequence_validation.SeqValidator('DNA', True, True, 200)
        seq = 'TGGGACTAGTGACACTTATTCCCAACCCATCGGAGCTCACCATTAACGGATCTGCCGTAG'
        result = validator.validate(seq)
        self.assertEqual(result, True)

    def test_div_by_3(self):
        validator = sequence_validation.SeqValidator('DNA', True, True, 200)
        seq = 'TGGGACTAGTGACACTTATTCCCAACCCATCGGAGCTCACCATTAACGGATCTGCCGTA'
        result = validator.validate(seq)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
