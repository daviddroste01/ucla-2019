dictionary = {

    "tatogucci":"everythings alright",
    "mmg":"mommy made eggs",
    "mmb":"i love my mom",
    "hdp":"happy birthday",
}


sentence="tatogucci mmg mmb hdp"
wordList=sentence.split(" ")
print(wordList)

for word in wordList:
    if word in dictionary.keys():
        print(dictionary[word])
