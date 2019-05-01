from httpPost import httpPost

text_data = {"text": "This came from a python script!"}
button_data = {"text": "This button is a dummy.  It does nothing!",
               "attachments":
                   [
                       {
                           "title": "Press the Button!",
               "actions": [
                   {"name": "dummy",
                    "type": "button",
                    "text": "yeet",
                    "style": "",
                    "value": "none"}
               ]
               }
                   ]
               }

while True:
    inputed = input("What do you want to send to Slack? Text or Button?\n")
    if inputed.upper() == "TEXT":
        httpPost.post(text_data)
    if inputed.upper() == "BUTTON":
        httpPost.post(button_data)


