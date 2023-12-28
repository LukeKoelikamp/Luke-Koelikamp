import bot
import json

def lambda_handler(event, context):
    print("LAMBDA_HANDLER")
    eventContent = event['Records'][0]['body']
    bot.run_discord_bot(eventContent)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
