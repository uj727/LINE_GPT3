# import os

# from linebot import (LineBotApi, WebhookHandler)
# from linebot.exceptions import (InvalidSignatureError)
# from linebot.models import *



def ask(): 
    openai.api_key = "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"
    #story='111'
    response = openai.Completion.create(
    model="text-curie-001",
    prompt="how old are you",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    story = response['choices'][0]['text'] 
    
    return story
    #print( str(story) )
#ask("what are the symptom of heartdisease") 