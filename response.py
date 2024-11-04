#take in one prompt and keep chatting with the person
import openai
import os
import json
from conv_logger import log_conversation, load_conversation_history

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
prompt_template_file = '/Users/raynahata/Desktop/Github/TTRProject/prompt'
data_file = '/Users/raynahata/Desktop/Github/TTRProject/occurances'
csv_history_file = '/Users/raynahata/Desktop/Github/TTRProject/conversation_history.csv'

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
user_message = None

while not done_chat:
    # Generate the conversational phrase with the current message history
    conversational_phrase = generate_conversational_phrase(messages, csv_history_file)
    
    if conversational_phrase:
        print("Robot:", conversational_phrase)
        
        # Add the robot's response to the conversation history
        messages.append({"role": "assistant", "content": conversational_phrase})

    # Get input from the user after the robot's response
    user_message = input("You: ").strip()
    log_conversation("User", user_message, csv_file=csv_history_file)
    
    # Check if the user wants to end the conversation
    if user_message.lower() == "bye":
        done_chat = True
        print("Ending conversation.")
    else:
        # Add the user’s response to the conversation history
        messages.append({"role": "user", "content": user_message})

# # # import openai
# # # import os
# # # import json
# # # from conv_logger import log_conversation, load_conversation_history


# # # client = openai.OpenAI(
# # #   api_key="sk-whnUEfTKRKbE8-73nOgpcg",
# # #   base_url="https://cmu.litellm.ai",
# # # )




# # # # def generate_conversational_phrase(prompt_template_file, data_file):
# # # #     # Read the prompt template from the text file
# # # #     with open(prompt_template_file, 'r') as file:
# # # #         prompt_template = file.read()

# # # #     # Read the data from the JSON file
# # # #     with open(data_file, 'r') as file:
# # # #         data = json.load(file)

# # # #     # Format the prompt using the data
# # # #     prompt = prompt_template.format(
# # # #         expected_action=data.get('expected_action', 'Unknown action'),
# # # #         actual_action=data.get('actual_action', 'Unknown action'),
# # # #         what_went_wrong=data.get('what_went_wrong', 'No details provided')
# # # #     )

# # # #     messages=[{"role": "system", "content": prompt}]

# # # #     # Call the OpenAI API
# # # #     response = client.chat.completions.create(
# # # #         model="gpt-4o", # Choose the appropriate GPT model
# # # #         messages = messages,
# # # #         max_tokens=100, # You can adjust the max tokens as needed
# # # #         temperature=0.7, # Controls the creativity of the response
# # # #         n=1,
# # # #         stop=None
# # # #     )

# # # #     # Extract the generated conversational phrase
# # # #     # conversational_phrase = response.choices[0].text.strip()
# # # #     print("Total Tokens:", response.usage.total_tokens)
# # # #     return  response.choices[0].message.content

# # # PARTICIPANT_ID = '1'

# # # def generate_conversational_phrase(prompt_template_file, data_file, csv_history_file):
# # #     # Load previous conversation history
    
    

# # #     folder_path = '/Users/raynahata/Desktop/Github/TTRProject/logs' 

# # #     if not os.path.exists(folder_path): 
# # #         os.makedirs(folder_path) 

# # #     if not os.path.isfile(csv_history_file):
# # #         log_conversation("System", "Conversation log initialized", csv_file=csv_history_file)
    
# # #     #messages = load_conversation_history(csv_history_file)

# # #     try:
# # #         # Read the prompt template from the text file
# # #         with open(prompt_template_file, 'r') as file:
# # #             prompt_template = file.read()

# # #         # Read the data from the JSON file
# # #         with open(data_file, 'r') as file:
# # #             data = json.load(file)

# # #         # Format the prompt using the data
# # #         prompt = prompt_template.format(**data)
# # # #         prompt = prompt_template.format(
# # # # #         expected_action=data.get('expected_action', 'Unknown action'),
# # # # #         actual_action=data.get('actual_action', 'Unknown action'),
# # # # #         what_went_wrong=data.get('what_went_wrong', 'No details provided')
# # # # #     )

