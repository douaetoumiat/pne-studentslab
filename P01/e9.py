from Seq1 import Seq
print("-----| Practice 1, Exercise 9 |------")
s = Seq()
s.read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/U5.txt")
print("sequence 1;", s,"\n", s.count(),"\n","REV:",s.reverse(),"\n","COMP:",s.complement())
