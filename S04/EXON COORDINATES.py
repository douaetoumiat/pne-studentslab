from pathlib import Path

def header(seq):
    sequences = []
    delimeter_space = " "
    for i in range(0,len(seq )):
        if  not (seq[i]).startswith(">") :
            sequences.append(seq[i])
    sequence = delimeter_space.join(sequences)

    return (sequence.replace(" ",""))

def find_exons(exon,code):
    positions = []
    for i in range(0,len(exon)):
        clean_exon = header(exon[i])
        positions.append(code.find(clean_exon))

    return positions




FILENAME = "/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/Homo_sapiens_ADA_sequence.txt"
FILENAME2 = "/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/ADA_EXONS.txt"
file_contents = Path(FILENAME).read_text()
exon_content = Path(FILENAME2).read_text()
exon_line = exon_content.split(">")
ADA_line= file_contents.split("\n")
gene_sequence = header(ADA_line)

print(find_exons(exon_line,gene_sequence))