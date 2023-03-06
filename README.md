# Chatbot-IDE
A WA bot that responds to different commands to respond in a certain context. You have the option of making a program in Python, as well as installing libraries. It answers certain common questions and if you ask it for a joke, it tells you thanks to an API.

## How to run it?

### twilio.com
1. First of all you have to create an account at twilio.com
2. Once inside, go to the Develop - Messaging - Try It Out - Send A WA Message tab
3. Follow the instructions

### Ngrok.com
Now, download ngrok needed for chatbot connection
1. follow the instructions in the setup and installation section
2. Enter the following command: ngrok http 5000
3. copy the link in the forwarding part
4. go back to the twilio page, in the "when a messege come in" part and paste the link, adding a "/bot" at the end
5. Save

Now is ready to execute the code

## How to run code?
Enter: #!python3 in the chat

## How to install libraries?
Enter !pip install in the chat

## How to ask for a joke?
Just ask and make sure that the word joke is in the phrase

## The bot can respond to the following questions:
1. What is your name?
2. How old are you?
3. some questions more because of the API.
