# open the folder contains the file
import os
os.chdir("/Users/zhangmaisha/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical8")
# open input and output files
import re
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output_file = open('duplicate_genes.fa', 'w')
# find different sequence 
for line in input_file:
    if line.startswith(">"):
        if re.search('duplication', line):
            name = re.findall(r'gene:(.+)\sgene_biotype', line) # see if it matches the regular expression
            name = str(name) + '\n'
            output_file.write(name) # write
    else:
        continue