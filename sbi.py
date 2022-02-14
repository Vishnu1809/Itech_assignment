# Read in the file
import re
file_name = '/home/vishnu/Desktop/itech/sbi/Merchant Names-NameStandardization.txt'

with open(file_name, 'r+') as f:
    text = f.read()
    final = re.sub('sbi|SBI|state bank of india|STATE BANK OF INDIA', 'State Bank Of India', text)
    
with open('final_text.txt', 'w') as final_text:
    final_text.write(final)