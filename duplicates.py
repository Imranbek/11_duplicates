import os
import sys

from collections import defaultdict


def main():
    folder = None
    if len(sys.argv) == 2:
        folder = sys.argv[1]

    else:
        exit('Try again with right format "$ python duplicates.py {folder}"')

    print('Collecting files from the folder, and counting files sizes...')

    file_name_size_paths = defaultdict(list)
    for route, directories, file_names in os.walk(folder):
        for file_name in file_names:
            file_path = '{}/{}'.format(route, file_name)
            file_size = get_size_of_file(file_path)

            file_name_size_paths[(file_name, file_size)].append(file_path)

    duplicates = [name_size for name_size, paths in file_name_size_paths.items()
                  if len(paths) > 1]
    if not len(duplicates):
        print('Congrats! There is no duplicated files in this folder.')
        return None

    print('There is some duplicated files: ')
    for file_name_size in duplicates:
        print('File "{}" with size {} bytes: {} files'.format(
            file_name_size[0],
            file_name_size[1],
            len(file_name_size_paths[file_name_size])
        )
        )
        print('--------------')


def get_size_of_file(file_path: str):
    if os.path.isfile(file_path):
        file_size = os.path.getsize(os.path.abspath(os.path.join(file_path)))
        return file_size


if __name__ == '__main__':
    main()
