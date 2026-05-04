import duino

# will default to `os.environ['DUINO_API_KEY']` if not explicitly set
Duino.api_key = "..."

# all client options can be configured just like the `Duino` instantiation counterpart
Duino.base_url = "https://..."
Duino.default_headers = {"x-foo": "true"}

# all API calls work in the exact same fashion as well
stream = Duino.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)

print()
