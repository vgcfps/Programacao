values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
number='IV'
total = 0
i = 0
while i < len(number):
    if i+1 < len(number) and values[number[i]]< values[number[i+1]]:
        total += values[number[i+1]]-values[number[i]]
        i +=2
    else:
        total += values[number[i]]    
        i+= 1
print(total)