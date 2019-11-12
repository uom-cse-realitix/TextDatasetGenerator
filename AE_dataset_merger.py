from librispeech_negative_data_generator import write_dataset_file

def get_text_data(FILE_PATH, data_class):
    with open(FILE_PATH, 'r') as text_file:
        lines = text_file.read().splitlines()
        if isinstance(data_class, int) and (data_class == 1 or data_class == 2):
            for i in range(len(lines)):
                lines[i] = lines[i] + ', ' + str(data_class) + '\n'
        else:
            raise Exception('Erroneous data class value')

    return lines

POSITIVE_DATASET = '/home/ashen/Documents/Dataset_AE_positive.txt'
NEGATIVE_DATASET = '/home/ashen/Documents/Dataset_AE_negative.txt'
POSITIVE = 1
NEGATIVE = 2

AE_DATASET_FILE = '/home/ashen/Documents/Dataset_AE.txt'

# print(get_text_data(POSITIVE_DATASET, POSITIVE))
positive_data = get_text_data(POSITIVE_DATASET, POSITIVE)
negative_data = get_text_data(NEGATIVE_DATASET, NEGATIVE)
write_dataset_file(AE_DATASET_FILE, positive_data + negative_data)