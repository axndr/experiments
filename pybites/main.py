names = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names_set = set(names)
    joined_names = []
    for name in names_set:
        split_names = name.split()
        split_names[0] = split_names[0].title()
        split_names[1] = split_names[1].title()
        joined_names.append(f'{split_names[0]} {split_names[1]}')
    return joined_names


def switch_names(name):
    joined_names = []
    for name in names:
        split_name = name.split()
        split_name[0], split_name[1] = split_name[1], split_name[0]
        joined_names.append(f'{split_name[0]} {split_name[1]}')
    return joined_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    org_names = dedup_and_title_case_names(names)
    ready_for_sort = switch_names(org_names)
    return switch_names(ready_for_sort.sort())

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # ...


if __name__ == '__main__':
    print(dedup_and_title_case_names(names))
    print(sort_by_surname_desc(names))
