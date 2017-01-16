import re


def build_match_and_apply_functions(a, b, c):
    def matches_rules(word):
        return re.search(a, word)

    def apply_rule(word):
        return re.sub(b, c, word)

    return (matches_rules, apply_rule)


def rules(rules_filename):
    with open(rules_filename, encoding='utf8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)


def plural(noun, rules_filename='fushuRules.txt'):
    for match_rule, apply_rule in rules(rules_filename):
        if match_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))

def fib (num):
    a,b,i = 0,1,0
    while i < num:
        i+=1
        yield a
        a,b = b,a+b



if __name__ == '__main__':
    testList = ('hello', 'world', 'bose', 'ketty', 'asdfs', 'wekljfay')
    for world in testList:
        print(plural(world))

    for n in fib(10):
        print (n)

    print(set(fib(20)))
