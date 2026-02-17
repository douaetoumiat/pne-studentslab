from pathlib import Path

FILENAME = "/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/Danio_rerio_U5_sequence.txt"

file_contents = Path(FILENAME).read_text()
line= file_contents.split("\n")
def header(seq):
    sequences = []
    delimeter_space = " "
    for i in range(0,len(seq )):
        if not (seq[i]).startswith(">") :
            sequences.append(seq[i])
    sequence = delimeter_space.join(sequences)

    return (sequence.strip())

print(header(line))