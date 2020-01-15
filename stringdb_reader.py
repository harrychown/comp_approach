"""
Homo sapien String DB search for high confidence interactions
The protein info and protein links files need to be downloaded from the
string database
The input file is in a text format
"""
import os
import gzip
# Set the input directory
input_dir = ("C:/Users/harry/Documents/uom/computational_approaches/project")
os.chdir(input_dir)

# Extract gene/protein input file
gene_file = open("gene_data_ctcfl_v2.txt")
gene_data = gene_file.readlines()
gene_data = [i.rstrip("\n") for i in gene_data] # Removes any new line characters
gene_file.close()

# Create a dictionary of StringID:GeneID and store the StringID counterpart of
# our input genes
protinfo_file = gzip.open("9606.protein.info.v11.0.txt.gz", "rt")
protinfo_data = protinfo_file.readlines()
protinfo_file.close()
string_dict = {}
input_stringID = []
for row in protinfo_data[1:]:
    row = row.rstrip("\n").split("\t")
    stringname = row[0]
    genename = row[1]
    string_dict[stringname] = genename
    if genename in gene_data:
        input_stringID.append(stringname)


# Search String DB for interactions
stringdb_file = gzip.open("9606.protein.links.v11.0.txt.gz", "rt")
stringdb_data = stringdb_file.readlines()
stringdb_file.close()
node1_list =[]
node2_list = []
for row in stringdb_data[1:]:
    row = row.rstrip("\n").split(" ")
    node1 = row[0]
    node2 = row[1]
    score = int(row[2])
    # Only select interactions involving our input and set the confidence 
    # threshold to high (0.9)
    if node1 in input_stringID and score > 900:
        node1_geneID = string_dict[node1]
        node2_geneID = string_dict[node2]
        node1_list.append(node1_geneID)
        node2_list.append(node2_geneID)

# Save the output in a text file
output = open("string_network.txt", "w")
for node1, node2 in zip(node1_list, node2_list):
    output.write(node1 + " " + node2 + "\n")
output.close()