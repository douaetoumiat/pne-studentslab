from pathlib import Path




def header(seq):
    sequences = []
    delimeter_space = " "
    for i in range(0,len(seq )):
        if  not (seq[i]).startswith(">") :
            sequences.append(seq[i])
    sequence = delimeter_space.join(sequences)

    return (sequence.replace(" ",""))





FILENAME = "/S04/text files/ADA.txt"
file_contents = Path(FILENAME).read_text()
line= file_contents.split("\n")
gene_sequence = header(line)
print("The numbe of bases is :", len(gene_sequence))