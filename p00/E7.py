from seq0 import *

seq = seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/Danio_rerio_U5_sequence.txt")
short_seq = seq[0:19]
print("GENE U5:")
print("frag:",short_seq)
print("comp:",seq_complement(short_seq))