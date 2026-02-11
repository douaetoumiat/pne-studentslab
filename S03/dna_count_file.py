from dna_count import  letters
def count_bases(seq1):
    count_total = 0
    bases = []

    for line in seq1:
        line = line.strip()
        count_total += len(line)

        for letter in line:
            if letter not in bases:
                bases.append(letter)

    return count_total, len(bases)

file  = open("/home/alumnos/douae/PycharmProjects/pne-studentslab/S03/dna.txt")
seq = file.readlines()
file.close()
answer = count_bases(seq)
print("the total bases are:",answer[0])
print("the different bases are:",answer[1])
print("A:",letters("A",seq))
print("C:",letters("C",seq))
print("G:",letters("G",seq))
print("T:",letters("T",seq))



