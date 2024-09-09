# ConCSE2
**ConCSE: Unified Contrastive Learning and Augmentation for Code-Switched Embeddings**

This repository contains the code and proposed Koglish datasets for our paper [ConCSE: Unified Contrastive Learning and Augmentation for Code-Switched Embeddings](https://arxiv.org/abs/2409.00120)

The contents of the folder are as follows : 
1. koglish_dataset: Contained examples of data from the Koglish-GLUE, Koglish-NLI, and Koglish-STS datasets.
2. Koglish_test: Koglish dataset validation experiment performed in Section 5.1.
3. ConCSE_test: Experiments with our proposed ConCSE from Section 5.2.

### Getting Started ###
```
pip install -r requirements.txt
```

### Download datasets ###
```
from datasets import load_dataset

koglish_glue = load_dataset("Jangyeong/Koglish_GLUE")
koglish_sts = load_dataset("Jangyeong/Koglish_STS")
koglish_sick = load_dataset("Jangyeong/Koglish_SICK")
koglish_sick = load_dataset("Jangyeong/Koglish_NLI")
 
```
