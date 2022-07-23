# Roman to integer



class Solution(object):
    def romanToInt(self, roman_last):
        conv_list = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        valid_list = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        valid_list_reverse = {
            'VI': 6,
            'XI': 11,
            'LX': 60,
            'CX': 110,
            'DC': 600,
            'MC': 1100,
        }
        addition = []
        
        for xyz in range(2):
            for key, value in valid_list.items():
                if key in roman_last:
                    addition.append(value)
                    roman_last = "".join(roman_last.split(key))
            valid_list = valid_list_reverse
    
        for char in roman_last:
            for key, value in conv_list.items():
                if key == char:
                    addition.append(value)

        return sum(addition)


solution = Solution()

print(f"Sum is: {solution.romanToInt('XVIII')}")


