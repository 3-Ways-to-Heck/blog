import base64

given = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"

alpha = list("abcdefghijklmnop")

def b16_d(ciph):
	plain = ""
	ciph = list(ciph)
	enc = [ciph[i * 2:(i + 1) * 2] for i in range((len(ciph) + 2 - 1) // 2)]
	for i in enc:
		bin1 = "{0:04b}".format(alpha.index(i[0]))
		bin2 = "{0:04b}".format(alpha.index(i[1]))
		binary = bin1 + bin2
		c = chr(int(binary, 2))
		plain += c
	return plain

all_flags = []

for key in alpha:
	unshifted = ""

	for i in given:
		c = alpha.index(i) + 194 - ord(key)
		f = 1
		while c not in range(97, 113):
			c = alpha.index(i) + 194 - ord(key) + 16 * f
			f += 1
		unshifted += chr(c)

	all_flags.append(b16_d(unshifted))

print("\n".join(all_flags))
