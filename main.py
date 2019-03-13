import os, re, aiohttp, asyncio
from tkinter import Tk

# get string from clipboard
clipboard = Tk().clipboard_get()

# get URL in between ${} for API call and %{} for python expression
# ${} GET request response / %{} eval() expression and return stdout
api_call_re = re.compile(r'\$\{(.+?)\}')
py_call_re = re.compile(r'\%\{(.+?)\}')

api_calls = api_call_re.finditer(clipboard)
py_calls = py_call_re.finditer(clipboard)

async def get_api(api_calls):
    global clipboard
    async with aiohttp.ClientSession() as session:
        for api_call in api_calls:
            async with session.get(api_call.groups()[0]) as resp:
                api_resp = await resp.text()
                # replace string 
                clipboard = clipboard.replace(api_call.group(), api_resp)

