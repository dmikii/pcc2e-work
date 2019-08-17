messages = ['hi there', 'how are you', 'that is great to hear']
sent_messages = []

def send_messages(messages, sent_messages):
	while messages:
		printed_message = messages.pop()
		print(f"Here's your message: {printed_message}")
		sent_messages.append(printed_message)

send_messages(messages[:], sent_messages)

print(messages, sent_messages)

# def show_messages(list):
# 	for message in messages:
# 		print(message.title())


# show_messages(messages)