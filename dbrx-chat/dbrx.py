from openai import OpenAI
import os
        
def get_dbrx_response(prompt):
    # WARNING: This is sample code to integrate Databricks Model Serving with Bot Framwork, DO NOT use PATs in production applications
    # It is recommended to swap this to use OAUTH for passthrough authentication. https://github.com/microsoft/BotBuilder-Samples/tree/main/samples/python/18.bot-authentication
    DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')
    DATABRICKS_URL = os.environ.get('DATABRICKS_URL') # https://{workspace-identifier}/serving-endpoints
    client = OpenAI(
        api_key=DATABRICKS_TOKEN,
        base_url=DATABRICKS_URL
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="databricks-dbrx-instruct",
        max_tokens=256
    )
    return chat_completion.choices[0].message.content
  
