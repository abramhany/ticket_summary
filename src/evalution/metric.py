from schema.ticket import Ticket
from prompt.summarizer import summary_prompt
import json
import pandas as pd
from schema.table import Table
import os
from dotenv import load_dotenv
import time

load_dotenv()

table_loc = os.environ['DATA_FILE_NAME']
output_loc = os.environ['OUTPUT_FILE_NAME']
metric_loc = os.environ['METRIC_FILE_NAME']
table  = Table(table_loc)

class TicketEvaluator:

    """"Evalute the llm respones on support tickets

    The evaluator is responsible for:
        - building the classifier prompt
        - calling the generator
        - parsing and validating the model output
        - comparing predictions with ground truth
        - preserving detailed error information
        - producing EvaluationResult objects
    """
    def __init__(self,generator):
        self.generator = generator


    def evalute_ticket(self,row,**karg):

       
        try:
            ticket = summary_prompt(row['message'])
        except ValueError:
            response = {
                            'ticket_id': row['ticket_id'] ,
                            'success':False,
                            'message': row['message'] ,
                            'category' : row['category'] ,
                            'sentiment': row['sentiment'] ,
                            'urgency': row['urgency'] ,
                        }
            return response
        
        try:
            
            result = self.generator(ticket,**karg)
            output = Ticket.model_validate_json(result)
            output = output.model_dump_json()
            dic_output = json.loads(output)

        except ValueError:
                    predicted = {
                                        'success':False,
                                         'pred_category' : False ,
                                         'pred_sentiment': False ,
                                         'pred_urgency': False ,
                                        'pred_summary' : False
                                    }
                    return predicted
        
        predicted = {
                    'success':True,
                     'pred_category' : dic_output['category'] ,
                     'pred_sentiment': dic_output['sentiment'] ,
                     'pred_urgency': dic_output['urgency'] ,
                    'pred_summary' : dic_output['summary']
                }
       
        return  predicted

    def evalutaion_dataframe(self,**karg):

        """ returns a dataframe containing id,
        message, actual:[category,sentiment,urgency],
        predicted:[category,sentiment,urgency], summary"""
        
        results = []
    
        length = table.return_length()
        for i in range(length):
            
            row = table.return_ticket(i)
            
            predicted =self.evalute_ticket(row,**karg)
            print(predicted)

            actual = {
                                        'ticket_id': row['ticket_id'] ,
                                        'message': row['message'] ,
                                        'category' : row['category'] ,
                                        'sentiment': row['sentiment'] ,
                                        'urgency': row['urgency'] ,
                                    }
            merged_dict = actual | predicted
            results.append(merged_dict)

        if not os.path.exists(output_loc):

            df = pd.DataFrame(results)
            df.to_csv(output_loc   )
            return df
        
        df = pd.DataFrame(results)
        df.to_csv(output_loc,mode='a')

        return df
    
                        
    def accuarcy_precentage(self,col):
        value=col.sum()
        precentage = (value / col.shape[0])*100

        return precentage
                           
    def accuracy_metric(self,df):
        """"takes the the dataframe and compares the predicted answer with the right answer and return the accuracy percentage"""
        df =df.iloc[-10:]
        df['category_accuracy'] =df['category'] == df['pred_category']
        df['sentiment_accuracy'] = df['sentiment'] == df['pred_sentiment']
        df['urgency_accuracy'] = df['urgency'] == df['pred_urgency']
        current_struct = time.localtime()
        metric= {
              'category_accuracy': self.accuarcy_precentage(df['category_accuracy']),
              'sentiment_accuracy':self.accuarcy_precentage(df['sentiment_accuracy']),
              'urgency_accuracy':self.accuarcy_precentage(df['urgency_accuracy']),
               'Time': time.strftime("%m-%d %H:%M", current_struct)
        }

        if not os.path.exists(metric_loc):

                df = pd.DataFrame([metric])
                df.to_csv(metric_loc)

                return df    
        
        df = pd.DataFrame([metric])
        df.to_csv(metric_loc,mode='a',header=False)    
        
        return metric
            
    
            


            


