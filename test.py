import os
import csv
import pandas as pd
from action_counting import aggregate_count
from action_count_plotting import plotting

# Store the counts computed for each audit trail file
counts = {}

# Analyze all files in the "sample_audit_trails" folder
directory = "sample_audit_trails/"
for _, _, files in os.walk(directory):
    for File in files:
        if File.endswith(".csv"):
            with open(directory + File, 'r') as audit_trail_csv:
                reader = csv.reader(audit_trail_csv)
                counts[File[:-4]] = aggregate_count.aggregate_count(reader)

"""
The following step may be optional for small-scale experiments or testing, whereas print(counts) 
should be sufficient for simple comparisons. However, storing counts in a csv is required for 
using the plotting functions in the next step. 
"""
# Record counts in a new csv file
with open("sample_outputs/Counts.csv", 'w') as record_csv:
    writer = csv.writer(record_csv)
    writer.writerow(["File Name", "Sketching", "3D Features", "Mating", "Visualizing",
                     "Browsing", "Other Organizing", "Creating", "Editing", "Deleting",
                     "Reversing", "Viewing", "Other"])
    for name, count_list in counts.items():
        temp = [name]
        temp.extend(count_list[0])
        temp.extend(count_list[1])
        writer.writerow(temp)

"""
The following functions allow some sample visualizations of the data (storing counts in a csv from 
the previous step is required). 
Usage: Uncomment one of the following to create plots. 
Optional: 
        specify figure size by adding figsize=(width, height) to the plotting functions
        e.g., plotting.design_space_percentage(count_data, fig_size=(9, 7))
        change the name of the saved figure by adding save_fig=NAME to the plotting functions 
        e.g., plotting.design_space_percentage(count_data, save_fig="sample")
"""
count_data = pd.read_csv("sample_outputs/Counts.csv")
plotting.design_space_percentage(count_data, save_fig="sample_outputs/design_space_plot")
plotting.action_type_percentage(count_data, save_fig="sample_outputs/action_type_plot")
plotting.cr_ratio(count_data, save_fig="sample_outputs/CR_ratio_plot")
