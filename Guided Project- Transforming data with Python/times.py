from dateutil.parser import parse
import read
df = read.load_data()

def hour_parse(date):
    hour = parse(date).hour

hours = df['submission_time'].apply(hour_parse)
print(hours.value_counts())



