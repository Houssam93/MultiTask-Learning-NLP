# Multitask learning for discovering semantic relations between words

The repository contains the code used for concurrent learning of semantic relations. The code is provided in the form of notebooks.

## Code 
The code is available in the notebook `paper_code_lexical_split_rumen.ipynb`

Requirements: 
- Keras v. 2.1.5
- Tensforflow v. 1.4.5 

## Data
The data of the paper are on the `data` directory. The notebook also assumes access to the [GloVe embeddings](https://nlp.stanford.edu/projects/glove/), in particular [these embeddings](http://nlp.stanford.edu/data/glove.6B.zip).

## Relevant papers
If using the code, please cite our [arxiv paper](https://arxiv.org/pdf/1807.10076.pdf): 
```
@article{balikas2018concurrent,
  title={Concurrent Learning of Semantic Relations},
  author={Balikas, Georgios and Dias, Gael and Moraliyski, Rumen and Amini, Massih-Reza},
  journal={arXiv preprint arXiv:1807.10076},
  year={2018}
}
```
