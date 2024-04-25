from openai import OpenAI
import os
        
def get_dbrx_response(prompt):
    DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')
    client = OpenAI(
        api_key=DATABRICKS_TOKEN,
        base_url="https://e2-dogfood.staging.cloud.databricks.com/serving-endpoints"
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
  
