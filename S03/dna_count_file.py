file  = open("/home/alumnos/douae/PycharmProjects/pne-studentslab/S03/dna.txt")
def count_bases(seq):
    count_total = 0
    count_bases = 0
    bases =[]
    for i in range(0,len(seq)):
         num = len(seq[i])
         count_total += num
        for l in range(0,len(seq[i])):
             if seq[i][l] not in bases :
             count_bases += 1
             bases.append[seq[i][l]]

