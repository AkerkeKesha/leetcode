
def romanToInt(s: str) -> int:
    roman_symbols = {
    'I': 1, 
    'V': 5, 
    'X': 10, 
    'L': 50, 
    'C': 100,
    'D': 500,
    'M': 1000
    }
    # subtraction_symbols = {'IX': 9, 'IV': 4, 'XL': 40, 'XC': 90, 'CD':400, 'CM': 900}

    result = 0
    for i in range(len(s)-1,-1,-2):
        current_char = s[i]
        next_char = s[i-1]
        print( str(roman_symbols[current_char]) + ' ; ' + str(roman_symbols[next_char]))
        result += roman_symbols[current_char] + roman_symbols[next_char]
        if next_char == 'I' and current_char in ['V', 'X']:
        	print('do -1')
        	--result
        elif next_char == 'X' and current_char in ['L', 'C']:
        	print('do -10')
        	result -= 10
        elif next_char == 'C' and current_char in ['D', 'M']:
        	print('do -100')
        	result -= 100
        print('result: ' + str(result))
    return result


if __name__ == "__main__":
	print(romanToInt('MCMXCIV'))