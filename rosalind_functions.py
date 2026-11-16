def DNA_count_A(seq):
    A_total = seq.count("A")
    return A_total

def DNA_to_RNA(seq):
       return(seq.replace "T", "U")

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

def gc_calc(seq):
    count_c = seq.count("C")
    count_g = seq.count("G")
    gc_percent = ((count_c + count_g) / len(seq)) * 100
    return gc_percent

