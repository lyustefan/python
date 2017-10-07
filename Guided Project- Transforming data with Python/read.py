import pandas as pd

def load_data():
    pass
    story = pd.read_csv("hn_stories.csv")
    story.columns = ['submission_time','upvotes','url','headline']
    return story
    
    if __name__ == "__main__":
        load_data()
        
print(load_data().head())
