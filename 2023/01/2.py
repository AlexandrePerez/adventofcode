answer = 0
spelled_digits = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
        }
with open('input.txt') as f:
    for line in f:
        digits = []
        last_alphas = ''
        for char in line:
            # handle real digits
            if char.isdigit():
                digits.append(char)
                last_alphas = ''
            # handle letters
            if char.isalpha():
                last_alphas += char
                for spelled_digit, real_digit in spelled_digits.items():
                    if spelled_digit in last_alphas:
                        digits.append(real_digit)
                        last_alphas = last_alphas[-1]  # only keep the last character
                        break

        if len(digits) >= 2:
            answer += int(digits[0] + digits[-1])
        else:
            answer += int(digits[0] + digits[0])
print(answer)
