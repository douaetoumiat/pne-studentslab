class Seq:


    def __init__(self, strbases):

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):


        return self.strbases

    def len(self):

        return len(self.strbases)

def print_list(seq_list):
    for i in range(len(seq_list)):
        print("sequence " , i,f" Length: {seq_list[i].len()}",seq_list[i])

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_list(seq_list)