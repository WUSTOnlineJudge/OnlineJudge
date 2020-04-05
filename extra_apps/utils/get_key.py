from random import choices
from os.path import join, exists
from os import mkdir


def get_random_str(number):
    chrs = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()+"
    return "".join(choices(chrs, k=number))


def get_key(work_dir):
    path = join(work_dir, 'secret.key')
    if not exists(path):
        key = get_random_str(30)
        with open(path, 'w') as f:
            f.write(key)
        return key
    else:
        with open(path, 'r') as f:
            return f.read()

