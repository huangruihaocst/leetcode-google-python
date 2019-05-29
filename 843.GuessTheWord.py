# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    @staticmethod
    def match(s, t):
        return sum(1 for i in range(len(s)) if s[i] == t[i])
    
    @staticmethod
    def get_max(word, current_list):
        counter = [0] * 7
        for w in current_list:
            counter[Solution.match(word, w)] += 1
        return max(counter)
    
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        correct = 0
        current = wordlist[:]
        times = 0
        while correct < 6 and times < 10:
            min_word, min_max = None, float('inf')
            for w in current:
                _max = Solution.get_max(w, current)
                if _max < min_max:
                    min_word, min_max = w, _max
            correct = master.guess(min_word)
            new = list()
            for w in current:
                if Solution.match(w, min_word) == correct:
                    new.append(w)
            current = new
            times += 1
                
