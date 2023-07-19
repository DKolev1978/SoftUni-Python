class vowels:
    def __init__(self, text: str) -> None:
        self.text = text
        self.all_vowels = ['a', 'i', 'e', 'u', 'o', 'y']
        self.current_index = -1
        self.end_index = len(self.text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index > self.end_index:
            raise StopIteration
        current_element = self.text[self.current_index]
        if current_element.lower() in self.all_vowels:
            return current_element
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
