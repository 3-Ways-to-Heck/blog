import string

LOWERCASE_OFFSET = ord("a") # 97
ALPHABET = string.ascii_lowercase[:16] # first 16 letters of the alphabet, from a - p

def b16_encode(plain):
	enc = "" # this is the ciphertext that is generated
	for c in plain: # iterate over every character in the plaintext
		binary = "{0:08b}".format(ord(c)) # convert the character's ASCII code into an 8-bit binary number (8 digits, so for example, A is 65 in decimal, so its binary variable would be "01000001")
		enc += ALPHABET[int(binary[:4], 2)] # take the first 4 digits of the binary number, turn it into decimal, get the letter at that decimal index in the "ALPHABET" array, and add it to the "enc" string
		enc += ALPHABET[int(binary[4:], 2)] # do the same for the last 4 digits of the binary variable
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET # subtracts 97 from the ASCII code of the character c
	t2 = ord(k) - LOWERCASE_OFFSET # same thing, but for k, which is just the key variable on line 20
	return ALPHABET[(t1 + t2) % len(ALPHABET)] # this is essentially just an implementation of a regular Caesar Cipher

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key]) # this tells us that every character in key is in the ALPHABET variable, so we can just bruteforce the key
assert len(key) == 1 # awesome! the key is only 1 letter long, so now we know that key is just a letter from a to p

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)]) # since the length of key, len(key), is just 1 (line 22), "key[i % len(key)]" can just be simplified into "key" (because any number mod 1 is just 0); every character of the string b16 is being shifted the same number of positions to the right
print(enc) # enc is the given cipher, "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
