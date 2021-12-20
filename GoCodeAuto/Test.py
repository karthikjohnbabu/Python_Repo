import pandas as pandasForSortingCSV

# assign dataset
csvData = pandasForSortingCSV.read_csv("CCG20.csv")

# displaying unsorted data frame
print("\nBefore sorting:")
print(csvData)

# sort data frame
csvData.sort_values(["Coverage Timeline"],
                    axis=0,
                    ascending=[False],
                    inplace=True)

# displaying sorted data frame
print("\nAfter sorting:")
print(csvData)