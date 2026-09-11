from model.model import get_model
import os
from dotenv import load_dotenv
from schema.ticket import Ticket 
import outlines
import torch
from evalution.metric import TicketEvaluator

print("CUDA available:", torch.cuda.is_available())
print("PyTorch CUDA:", torch.version.cuda)

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))

load_dotenv()

name = os.getenv('MODEL_NAME')
print(name)
hf_model,hf_tokenizer = get_model(name)

print(hf_model.eval())

model = outlines.from_transformers(hf_model,hf_tokenizer)


evaluator = TicketEvaluator(generator=model)

df = evaluator.evalutaion_dataframe(output_type=Ticket,max_new_tokens=200)



metric=evaluator.accuracy_metric(df)



print(metric)