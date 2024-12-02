#take in one prompt and keep chatting with the person
import openai
import os
import json
from conv_logger import log_conversation, load_conversation_history
#from AWS_STT import start_transcription
import string
from gtts import gTTS
#import speech as sp

import pyaudio
import time 



client = openai.OpenAI(
    api_key="sk-whnUEfTKRKbE8-73nOgpcg",
    base_url="https://cmu.litellm.ai",
)

PARTICIPANT_ID = '1'

def generate_conversational_phrase(messages, csv_history_file):
    try:
        # Call the OpenAI API with the updated conversation history
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=100,
            temperature=0.7,
            n=1
        )

        # Extract the generated conversational phrase
        conversational_phrase = response.choices[0].message.content.strip()
        log_conversation("Robot", conversational_phrase, csv_file=csv_history_file)
        print("Total Tokens:", response.usage.total_tokens)
        return conversational_phrase

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
base_path = os.path.dirname(os.path.abspath(__file__))
prompt_template_file = os.path.join(base_path, 'prompt')
data_file = os.path.join(base_path, 'occurance1')
#data_file = os.path.join(base_path, 'occurance2')
#data_file = os.path.join(base_path, 'occurance3')
csv_history_file = os.path.join(base_path, 'conversation_history.csv')


# Initialize conversation log if it doesn't exist
if not os.path.isfile(csv_history_file):
    log_conversation("System", "Conversation log initialized", csv_file=csv_history_file)

# Read the initial prompt and data for the first system message
with open(prompt_template_file, 'r') as file:
    prompt_template = file.read()

with open(data_file, 'r') as file:
    data = json.load(file)

# Format the initial prompt using the data
initial_prompt = prompt_template.format(**data)
messages = [{"role": "system", "content": initial_prompt}]
done_chat = False
initial_response = await generate_conversational_phrase(messages, csv_history_file)

#sp.text_to_speech(initial_response)  # Speak the initial response

#done_chat = False
#user_message = None
#print("Generating initial response...")
if initial_response:
    messages.append({"role": "assistant", "content": initial_response})
while not done_chat:
    print("Waiting for user response...")
    user_response_start_time = time.time()  # Timer for when user input process starts
    
    try:
        # Start transcription
        user_message = await start_transcription()
        user_response_end_time = time.time()  # Timer for when user input finishes

        log_conversation("User", user_message, csv_file=csv_history_file)
        print("You:", user_message)
        
        if user_message.lower().replace(" ", "").strip(string.punctuation) == "bye":
            done_chat = True
            print("Ending conversation.")
            break

        messages.append({"role": "user", "content": user_message})
        
        # Generate robot's response
        print("Generating robot response...")
        
        conversational_phrase = await generate_conversational_phrase(messages, csv_history_file)
        robot_response_start_time = time.time()

        if conversational_phrase:
            #sp.text_to_speech(conversational_phrase)
            
            # Log time intervals
            print("Time from user speech start to robot response start:", robot_response_start_time - user_response_start_time)
            print("Time from user speech end to robot response start:", robot_response_start_time - user_response_end_time)
            print("Time for STT to complete:",user_response_end_time - user_response_start_time)
            
            messages.append({"role": "assistant", "content": conversational_phrase})
    
    except Exception as e:
        print(f"Error during user response or robot generation: {e}")

    # while not done_chat:



