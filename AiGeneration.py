import openai
from openai import Completion
import random

#Returns text from OpenAI based off of prompt
#Used for "player says"
def AiGeneration(): 
  # Set up the OpenAI API key
  openai.api_key = "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"
  
  # Set up the GPT-3 model
  model_engine = "babbage-002"
  prompt = "Generate a very creative and random comment. It can be mean, funny, gross, weird, extreme or scary. The comment would take place in a video game."
  temperature = 1
  max_tokens = 100
  
  # Generate the funny comment using the OpenAI API
  response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      temperature=temperature,
      max_tokens=max_tokens,
      n=1,
      stop=None,
  )
  
  # Print the funny comment
  comment = response.choices[0].text.strip()
  return comment



#Returns text from OpenAI based off of prompt
#Used for winner
def AiGenerationWinner(): 
  # Set up the OpenAI API key
  openai.api_key = "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"
  
  # Set up the GPT-3 model
  model_engine = "babbage-002"
  prompt = "Generate a creative annoucement. It can be themed victorious, funny, gross, weird, extreme or scary. The comment would take place in a video game talking about the winner of game."
  temperature = 1
  max_tokens = 100
  
  # Generate the funny comment using the OpenAI API
  response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      temperature=temperature,
      max_tokens=max_tokens,
      n=1,
      stop=None,
  )
  
  # Print the funny comment
  comment = response.choices[0].text.strip()
  return comment

#Returns a random pair in a list // this is used with the AiGeneration() function
def random_pair(lst):
  # Shuffle the list randomly
  random.shuffle(lst)
          
  # Return a tuple of the first two items in the shuffled list
  return tuple(lst[:2])