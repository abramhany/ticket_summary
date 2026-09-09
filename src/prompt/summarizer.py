from .base import base_prompt


def summary_prompt(user_input):

    return base_prompt(
        user_input=user_input,
        role="You are a precise ticket classification assistant.",
        task="Classify the customer ticket.",
        constraints=[
            "Return only the requested result.",
            "Do not provide explanations.",
            "Do not use markdown.",
            "summary must be one sentence as max"
        ],)