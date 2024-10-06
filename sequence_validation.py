
class SeqValidator:
    """
        Class for validating sequences. Use function .validate for usage.
    """
    def __init__(self,
                 mode: str,
                 div_by_3: bool,
                 only_base_letters: bool,
                 max_length: int):

        self.mode = mode.upper()
        self.div_by_3 = div_by_3
        self.only_base_letters = only_base_letters
        self.max_len = max_length

    def validate(self, sequence: str) -> bool:
        f"""
            Validation of inputted sequences.\n 
            Parameter: sequence(String)\n
            Output: boolean\n
            Checks if decidable through 3 (tripplets), max length, valid DNA acids and valid RNA acids. 

        """

        validation = True

        length = len(sequence)
        if length > self.max_len:
            validation = False

        elif self.div_by_3 and length % 3 != 0:
            validation = False

        elif self.only_base_letters:
            if self.mode == 'DNA':
                for letter in sequence:
                    if letter != 'A' and letter != 'C' and letter != 'T' and letter != 'G':
                        validation = False

            elif self.mode == 'RNA':
                for letter in sequence:
                    if letter != 'A' and letter != 'C' and letter != 'U' and letter != 'G':
                        validation = False

        return validation
