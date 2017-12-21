
import string
import re
from sortedcontainers import SortedDict
newList = []
newMeaningList = []

def dictionaryProcessing():
    global newList
    global newMeaningList
    file = open("/Users/Nikita/PycharmProjects/FYPPuzzle/static/dictFile1.txt", "r")
    wordList = []
    meaningList = []
    # lines = file.readlines()
    # lines.sort(key=lambda a_line: a_line.split(" ")[0])


    for line in file:
        lines = line.split(" ", 1)
        if (len(lines) > 1):
            word = lines[0]
            meaning = lines[1]
            wordList.append(word)
            meaningList.append(word + " " + meaning)

    print(len(wordList))

    alphabet = list(string.ascii_uppercase)
    newList = []
    newMeaningList = []

    for index, word in enumerate(wordList):
        word = re.sub(r'[^\w]', ' ', word)
        word = word.replace(" ", "")
        if word not in alphabet:
            if (word != ""):
                word1 = word
                word1 = word1.lower()
                newList.append(word1)
                newMeaningList.append(meaningList[index])


    wd = dict(zip(newList, newMeaningList))
    s = SortedDict(wd)

    for key, value in s.items():
        newList.append(key)
        newMeaningList.append(value)
    # print (wordList[10])
    # print (newList)

    # print(newList)
    # print(newMeaningList)



horiList1= []
horidict1 = []
verList1 = []
verdict1 = []
diagList1 = []
diagdict1 = []
horiList2  = []
horidict2 = []
diagList2 = []
diagdict2 = []
verList3 = []
verdict3 = []
diagList3 = []
diagdict3 = []
diagList4 = []
diagdict4 = []

