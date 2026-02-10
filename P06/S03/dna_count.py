
def letters(letter,seq):
    count = 0
    for i in range(0,len(seq)+1):
        if i == letter :
            count += 1
    return count


print("The lenght of the sequence is:", len("CATGTAGACTAG"))
print("A:",letters("A","CATGTAGACTAG"))
print("C:",letters("C","CATGTAGACTAG"))
print("G:",letters("G","CATGTAGACTAG"))
print("T:",letters("T","CATGTAGACTAG"))