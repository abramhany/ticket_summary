import pandas as pd


class Table:
    def __init__(self,file_loc):

        self.file_loc = file_loc
        self.df = pd.read_csv(self.file_loc)

    def read_data(self):
       
       return pd.read_csv(self.file_loc)

    def category_cat(self):

        df = self.read_data(self.file_loc)

        return df['category'].unique().to_list()

    def sentiment_cat(self):

        df = self.read_data(self.file_loc)

        return df['sentiment'].unique().to_list()

    def urgency(self):
        
        df = self.read_data(self.file_loc)
        
        return df['urgency'].unique().to_list()

    def return_ticket(self,number:int):

    
        if number > self.df['message'].value_counts().sum():
            return "number is wrong"
        return self.df.iloc[number,1]
    