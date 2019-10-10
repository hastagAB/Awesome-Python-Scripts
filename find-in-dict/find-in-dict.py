#!/usr/bin/python3
def find_pattern_by_list(my_dict: dict, pattern: list, index=0) -> str:

    try:
        for key, value in my_dict.items():
            if key == pattern[index]:
                return find_pattern_by_list(value[0] if type(value) is list else value, pattern, index + 1)
    except AttributeError:
        return str(my_dict)


def find_first_pattern(my_dict: dict, pattern: str, index=0) -> str:

    try:
        for key, value in my_dict.items():
            if type(value) is not int and (pattern in value or pattern == key):
                try:
                    return value[pattern]
                except TypeError:
                    return value
            elif type(value) is dict or type(value) is list:
                return find_first_pattern(value[0] if type(value) is list else value, pattern, index + 1)

    except AttributeError:
        return str(my_dict)


if __name__ == '__main__':

    my_dict_1 = {
        2: 'message',
        'some_dict': {
            'Id': 1,
            'group': 'DICT',
            'id': 7,
            'name': {
                'test': 'YAY1!',
                'some_key': 'some_value'
            },
            'description': 'This is a dictionary text'
        },
        'id': 123213
    }

    my_dict_2 = {
        'some_dict': {
            'some_array': [
                {
                    'random': 'lolrandom',
                    'message': 'YAY2!'
                }
            ],
            'text': 'message',
            'ContentType': 'application/json',
        }
    }

    pattern_list_1 = ['some_dict', 'name', 'test']
    pattern_1 = 'test'
    pattern_list_2 = ['some_dict', 'some_array', 'message']
    pattern_2 = 'message'

    print(find_pattern_by_list(my_dict_1, pattern_list_1))
    print(find_first_pattern(my_dict_1, pattern_1))
    print(find_pattern_by_list(my_dict_2, pattern_list_2))
    print(find_first_pattern(my_dict_2, pattern_2))