def getCombinationWords(detected):
    global horiList1
    global horidict1
    global verList1
    global verdict1
    global diagList1
    global diagdict1
    global horiList2
    global horidict2
    global diagList2
    global diagdict2
    global verList3
    global verdict3
    global diagList3
    global diagdict3
    global diagList4
    global diagdict4
    # Get combination of words

    information = {}

    def getHorizontalList(puzzle, direction, original):
        horizontalList = []
        list1 = []
        for i in range(len(puzzle)):
            col = len(puzzle[i])
            strNew = ""
            listA = []
            for j in range(col):
                index1 = i
                index2 = j
                strNew = ""
                indexList = []
                while (index1 != col and index2 != col):
                    strNew += puzzle[index1][index2]
                    strNew = strNew.lower()
                    indexList.append(index2)
                    if len(strNew) > 1:
                        listA.append(direction)
                        if (original == "flip0"):
                            listA.append(i + 1)
                            listA.append(indexList[0] + 1)
                        if (original == "flip1"):
                            listA.append(i + 1)
                            listA.append(col - indexList[0])
                        if (original == "flip2"):
                            listA.append(len(puzzle) - i)
                            listA.append(indexList[0] + 1)

                        if (original == "flip3"):
                            listA.append(len(puzzle) - i)
                            listA.append(col - indexList[0])

                        length = len(strNew)
                        listA.append(length)
                        information[strNew] = listA
                        list1.append(strNew)
                        listA = []
                        #                     print(information)
                        #                     print("-----------------")
                    index2 += 1

        for index, temp in enumerate(list1):
            #     print(temp, len(temp))
            if (len(temp) > 1):
                horizontalList.append(temp)
        return horizontalList, information

    # print(information)

    informationVer = {}

    def getVerticalList(puzzle, direction, original):
        verticalList = []
        list1 = []
        for i in range(len(puzzle)):
            col = len(puzzle[i])
            str = ""
            strNew = ""
            listA = []
            for j in range(col):
                index1 = i
                index2 = j
                strNew = ""
                indexList = []
                while (index1 != col and index2 != col):
                    strNew += puzzle[index1][index2]
                    strNew = strNew.lower()
                    indexList.append(index1)
                    if (len(strNew) > 1):
                        listA.append(direction)
                        if (original == "flip0"):
                            listA.append(indexList[0] + 1)
                            listA.append(j + 1)
                        if (original == "flip1"):
                            listA.append(indexList[0] + 1)
                            listA.append(col - j)
                        if (original == "flip2"):
                            listA.append(len(puzzle) - indexList[0])
                            listA.append(j + 1)
                        if (original == "flip3"):
                            listA.append(len(puzzle) - indexList[0])
                            listA.append(col - j)

                        leng = len(strNew)
                        listA.append(leng)
                        informationVer[strNew] = listA
                        list1.append(strNew)
                        listA = []
                        #                     print(informationVer)
                        #                     print("-----------------")

                    index1 += 1

        for index, temp in enumerate(list1):
            #     print(temp, len(temp))
            if (len(temp) > 1):
                verticalList.append(temp)
        return verticalList, informationVer

    informationDiag = {}

    def getDiagonalList(puzzle, direction, original):
        diagonalList = []
        list1 = []
        for i in range(len(puzzle)):
            col = len(puzzle[i])
            strNew = ""
            listA = []
            for j in range(col):
                index1 = i
                index2 = j
                strNew = ""
                indexList = []
                indexList1 = []
                while (index1 != col and index2 != col):
                    strNew += puzzle[index1][index2]
                    strNew = strNew.lower()
                    indexList.append(index1)
                    indexList1.append(index2)
                    if (len(strNew) > 1):
                        listA.append(direction)
                        if (original == "flip0"):
                            listA.append(indexList[0] + 1)
                            listA.append(indexList1[0] + 1)
                        if (original == "flip1"):
                            listA.append(indexList[0] + 1)
                            listA.append(col - indexList1[0])
                        if (original == "flip2"):
                            listA.append(len(puzzle) - indexList[0])
                            listA.append(indexList1[0] + 1)
                        if (original == "flip3"):
                            listA.append(len(puzzle) - indexList[0])
                            listA.append(col - indexList1[0])

                        leng = len(strNew)
                        listA.append(leng)
                        informationDiag[strNew] = listA
                        list1.append(strNew)
                        listA = []
                        #                     print(informationDiag)
                        #                     print("-----------------")

                    index1 += 1
                    index2 += 1

        for index, temp in enumerate(list1):
            if (len(temp) > 1):
                diagonalList.append(temp)

        return diagonalList, informationDiag

    puzzle = detected

    matchedWords = []
    puzzleVer = []

    direc = ["right", "down", "down and to the right"]
    direcVer = ["left", "down", "down and to the left"]
    direcHori = ["right", "up", "up and to the right"]
    direcVerHori = ["left", "up", "up and to the left"]

    # to shift right to left
    for item in puzzle:
        puzzleVer.append(item[::-1])

    # to shift bottom to top
    puzzleHori = puzzle[::-1]

    puzzleVerHori = []

    # to shift last index to first
    for item in puzzleHori:
        puzzleVerHori.append(item[::-1])

    original = "flip0"

    horiList1, horidict1 = getHorizontalList(puzzle, direc[0], original)
    verList1, verdict1 = getVerticalList(puzzle, direc[1], "flip0")
    diagList1, diagdict1 = getDiagonalList(puzzle, direc[2], "flip0")

    horiList2, horidict2 = getHorizontalList(puzzleVer, direcVer[0], "flip1")
    # verList2 = getVerticalList(puzzleVer, direcVer[1], "flip1") #same as verList1 jastae list
    diagList2, diagdict2 = getDiagonalList(puzzleVer, direcVer[2], "flip1")

    # horiList3 = getHorizontalList(puzzleHori, direcHori[0], "flip2") #same huncha horiList1 jastae
    verList3, verdict3 = getVerticalList(puzzleHori, direcHori[1], "flip2")
    diagList3, diagdict3 = getDiagonalList(puzzleHori, direcHori[2], "flip2")

    # horiList4 = getHorizontalList(puzzleVerHori, direcVerHori[0], "flip3") #same huncha horiList2 jastae
    # verList4 = getVerticalList(puzzleVerHori, direcVerHori[1], "flip3") #same as verlist3
    diagList4, diagdict4 = getDiagonalList(puzzleVerHori, direcVerHori[2], "flip3")

    print(len(horiList1) + len(verList1) + len(diagList1) + len(horiList2) + len(diagList2) + len(verList3) + len(
        diagList3) + len(diagList4))




