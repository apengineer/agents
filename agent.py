from strands import Agent, tool
from strands_tools import calculator, current_time

@tool
def letter_counter(word: str, letter: str) -> int:
    if len(word) == 0:
        raise ValueError("Word cannot be empty")

    return word.lower().count(letter.lower())

agent = Agent(
    tools=[letter_counter, calculator]
)

message = """
I have 2 requests:
1. Calculate 3111696 / 74088
2. Tell me how many letter R's are in the word "strawberry"
"""

agent(message)
