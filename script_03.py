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
        genes[name] += line
print(genes)
