from .base import base_data_split

def svamp_split(dataset, data_type, keys_list):
    all_dataset, num_data = base_data_split(dataset, data_type, keys_list)
    data_list = [
        [
            example['Body'],
            example['Question'],
            example['Answer']
            ] for example in all_dataset]
    return data_list, num_data
