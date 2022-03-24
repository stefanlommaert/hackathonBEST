### OBJECTIVE ###
"""
You are given a hash. The goal is to find the password that generated the hash and hack your way through the protection.
The password is just a string of integers. As you can see there's a few functions that you can already use. You can also
find the hashfunction. Do not try to brute force the solution. It may be possible to do so with the given example, but
you will need to be smarter for a stronger password.

Disclaimer: This is an educational example and BEST obviously doesn't condone any hacking. Luckily real hashfunctions
are a bit more complicated and less vulnerable than this one.
"""

### INPUT - DO NOT TOUCH ###
retrievedHash = int(input())
### END INPUT ###

### INPUT - DO NOT TOUCH ###
retrievedEncryptedPassword = int(input())
### END INPUT ###

### HELPER FUNCTIONS - READ DOCUMENTATION ###
def myEncryption(password: str) -> int:
    """
    :param password: str: Password to be encrypted
    :return: Returns the hash of a password. -> int
    """
    prime = 17
    result = 1
    for _ in range(len(password)):
        result = result * prime + len(password)
    for digit in password:
        result = result * prime + int(digit)

    return result


def correctLength(givenEncrypted: int, guess: str) -> bool:
    """
    :param givenEncrypted: int: This is the given hash of the password we are trying to find.
    :param guess: str: This is your guess at what the password could be.
    :return: Returns if your guess at what the password could be has the correct length -> bool
    """
    guessLonger: str = guess + "0"
    encryptionGuess: int = myEncryption(guess)
    encryptionGuessLonger: int = myEncryption(guessLonger)
    return givenEncrypted - encryptionGuess >= 0 and not (givenEncrypted - encryptionGuessLonger >= 0) # can we add any digits?


def correctUpToNDigits(givenEncrypted: int, guess: str, n: int) -> bool:
    """
    We check if the guess is correct up to n digits. We do this inductively by checking if it is correct up to n-1 digits
    and checking if the last digit is also correct. This function only behaves the expected way if the guess has the correct
    length.
    :param givenEncrypted: int: The encrypted password.
    :param guess: str: This is your guess at what the password could be.
    :param n: int: How many digits do you think are correct?
    :return: Returns True if the first n digits are correct, otherwise it returns false. -> bool
    """
    if n == 0:
        return True # base case
    digit: int = int(guess[n-1]) # locate the nth digit
    encryptionGuess: int = myEncryption(guess)
    OK: bool = (givenEncrypted - encryptionGuess) >= 0 # check if we aren't too high already
    higherOK: bool = False # initialize this value in case we don't take the branch.. it can't be higher than 9 so False
    if digit < 9:
        guessHigher: str = guess[:n-1] + str(digit + 1) + guess[n:] # guess 1 higher
        encryptionHigher: int = myEncryption(guessHigher)
        higherOK = (givenEncrypted - encryptionHigher) >= 0 # check if this is too high

    return OK and not higherOK and correctUpToNDigits(givenEncrypted, guess, n-1) # if we aren't too high but the next
                                                                # one is, this case is OK, the rest is done inductively
### END HELPER FUNCTIONS ###


def crack(givenHash):
    # TODO
    pass


### EXAMPLE INPUT - YOU MAY COPY THIS LINE INTO YOUR TERMINAL ###
### 2645991644921 ###


### OUTPUT - DO NOT TOUCH ###
result = crack(retrievedEncryptedPassword)
print(result)
### END OUTPUT ###

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THE FOLOWWING LINES TO CHECK YOUR CODE ###
# assert result == "12345"
