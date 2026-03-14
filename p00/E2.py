from seq0 import seq_read_fasta
count = 0
seq = seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/U5.txt")
while count < 21:
    print(seq[count],end ="")
    count += 1