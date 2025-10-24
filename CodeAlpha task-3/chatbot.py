def get_response(user_input):
    """
    Analyzes the user's input and returns a predefined response based on rules.
    
    This function uses if-elif statements for simple keyword matching.
    """
    # Normalize input for case-insensitive matching and remove leading/trailing spaces
    normalized_input = user_input.lower().strip()

    # --- Rule 1: Greeting ---
    if "hello" in normalized_input or "hi" in normalized_input or "hey" in normalized_input:
        return "Hi there! What can I help you with today?"

    # --- Rule 2: Inquiry about status/well-being ---
    elif "how are you" in normalized_input or "how are things" in normalized_input:
        return "I'm doing fine, thank you for asking! I'm ready to chat."
    
    # --- Rule 3: Exit/Goodbye ---
    elif "bye" in normalized_input or "goodbye" in normalized_input or "cya" in normalized_input:
        # Note: The main loop handles the actual exit, this is just the final reply
        return "Goodbye! Come back soon."

    # --- Default Rule: If no match is found ---
    else:
        return "I'm a simple bot and don't quite understand that. Try asking 'hello' or 'how are you'!"

def run_chatbot():
    """
    Runs the main conversation loop for the chatbot using a while loop and input/output.
    """
    print("🤖 Simple Rule-Based Chatbot")
    print("--------------------------------")
    print("Type 'bye', 'quit', or 'exit' to end the conversation.")
    
    # Start the infinite conversation loop
    while True:
        # Input from user
        user_input = input("You: ")
        
        # Normalize input for exit check
        normalized_input = user_input.lower().strip()
        
        # Check for explicit exit commands
        if normalized_input in ["bye", "quit", "exit"]:
            # Give a final response before breaking the loop
            print(f"Bot: Goodbye! Come back soon.")
            break
            
        # Get and print the bot's response
        response = get_response(user_input)
        print(f"Bot: {response}")

# Execute the chatbot when the script runs
if __name__ == "__main__":
    run_chatbot()
