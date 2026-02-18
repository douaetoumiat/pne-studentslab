from seq0 import *
genes = ["Danio_rerio_U5_sequence","Homo_sapiens_ADA_sequence","Homo_sapiens_FRAT1_sequence","Homo_sapiens_FXN_sequence"]
for i in range(0,len(genes)):
    print(genes[i], "\n", seq_count(seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/"+ genes[i] + ".txt")))