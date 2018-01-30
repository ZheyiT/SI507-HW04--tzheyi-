a = input("What is your question?")
if a == 'quit':
	quit()
while a[-1] is not '?':
	a = input("I’m sorry, I can only answer questions. To quit, enter'quit'. \nPlease input your question again:")
