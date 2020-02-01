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
    file_data_stack = []
    for path in list_of_file_paths:
        file_name = path.split('/')[-1]
        file_size = get_size_of_file(path)

        file_data_stack.append((file_name, file_size))

    print('Duplicate finding...')
    duplicate_list = []
    for file_data in file_data_stack:
        duplicate_count = file_data_stack.count(file_data)
        if duplicate_count > 1:
            f_name = file_data[0]
            f_size = file_data[1]
            if file_data not in duplicate_list:
                duplicate_list.append(file_data)
                if len(duplicate_list) == 1:
                    print('There is some duplicated files: ')
                print('File "{}" with size {} bytes: {} files'.format(
                    f_name,
                    f_size,
                    duplicate_count))
                print('--------------')

    if len(duplicate_list) == 0:
        print('Congrats! There is no duplicated files in this folder.')


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
