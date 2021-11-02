def romanToInt(s: str) -> int:
    sum_so_far = 0
    for i in range(len(s)-1, -1, -1):
        #print(i)
        if s[i] == 'I':
            sum_so_far += 1 if sum_so_far < 5 else -1
        elif s[i] == 'V':
        	sum_so_far += 5
        elif s[i] == 'X':
        	sum_so_far += 10 if sum_so_far < 50 else -10
        elif s[i] == 'L':
        	sum_so_far += 50 
        elif s[i] == 'C':
        	sum_so_far += 100 if sum_so_far < 500 else -100
        elif s[i] == 'D':
        	sum_so_far += 500
        else:
        	sum_so_far += 1000
    return sum_so_far


if __name__ == "__main__":
    #'III'
    #'IV'
    print(romanToInt('MCMXCIV'))