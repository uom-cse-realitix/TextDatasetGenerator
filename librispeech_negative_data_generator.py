import os
import random

def get_transcript_file_list(DIR_PATH):
    transcript_file_paths = []
    for root, dirs, files in os.walk(DIR_PATH):
        for file in files:
            if file.endswith(".txt"):
                transcript_file_paths.append(os.path.join(root, file))
    return transcript_file_paths

def get_transcripts(FILE_PATH):
    with open(FILE_PATH, 'r') as text_file:
        for line in text_file:
            r = random.randint(1, int(3 * (len(line.split(" ")) / 4)))
            t_lines.append(line.split(' ', r)[r].lower())

def write_dataset_file(DATASET_FILE, lines):
    with open(DATASET_FILE, 'w+') as file:
        for line in lines:
            file.write(line)


DATASET_FILE = '/home/ashen/Documents/Dataset_AE_negative.txt'
t_lines = []

transcripts = get_transcript_file_list("/media/ashen/52DAB5C7DAB5A81D/Users/Ashen/Downloads/LibriSpeech/train-clean-100")

for file_no in range(len(transcripts)):
    get_transcripts(transcripts[file_no])
    if len(t_lines) > 10000 or file_no == len(transcripts) - 1:
        write_dataset_file(DATASET_FILE, t_lines)
        t_lines = []