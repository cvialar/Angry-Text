# AnGrY tExT gENeRaToR
import random

if __name__ == "__main__":
	# texttype determines whether the programme will work with user input text or with a text file
	texttype = int(input("text file? 1/0:\n"))
	if texttype == 0:
		en = list(input("Text to process:\n"))
	else:
		with open("angry.txt", "r") as tf:
			en = list(tf.read())

	# discourse management - if text chunks are between quotation marks, only these chunks will be transformed
	if '"' in en:
		dd = 0
	else:
		dd = 1

	# transformation
	j = 0
	for i in range(len(en)):
		j = j + 1
		k = random.randint(1, 7)  # randomisation factor
		if en[i] == '"':
			dd = dd + 1
		if (en[i] not in ["i", "L"]) and (j % 2 == 0) and (k < 6) and (
				dd % 2 != 0):  # swaps 1/2 times, but swaps only if the randomisation factor is active
			# (default: 6/7th of the time), and if the text is between quotation marks if there are some in the text
			en[i] = en[i].swapcase()
	en = "".join(en)

	# export generated text, either to the console or into a text file
	if texttype == 0:
		print(en)
	else:
		with open("angry-result.txt", "w") as tfo:
			tfo.write(en)
