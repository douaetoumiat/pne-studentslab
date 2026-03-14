from seq0 import *

seq = seq_read_fasta("/S04/text files/U5.txt")
short_seq = seq[0:19]
print("GENE U5:")
print("frag:",short_seq)
print("comp:",seq_complement(short_seq))