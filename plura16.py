from newfushu import build_match_and_apply_functions


class LazyRules:
    rules_filname = 'fushuRules.txt'

    def __init__(self):
        self.pattern_file = open(self.rules_filname, encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(pattern, search, replace)
        self.cache.append(funcs)
        return funcs


class MyPlura:
    FILENAME = 'fushuRules.txt'

    def __init__(self):
        self.rules = []
        with open(self.__class__.FILENAME, encoding='utf-8') as fileContents:
            for lines in fileContents:
                a, b, c = lines.split(None, 3)
                self.rules.append(build_match_and_apply_functions(a, b, c))

    def plura(self, word):
        for a, b in self.rules:
            if a(word):
                return b(word)
        return word


if __name__ == '__main__':
    testList = ('hello', 'world', 'bose', 'ketty', 'asdfs', 'wekljfay');
    myp = MyPlura()
    for i in testList:
        print(myp.plura(i))
