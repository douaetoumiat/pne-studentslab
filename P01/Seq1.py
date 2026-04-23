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

    def ping(self):
        return("Ok!\n")


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
    def biggest(self):
        s = "ACGT"
        list = []
        biggest = 0
        for m in s:
            base_count = self.strbases.count(m)

            if base_count > biggest:
                list.append(f"{m}")
                biggest = base_count
        return list[-1]
    def count(self):

        s = "ACGT"
        if not self.strbases:
            return "No sequence provided."

        for base in self.strbases:
            if base not in s:
                return "Error: Invalid bases detected in sequence."

        total_bases = len(self.strbases)

        report = f"Total bases: {total_bases} \n"

        for m in s:
            base_count = self.strbases.count(m)
            percentage = (base_count / total_bases * 100) if total_bases > 0 else 0
            report += f"Base {m}: {base_count} ({percentage:.2f}%) \n"


        return report



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


