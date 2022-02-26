import pandas as pd

PATH = "Dataset/"

db0_excel = pd.read_excel(PATH + "valset_log.xlsx", sheet_name="dB0")
db5_excel = pd.read_excel(PATH + "valset_log.xlsx", sheet_name="dB5")
db10_excel = pd.read_excel(PATH + "valset_log.xlsx", sheet_name="dB10")
db15_excel = pd.read_excel(PATH + "valset_log.xlsx", sheet_name="dB15")

print(db0_excel[1].value_counts())
print(db5_excel[1].value_counts())
print(db10_excel[1].value_counts())
print(db15_excel[1].value_counts())
