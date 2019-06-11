import pandas as pd
import numpy as np


# List1  
Name = ['tom', 'krish', 'nick', 'juli']  
    
# List2  
Age = [25, 30, 26, 22]  
    
# get the list of tuples from two lists.  
# and merge them by using zip().  
list_of_tuples = list(zip(Name, Age))  
    
# Assign data to tuples.  
list_of_tuples   
  
  
# Converting lists of tuples into  
# pandas Dataframe.  
df = pd.DataFrame(list_of_tuples, columns = ['Name', 'Age'])  
     
# Print data.  
df  

# add categorical identity columns
# thank god: https://stackoverflow.com/questions/50670452/add-columns-to-a-dataframe-based-on-categorical-values-of-existing-column
df = df.join(pd.get_dummies(df.Age).replace(0, np.nan).mul(df.Age, axis=0))


df = df.join(pd.get_dummies(df.Flaw).replace(0, np.nan).mul(df.Flaw, axis=0))

df = df.join(pd.get_dummies(df.Flaw).replace(0, False))
