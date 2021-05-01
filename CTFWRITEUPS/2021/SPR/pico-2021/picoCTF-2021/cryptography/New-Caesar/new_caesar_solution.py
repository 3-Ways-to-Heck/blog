import base64

given = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
ALPHABET = list("abcdefghijklmnop")

def b16_decode(ciph):
	plain = ""
	ciph = list(ciph)
	enc = [ciph[i * 2:(i + 1) * 2] for i in range((len(ciph) + 2 - 1) // 2)]
	for i in enc:
		bin1 = "{0:04b}".format(ALPHABET.index(i[0]))
		bin2 = "{0:04b}".format(ALPHABET.index(i[1]))
		binary = bin1 + bin2
		c = chr(int(binary, 2))
		plain += c
	return plain

possible_flags = []

for key in ALPHABET:
	enc = ""

	for i in given:
		c = ALPHABET.index(i) + 194 - ord(key)
		f = 1
		while c not in range(97, 113):
			c = ALPHABET.index(i) + 194 - ord(key) + 16 * f
			f += 1
		enc += chr(c)

	possible_flags.append(b16_decode(enc))

print("\n".join(possible_flags))
