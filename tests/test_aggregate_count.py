from action_counting import aggregate_count
import os
import csv

# Store the counts for each audit trail file
counts = {}

# Analyze all files in the "Audit Trails" folder
directory = "../sample_audit_trails/"
for _, _, files in os.walk(directory):
    for File in files:
        if File.endswith(".csv"):
            with open(directory + File, 'r') as audit_trail_csv:
                reader = csv.reader(audit_trail_csv)
                counts[File[:-4]] = aggregate_count.aggregate_count(reader)

"""
The following step is optional for small-scale experiments or testing, whereas print(counts) 
should be sufficient for simple comparisons. 
However, storing counts in a csv is required for using the plotting functions. 
"""
# Record counts in a new csv file
with open("Counts.csv", 'w') as record_csv:
    writer = csv.writer(record_csv)
    writer.writerow(["File Name", "Sketching", "3D Features", "Mating", "Visualizing",
                     "Browsing", "Other Organizing", "Creating", "Editing", "Deleting",
                     "Reversing", "Viewing", "Other"])
    for name, count_list in counts.items():
        temp = [name]
        temp.extend(count_list[0])
        temp.extend(count_list[1])
        writer.writerow(temp)
