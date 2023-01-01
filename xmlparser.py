#this script runs command2 against the input
# Import the openai module

import openai


# Configure the openai module by setting the secret key

openai.api_key_path = "key"



# Open a file named input.txt and read that entire file into a variable named input

with open('command3.txt') as c, open("input2.txt") as f:
    command3 = c.read()
    input = f.read()


# Print the value of the variable named input

print(command3 + '\n' + '\n' + input)



# create a completion

response = openai.Completion.create(

    model="text-davinci-003",

    max_tokens=300,

    prompt=command3+  '\n' + '\n' + input,

    temperature=0.3,

    top_p=1,

    stop="|<EndOfText>|"

)

# print the completion

print(response.choices[0].text)