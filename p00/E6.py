from seq0 import *

seq = seq_read_fasta("/S04/text files/U5.txt")
short_seq = seq[0:19]
print("GENE U5:")
print("original:",short_seq)
print("reversed:",seq_reverse(short_seq))