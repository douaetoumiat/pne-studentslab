
def count_bases(seq1):
    count_total = 0
    count_bases1 = 0
    bases =[]
    for i in range(0,len(seq1)):
        num = len(seq1[i])
        count_total += num
        seq1[i] = seq1[i].strip()
        for l in range(0,len(seq1[i])):
            if seq1[i][l] not in bases :
                count_bases1 += 1
                bases.append(seq1[i][l])
    return count_total ,count_bases1



file  = open("/home/alumnos/douae/PycharmProjects/pne-studentslab/S03/dna.txt")
seq = file.readlines()
answer = count_bases(seq)
print("the total bases are:",answer[0])
print("the different bases are:",answer[1])



