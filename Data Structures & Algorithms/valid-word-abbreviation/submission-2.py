def valid_abbr(word: str, abbr: str) -> bool:
    w_i = 0
    a_i = 0

    while w_i < len(word) and a_i < len(abbr):
        if word[w_i] == abbr[a_i]:
            w_i += 1
            a_i += 1
            continue
        
        assert word[w_i] != abbr[a_i]
        
        if not abbr[a_i].isdigit():
            return False
        
        assert abbr[a_i].isdigit()
        
        count = 0
        while a_i < len(abbr) and abbr[a_i].isdigit():
            x = int(abbr[a_i])
            if count == 0 and x == 0:
                return False # leading zero not allowed
            count = count * 10 + x
            a_i += 1
        w_i += count
    
    return w_i == len(word) and a_i == len(abbr)

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        return valid_abbr(word, abbr)