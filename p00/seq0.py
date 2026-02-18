from pathlib import Path
def seq_ping():
    print("Ok")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    line = file_contents.split("\n")
    delimeter_space = " "
    sequences = []
    for i in range(0, len(line)):
        if not (line[i]).startswith(">"):
            sequences.append(line[i])
    sequence = delimeter_space.join(sequences)

    return (sequence.replace(" ", ""))

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    base_count = 0
    for i in range(0,len(seq)):
        if seq[i] == base :
            base_count += 1

    return base_count

def seq_count(seq):
    s = "ACGT"
    h = {}
    for m in s:
      count = 0
      for n in seq:
         if n == m :
           count += 1
      h[m] = count
    return h
def seq_reverse(seq):
   return seq[::-1]

def seq_complement(seq):
    new_seq = []
    delimeter_space = ""
    for i in range (0,len(seq)):
        if seq[i] == "A":
            new_seq.append("T")
        if seq[i] == "T":
            new_seq.append("A")
        if seq[i] == "C":
            new_seq.append("G")
        if seq[i] == "G":
            new_seq.append("C")

    final_seq = delimeter_space.join(new_seq)
    return final_seq

print(seq_count_base(seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/Homo_sapiens_ADA_sequence.txt"),"A"))
print(seq_complement(seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/Homo_sapiens_ADA_sequence.txt")))