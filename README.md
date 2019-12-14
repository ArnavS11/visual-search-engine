## File description

img_to_vec.py is used to exctract the feature vectors from the image dataset

DatabaseExtraction.py was used for extracting the images from the images folder and converting into encoded string tokens.

ElementWiseRounding.py achieves string token encoding through element-wise rounding of the feature vectors.

elasticsearch.py is the section of code for indexing and as well as searching phases using the encoded string tokens.

ranking.py reranks the results of elasticsearch.py and returns m best result images.

app.py is the python flask server used to search the queries.


## Instructions to run

1. Clone the repository on your machine.

2. Install the required dependencies -
    - Packages Required(latest versions unless specified otherwise):
    - Anaconda
    - Pytorch
    - Elasticsearch and elasticsearch-py (Elastic Search 6.0)
    - Scipy
    - Numpy
    - Flask

3. Run the command `python3 app.py`

4. Submit any .jpg image of a car via the GUI in app.py, for an expected output of the 4 most similiar(relevant) images in the dataset.
