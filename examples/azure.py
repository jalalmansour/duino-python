from duino import AzureDuino

# may change in the future
# https://learn.microsoft.com/en-us/azure/ai-services/Duino/reference#rest-api-versioning
api_version = "2023-07-01-preview"

# gets the API Key from environment variable AZURE_DUINO_API_KEY
client = AzureDuino(
    api_version=api_version,
    # https://learn.microsoft.com/en-us/azure/cognitive-services/Duino/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://example-endpoint.Duino.azure.com",
)

completion = client.chat.completions.create(
    model="deployment-name",  # e.g. gpt-35-instant
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.to_json())


deployment_client = AzureDuino(
    api_version=api_version,
    # https://learn.microsoft.com/en-us/azure/cognitive-services/Duino/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://example-resource.azure.Duino.com/",
    # Navigate to the Azure Duino Studio to deploy a model.
    azure_deployment="deployment-name",  # e.g. gpt-35-instant
)

completion = deployment_client.chat.completions.create(
    model="<ignored>",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.to_json())
