#!/usr/bin/env -S poetry run python

import asyncio

from duino import AsyncDuino

# gets API Key from environment variable DUINO_API_KEY
client = AsyncDuino()


async def main() -> None:
    stream = await client.completions.create(
        model="DuinoBot",
        prompt="Say this is a test",
        stream=True,
    )
    async for completion in stream:
        print(completion.choices[0].text, end="")
    print()


asyncio.run(main())
