digits = {
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000
}


# def main():
# 	number = "MCMXCIV"
# 	converted_digits = [digits[n] for n in list(number)][::-1]
# 	print(converted_digits)
# 	res = 0
# 	for idx, current_digit in enumerate(converted_digits):
# 		if idx == len(converted_digits) - 1:
# 			res += current_digit
# 			break
# 		print(current_digit)
# 		next_digit = converted_digits[idx+1]
# 		if next_digit < current_digit:
# 			res -= current_digit
# 		else:
# 			res += current_digit
# 		print(res)
# 	# print("Res: ", res)
	



# if __name__ == "__main__":
# 	main()