def LinearSearchImplementation():
    global horiList1
    global horidict1
    global verList1
    global verdict1
    global diagList1
    global diagdict1
    global horiList2
    global horidict2
    global diagList2
    global diagdict2
    global verList3
    global verdict3
    global diagList3
    global diagdict3
    global diagList4
    global diagdict4
    global newMeaningList
    global newList
    # LinearSearch

    matchedMeaning = []
    matchedWords = []
    matchedDirection = []

    for i, item in enumerate(horiList1):
        for j, words in enumerate(newList):
            item = item.lower()
            if item == words and item not in matchedWords:
                matchedDirection.append(horidict1[item])
                matchedWords.append(item)
                matchedMeaning.append(newMeaningList[j])

    for i, item in enumerate(verList1):
        for j, words in enumerate(newList):
            item = item.lower()
            if item == words and item not in matchedWords:
                matchedDirection.append(verdict1[item])
                matchedWords.append(item)
                matchedMeaning.append(newMeaningList[j])

    for i, item in enumerate(diagList1):
        for j, words in enumerate(newList):
            item = item.lower()
            if item == words and item not in matchedWords:
                matchedDirection.append(diagdict1[item])
                matchedWords.append(item)
                matchedMeaning.append(newMeaningList[j])

    for i, item in enumerate(horiList2):
        for j, words in enumerate(newList):
            item = item.lower()
            if item == words and item not in matchedWords:
                matchedDirection.append(horidict2[item])
                matchedWords.append(item)
                matchedMeaning.append(newMeaningList[j])

    for i, item in enumerate(diagList2):
        for j, words in enumerate(newList):
            item = item.lower()
            if item == words and item not in matchedWords:
                matchedDirection.append(diagdict2[item])
                matchedWords.append(item)
                matchedMeaning.append(newMeaningList[j])

    for i, item in enumerate(verList3):
        for j, words in enumerate(newList):
            item = item.lower()
            if item == words and item not in matchedWords:
                matchedDirection.append(verdict3[item])
                matchedWords.append(item)
                matchedMeaning.append(newMeaningList[j])

    for i, item in enumerate(diagList3):
        for j, words in enumerate(newList):
            item = item.lower()
            if item == words and item not in matchedWords:
                matchedDirection.append(diagdict3[item])
                matchedWords.append(item)
                matchedMeaning.append(newMeaningList[j])

    for i, item in enumerate(diagList4):
        for j, words in enumerate(newList):
            item = item.lower()
            if item == words and item not in matchedWords:
                matchedDirection.append(diagdict4[item])
                matchedWords.append(item)
                matchedMeaning.append(newMeaningList[j])

    return (matchedWords, matchedMeaning, matchedDirection)




def initializeTrie():
    global trie
    global newList
    global newMeaningList

    y = []


