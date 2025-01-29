# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        result = []

        for w in words:
            if sorted([letter for letter in w]) == sorted([l for l in self.word]): 
                result.append(w)
                
        return result
            

