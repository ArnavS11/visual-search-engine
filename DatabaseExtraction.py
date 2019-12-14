from img_to_vec import Img2Vec
from PIL import Image

import os

from ElementWiseRounding import ElementWiseRounding

img2vec = Img2Vec()

input_path = './Cars'

output = open("database_vectors.txt","w") 

count = 0

for file in os.listdir(input_path):

    filename = os.fsdecode(file)

    img = Image.open(os.path.join(input_path, filename))

   	count = count + 1    

    vec = img2vec.get_vec(img)

    flag = 0

    try:
    	vec = vec.tolist()
    except:
    	flag = 1	

    if(flag==1):
	   	continue
    # print(vec)

    encoded_string_vector = ElementWiseRounding(vec, 2 , 64)

    output.write(str(count))
    output.write('\n')
    output.write(str(encoded_string_vector))
    output.write('\n')

    # print(encoded_string_vector)

output.close()
