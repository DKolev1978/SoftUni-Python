from typing import List


class reverse_iter:
    def __init__(self, list_numbers: List):
        self.list_numbers = list_numbers

    def __iter__(self):
        return self

    def __next__(self) -> List:
        if len(self.list_numbers) == 0:
            raise StopIteration
        return self.list_numbers.pop()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
