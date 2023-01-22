import openai


# Authenticate with the OpenAI API
secrets = input("Enter secret: ")
print(secrets)


openai.api_key = secrets

# Get the input blog article
article = input("Enter the text of the blog article: ")

# Use ChatGPT to generate a summary
response = openai.Completion.create(
engine="text-davinci-002",
prompt=f"Please summarize the following article: {article}",
max_tokens=50
)
summary = response["choices"][0]["text"]

# Use ChatGPT to generate comments on the article and summary
comments = []
for i in range(18):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please write a 2-line comment on the following article and summary: {article} {summary}",
        max_tokens=20
    )
comments.append(response["choices"][0]["text"])

# Categorize the output and store it in a database
# (You will need to write code to accomplish this step)

print("Summary: " + summary)
print("Comments:")
for comment in comments:
    print(comment)