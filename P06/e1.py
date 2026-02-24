
class Seq:

    def __init__(self, strbases):
       self.strbases = strbases
       bases = ["A","T","C","G"]
       valid = True
       for i in range(0,len(strbases)):
           if strbases[i] not in bases:
               valid = False
       if valid:
            print("New sequence created!")
       else:
           print("INCORRECT Sequence detected")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
