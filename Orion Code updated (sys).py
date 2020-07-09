import pandas as pd
import csv
#import tkinter as tk
#from tkinter import filedialog
import sys

#root = tk.Tk()
#root.withdraw()
#input_file_path = tk.filedialog.askopenfilename()
input_file_path = sys.argv[1]

df = pd.read_csv(input_file_path, header=1)
list_HouseholdId = df['HHID'].to_list()

dfs = df.iloc[:,[0,2,3,4,5,6,7]]
dft = dfs.set_index('HHID').T

l = ['USEquity','DevelopedEquity','EmergingEquity','RealEstate', 'FixedIncome','Other']
dft['Type'] = l
out = pd.melt(dft, id_vars = ['Type'], value_vars= list_HouseholdId)

out.to_csv(r"C:\Users\Everybody\Documents\Project Orion\Orionv4.csv")