# # #         messages=[{"role": "system", "content": prompt}]

# # #         # Add the new prompt as a 'system' message
# # #         #messages.append({"role": "system", "content": prompt})

# # #         # Call the OpenAI API
# # #         response = client.chat.completions.create(
# # #             model="gpt-4o",
# # #             messages=messages,
# # #             max_tokens=100,
# # #             temperature=0.7,
# # #             n=1
# # #         )

# # #         # Extract the generated conversational phrase
# # #         conversational_phrase = response.choices[0].message.content.strip()
# # #         log_conversation("Robot", conversational_phrase, csv_file=csv_history_file)
# # #         print("Total Tokens:", response.usage.total_tokens)
# # #         return conversational_phrase

# # #     except FileNotFoundError as e:
# # #         print(f"Error: {e}. Please check the file path.")
# # #     except json.JSONDecodeError:
# # #         print("Error: Data file is not a valid JSON.")
    
    
# # # # Example usage
# # # prompt_template_file = '/Users/raynahata/Desktop/Github/TTRProject/prompt'
# # # data_file = '/Users/raynahata/Desktop/Github/TTRProject/occurances'
# # # folder_path = '/Users/raynahata/Desktop/Github/TTRProject/logs'
# # # csv_history_file = '/Users/raynahata/Desktop/Github/TTRProject/conversation_history.csv'

# # # if not os.path.isfile(csv_history_file):
# # #     log_conversation("System", "Conversation log initialized", csv_file=csv_history_file)

# # # done_chat=False
# # # while not done_chat:

# # #     # Generate the conversational phrase
# # #     conversational_phrase = generate_conversational_phrase(prompt_template_file, data_file, csv_history_file)

# # #     if content=="bye":
# # #         done_chat=True
# # #         break
# # # if conversational_phrase:
# # #     print("Conversational Phrase:", conversational_phrase)

# # import openai
# # import os
# # import json
# # from conv_logger import log_conversation, load_conversation_history

# # client = openai.OpenAI(
# #     api_key="sk-whnUEfTKRKbE8-73nOgpcg",
# #     base_url="https://cmu.litellm.ai",
# # )

# # PARTICIPANT_ID = '1'

# # def generate_conversational_phrase(prompt_template_file, data_file, csv_history_file, user_message=None):
# #     # Load previous conversation history
# #     folder_path = '/Users/raynahata/Desktop/Github/TTRProject/logs'

# #     if not os.path.exists(folder_path): 
# #         os.makedirs(folder_path) 

# #     if not os.path.isfile(csv_history_file):
# #         log_conversation("System", "Conversation log initialized", csv_file=csv_history_file)

# #     try:
# #         # Read the prompt template from the text file
# #         with open(prompt_template_file, 'r') as file:
# #             prompt_template = file.read()

# #         # Read the data from the JSON file
# #         with open(data_file, 'r') as file:
# #             data = json.load(file)

# #         # Format the prompt using the data
# #         prompt = prompt_template.format(**data)
# #         messages = [{"role": "system", "content": prompt}]

# #         # Add the user message to the conversation if provided
# #         if user_message:
# #             messages.append({"role": "user", "content": user_message})

# #         # Call the OpenAI API
# #         response = client.chat.completions.create(
# #             model="gpt-4o",
# #             messages=messages,
# #             max_tokens=100,
# #             temperature=0.7,
# #             n=1
# #         )

# #         # Extract the generated conversational phrase
# #         conversational_phrase = response.choices[0].message.content.strip()
# #         log_conversation("Robot", conversational_phrase, csv_file=csv_history_file)
# #         print("Total Tokens:", response.usage.total_tokens)
# #         return conversational_phrase

# #     except FileNotFoundError as e:
# #         print(f"Error: {e}. Please check the file path.")
# #     except json.JSONDecodeError:
# #         print("Error: Data file is not a valid JSON.")

