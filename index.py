from dotenv import load_dotenv
import os
from notes_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf_engine import konosuba_engine

load_dotenv()
context = """The purpose of this agent is to provide normies information about kono subarashii sekai ni shukufuku wo! and save notes."""

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=konosuba_engine,
        metadata=ToolMetadata(
            name='konosuba_index',
            description='search the konosuba index for information'
        )
    )
    
]

llm = OpenAI(model='gpt-3.5-turbo')
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)