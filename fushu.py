import re

def build_match_and_apply_functions(pattern,search,replace):
    def matches_rules(word):
        return re.search(pattern,word)
    def apply_rule(word):
        return re.sub(search,replace,word)
    return (matches_rules,apply_rule)

patterns = (('[sxz]$','$','es'),
            ('[^aeioudgkprt]h$','$','es'),
            ('(qu|[^aeiou])y$','y$','ies'),
            ('$','$','s'))

rules = [build_match_and_apply_functions(a,b,c) for (a,b,c) in patterns]

def plura(noun):
    for (match,replace) in rules:
        if (match(noun)):
            return replace(noun)


if __name__ == '__main__':
    testList = ('hello','world','bose','ketty','asdfs','wekljfay')
    for world in testList:
        print(plura(world))
