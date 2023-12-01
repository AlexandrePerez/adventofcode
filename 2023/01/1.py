answer = 0
with open('input.txt') as f:
    for line in f:
        digits = ''.join(c for c in line if c.isdigit())
        if len(digits) >= 2:
            answer += int(digits[0] + digits[-1])
        else:
            answer += int(digits[0] + digits[0])
print(answer)
