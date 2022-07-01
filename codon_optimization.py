import loading
import json

root = "/home/jp/coding/gene-optimization/"


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
        if isDNA:
            seq = self.transcription(seq)

        new_sequence = []
        for i in range(0, len(seq), 3):
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
        seq = seq.upper()
        seq = seq.replace('A', 'U')
        seq = seq.replace('T', 'A')
        seq = seq.replace('C', 'X') # X as temporary G
        seq = seq.replace('G', 'C')
        seq = seq.replace('X', 'G')
        return seq

    @staticmethod
    def reverse_transcription(seq: str) -> str:
        seq = seq.upper()
        seq = seq.replace('A', 'T')
        seq = seq.replace('C', 'X') # X as temporary G
        seq = seq.replace('G', 'C')
        seq = seq.replace("X", "G")
        seq = seq.replace('U', 'A')
        return seq

    def get_current_setup(self) -> tuple[str, str]:
        return self.origin_name, self.target_name

    def change_organisms(self, origin_organism: str, target_organism):
        self.origin_name = origin_organism
        self.origin = self.loader.load_codon_usage_table(f'{root}codon_usages/codon_usage_{origin_organism}.csv')
        self.loader.usage_table_to_percentage(self.origin)

        self.target_name = target_organism
        self.target = self.loader.load_codon_usage_table(f'{root}codon_usages/codon_usage_{target_organism}.csv')
        self.loader.usage_table_to_percentage(self.target)



