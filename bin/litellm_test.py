from litellm import completion

from ulib.utils.env_reader import read_deepseek_api_key

messages = [{"content": "Hello, how are you?", "role": "user"}]

response = completion(
    base_url="https://api.deepseek.com/v1",
    api_key=read_deepseek_api_key(),
    model="deepseek-chat",
    messages=messages,
)

print(response)
