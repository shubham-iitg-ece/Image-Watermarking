def isValid(i, j, M, N):
    if(i >= 0 and i < M and j >= 0 and j < N):
        return True
    else:
        return False

def mean_filter(img, x, y):
    value = 0
    N = 0
    dx = [0, 1, 1, 1, 0, 0, -1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, 0, -1]
    
    for l in range(9):
        i = x+dx[l]
        j = y+dy[l]
        if(isValid(i, j, original_height, original_width)):
            value+=img[i, j]
            N+=1

    return value/float(N)

def exor(x ,y):
    if(x == 0 and y == 0):
        return 0
    elif(x == 0 and y != 0):
        return 255
    elif(x != 0 and y == 0):
        return 255
    elif(x !=0 and y != 0):
        return 0
