# dbrx-chat

Use Databricks Serving Endpoints for Prompt Engineering, RAG, and Fine tuned LLMs

This bot has been created using [Bot Framework](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-quickstart-create-bot?view=azure-bot-service-4.0&tabs=python,vs), it shows how to create a simple bot that accepts input from the user and pipes it to a Databricks Served model for securely hosted inferencing of LLMs. Use this for model optionality, querying your RAG architectures, or your fine tuned/pretrained models.

The only custom code from the sample echo chatbot is the [dbrx.py](dbrx.py) file. For enterprise use, this will need to be extended and secured. 

> You can easily change the model used in the dbrx.py file. It can even be specified at runtime to let the user choose between different models.

## Prerequisites

This sample **requires** prerequisites in order to run.

### Install Python 3.6 or greater

### Using a Python Virtual Env is recommended


## Running the sample
- Run `export DATABRICKS_TOKEN=your_token` 
- Run `export DATABRICKS_URL=your_workspace_url` 
  - your_workspace_url is in the format `https://{workspace-identifier}/serving-endpoints` 
  - eg: `https://adb-984752964297111.11.azuredatabricks.net/serving-endpoints`
- Run `pip install -r requirements.txt` to install all dependencies
- Run `python app.py`


## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- Enter a Bot URL of `http://localhost:3978/api/messages`


## Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Dialogs](https://docs.microsoft.com/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0)
- [Gathering Input Using Prompts](https://docs.microsoft.com/azure/bot-service/bot-builder-prompts?view=azure-bot-service-4.0&tabs=csharp)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Language Understanding using LUIS](https://docs.microsoft.com/azure/cognitive-services/luis/)
- [Channels and Bot Connector Service](https://docs.microsoft.com/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)