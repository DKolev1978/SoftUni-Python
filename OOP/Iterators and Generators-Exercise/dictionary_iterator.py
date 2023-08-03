class dictionary_iter:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __iter__(self):
        return


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)