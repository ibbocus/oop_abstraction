dna = "GCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

A = []
C = []
G = []
T = []

for letter in dna:
    if letter == "A":
        A.append(letter)
    elif letter == "C":
        C.append(letter)
    elif letter == "G":
        G.append(letter)
    elif letter == "T":
        T.append(letter)

count_A = len(A)
count_C = len(C)
count_G = len(G)
count_T = len(T)

print(count_A, count_C, count_G, count_T)

