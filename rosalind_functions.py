#DNA
def DNA_count_A(seq):
    A_total = seq.count("A")
    C_total = seq.count("C")
    G_total = seq.count("G")
    T_total = seq.count("T")

    return  A_total, C_total, G_total, T_total

#RNA
def DNA_to_RNA(seq):
    return seq.replace("T", "U")


#REVC
bp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
def reverse_complement(seq):
    seq = seq.upper()
    reverse = seq[::-1]
    answer = ''
    for letter in reverse:
        if letter in bp:
            answer += bp[letter]
        else:
            answer += 'X'
    return answer

#GC
def gc_calc(seq):
    count_c = seq.count("C")
    count_g = seq.count("G")
    gc_percent = ((count_c + count_g) / len(seq)) * 100
    return gc_percent

#HAMM
def HAMM(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

#PROT
def PROT():
    #

#SUBS
def SUBS(s1, s2):
    positions = []
    start = s1.find(s2)
    while start != -1:
        positions.append(start + 1)
        start = s1.find(s2, start + 1)
    return positions

#PRTM
mass_AAs = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333,}

def protein_mass(protein_seq):
  mass_total = sum(mass_AAs[aa] for aa in protein_seq)
  return round(mass_total, 3)




