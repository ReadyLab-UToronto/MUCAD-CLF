import os
import csv
import pandas as pd
from action_counting import aggregate_count
from action_count_plotting import plotting

# Store the counts computed for each audit trail file
counts = {}

# Analyze all files in the "sample_audit_trails/single_user" folder
directory = "sample_audit_trails/single_user/"  # TODO: locate local directory and modify

separate_users = False  # TODO: modify if necessary
"""
If more than one users are found in one CSV audit trail, would you like to analyze these users 
separately, or would you like to analyze each CSV file as an aggregate entity. 
1. separate_users = False: analyze each CSV as an aggregate entity. 
2. separate_users = True: analyze each user separately in each CSV file.   
"""

for _, _, files in os.walk(directory):
    for File in files:
        if File.endswith(".csv"):
            with open(directory + File, 'r') as audit_trail_csv:
                reader = csv.reader(audit_trail_csv)
                counts = {**counts, **aggregate_count.aggregate_count(
                    reader, File[:-4], separate_users=separate_users)}

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
order_by_count = False  # TODO: modify if necessary
"""
Two options for displaying the counts in the plots: 
1. order_by_count = False: users are ordered in alphabetical order 
2. order_by_count = True: users are ordered from the highest to the lowest total action counts  
"""
count_data = pd.read_csv("sample_outputs/Counts.csv")
if order_by_count:
    count_data = count_data.sort_values(by=["Total"], ascending=False)

plotting.design_space_percentage(count_data, save_fig="sample_outputs/design_space_plot")
plotting.action_type_percentage(count_data, save_fig="sample_outputs/action_type_plot")
plotting.cr_ratio(count_data, save_fig="sample_outputs/CR_ratio_plot")

"""
The following code can be used to visualize users' percentage contribution (of different categories 
of actions as defined by the MUCAD-CLF) in one CSV audit trail record. However, please note that: 
1. Only one CSV file can be analyzed at a time. 
2. There should be more than one user present in the audit trail for the plot to be useful. 
3. The directory being pasted to the variable below should be the directory of a CSV file instead 
    of the previously used directory of the folder. 
"""

# TODO: locate local directory and modify
csv_directory = "sample_audit_trails/multi_user/Combined.csv"

# Analyze the specified CSV file
with open(csv_directory, 'r') as audit_trail_csv:
    reader = csv.reader(audit_trail_csv)
    contri_counts = aggregate_count.aggregate_count(reader, csv_directory.split("/")[-1])

# Record counts in a new csv file
with open("sample_outputs/Counts.csv", 'w') as record_csv:
    writer = csv.writer(record_csv)
    writer.writerow(["User Name", "Sketching", "3D Features", "Mating", "Visualizing",
                     "Browsing", "Other Organizing", "Creating", "Editing", "Deleting",
                     "Reversing", "Viewing", "Other", "Total"])
    for name, count_list in counts.items():
        temp = [name]
        temp.extend(count_list[0])
        temp.extend(count_list[1])
        temp.append(sum(count_list[1]))
        writer.writerow(temp)

order_by_count = False  # TODO: modify if necessary
"""
Two options for displaying the counts in the plots: 
1. order_by_count = False: users are ordered in alphabetical order 
2. order_by_count = True: users are ordered from the highest to the lowest total action counts  
"""

count_data = pd.read_csv("sample_outputs/Counts.csv")
if order_by_count:
    count_data = count_data.sort_values(by=["Total"], ascending=False)
"""
Options of action category for percentage contribution plotting: 
["Total", "Sketching", "3D Features", "Mating", "Visualizing", "Browsing", "Other Organizing", 
"Creating", "Editing", "Deleting", "Reversing", "Viewing", "Other"] 
"""
plotting.plot_contribution(count_data, "Total", save_fig="sample_outputs/contribution_per_plot")
