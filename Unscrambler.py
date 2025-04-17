import os
import time
import datetime

def import_list():
    Words = []
    try:
        file = open("newWordList.txt", "r")#location of your dictionary or provided wordlist
        fileContents = file.readlines() #read text file and store each new line as a string
    except:
        print("Word list file read error,restart program")
        input("Press enter")
        exit()
    finally:
        file.close()
        
    for i in range(len(fileContents)):
        Words.extend(fileContents[i].split()) #changes the list by removing \n's from line breaks in text file
    return Words


def unscramble_word(scrambledWord, wordList):
    countToMatch = len(scrambledWord)   #letter count of the search word
    unscrambled = ""
    flag = 0                            #flag to indicate found word           

    for word in wordList:
        if len(word) == countToMatch:
            count = 0                       #count of search word's letter in dictionary word's letter
            for x in scrambledWord.lower(): #lowercase comparison of words
                if x in word.lower():
                    count += 1
                if count == countToMatch:
                    flag = 1
                    unscrambled = word
                    break
    DSA.end()
    if flag == 0:
        print("Word not found")
    else:
        if len(unscrambled) == countToMatch:
            print("Matched word found: " + unscrambled)

def permutation(scrambled):
    if scrambled == "":         #base case
        return [scrambled]
    else:                       #general case
        arrangements = []
        for part in permutation(scrambled[1:]):
            for index in range(len(part)+1):
                arrangements.append(part[:index]+scrambled[0]+part[index:])
        return arrangements

def unscramblePerm(scrambledWord, wordList):
    flag = 0
    matchedWords = []
    permutations = permutation(scrambledWord)   #array of permutations of scrambled word
    #Linear search in dictionary array
    for word in wordList:
        for arrangement in permutations:
            if arrangement.lower() == word.lower():
                matchedWords.append(word)

    DSA.end()
    if len(matchedWords):
        for word in matchedWords:
            print(scrambledWord, " is ", word)
    else:
        print("Word not found")

class DSA:
    #class made for algorithm stats tools
    #count n and execution time
    executionTime = float(0.0)
    arguments = 0
    currentSystemTime = float(time.time())

    @staticmethod
    def setn(count):
        DSA.arguments = count

    @staticmethod
    def begin():
        DSA.currentSystemTime = float(time.time())

    @staticmethod
    def end():
        executionTime = float(time.time() - DSA.currentSystemTime)
        print("\t\tn =", DSA.arguments, " time taken: ", round(executionTime * 1000, 0)," ms\n")

def menu():
    print("""
***************************
* Welcome to the DefScram *
***************************
""")
    print("We have two unscrambling methods")
    print("1: Character and word check")
    print("2: Permutation existence")
    print("\n3: Exit the program")
           

def choice_input():
    choice = 0
    #input verification
    while not choice in [1,2,3]:
        try: choice = int(input("\n\t Enter your choice: "))
        except: continue
    return choice


def main():
    wordList = import_list()
    menu()
    
    while (True):
        choice = choice_input()
        if choice == 3: exit()

        if choice == 1:
            #Technique 1
            os.system("cls")
            searchWord = input("\n\nEnter your word (avoid a plural word ending with 's')\n ")            
            DSA.setn(len(searchWord))
            DSA.begin()
            unscramble_word(searchWord,wordList)

        if choice == 2:
            #Technique 2
            os.system("cls")
            searchWord = input("\n\nEnter your word (avoid a plural word ending with 's')\n ")
            DSA.setn(len(searchWord))
            DSA.begin()
            unscramblePerm(searchWord,wordList)   

        input("Press enter")
        os.system("cls")
        menu()
        
main()
