from img_to_vec import Img2Vec
from PIL import Image
from elasticserch import Elasticsearch
import os

from ElementWiseRounding import ElementWiseRounding

img2vec = Img2Vec()

input_path = './cars_test'

output = open("test_vectors.txt","w") 
#es= Elasticsearch()

count = 0
wrong = 0
for file in os.listdir(input_path):

    filename = os.fsdecode(file)

    img = Image.open(os.path.join(input_path, filename))
    count = count + 1
    flag=0

    try:
      vec = img2vec.get_vec(img)
    except:
      flag=1
    if(flag==1):
      wrong=wrong+1
      continue
    vec = vec.tolist()

    # print(vec)
    
    encoded_string_vector = ElementWiseRounding(vec, 2 , 64)
    

#Elasticsearch indexing

    res=es.index(index='image_index',doc_type='images',id=count,body={
    'image_vector' : str(vec)
    'encoded_strings': str(set(encoded_string_vector))
    })

       	
    output.write(str(count))
    output.write('\n')
    output.write(str(encoded_string_vector))
    output.write('\n')
    
    # print(encoded_string_vector)

output.close()

# Elasticsearch query

    res=es.search(index=index='image_index',doc_type='images',id=count,body={
    
     "size": s,
     "query": {
       "function_score": {
         "functions": [
         {
           "filter": {
             "term": {
              "image_encoded_tokens": "query_encoded_token_1"
              }
            },
            "weight": 1
         },
         ...,
         {
           "filter": {
             "term": {
             "image_encoded_tokens": "query_encoded_token_m"
              }
            },
           "weight": 1
            }
           ],
          "score_mode": "sum",
          "boost_mode": "replace"
          }
      },
    "rescore": {
      "window_size": r,
      "query": {
        "rescore_query": {
          "function_score": {
             "script_score": {
               "script": {
                 "lang": "custom_scripts",
                 "source": "negative_euclidean_distance",
                 "params": {
                   "vector_field": "image_actual_vector",
                   "query_vector":
                     [0.1234, -0.2394, 0.0657, ...]
                   }
                }
              },
              "boost_mode": "replace"
           }
         },
         "query_weight": 0,
         "rescore_query_weight": 1
       }
    }
  }

    })    