def TriesImplementation():
    global horiList1
    global horidict1
    global verList1
    global verdict1
    global diagList1
    global diagdict1
    global horiList2
    global horidict2
    global diagList2
    global diagdict2
    global verList3
    global verdict3
    global diagList3
    global diagdict3
    global diagList4
    global diagdict4
    global trie
    global newList
    global newMeaningList


    # Using Tire to detect
    matchedWordsTrie = []
    matchedMeaningTrie = []
    matchedDirectionTrie = []

    class Node:
        def __init__(self):
            self.word = None
            self.nodes = {}  # dict of nodes
            self.meaning = {}  # dict of meaning associated with the nodes

        def __get_all__(self):
            x = []
            for key, node in self.nodes.items():
                if (node.word is not None and node.meaning is not None):
                    x.append(node.word)
                    y.append(node.meaning)
                x += node.__get_all__()
            return x

        def __str__(self):
            return self.word

        def __insert__(self, word, meaning, string_pos=0):
            current_letter = word[string_pos]
            # Create the Node if it does not already exist
            if current_letter not in self.nodes:
                self.nodes[current_letter] = Node();

            if (string_pos + 1 == len(word)):
                self.nodes[current_letter].word = word
                self.nodes[current_letter].meaning = meaning
            else:
                self.nodes[current_letter].__insert__(word, meaning, string_pos + 1)

            return word

        def __get_all_with_prefix__(self, prefix, string_pos):
            x = []
            for key, node in self.nodes.items():
                # If the current character of the prefix is one of the nodes or we have
                # already satisfied the prefix match, then get the matches
                if (string_pos >= len(prefix) or key == prefix[string_pos]):
                    if (node.word is not None):
                        x.append(node.word)

                    if (node.nodes != {}):
                        if (string_pos + 1 <= len(prefix)):
                            x += node.__get_all_with_prefix__(prefix, string_pos + 1)
                        else:
                            x += node.__get_all_with_prefix__(prefix, string_pos)
            return x

        def __check_item_presence__(self, prefix, string_pos):
            item = prefix
            x = []
            for key, node in self.nodes.items():
                # If the current character of the prefix is one of the nodes or we have
                # already satisfied the prefix match, then get the matches
                if (string_pos == len(prefix) or key == prefix[string_pos]):
                    if (node.word is not None):
                        if (node.word == item and len(node.word) == len(item)):
                            x.append(node.word)
                            y.append(node.meaning)

                    if (node.nodes != {} or prefix not in x):
                        if (string_pos + 1 <= len(prefix)):
                            x += node.__check_item_presence__(prefix, string_pos + 1)
                        else:
                            x += node.__check_item_presence__(prefix, string_pos)
            return x

    class Trie:
        def __init__(self):
            self.root = Node()

        def insert(self, word, meaning):
            self.root.__insert__(word, meaning)

        def get_all(self):
            return self.root.__get_all__()

        def get_all_with_prefix(self, prefix, string_pos=0):
            return self.root.__get_all_with_prefix__(prefix, string_pos)

        def get_item_word(self, word, string_pos=0):
            return self.root.__check_item_presence__(word, string_pos)

    y = []
    trie = Trie()
    for i, item in enumerate(newList):
        trie.insert(item, newMeaningList[i])


    for i, item in enumerate(horiList1):
        y = []
        if (len(trie.get_item_word(item)) != 0) and item not in matchedWordsTrie:

            matchedDirectionTrie.append(horidict1[item])
            matchedWordsTrie.append(item)
            matchedMeaningTrie.append(y[0])


    for i, item in enumerate(verList1):
        y = []
        if (len(trie.get_item_word(item)) != 0) and item not in matchedWordsTrie:
            matchedDirectionTrie.append(verdict1[item])
            matchedWordsTrie.append(item)
            matchedMeaningTrie.append(y[0])


    for i, item in enumerate(diagList1):
        y = []
        if (len(trie.get_item_word(item)) != 0) and item not in matchedWordsTrie:
            matchedDirectionTrie.append(diagdict1[item])
            matchedWordsTrie.append(item)
            matchedMeaningTrie.append(y[0])


    for i, item in enumerate(horiList2):
        y = []
        if (len(trie.get_item_word(item)) != 0) and item not in matchedWordsTrie:
            matchedDirectionTrie.append(horidict2[item])
            matchedWordsTrie.append(item)
            matchedMeaningTrie.append(y[0])


    for i, item in enumerate(diagList2):
        y = []
        if (len(trie.get_item_word(item)) != 0) and item not in matchedWordsTrie:
            matchedDirectionTrie.append(diagdict2[item])
            matchedWordsTrie.append(item)
            matchedMeaningTrie.append(y[0])


    for i, item in enumerate(verList3):
        y = []
        if (len(trie.get_item_word(item)) != 0) and item not in matchedWordsTrie:
            matchedDirectionTrie.append(verdict3[item])
            matchedWordsTrie.append(item)
            matchedMeaningTrie.append(y[0])

    for i, item in enumerate(diagList3):
        y = []
        if (len(trie.get_item_word(item)) != 0) and item not in matchedWordsTrie:
            matchedDirectionTrie.append(diagdict3[item])
            matchedWordsTrie.append(item)
            matchedMeaningTrie.append(y[0])


    for i, item in enumerate(diagList4):
        y = []
        if (len(trie.get_item_word(item)) != 0) and item not in matchedWordsTrie:
            matchedDirectionTrie.append(diagdict4[item])
            matchedWordsTrie.append(item)
            matchedMeaningTrie.append(y[0])

    return (matchedWordsTrie, matchedMeaningTrie, matchedDirectionTrie)



