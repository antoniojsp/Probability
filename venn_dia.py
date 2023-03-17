# library
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

# Use the venn2 function
v=venn3(subsets = (10, 8, 22, 6,9,4,2), set_labels = ('Group A', 'Group B', 'Group C'))
plt.show()