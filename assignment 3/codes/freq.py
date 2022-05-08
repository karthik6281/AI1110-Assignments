import numpy as np
import pandas as pd

# Importing data from excel
read = pd.read_table(r'Tables/raw_data.txt',header =None)
raw_data = np.array(read)

# Generating class intervals
class_limits = [0+10*i for i in range(4)] 
class_intervals = ["%d-%d"%(class_limits[i],class_limits[i+1]) for i in range(3)]

frequency = np.histogram(raw_data,class_limits)

print("The frequencies of classes are ")
print(frequency[0])

# Creating new excel file after sorting the raw data into classes.
write = pd.DataFrame({"class interval":class_intervals,"Frequency":frequency[0]})
write.to_excel('Tables/frequency_distribution.xlsx',index=False)
