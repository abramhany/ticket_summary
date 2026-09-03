from transformers import AutoModelForCausalLM, AutoTokenizer

def get_model(name):
    
    model = AutoModelForCausalLM.from_pretrained(name, torch_dtype="auto",
    device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(name)
    print("model downloaded")
    return model , tokenizer


