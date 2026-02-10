
def letters(letter,seq):
    count = 0
    for i in range(0,len(seq)):
        if seq[i] == letter :
            count += 1
    return count

if __name__ == "__main__":
    sec = input("introduce a sequence")
    print("The lenght of the sequence is:", len(sec))
    print("A:",letters("A",sec))
    print("C:",letters("C",sec))
    print("G:",letters("G",sec))
    print("T:",letters("T",sec))

