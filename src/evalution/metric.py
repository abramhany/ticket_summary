from schema.ticket import Ticket
from prompt.summarizer import summary_prompt
import json

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

        compares = ['category','sentiment','urgency']
        metric = {}
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
                    response = {
                                    'ticket_id': row['ticket_id'].values ,
                                    'success':False,
                                    'message': row['message'] ,
                                    'category' : row['category'] ,
                                    'sentiment': row['sentiment'] ,
                                    'urgency': row['urgency'] ,
                                }
                    return response
        
        predicted = {
                    'ticket_id': row['ticket_id'].values ,
                    'success':True,
                    'message': row['message'] ,
                     'category' : dic_output['category'] ,
                     'sentiment': dic_output['sentiment'] ,
                     'urgency': dic_output['urgency'] ,
                    'summary' : dic_output['summary']
                }
        for compare in compares :
            if predicted[compare] == row[compare]:
                 metric[compare] = True
            else:
                 metric[compare] = False

        return metric , predicted

        