# input the repetitive sequence
repetitive_seq = input("Plsase input ‘GTGTGT’ or ‘GTCTGT’.\n")
# open the folder contains the file
import os
os.chdir("/Users/zhangmaisha/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical8")
# open input and output files
import re
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
if repetitive_seq == 'GTGTGT':
    output_file = open('GTGTGT_duplicate_genes.fa','w')
if repetitive_seq == 'GTCTGT':
    output_file = open('GTCTGT_duplicate_genes.fa','w')
seq = ''
i = 0
# iterate each line in the input file
for line in input_file:
    line = line.strip()
    if line.startswith(">"):
        # If the sequence contains the repetitive element, write gene info to output file
        if repetitive_seq in seq:
            output_file.write(f'>{gene_name} {seq.count(repetitive_seq)}\n{seq}\n\n')  #Add an extra newline between gene name and sequence
        # Update gene name and reset sequence
        gene_name = re.findall(r'gene:(.+)\sgene_biotype', line)[0]
        seq = ''
    else:
        seq += line

# Write last gene info to output file
if repetitive_seq in seq:
    output_file.write(f'>{gene_name} {seq.count(repetitive_seq)}\n{seq}\n\n')  #Add an extra newline between gene name and sequence
