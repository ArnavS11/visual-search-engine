from img_to_vec import Img2Vec
from PIL import Image

from ElementWiseRounding import ElementWiseRounding

img2vec = Img2Vec()

img = Image.open('messi.jpg')

vec = img2vec.get_vec(img)

vec = vec.tolist()
    
encoded_string_vector = ElementWiseRounding(vec, 2 , 64)

print(encoded_string_vector)    	