# # # Example usage
# # prompt_template_file = '/Users/raynahata/Desktop/Github/TTRProject/prompt'
# # data_file = '/Users/raynahata/Desktop/Github/TTRProject/occurances'
# # csv_history_file = '/Users/raynahata/Desktop/Github/TTRProject/conversation_history.csv'

# # if not os.path.isfile(csv_history_file):
# #     log_conversation("System", "Conversation log initialized", csv_file=csv_history_file)

# # done_chat = False
# # user_message = None

# # while not done_chat:
# #     # Generate the conversational phrase with the user message
# #     conversational_phrase = generate_conversational_phrase(prompt_template_file, data_file, csv_history_file, user_message)
    
# #     if conversational_phrase:
# #         print("Conversational Phrase:", conversational_phrase)

# #     # Get input from the user after the robot's initial response
# #     user_message = input("You: ").strip()
# #     log_conversation("User", user_message, csv_file=csv_history_file)
    
# #     if user_message.lower() == "bye":
# #         done_chat = True
# #         print("Ending conversation.")

# import openai
# import os
# import json
# from conv_logger import log_conversation, load_conversation_history

# client = openai.OpenAI(
#     api_key="sk-whnUEfTKRKbE8-73nOgpcg",
#     base_url="https://cmu.litellm.ai",
# )

# PARTICIPANT_ID = '1'

# def generate_conversational_phrase(messages, csv_history_file):
#     try:
#         # Call the OpenAI API with the updated conversation history
#         response = client.chat.completions.create(
#             model="gpt-4o",
#             messages=messages,
#             max_tokens=100,
#             temperature=0.7,
#             n=1
#         )

#         # Extract the generated conversational phrase
#         conversational_phrase = response.choices[0].message.content.strip()
#         log_conversation("Robot", conversational_phrase, csv_file=csv_history_file)
#         print("Total Tokens:", response.usage.total_tokens)
#         return conversational_phrase

#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# # Example usage
# prompt_template_file = '/Users/raynahata/Desktop/Github/TTRProject/prompt'
# secondary_prompt_file = '/Users/raynahata/Desktop/Github/TTRProject/secondary_prompt'
# data_file = '/Users/raynahata/Desktop/Github/TTRProject/occurances'
# csv_history_file = '/Users/raynahata/Desktop/Github/TTRProject/conversation_history.csv'

# # Initialize conversation log if it doesn't exist
# if not os.path.isfile(csv_history_file):
#     log_conversation("System", "Conversation log initialized", csv_file=csv_history_file)

# # Read the initial prompt and data for the first system message
# with open(prompt_template_file, 'r') as file:
#     prompt_template = file.read()

# # with open(secondary_prompt_file, 'r') as file:
# #     secondary_prompt_template = file.read()

# with open(data_file, 'r') as file:
#     data = json.load(file)

# # Format the initial prompt using the data
# initial_prompt = prompt_template.format(**data)
# messages = [{"role": "system", "content": initial_prompt}]

# done_chat = False
# user_message = None
# #first_response = True

# while not done_chat:
#     # Generate the conversational phrase with the current message history
#     conversational_phrase = generate_conversational_phrase(messages, csv_history_file)
    
#     if conversational_phrase:
#         print("Robot:", conversational_phrase)
        
#         # Add the robot's response to the conversation history
#         messages.append({"role": "assistant", "content": conversational_phrase})

#     # Get input from the user after the robot's response
#     user_message = input("You: ").strip()
#     log_conversation("User", user_message, csv_file=csv_history_file)
    
#     # Check if the user wants to end the conversation
#     if user_message.lower() == "bye":
#         done_chat = True
#         print("Ending conversation.")
#     else:
#         # Add the user’s response to the conversation history
#         messages.append({"role": "user", "content": user_message})
        
#         # # After the first response, switch to the secondary prompt if not already included
#         # if first_response:
#         #     secondary_prompt = secondary_prompt_template.format(**data)
#         #     messages.append({"role": "system", "content": secondary_prompt})
#         #     first_response = False

