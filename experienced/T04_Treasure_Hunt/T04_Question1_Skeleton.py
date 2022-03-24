### OBJECTIVE
"""
If you concatenate all positive integers into a long string you get the following result:
123456789101112131415161718192021...
It can be seen that the 12th digit of this string is 1.
If dn represents the nth digit of the string, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
# def getDN():
#     dn = ''
#     i = 1
#     while (len(dn)<1000000):
#         dn+=str(i)
#         i+=1
#     print(i)
#     return dn


def getDN():
    dn = ''
    for i in range(1,185188):
        dn+=str(i)
    return dn

def get_final_value() -> int:
    dn = getDN()
    total = int(dn[0]) *int(dn[9])*int(dn[99])*int(dn[999])*int(dn[9999])*int(dn[99999])*int(dn[999999])
    return total
### OUTPUT - DO NOT TOUCH
print(get_final_value())
### END OUTPUT