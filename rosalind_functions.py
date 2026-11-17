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
def PRTN(RNA_seq):
    RNA_codons = {
       "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
       "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
       "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
       "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
       "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
       "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
       "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
       "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
       "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
       "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
       "UAA":  "", "CAA": "Q", "AAA": "K", "GAA": "E",
       "UAG":  "", "CAG": "Q", "AAG": "K", "GAG": "E",
       "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
       "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
       "UGA":  "", "CGA": "R", "AGA": "R", "GGA": "G",
       "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }
    codons = []
    for i in range(0, len(RNA_seq), 3):
        RNA = RNA_seq[i: i + 3]
        codons.append(RNA_codons.get(RNA, ''))
    return ''.join(codons)

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


#REVP
bp = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}

def reverse_comp(seq):
    return ''.join(bp[letter] for letter in reversed(seq))

def reverse_palindrome(seq):
    results = []
    for i in range(len(seq)):
        for length in range(4, 13):
            if i + length > len(seq):
                break
            sub = seq[i:i + length]
            if sub == reverse_comp(sub):
                results.append((i + 1, length)) 
    return results

for pos, length in reverse_palindrome(seq):
    return(pos, length)

#TRAN
def TRAN(s1: str, s2: str) -> float:
    transitions_set = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}
    
    transitions = 0
    transversions = 0
    

    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            if (base1, base2) in transitions_set:
                transitions += 1
            else:
                transversions += 1
                
    return transitions / transversions


