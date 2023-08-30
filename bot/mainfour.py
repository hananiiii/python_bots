messages ={
    "hello":"hi",
    "how are you" :"im good ,you?",
    "im fine too ,thank yoiu" :"do you want something?",
    "yeah i wanna ask about something":"if i were you i would go and ask google instead"
}

def chat(user_message):
    
    user_message=user_message.lower()
    message=messages.get(user_message,"...")
    return message


while True :
    user_message=input('you:')
    if user_message=='bye':
        print('bot :','good bye ,take care')
        break
    
    message=chat(user_message)
    print('bot:',message)