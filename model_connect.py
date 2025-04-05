'''
# Use a pipeline as a high-level helper
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model directly
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1", trust_remote_code=True)

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1", trust_remote_code=True)
pipe(messages)
'''


from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='deepseek-r1', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)