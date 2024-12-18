from conv_logger import log_conversation

def generate_robot_response(user_input):
    # Example logic for generating a response
    response = f"Received your input: {user_input}. Here’s my response!"
    
    # Log the robot's response
    log_conversation("Robot", response)
    
    return response


# # Example usage
# user_message = "How can I move the robot from point A to point B?"
# log_conversation("User", user_message)  # Log the user's message
# robot_reply = generate_robot_response(user_message)  # Generate and log robot's response
