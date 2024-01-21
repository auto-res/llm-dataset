# LLMdataset

## How to use
- Install
    - https://pypi.org/project/llmdataset/
```
pip install llmdataset
```
- Select dataset
```python
from llmdataset import LLMdataset

llmdataset = LLMdataset(
    dataset_name="ChilleD/MultiArith",  # Name of the Dataset on the HuggingFace
    subset="main"　# If the dataset requires the input of a subset, please specify it.
    )
```
- Output setting
```python
dataloader = llmdataset.dataloader(
    data_type='train',
    batch_size=4,
    seed=3655,
    max_data=5
    )
```
- Execution
```python
for i in dataloader:
    print('------')
    print(i)
```

## Useful dataset
Currently available datasets
- GSM8K
    - https://huggingface.co/datasets/gsm8k
```python
llmdataset = LLMdataset(dataset_name="gsm8k", subset='main')
```
- MultiArith
    - https://huggingface.co/datasets/ChilleD/MultiArith
```python
llmdataset = LLMdataset(dataset_name="ChilleD/MultiArith")
```

- Big Bench
    - https://huggingface.co/datasets/bigbench
```python
llmdataset = LLMdataset(dataset_name="tasksource/bigbench", subset = "abstract_narrative_understanding")
```

- Big Bench Hard
    - https://huggingface.co/datasets/lukaemon/bbh
```python
llmdataset = LLMdataset(dataset_name="reasoning-machines/gsm-hard", subset="boolean_expressions")
```

- GSM Hard
    - https://huggingface.co/datasets/reasoning-machines/gsm-hard
```python
llmdataset = LLMdataset(dataset_name="reasoning-machines/gsm-hard")
```

- wikitablequestions
    - https://huggingface.co/datasets/wikitablequestions?row=0
```python
llmdataset = LLMdataset(dataset_name="wikitablequestions")
```

- StrategyQA
    - https://huggingface.co/datasets/ChilleD/StrategyQA?row=0
```python
llmdataset = LLMdataset(dataset_name="ChilleD/StrategyQA")
```

- ARC
    - https://huggingface.co/datasets/allenai/ai2_arc
```python
llmdataset = LLMdataset(dataset_name="allenai/ai2_arc", subset = "ARC-Challenge")
```

- AQuA-RAT
    - https://huggingface.co/datasets/aqua_rat/viewer/raw
```python
llmdataset = LLMdataset(dataset_name="aqua_rat", subset = "raw")
```

- GPQA
    - https://huggingface.co/datasets/Idavidrein/gpqa
```python
llmdataset = LLMdataset(dataset_name="Idavidrein/gpqa", subset = "gpqa_diamond")
```

- SVAP
    - https://huggingface.co/datasets/ChilleD/SVAMP?row=0
```python
llmdataset = LLMdataset(dataset_name="ChilleD/SVAMP")
```

- CommonsenseQA
    - https://huggingface.co/datasets/tau/commonsense_qa
```python
llmdataset = LLMdataset(dataset_name="tau/commonsense_qa")
```
