# LLM dataset

## How to use
https://pypi.org/project/llmdataset/
```
pip install llmdataset
```

## Useful dataset
- GSM8K
```python
llmdataset = main.LLMdataset(dataset_name="gsm8k", subset='main')
```
- MultiArith
```python
llmdataset = main.LLMdataset(dataset_name="ChilleD/MultiArith")
```

- Big Bench Hard
