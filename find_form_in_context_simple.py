import re

def trim_text(text):
	for line in text:
		if line.startswith("["):
			page_id = line.strip("[").replace("]", "")
		return page_id

def find_form(text_file, form):
	with open(text_file, "r") as f:
		text = f.read()
		words = re.findall(r"[\w']+", text)
		context = []
		for i in range(len(words)):
			if form == words[i]:
				context.append({"left":words[i-1], "kwic":words[i], "right":words[i+1]})
	return context

my_analysis = find_form("stitny.txt", "jest")
print(my_analysis)
print(len(my_analysis))