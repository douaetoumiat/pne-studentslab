from seq0 import seq_read_fasta
count = 0
seq = seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/Danio_rerio_U5_sequence.txt")
while count < 21:
    print(seq[count],end ="")
    count += 1