import os
import os.path

dataset_path = 'aclImdb/test_dataset'


def load_dataset(path):
    data = ''
    if os.path.isdir(path) is not True:
        with open(path) as f:
            data = f.readline()
            return data
    else:
        for each_file in os.listdir(path):
            with open(dataset_path + '/' + each_file) as f:
                data = data + f.readline()
        return data


if __name__ == '__main__':
    test_data = load_dataset(dataset_path)
    test_data = test_data.replace('.', '\n')
    test_data = test_data.replace('<br /><br />', '\n')
    print(test_data)
