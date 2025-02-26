from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

llm = ChatOllama(
    model="mistral:latest",
    temperature=0,
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)


AIMessage(content='The translation of "I love programming" from English to French is:\n\n"J\'adore programmer."',
          response_metadata={'model': 'mistral:latest', 'created_at': '2024-08-19T16:05:32.81965Z',
                             'message': {'role': 'assistant', 'content': ''}, 'done_reason': 'stop', 'done': True,
                             'total_duration': 2167842917, 'load_duration': 54222584, 'prompt_eval_count': 35,
                             'prompt_eval_duration': 893007000, 'eval_count': 22, 'eval_duration': 1218962000},
          id='run-0863daa2-43bf-4a43-86cc-611b23eae466-0',
          usage_metadata={'input_tokens': 35, 'output_tokens': 22, 'total_tokens': 57})

print(ai_msg.response_metadata)