import loading
import json

root = "" # Add filepath prefix if needed


class CodonOptimizer:

    def __init__(self, origin_organism: str, target_organism: str):
        self.loader = loading.Loader(amino_acid_file=f"{root}amino_acids.json")

        with open(f'{root}amino_acids.json', 'r') as file:
            self.triplet_codes: dict = json.loads(file.read())

        self.origin_name: str = origin_organism
        self.origin: dict = self.loader.load_codon_usage_table(f'{root}codon_usages/codon_usage_{origin_organism}.csv')
        self.loader.usage_table_to_percentage(self.origin)

        self.target_name: str = target_organism
        self.target: dict = self.loader.load_codon_usage_table(f'{root}codon_usages/codon_usage_{target_organism}.csv')
        self.loader.usage_table_to_percentage(self.target)

    def optimize(self, seq: str, isDNA = False, returnDNA = False) -> str:
        """
        Optimize the sequence given, transcribing it and returning the new sequence.
        :param seq: String of gene sequence
        :param isDNA: Default = False
        :param returnDNA: Default = False
        :return: string of sequence
        """
        if isDNA:
            seq = self.transcription(seq)

        new_sequence = []
        for i in range(0, len(seq), 3): # iterating through tripplets (codons each having 3 acids)
            codon_origin = seq[i: i+3]
            amino_acid = self.triplet_codes["RNA"].get(codon_origin)[0]
            oc_origin = self.origin.get(amino_acid).get(codon_origin)

            min_key = codon_origin  # origin used as initial value

            for key in self.target[amino_acid].keys():
                oc_origin = oc_origin
                oc_target = self.target[amino_acid].get(key)
                diff = abs(oc_origin - oc_target)

                oc_current_min = self.target[amino_acid].get(min_key)
                diff_current = abs(oc_origin - oc_current_min)

                if diff < diff_current:
                    min_key = key

            new_sequence.append(min_key)

        if returnDNA:
            return self.reverse_transcription(''.join(new_sequence))

        return ''.join(new_sequence)

    @staticmethod
    def transcription(seq: str) -> str:
        f"""
        The transcription is the part of the protein bio synthesis where DNA is turned to RNA.\n
        DNA and RNA use different acids (instead of Adenin[A] Uracil[U]) and use the opposite acid (C to G).\n

        :param seq:  DNA sequence
        :return: DNA sequence as RNA sequence
        """
        seq = seq.upper()
        seq = seq.replace('A', 'U')
        seq = seq.replace('T', 'A')
        seq = seq.replace('C', 'X') # X as temporary G
        seq = seq.replace('G', 'C')
        seq = seq.replace('X', 'G')
        return seq

    @staticmethod
    def reverse_transcription(seq: str) -> str:
        f"""
        The reverse transcription is the part of the protein bio synthesis where RNA is turned to DNA.\n
        DNA and RNA use different acids (instead of Adenin[A] Uracil[U]) and use the opposite acid (C to G).\n
        Not all cells use reverse transcription. It is mainly being used by viruses and some bacteria.\n

        :param seq: RNA sequence
        :return: RNA sequence as DNA sequence
        """
        seq = seq.upper()
        seq = seq.replace('A', 'T')
        seq = seq.replace('C', 'X') # X as temporary G
        seq = seq.replace('G', 'C')
        seq = seq.replace("X", "G")
        seq = seq.replace('U', 'A')
        return seq


    def change_organisms(self, origin_organism: str, target_organism):
        self.origin_name = origin_organism
        self.origin = self.loader.load_codon_usage_table(f'{root}codon_usages/codon_usage_{origin_organism}.csv')
        self.loader.usage_table_to_percentage(self.origin)

        self.target_name = target_organism
        self.target = self.loader.load_codon_usage_table(f'{root}codon_usages/codon_usage_{target_organism}.csv')
        self.loader.usage_table_to_percentage(self.target)



