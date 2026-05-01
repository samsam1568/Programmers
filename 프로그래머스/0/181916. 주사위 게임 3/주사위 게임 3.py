
def solution(a, b, c, d):
    answer = 0
    dice = {}
    
    for i in [a,b,c,d]:
        if i in dice:
            dice[i] += 1
        else:
            dice[i] = 1
    p,q,r = 0,0,0
    if len(dice.items()) == 1:
        for key,value in dice.items():
            answer = key * 1111

    if len(dice.items()) == 2:
        for key,value in dice.items():
            if value == 3:
                p = key
            if value == 1:
                q = key
        answer = (10*p+q) ** 2
        
        if answer == 0:
            for idx, (key, value) in enumerate(dice.items()):
                if idx == 0:
                    p = key
                if idx == 1:
                    q = key
            answer = (p+q) * abs(p-q)
            
    if len(dice.items()) == 3:
        for key, value in dice.items():
            if value == 2:
                p = key
            if value == 1:
                if q == 0:
                    q = key
                else:
                    r = key
                    
        answer = q * r
        
    if len(dice.items()) == 4:
        answer = min(a,b,c,d)
    
                
    
    
    return answer