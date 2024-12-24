# import regular expressins packge
# import numbers package

import numpy as np
import re

def readFile(fileName):
    file = open(fileName,'r',encoding="cp437")
    fileText = ""
    for line in file:
        fileText += line
    return fileText
        
# preprocess text   
def preProcess(text):
# Remove non-letter chars
    text = re.sub("[^a-zA-Z ]"," ", text)
# Remove extra spaces
    text = re.sub(" +"," ", text)
# Change characters to lower  
    text = text.lower()
    return text

# generate a word set of a given text
def genDictionary(texts,stopWords):
# concatenate the texts
    allText = ""
    for line in texts:
        allText += line

    # Generate a word list
    wordsList =  allText.split()
    # Generate a word set
    wordsSet =  set(wordsList)
    
# Remove the stop words from the word list    
    stopWordsList = stopWords.split()
    stopWordsSet = set(stopWordsList)    
    dictSet = wordsSet.difference(stopWordsSet)
    return list(dictSet)

# find the distance between arrays
def arrayDist(freqArray1,freqArray2):
    diffArray = freqArray1-freqArray2
#        copute the distance ("pitagoras") 
    sqrArray =  np.square(diffArray)
    sumArray =  np.sum(sqrArray)
    return np.sqrt(sumArray)

def getWordFrequency(texts,dictList):
    dictSize = len(dictList)
    nTexts = len(texts)
    wordFreq = np.empty((nTexts,dictSize),dtype=np.int64)
    for i in range(nTexts):
        print("text" + str(i))
        for j in range(dictSize):        
            wordFreq[i,j] = len(re.findall(dictList[j],texts[i]))
    return wordFreq 

bookTexts = []

#read  and preprocess files 
bookTexts += [readFile('DB1.txt')]
bookTexts += [readFile('DB2.txt')]
bookTexts += [readFile('Eliot1.txt')]
bookTexts += [readFile('Eliot2.txt')]

texts = []
for text in bookTexts:
    texts += [preProcess(text)]
    
# Read stop words file - words that can be removed
stopWords = readFile('stopwords_en.txt')

# get dictionary list
dictList = genDictionary(texts,stopWords)

# Find the frequency of the dictionary words in the files
wordFreq = getWordFrequency(texts,dictList)

# find the distance matrix between the text files
rows,colomns = wordFreq.shape
dist = np.empty((rows,rows))
for i in range(rows): 
    for j in range(rows):
        # calculate the distance between the frequency vectors
        dist[i,j] = arrayDist(wordFreq[i],wordFreq[j])
np.set_printoptions(precision=0)
print("dist matrix = \n",dist)        