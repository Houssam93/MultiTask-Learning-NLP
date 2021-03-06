# Multitask learning for discovering semantic relations between words

The repository contains the code used for Learning Lexical-Semantic Relations Using Intuitive
Cognitive Links, this paper will be published in the 41st European Conference on Information Retrieval (ECIR 2019). The code is provided in the form of notebooks.

## Code 
The code is available in the notebook `MultiTaskV0.0-c.ipynb`

Requirements: 
- Keras v. 2.1.5
- Tensforflow v. 1.4.5 

## Data
The data of the paper are on the `data` directory. The notebook also assumes access to the [GloVe embeddings](https://nlp.stanford.edu/projects/glove/), in particular [these embeddings](http://nlp.stanford.edu/data/glove.6B.zip).

## Note

In this first version, and for the sake of reproducing the results displayed in the paper, multi-task network alternates between tasks (in the shared layer) after each epoch and not after each batch. This issue will be improved in future relases

## Relevant papers
If using the code, please cite our paper : 
```
@inproceedings{BalikasECIR2019,
        Author = {Balikas, Georgios and Dias, Ga\"el and Moraliyski, Rumen and
Akhmouch, Houssam and Amini, Massih-Reza},
        Booktitle = {Proceedings of the 41st European Conference on Information
Retrieval (ECIR)},
        Title = {Learning Lexical-Semantic Relations Using Intuitive Cognitive
Links},
        Year = {2019 }
}
```
