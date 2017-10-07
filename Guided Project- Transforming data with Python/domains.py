import read
df = read.load_data()

domains = df['url'].value_counts()
for name,row in domains.items():
    print("{0}: {1}".format(name,row))
    
