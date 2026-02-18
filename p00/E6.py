from seq0 import *

seq = seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/Danio_rerio_U5_sequence.txt")
short_seq = seq[0:19]
print(seq_reverse(short_seq))