import pandas as pd


class Table:
    def __init__(self,file_loc):

        self.file_loc = file_loc
        self.df = pd.read_csv(self.file_loc)

    def return_ticket(self,number:int):

        if number > self.df.shape[0]:
            raise "number is wrong"
        return self.df.loc[number]

    def return_samples(self,number:int):

        if number > self.df['message'].value_counts().sum():
            raise "Number is wrong" 
        return self.df.sample(n=number,random_state=8)

    
    def return_length(self):
        return self.df.shape[0]