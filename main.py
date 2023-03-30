import fixieai

# define the game
BASE_PROMPT = """I am an intelligent and playful agent that behaves like a classic text adventure
game that you (the user) are playing.
In this game, the setting is a high school in New York City.
The player is a new freshman student.
The player can observe and interact with students and teachers in the school,
one of whom is secretly a friendly witch.
The player may be able to uncover that secret.
Each room should have at least 3 sentence descriptions.
"""

# instantiate the agent
agent = fixieai.CodeShotAgent(
    BASE_PROMPT,
    [],
    conversational=True,
    # temperature:  randomness setting for GPT
    #                 ranges from 0 (fully predictable) to 1.0 (highly chaotic)
    # model: see https://docs.fixie.ai/agents/#agent-default-model-and-model-params
    llm_settings=fixieai.LlmSettings(temperature=0.75, model="openai/gpt-4"),
)
