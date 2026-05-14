# Simple Python Chat Application   

messages = []  

print("=== Simple Chat Application ===")                            
print("Type 'exit' to close the chat\n")   

while True:  

    # User enters message 
    user_message = input("You: ")    


    if user_message.lower() == "exit":
        print("Chat closed.")
        break

    # Store message
    messages.append(user_message) 

    # Simple bot reply 
    bot_reply = "I received your message: " + user_message

    # Display bot reply
    print("Bot:", bot_reply)

    # Store bot reply
    messages.append(bot_reply)

print("\nChat History:")

for msg in messages:
    print("-", msg)