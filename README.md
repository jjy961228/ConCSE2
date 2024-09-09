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
* You can download the Koglish dataset using the datasets library as shown below.
* Koglish_glue was used in the experiments in **section 5.1**. 
* In the **ConCSE** experiment in **Section 5.2**, Koglish_sts, Koglish_SICK, and Kolgish NLI were used: Koglish_NLI was used for training, and Koglish_sts and Koglish_SICK were used for testing.
``` python
from datasets import load_dataset

koglish_glue = load_dataset("Jangyeong/Koglish_GLUE")
koglish_nli = load_dataset("Jangyeong/Koglish_NLI")
koglish_sts = load_dataset("Jangyeong/Koglish_STS")
koglish_sick = load_dataset("Jangyeong/Koglish_SICK")
```
 

