import os
import sys

from collections import defaultdict
from pathlib import Path


def main():
    directory = get_directory_from_arguments()
    if not directory:
        exit('Try again with right format "$ python duplicates.py {directory}"')

    file_name_size_paths = collect_files_information_from_directory(directory=directory)

    duplicates = [{name_size: paths} for name_size, paths in file_name_size_paths.items()
                  if len(paths) > 1]
    if not len(duplicates):
        print('Congrats! There is no duplicated files in this directory.')
        return None

    print('There is some duplicated files: ')
    print_name_size_paths(name_size_paths=duplicates)


def get_directory_from_arguments():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        return None

    assert check_path_is_a_directory(path=path), 'Path is not a directory, ' \
                                                 'please, try again with directory path'

    return path


def print_name_size_paths(name_size_paths: list):
    for file_information in name_size_paths:
        ((file_name, file_size), paths), = file_information.items()
        print('File "{}" with size {} bytes.'.format(
            file_name,
            file_size)
        )
        print('Paths:')
        print(*paths, sep="\n")
        print('--------------')


def collect_files_information_from_directory(directory: str):
    print('Collecting files from the directory, and counting files sizes...')
    file_name_size_paths = defaultdict(list)
    for route, directories, file_names in os.walk(directory):
        for file_name in file_names:
            file_path = os.path.join(route, file_name)
            file_size = get_size_of_file(file_path)

            file_name_size_paths[(file_name, file_size)].append(file_path)

    return file_name_size_paths


def get_size_of_file(file_path: str):
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        return file_size


def check_path_is_a_directory(path: str):
    path_to_check = Path(path)
    return path_to_check.is_dir()


if __name__ == '__main__':
    main()
