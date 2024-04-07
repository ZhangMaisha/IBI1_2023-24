seq ='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
  
# Define the repeat sequences to search for  
repeats = ['GTGTGT', 'GTCTGT']  
   
# Iterate over the sequence, checking for overlap
count = 0  
for repeat in repeats:  
    i = 0  
    while i < len(seq) - len(repeat) + 1:  
        if seq[i:i+len(repeat)] == repeat:  
            count += 1  
            i += 1  
        #Move to the next possible location
        else:  
            i += 1  
  
  
# print the total repeat count 
print(f"Total number of repetitive elements is {count}")
