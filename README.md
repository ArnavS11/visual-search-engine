# Visual search engine built over Elasticsearch

This repository contains the code for an end-to-end content based image retrieval system based on Elasticsearch.

The project was completed in partial fulfilment of the BITS Pilani curriculum course CS F469: Information Retrieval.

It provides an end-to-end implementation of the research paper ["Towards Practical Visual Search Engine
Within Elasticsearch"](https://arxiv.org/abs/1806.08896).



## Components

- **Dataset** - A dataset on car images by Stanford found [here](https://ai.stanford.edu/~jkrause/cars/car_dataset.html). 

    *Note: A subset of ~600 images from our database of ~16000 car images has been included in this folder for demo purposes*
- `img_to_vec.py` is used to exctract the feature vectors from the image dataset

- `DatabaseExtraction.py` was used for extracting the images from the images folder and converting into encoded string tokens.

- `ElementWiseRounding.py` achieves string token encoding through element-wise rounding of the feature vectors.

- `elasticsearch.py` is the section of code for indexing and as well as searching phases using the encoded string tokens.

- `ranking.py` reranks the results of elasticsearch.py and returns m best result images.

- `app.py` is the python flask server used to search the queries.


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
