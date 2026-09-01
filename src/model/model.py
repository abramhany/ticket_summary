from transformers import AutoModelForCausalLM, AutoTokenizer

def get_model(name):
    model = AutoModelForCausalLM.from_pretrained(name)
    tokenizer = AutoTokenizer.from_pretrained(name)

    return model , tokenizer


