secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
letdict = {}
num = 1
for letter in str('abcdefghijklmnopqrstuvwxyz'):
    letdict[letter] = num
    num += 1
encrypted = ''
lets = list(letdict.keys())
nums = list(letdict.values())
newchar = ''
newnum = 0
for char in list(secret):
    if char.islower():
        newnum = letdict[char] - cipher
        if newnum <= 0:
            newnum += 26
        newchar = lets[nums.index(newnum)]
    elif char.isupper():
        newnum = letdict[char.lower()] - cipher
        if newnum <= 0:
            newnum += 26
        newchar = lets[nums.index(newnum)]
        newchar.upper()
    else:
        newchar = char
    encrypted += newchar
print(encrypted)
