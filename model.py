from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
def ask(q):
    import openai
    openai.api_key = " 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"
                   
    response = openai.Completion.create(
    model="curie:ft-yzu-2022-07-31-15-46-24",
    prompt=q+"$",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["END"]
)                     
    story = response['choices'][0]['text'] 
    return story
