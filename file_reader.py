'''
This script takes a folder of the String DB TSV files and returns just the first two
columns. The script creates an output of the all the genes, separated by a tab character,
inside the input folder.
'''
import os

# Change the directory to the relevant folder on your system
input_dir = ("C:/Users/harry/Documents/uom/computational_approaches/project/string_interactions")
os.chdir(input_dir)
# Output file name
output = open("gene_network.txt", "w")
for filename in os.listdir(input_dir):
    # Input String file
    input_file = open(filename, newline='')
    file = input_file.readlines()
    input_file.close()
    for row in file:
        col_split = row.split("\t")
        if col_split[0] == "#node1" :
            continue 
        output.write(col_split[0] + "\t" + col_split[1] + "\n")
        
output.flush()
output.close()
            
