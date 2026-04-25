def solution(wallpaper):
    answer = []
    file_locationX = []
    file_locationY = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                file_locationX.append(j)
                file_locationY.append(i)
    answer.append(min(file_locationY))
    answer.append(min(file_locationX))
    answer.append(max(file_locationY)+1)     
    answer.append(max(file_locationX)+1)             
          
    return answer