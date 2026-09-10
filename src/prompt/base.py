def base_prompt(role:str,task:str,user_input:str,constraints:list[str]|None =None):

   constraints_text = ''

   if constraints:
        constraints_text = '\n'.join(f"- {item}" for item in constraints)
      
   prompt = f"""
   Role: 
   {role}

   task: 
   {task}

   Constraints: 
   {constraints_text}

    input : 
    {user_input}
""".strip()

   return prompt
