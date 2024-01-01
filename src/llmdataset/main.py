from .dataset.gsm8k import gsm8k_dataset
import random


class LLMdatasets:
    def __init__(
        self,
        dataset_name = None
        ):
        self.dataset_name = dataset_name
        if self.dataset_name:
            self.num_data, self.dataset = self._select_dataset()
            print(f"Number of data:{self.num_data}")

    def _select_dataset(self):
        if self.dataset_name == 'gsm8k':
            count, dataset = gsm8k_dataset(data_type='train')
            return count, dataset

    def dataloader(self, batch_size=1, seed=None, max_data=5):
        if seed is not None:
            random.seed(seed)

        # 現在のデータセットのサイズと max_data を比較
        if max_data is not None and max_data > self.num_data:
            raise ValueError(f"max_data ({max_data}) cannot be greater than the size of the dataset ({self.num_data}).")

        if max_data is not None:
            data_list = random.sample(self.dataset, max_data)
        else:
            data_list = self.dataset[:max_data]

        # バッチサイズでデータセットを分割し、ジェネレータとして提供
        for i in range(0, len(data_list), batch_size):
            yield data_list[i:i + batch_size]

