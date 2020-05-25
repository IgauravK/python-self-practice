def find_it(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
        raise NotFoundError (f'{expected} not found in provided iterable.')

class NotFoundError (Exception):
    pass

print (__name__)