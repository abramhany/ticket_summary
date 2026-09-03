from model.model import get_model
from dotenv import load_dotenv
import os


load_dotenv()
name = os.getenv('MODEL_NAME')
print(name)
get_model(name)