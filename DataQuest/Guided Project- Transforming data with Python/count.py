import read
from collections import Counter
df = read.load_data()

# Combine all the headlines into one single string
item = df['headline']
s = ''
if ".co.uk" not in str(item) and ".com.au" not in str(item) and ".ac.uk" not in str(item) and ".com.br" not in str(item) and ".com.com" not in str(item) and ".org.uk" not in str(item) and ".net.au" not in str(item):
    for each in item:
        s += str(each)+" "

lower = s.lower().split()
most_common = Counter(lower).most_common(100)
print(most_common)