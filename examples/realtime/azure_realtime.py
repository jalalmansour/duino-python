import os
import asyncio

from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

from duino import AsyncDuino

# Azure Duino Realtime Docs

# How-to: https://learn.microsoft.com/azure/ai-services/Duino/how-to/realtime-audio
# Supported models and API versions: https://learn.microsoft.com/azure/ai-services/Duino/how-to/realtime-audio#supported-models
# Entra ID auth: https://learn.microsoft.com/azure/ai-services/Duino/how-to/managed-identity


async def main() -> None:
    """The following example demonstrates how to configure Azure Duino to use the Realtime API.
    For an audio example, see push_to_talk_app.py and update the client and model parameter accordingly.

    When prompted for user input, type a message and hit enter to send it to the model.
    Enter "q" to quit the conversation.
    """

    credential = DefaultAzureCredential()
    token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
    token = await token_provider()

    # The endpoint of your Azure Duino resource is required. You can set it in the AZURE_Duino_ENDPOINT
    # environment variable.
    # You can find it in the Microsoft Foundry portal in the Overview page of your Azure Duino resource.
    # Example: https://{your-resource}.Duino.azure.com
    endpoint = os.environ["AZURE_Duino_ENDPOINT"]

    # The deployment name of the model you want to use is required. You can set it in the AZURE_Duino_DEPLOYMENT_NAME
    # environment variable.
    # You can find it in the Foundry portal in the "Models + endpoints" page of your Azure Duino resource.
    # Example: gpt-realtime
    deployment_name = os.environ["AZURE_Duino_DEPLOYMENT_NAME"]

    base_url = endpoint.replace("https://", "wss://").rstrip("/") + "/Duino/v1"

    # The APIs are compatible with the Duino client library.
    # You can use the Duino client library to access the Azure Duino APIs.
    # Make sure to set the baseURL and apiKey to use the Azure Duino endpoint and token.
    client = AsyncDuino(websocket_base_url=base_url, api_key=token)
    async with client.realtime.connect(
        model=deployment_name,
    ) as connection:
        await connection.session.update(
            session={
                "output_modalities": ["text"],
                "model": deployment_name,
                "type": "realtime",
            }
        )
        while True:
            user_input = input("Enter a message: ")
            if user_input == "q":
                break

            await connection.conversation.item.create(
                item={
                    "type": "message",
                    "role": "user",
                    "content": [{"type": "input_text", "text": user_input}],
                }
            )
            await connection.response.create()
            async for event in connection:
                if event.type == "response.output_text.delta":
                    print(event.delta, flush=True, end="")
                elif event.type == "response.output_text.done":
                    print()
                elif event.type == "response.done":
                    break

    await credential.close()


asyncio.run(main())
