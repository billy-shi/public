from openai import OpenAI
import csv

class LLM:
    def __init__(self, frequency_penalty=0, logit_bias=None, 
                 logprobs=False, n=1, 
                 presence_penalty=0, stop=None, temperature=1, 
                 tools=None, tool_choice=None, model='gpt-4-turbo-preview', sys_msg=''):
        self.model = model
        self.api_key = ""     ###### ---------------------------- <<<<<<< ENTER YOUR OPENAI API KEY
        self.client = OpenAI(api_key=self.api_key)
        self.frequency_penalty = frequency_penalty
        self.logit_bias = logit_bias
        self.logprobs = logprobs
        self.n = n
        self.presence_penalty = presence_penalty
        self.stop = stop
        self.temp = temperature
        self.tools = tools
        self.tool_choice = tool_choice
        if sys_msg == '':
            self.sys_msg = """You are an expert in Python software programming, but do not have knowledge in anything else.
        If asked anything not related to Python programs, software testing or computer science, you will be honest and say you do not know.
        If asked about software testing, which is your area of expertise, you provide concise and short answers in a maximum of 3 bullet points. 
        When giving examples, please be specific and explain reasoning in short phrases."""     ####### ------------------------ <<<<<<< REPLACE THIS WITH YOUR OWN SYSTEM MESSAGE.
        ###### MORE DETAILED SYSTEM MESSAGE IS NOT ALWAYS BETTER.
        else:
            self.sys_msg = sys_msg
        self.conversation = [{"role": "system", "content": self.sys_msg}]
    
    def output_conversation(self, file_name, clear_convo=True):
        with open(file_name, "w") as file:
            for item in self.conversation:
                file.write(f"{item}\n")
        if clear_convo:
            self.conversation = [{"role": "system", "content": self.sys_msg}]

    def change_model(self, new_model):
        self.model = new_model
    
    def change_tone(self, tone):
        "tone is a number from 0 to 1, 0 is most deterministic and technical, 1 is most creative and conversational"
        "this is for the responsive interactive format"
        self.temp = tone
    
    def reply(self, input):
        self.conversation.append({"role": "user", "content": input})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation,
            temperature=self.temp)
        self.conversation.append({"role": "assistant", "content": response.choices[0].message.content.strip()})
        return response.choices[0].message.content.strip()

    def reply_stream(self,input):
        self.conversation.append({"role": "user", "content": input})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation,
            temperature=self.temp,
            stream=True)
        return response
