import os


def find_using_loop(suffix, path):
    files = []
    paths = []
    paths.append(path)

    while len(paths) > 0:
        path = paths.pop()
        if os.path.isfile(path):
            if path.endswith(suffix):
                files.append(path)
        else:
            new_paths =  os.listdir(path)
            for item in new_paths:
                paths.append("{}/{}".format(path, item))

    return files

print(find_using_loop('.c', '.'))
print('\n')

print(find_using_loop('', '.'))
print('\n')

print(find_using_loop('.h', '.'))
