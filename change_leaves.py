#!/usr/bin/env python
# coding: utf-8

# You can use this code to rename leaves on the tree.
# 
# It will modify leaves corresponding to file's name.
# 
# First of all, chose the folder with all fastas you have.
# 
# Then, indicate the tree as nwk file.
# 
# As a result, this program saves the tree (.nwk) with new leaves.

# In[3]:


pip install biopython


# In[4]:


import os
from Bio import SeqIO
from Bio import Phylo

def parse_fasta_from_folder(folder_path):
    sequences = {}
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".fasta") or filename.endswith(".fa"):  
            file_path = os.path.join(folder_path, filename)
            # Remove the file extension to use as the new name
            file_name_no_extension = os.path.splitext(filename)[0]
            
            # Parse the FASTA file and map the sequence IDs to the file name without extension
            for record in SeqIO.parse(file_path, "fasta"):
                sequences[record.id] = file_name_no_extension  # Create a dictionary {record.id: new_name}
    
    return sequences

# Step 1: Parse FASTA files and build the renaming dictionary
folder_path = "allfastas/"  # Replace with your folder path 

# WARNING! There should not be any multiple sequence fasta files in the folder
output_sequences = parse_fasta_from_folder(folder_path)

# print("Renaming dictionary")  # Check the dictionary of renaming

# Step 2: Load the Newick tree
tree = Phylo.read('tree_h_n.nwk', 'newick')  # Replace with your actual Newick file path

# Step 3: Rename the leaves using the dictionary from FASTA parsing
for clade in tree.find_clades():
    if clade.name in output_sequences:
        clade.name = output_sequences[clade.name]  # Rename using the dictionary

# Step 4: Save the modified tree to a new Newick file
Phylo.write(tree, 'renamed_tree_h_n.nwk', 'newick')  # Save the modified tree as 'modified_tree.nwk'

print("Tree modified and saved as 'renamed_tree_h_n.nwk'")


# In[ ]:




