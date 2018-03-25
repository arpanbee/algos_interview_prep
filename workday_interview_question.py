# Complete the function below.

def minimumMoves(a, m):
    i = 0
    moves = 0
    while i < len(a):
        tempA = a[i]
        tempB = m[i]
        stringA = str(tempA)
        stringB = str(tempB)

        x = 0 
        while x < len(stringA):
            intTempA = int(stringA[x])
            intTempB = int(stringB[x])
            while intTempA != intTempB:
                if intTempA < intTempB:
                    intTempA += 1
                    moves += 1
                if intTempA > intTempB:
                    intTempA -= 1
                    moves += 1
            x += 1
        i += 1
        
    return moves
    

