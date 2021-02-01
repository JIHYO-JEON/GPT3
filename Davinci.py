import openai
import os
import json

openai.api_key = ""

def bot(prompt, question):
    if prompt == "":
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: {}\nAI:".format(question),
    else:
        prompt = prompt + "Human:{}\nAI:".format(question)

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        stop=["Human:","\n"],
        temperature=0.9,
        presence_penalty=0.6,
        max_tokens=200
    )

    # print(response)
    json_response = json.dumps(response)

    rep = json.loads(json_response)
    print(rep)

    bot_reply = rep['choices'][0]['text']

    prompt = str(prompt) + str(bot_reply)

    # print(question)
    # print(str(bot_reply))
    # print(prompt)

    return str(bot_reply), prompt


prompt = ""
while True:
    question = input("Human:")
    if question == "":
        break
    else:
        reply, prompt = bot(prompt, question)
        print("AI:", reply)