def binarySearchImplementation():


    global horiList1
    global horidict1
    global verList1
    global verdict1
    global diagList1
    global diagdict1
    global horiList2
    global horidict2
    global diagList2
    global diagdict2
    global verList3
    global verdict3
    global diagList3
    global diagdict3
    global diagList4
    global diagdict4
    global newList
    global  newMeaningList
    matchedWordsBinarySearch = []
    matchedMeaningBinarySearch = []
    matchedDirectionBinarySearch = []
    meaningDict = dict(zip(newList, newMeaningList))
    newList1 = sorted(newList)

    def find(L, target):
        start = 0
        end = len(L) - 1
        while start <= end:
            middle = (start + end) // 2
            midpoint = L[middle]
            if midpoint > target:
                end = middle - 1
            elif midpoint < target:
                start = middle + 1
            else:
                return midpoint


    for i, item in enumerate(horiList1):
        if (find(newList1, item) != None) and (item not in matchedWordsBinarySearch):
            matchedDirectionBinarySearch.append(horidict1[item])
            matchedWordsBinarySearch.append(item)
            matchedMeaningBinarySearch.append(meaningDict[item])

    for i, item in enumerate(verList1):
        if (find(newList1, item) != None) and (item not in matchedWordsBinarySearch):
            matchedDirectionBinarySearch.append(verdict1[item])
            matchedWordsBinarySearch.append(item)
            matchedMeaningBinarySearch.append(newMeaningList[i])

    for i, item in enumerate(diagList1):
        if (find(newList1, item) != None) and (item not in matchedWordsBinarySearch):
            matchedDirectionBinarySearch.append(diagdict1[item])
            matchedWordsBinarySearch.append(item)
            matchedMeaningBinarySearch.append(newMeaningList[i])

    for i, item in enumerate(horiList2):
        if (find(newList1, item) != None) and (item not in matchedWordsBinarySearch):
            matchedDirectionBinarySearch.append(horidict2[item])
            matchedWordsBinarySearch.append(item)
            matchedMeaningBinarySearch.append(newMeaningList[i])

    for i, item in enumerate(diagList2):
        if (find(newList1, item) != None) and (item not in matchedWordsBinarySearch):
            matchedDirectionBinarySearch.append(diagdict2[item])
            matchedWordsBinarySearch.append(item)
            matchedMeaningBinarySearch.append(newMeaningList[i])

    for i, item in enumerate(verList3):
        if (find(newList1, item) != None) and (item not in matchedWordsBinarySearch):
            matchedDirectionBinarySearch.append(verdict3[item])
            matchedWordsBinarySearch.append(item)
            matchedMeaningBinarySearch.append(newMeaningList[i])

    for i, item in enumerate(diagList3):
        if (find(newList1, item) != None) and (item not in matchedWordsBinarySearch):
            matchedDirectionBinarySearch.append(diagdict3[item])
            matchedWordsBinarySearch.append(item)
            matchedMeaningBinarySearch.append(newMeaningList[i])

    for i, item in enumerate(diagList4):
        if (find(newList1, item) != None) and (item not in matchedWordsBinarySearch):
            matchedDirectionBinarySearch.append(diagdict4[item])
            matchedWordsBinarySearch.append(item)
            matchedMeaningBinarySearch.append(newMeaningList[i])

    return (matchedWordsBinarySearch, matchedMeaningBinarySearch, matchedDirectionBinarySearch)





