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
name = []
# Import regex to solve the problem where the re cannot find fields that match the expression in overlapping areas
import regex 
for line in input_file:
    if line.startswith(">"):
        name.append(str(re.findall(r'gene:(.+)\sgene_biotype', line))) # see if it matches the regular expression
        n = regex.findall(repetitive_seq, seq, overlapped = True) # add overlapped to search overlapping areas
        count = len(n)
        if count != 0: # if the repetitive sequence exist
            name[i-1] = name[i-1] + ' has '+ str(count) +' '+ repetitive_seq + '\n'
            output_file.write(name[i-1]) # write
        i += 1
        seq = ''
    else:
        seq += re.sub(r'\n','', line) # store the whole sequence without '\n' in the string