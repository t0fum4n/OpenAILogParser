# Import the openai module

import openai


# Configure the openai module by setting the secret key

openai.api_key_path = "key"



# Open a file named input.txt and read that entire file into a variable named input

with open('command2.txt') as c, open("input.txt") as f:
    command2 = c.read()
    input = f.read()


# Print the value of the variable named input

print(command2 + '\n' + '\n' + input)



# create a completion

response = openai.Completion.create(

    model="text-davinci-002",

    max_tokens=300,

    prompt=command2+  '\n' + '\n' + input,

    temperature=0.3,

    top_p=1,

    stop="|<EndOfText>|"

)

# print the completion

print(response.choices[0].text)