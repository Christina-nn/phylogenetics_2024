#!/usr/bin/env python
# coding: utf-8

# You can root the tree and get some kind of visualisation here.

# In[ ]:


pip install ete3


# In[ ]:


pip install biopython


# In[3]:


from ete3 import Tree

# Load the tree from a Newick file
t = Tree("./allfastas/tree_neand_denis_pan.nwk")

# Set the outgroup for rooting the tree
outgroup = "D38116.1"  # Replace with the name of your outgroup. Here I chose the Pan paniscus
t.set_outgroup(outgroup)

# Print the rooted tree
print("\n Your rooted tree:")
print(t)

# Save the rooted tree to a file
t.write(outfile="rooted_tree.nwk")


# The next code provides a picture (.png) of the tree, but on the low-power computer (like my laptop) it works only in google colab.
# 
# You can also change some parameters of the image

# In[5]:


pip install matplotlib


# In[8]:


from Bio import Phylo
import matplotlib.pyplot as plt

# Read the Newick file
tree = Phylo.read("rooted_tree.nwk", "newick")

# Function to scale the branch lengths (optional)
def scale_branch_lengths(clade, factor):
    if clade.branch_length:  # Only scale if there's a branch length
        clade.branch_length *= factor
    for subclade in clade.clades:
        scale_branch_lengths(subclade, factor)

# Optionally scale the branch lengths by a factor
scale_factor = 1  # Change to a value like 0.5 or 2 to shrink/expand
scale_branch_lengths(tree.root, scale_factor)

# Adjust the figure size to make the nodes wider (20 is wider)
plt.figure(figsize=(25, 15))  # Wider figure

# Create the axes and set an aspect ratio for more control
ax = plt.subplot(1, 1, 1)

# Draw the tree on the custom axes
Phylo.draw(tree, axes=ax)

# Optionally, set the x-limits or y-limits if you want to control zoom level
# ax.set_xlim([0, 10])  # Adjust limits for zooming horizontally
# ax.set_ylim([0, 10])  # Adjust limits for zooming vertically

# Show the plot
plt.show()
plt.savefig("phylogenetic_tree.png", dpi=300, bbox_inches='tight') 



# In[ ]:




