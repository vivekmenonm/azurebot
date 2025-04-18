from fastapi import FastAPI, Request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

# Environment config
APP_ID = os.getenv("MICROSOFT_APP_ID", "")
APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD", "")

print("App ID:", APP_ID)
print("App Secret:", APP_PASSWORD)


settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(settings)

# Simple Bot Logic
async def bot_logic(turn_context: TurnContext):
    text = turn_context.activity.text.strip().lower()
    await turn_context.send_activity(f"You said: {text}")

# FastAPI App
app = FastAPI()

@app.post("/api/messages")
async def messages(req: Request):
    body = await req.json()
    activity = Activity().deserialize(body)

    auth_header = req.headers.get("Authorization", "")
    response = Response()

    async def aux_func(turn_context):
        await bot_logic(turn_context)

    await adapter.process_activity(activity, auth_header, aux_func)
    return response
