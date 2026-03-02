from pathlib import Path
class Seq:

    def __init__(self, strbases=None):
        bases = "ATCG"
        self.strbases = strbases
        valid = True
        if self.strbases is None:
            print("-- Creating a Null sequence")
        else :
            for i in range(0,len(self.strbases)):
                if self.strbases[i] not in bases :
                     valid = False


            if valid :
                print("New sequence created!")
            elif not valid:
                print("-- Creating a INVALID sequence")


    def __str__(self):
        bases = "ATCG"
        valid = True
        if self.strbases is None:
            return"Null"
        else:
            for i in range(0, len(self.strbases)):
                if self.strbases[i] not in bases:
                    valid = False

            if valid:
               return  self.strbases
            elif not valid:
                return "Error"


    def len(self):
        bases = "ATCG"
        valid = True
        if self.strbases is None:
            return 0
        else:
            for i in range(0, len(self.strbases)):
                if self.strbases[i] not in bases:
                    valid = False

            if valid:
                return len(self.strbases)
            elif not valid:
                return 0


    def count_base(self,base):
        count = 0
        h = {"A" : 0,"T":0,"G":0,"C":0}
        if self.strbases is not None and len(self.strbases)!= 0:
            for i in range(0, len(self.strbases)):
                if self.strbases[i] == base:
                    h[base] += 1
            return h
        else:
            return h

    def count_base_number(self,base ):
        count = 0
        if self.strbases is not None and len(self.strbases) != 0:
            for i in range(0, len(self.strbases)):
                if self.strbases[i] == base:
                    count += 1
            return count
        else:
            return count

    def count(self):
        s = "ACGT"
        valid = True
        h =  {"A" : 0,"T":0,"G":0,"C":0}
        if self.strbases  is not None:
            for i in range(0, len(self.strbases)):
                if self.strbases[i] not in s:
                    valid = False
            if  valid :
                for m in s:
                  count = 0
                  for n in self.strbases:
                    if n == m:
                        count += 1
                  h[m] = count
                return h
            else :
                return h
        else :
             return h



    def reverse(self):
        valid = True
        bases ="ACGT"
        if self.strbases is None:
            return"Null"
        else:
            for i in range(0, len(self.strbases)):
                if self.strbases[i] not in bases:
                    valid = False
            if valid:
                return self.strbases[::-1]
            else:
                return "Error"


    def complement(self):
        new_seq = []
        valid = True
        bases = "ATCG"
        delimeter_space = ""
        if self.strbases is None:
            return "Null"
        else:
            for i in range(0, len(self.strbases)):
                if self.strbases[i] not in bases:
                    valid = False
            if valid:
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

            else:
                return "Error"



    def read_fasta(self,filename):
        file_contents = Path(filename).read_text()
        line = file_contents.split("\n")
        delimeter_space = ""
        sequences = []
        for i in range(0, len(line)):

            if not (line[i]).startswith(">"):
                line[i] = line[i].strip()
                sequences.append(line[i])
        self.strbases  = (delimeter_space.join(sequences))

        return self.strbases


