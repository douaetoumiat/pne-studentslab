from seq0 import *
genes = ["Danio_rerio_U5_sequence","Homo_sapiens_ADA_sequence","Homo_sapiens_FRAT1_sequence","Homo_sapiens_FXN_sequence"]
bases = ["A","T","G","C"]
result = {}
for i in range(0, len(genes)):
    result[genes[i]] = {}
    for m in range(0, len(bases)):
        result[genes[i]][bases[m]] = seq_count_base(
            seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/" + genes[i] + ".txt"), bases[m]
        )


    result[genes[i]] = dict(sorted(result[genes[i]].items(), key=lambda item: item[1], reverse=True))
    most_used_base = list(result[genes[i]].keys())[0]
    most_used_count = result[genes[i]][most_used_base]


    print(f"Most used base in {genes[i]}: {most_used_base} with count {most_used_count}")