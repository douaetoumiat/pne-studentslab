from pathlib import Path
class Seq:

    def __init__(self, strbases):

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):


        return self.strbases

    def len(self):

        return len(self.strbases)

    def count_base(self,base):
        count = 0
        for i in range(0, len(self.strbases)):
            if self.strbases[i] == base:
                count += 1
        return count

    def count(self):
        s = "ACGT"
        h = {}
        for m in s:
            count = 0
            for n in self.strbases:
                if n == m:
                    count += 1
            h[m] = count
        return h
    def reverse(self):
        return self.strbases[::-1]

    def complement(self):
        new_seq = []
        delimeter_space = ""
        for i in range(0, len(self.strbases)):
            if self.strbases[i] == "A":
                new_seq.append("T")
            if self.strbases[i] == "T":
                new_seq.append("A")
            if self.strbases[i] == "C":
                new_seq.append("G")
            if self.strbases[i] == "G":
                new_seq.append("C")

        final_seq = delimeter_space.join(new_seq)
        return final_seq

    def read_fasta(self,filename):
        file_contents = Path(filename).read_text()
        line = file_contents.split("\n")
        delimeter_space = " "
        sequences = []
        for i in range(0, len(line)):
            if not (line[i]).startswith(">"):
                sequences.append(line[i])
        sequence = delimeter_space.join(sequences)
        return sequence

