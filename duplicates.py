import os
import sys


def main():
    file_path = None
    if len(sys.argv) == 2:
        file_path = sys.argv[1]

    else:
        exit('Try again with right format "$ python duplicates.py {folder}"')

    print('Collecting files from the folder...')
    list_of_file_paths = load_list_of_file_paths(file_path=file_path)

    print('Counting files sizes...')
    file_name_size_stack = []
    for path in list_of_file_paths:
        file_name_size_stack.append(count_file_size(file_path=path))

    print('Finding duplicates...')
    duplicate_list = []
    for file_name_size in file_name_size_stack:
        file_name_size_count = get_tuple_duplicate_more_than_one(
            file_name_size=file_name_size,
            file_name_size_stack=file_name_size_stack)
        duplicate_list.append(file_name_size_count)

    final_duplicate_list = set(duplicate_list)
    final_duplicate_list.remove(None)

    if not len(final_duplicate_list):
        print('Congrats! There is no duplicated files in this folder.')
        return None

    print('There is some duplicated files: ')
    for file_name_size in final_duplicate_list:
        print('File "{}" with size {} bytes: {} files'.format(
            file_name_size[0],
            file_name_size[1],
            file_name_size[2]))
        print('--------------')


def get_tuple_duplicate_more_than_one(file_name_size: tuple,
                                      file_name_size_stack: list):
    duplicate_count = file_name_size_stack.count(file_name_size)
    if duplicate_count > 1:
        file_name_size_count = (file_name_size[0], file_name_size[1], duplicate_count)
        return file_name_size_count


def count_file_size(file_path: str):
    file_name = file_path.split('/')[-1]
    file_size = get_size_of_file(file_path)
    name_size = (file_name, file_size)

    return name_size


def load_list_of_file_paths(file_path: str):
    files_paths = []
    for r, d, f in os.walk(file_path):
        for file in f:
            files_paths.append(os.path.join(r, file))

    return files_paths


def get_size_of_file(file_path: str):
    if os.path.isfile(file_path):
        file_size = os.path.getsize(os.path.abspath(os.path.join(file_path)))
        return file_size


if __name__ == '__main__':
    main()
