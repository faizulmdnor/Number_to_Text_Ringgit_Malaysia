class nombor_melayu:
    """
    nombor_melayu
    This class converts numeric values into Malay text representation for currency (Ringgit Malaysia).

    Methods:
        number_to_text(num): Converts a number into Malay text format with proper currency denomination.
    """

    @staticmethod
    def number_to_text(num):
        """
        Convert a number into Malay text representation.

        Parameters:
        num (float or int): The number to be converted.

        Returns:
        str: The number in Malay text format.
        """
        units = ['', ' ribu', ' juta', ' bilion', ' trilion']
        ones = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'lapan', 'sembilan']
        special = {10: 'sepuluh', 11: 'sebelas', 12: 'dua belas', 13: 'tiga belas', 14: 'empat belas', 15: 'lima belas',
                   16: 'enam belas', 17: 'tujuh belas', 18: 'lapan belas', 19: 'sembilan belas'}

        def three_digit_to_text(n):
            """
            Convert three-digit numbers into Malay text representation.

            Parameters:
            n (int): The three-digit number.

            Returns:
            str: The number in Malay text format.
            """
            text = ''
            hundreds = n // 100
            remainder = n % 100
            tens = remainder // 10
            ones_digit = remainder % 10

            if hundreds > 0:
                text += ones[hundreds] + ' ratus'
            if remainder > 0:
                if 10 <= remainder <= 19:
                    text += ' ' + special[remainder]
                else:
                    if tens > 0:
                        text += ' ' + ones[tens] + ' puluh'
                    if ones_digit > 0:
                        text += ' ' + ones[ones_digit]
            return text.strip()

        if num == 0:
            return 'kosong'
        elif num == 1:
            return 'satu'

        if isinstance(num, float):
            whole = int(num)
            sen_str = str(num).split('.')[-1].ljust(2, '0')[:2]  # Ambil 2 digit tanpa pembundaran
            sen = int(sen_str)
            if sen > 0:
                return f"{nombor_melayu.number_to_text(whole)} Ringgit dan {nombor_melayu.number_to_text(sen)} Sen Sahaja".strip()
            else:
                return f"{nombor_melayu.number_to_text(whole)} Ringgit Sahaja".strip()

        num_str = str(num)
        if '.' in num_str:
            num_str = num_str.split('.')[0]

        num_str = num_str[::-1]
        parts = [num_str[i:i + 3][::-1] for i in range(0, len(num_str), 3)]
        result = []

        for i, part in enumerate(parts):
            if part.isdigit() and int(part) > 0:
                result.append(three_digit_to_text(int(part)) + units[i])

        return ' '.join(reversed(result)).strip()