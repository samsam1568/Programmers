def solution(players, callings):
    # 이름 -> 등수 딕셔너리
    mydict = {players[i]: i for i in range(len(players))}
    
    for name in callings:
        rank = mydict[name]
        front = players[rank - 1]
        
        players[rank], players[rank - 1] = players[rank - 1], players[rank]
        
        mydict[name] -= 1
        mydict[front] += 1
    
    return players