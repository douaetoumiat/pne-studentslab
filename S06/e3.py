class Seq:


    def __init__(self, strbases):

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):


        return self.strbases

    def len(self):

        return len(self.strbases)

def generate_seqs(pattern,number):
    list_s  = []
    count = 0
    bases = pattern
    while count < number :
        list_s.append(bases)
        count += 1
        bases = pattern + list_s[count-1]
    for i in range(0,len(list_s)):
        list_s[i] = Seq(list_s[i])
    return list_s


def print_seqs(seq_list):
    for i in range(len(seq_list)):
        print("sequence " , i,f" Length: {seq_list[i].len()}",seq_list[i])


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)


print("List 2:")
print_seqs(seq_list2)
