import re


def build_match_and_apply_functions(a,b,c):
    def matches_rules(word):
        return re.search(a, word)

    def apply_rule(word):
        return re.sub(b, c, word)

    return (matches_rules, apply_rule)

rules = []
with open('fushuRules.txt', encoding='utf-8') as patterns:
    rules = [build_match_and_apply_functions(*lines.split(None, 3)) for lines in patterns]
    # for lines in patterns:
    #     test = lines.split(None,3)
    #     # pattern,search,replace = lines.split(None,3)
    #     rules.append(build_match_and_apply_functions(test))


def plura(noun):
    for (match, replace) in rules:
        if (match(noun)):
            return replace(noun)


if __name__ == '__main__':
    testList = ('hello', 'world', 'bose', 'ketty', 'asdfs', 'wekljfay')
    for world in testList:
        print(plura(world))
