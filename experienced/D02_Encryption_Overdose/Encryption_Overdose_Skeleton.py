### OBJECTIVE
"""
Again you are given a encrypted string that you need to decrypt.

Hint: "APPLE"
"""

### INPUT - DO NOT TOUCH
text = eval(input())
### END INPUT

def decrypt(text):
    decode = [1, 16, 16, 12, 5]
    decoded_string = ""

    for i in text:
        if i == " ":
            decoded_string += " "
            continue

        


### OUTPUT - DO NOT TOUCH
print(decrypt(text))
### END OUTPUT


### EXAMPLE INPUT - YOU MAY COPY THIS INTO THE TERMINAL TO TEST YOUR CODE
### "J DUHJS HUMQMO BUPFT QBUMUI FT CU XASFIJ NZU YV ETNUEZJ FLUD KJDTE TVJ JTJZ MYXQ BBMMDT AUQU NQAUSH VKZ TG CU"

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THIS LINE TO CHECK THE EXAMPLE INPUT
### assert decrypt(text) == "I NEVER REALLY LIKED APPLES TO BE HONEST BUT IF SOMEONE EVER FINDS OUT THEY WILL ALWAYS KEEP MAKING FUN OF ME"