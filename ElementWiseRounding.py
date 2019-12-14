def ElementWiseRounding(vector, p, m):
    
    # p is the number of digits to round-up to
    # m is the top-m entries in terms of magnitude in the vector to be selected
    
    l = len(vector)
    
    copy = vector.copy()
    vect = vector.copy()
    
    for i in range(l):
        copy[i] = abs(copy[i])
        
    copy.sort(reverse = True)
    
    key = copy[m-1]
        
    for i in range(l):
        
        vector[i] = round(vector[i], p)
        vector[i] = "pos" + str(i+1) + "val" + str(vector[i])
        
    count = 0
    encoded_vector = []
        
    for i in range(l):
        if(abs(vect[i]) >= key):
            encoded_vector.append(vector[i])
            count = count + 1
        if(count == m):
            break
    
    return encoded_vector
