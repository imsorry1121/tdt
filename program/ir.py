import os
from stemming.porter2 import stem
import re
import math
import json

input_path = "../input/"
intermediat_path = "../intermediate/"
output_path = "../output/"
stopwordFileName = "stopword.txt"
dictionaryFileName = "dictionary.txt"


# Description: build tfidf for the docs
# Input: numbers of docs
# Output: tfidf for every doc in docs folder
# doc: {term: {"tf":,"tfidf":,"t_index"}}
def buildTfidf():
	# 1. stopwords and init
	stopwords = readStopwords()
	docs = dict()
	dictionary = dict()
	termIndex = dict()
	# 2. stem the documents
	for path, folders, filenames in os.walk(input_path):
		for filename in filenames:
			if '.txt' not in filename:
				continue
			doc = getDocTf(os.path.join(path, filename), stopwords)
			docs[path.split("/")[-1]+filename] = doc
	# 3. build dictionary and df 
	for docname, terms in docs.items():
		for term in terms:
			if term not in dictionary.keys():
				dictionary[term] = 1
			else:
				dictionary[term] = dictionary[term]+1
	# 4. write dictionary
	termIndex = writeDictionary(dictionary)
	# 5. build idf
	total = len(docs)
	for (term, df) in dictionary.items():
		dictionary[term] = math.log(float(total)/df, 10)
	# 6. tfidf of every document and unit vector 
	for docname, terms in docs.items():
		norm = float()
		for (term, tf) in terms.items():
			docs[docname][term] = tf * dictionary[term]
			norm += docs[docname][term] ** 2
		norm = math.sqrt(norm)
		for term in terms:
			docs[docname][term] = docs[docname][term]/norm
	# 7. write the unit vector for every doc
	for docname, terms in docs.items():
		with open(output_path+docname, "w") as fo:
			fo.write(json.dumps(terms))
# Description: get the tf of doc 
# Input: filename
# Return: tf dictionary for one doc
def getDocTf(fileName, stopwords):
	doc = dict()
	with open(fileName, "r") as fi:
		for line in fi:
			for word in re.split("[^a-zA-Z0-9]", line.strip()):
				word = word.lower()
				if word != "" and word!="'" and stem(word) not in stopwords:
					if doc.get(stem(word), 0) == 0:
						doc[stem(word)] = 1
					else:
						doc[stem(word)] = doc[stem(word)]+1
	return doc

# Description: get the stopwords by file
# Input: stopword filename
# Return: stopwords
def readStopwords():
	stopwords = list()
	with open(stopwordFileName, "r") as fs:
		for line in fs:
			stopwords.append(line.strip())
	return stopwords

# Description: get the dictionary of the docs
# Input: dictionary with df
# Output: dictionary file
# Return: t_index mapping
def writeDictionary(dictionary):
	# sort by key
	termIndex = dict()
	with open(dictionaryFileName,"w") as fo:
		# header
		fo.write("t_index\tterm\tdf\n")
		i = 1
		for term in sorted(dictionary.keys()):
			fo.write(str(i)+"\t"+term+"\t"+str(dictionary[term])+"\n")
			termIndex[term] = i
			i+=1
	return termIndex



# Description: cosine similarity for two files
def cosine(file1, file2):
	if not os.path.isdir("docs"):
		buildTfidf()
	vector1 = readVector(file1)
	vector2 = readVector(file2)
	sim = float()
	for (key, value) in vector1.items():
		sim += float(value)*float(vector2.get(key, 0))
	print("Cosine similarity between "+file1+" and "+file2+" is "+str(sim))

# Description: read the file to get the tfidf vector of doc
# Input: filename
# Return: vector
def readVector(fileName):
	vector = dict()
	with open(fileName, "r") as fi:
		fi.readline()
		fi.readline()
		for line in fi:
			tmps = line.strip().split("\t")
			index = tmps[0]
			tfidf = tmps[1]
			vector[index] = tfidf
	return vector


		
if __name__ == "__main__":
	buildTfidf()
