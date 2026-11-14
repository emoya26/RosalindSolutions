with open('human_genes.fasta', 'r') as file:
    lines = file.readlines()

genes = {}
name = None

for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith('>'):
        name = line[1:].split()[0]
        genes[name] = ''
    elif name is not None:
        genes[name] += line.upper()

with open('gc_report.txt', 'w') as out:
    for key in genes:
        seq = genes[key]
        gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
        print(key, round(gc, 1))
        out.write(f"{key}\t{gc:.1f}\n")
