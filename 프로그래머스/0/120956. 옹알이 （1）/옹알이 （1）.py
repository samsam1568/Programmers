from itertools import permutations

def possible_word(word):
    word_list = []
    
    for i in range(len(word)+1):
        perms = list(permutations(word, i))
        word_list.append(["".join(p) for p in perms])
        
    return word_list


def solution(babbling):
    answer = 0
    pw = possible_word(["aya", "ye", "woo", "ma"])
    print(pw)
    for i in babbling:
        for j in pw:
            for k in j:
                if k == i:
                    answer += 1
    
    
    return answer