# Integer to Roman

def intToRoman(int_number):
    conv_list = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    str_number = [char for char in str(int_number)]
    collection_roman = []
    max_index = len(str_number)
    for index, item in enumerate(str_number):

        zero_count = max_index - index - 1
        num = int(item + "".join('0' for zero in range(zero_count)))


        for key, value in conv_list.items():
            if num == value:
                collection_roman.append(key)
                break
            else:
                if num != 0 and int(num/value) == int(str(num)[0]) and num not in list(conv_list.values()):
                    roman = "".join([key for i in range(int(num/value))])
                    collection_roman.append(roman)



    for index, roman in enumerate(collection_roman):
        if len(roman) == 4:
            next_index = list(conv_list.keys()).index(roman[0]) + 1
            roman = roman[0] + list(conv_list.keys())[next_index]
            collection_roman[index] = roman

        elif len(roman) > 5 and len(roman) < 9:
            prefix = list(conv_list.keys())[
                (list(conv_list.values()).index(conv_list[roman[0]] * 5))]
            roman = prefix + roman[5:]
            collection_roman[index] = roman

        elif len(roman) == 9:
            roman = roman[0]
            prefix = list(conv_list.keys())[
                (list(conv_list.values()).index(conv_list[roman[0]] * 10))]
            collection_roman[index] = roman + prefix

    return "".join(collection_roman)



tests = [3, 58, 1994]
answers = ['III', 'LVIII', 'MCMXCIV']


for i in range(3):
    answer = intToRoman(tests[i])
    print(f"TEST: {tests[i]}")
    print(f"EXPECTED: {answers[i]}")
    print(f"GOT: {answer}")
    if answer == answers[i]:
        print("PASS")
    else:
        print("FAIL")

    print('----------------------')
    
