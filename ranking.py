from scipy.spatial import distance

# database db is a list of lists
# r is the number of nearest vectors to be retrieved

def NearestR(list, db, r):

    length = len(db)

    distances = []

    for i in range(length):

        dist = distance.euclidean(list,db[i])

        distances.append([dist, i+1])

    distances.sort()

    nearest_r_indices = []

    for i in range(r):

        nearest_r_indices.append(distances[i][1])
        
    return nearest_r_indices            
        
    
    