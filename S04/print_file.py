from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "/home/alumnos/douae/Descargas/Homo_sapiens_RNU6_269P_sequence.fa"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)
