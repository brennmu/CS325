import subprocess

# Function to read prompts from a file
def read_prompts(file_path):
    """
    This function reads prompts from a text file.
    :param file_path: Path to the file containing prompts.
    :return: List of prompts.
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        prompts = file.readlines()
    return [prompt.strip() for prompt in prompts]

# Function to write responses to a file
def write_responses(file_path, responses):
    """
    This function writes the model responses to a text file.
    :param file_path: Path to the file where responses will be stored.
    :param responses: List of responses from the model.
    """
    with open(file_path, 'w', encoding="utf-8") as file:
        for response in responses:
            file.write(response + "\n")

# Function to interact with the Ollama model (phi3) using the 'run' command with input through stdin
def get_model_response(prompt):
    """
    This function sends a prompt to the locally running phi3 model using Ollama CLI and receives the response.
    :param prompt: The prompt to send to the model.
    :return: Model's response as a string.
    """
    #This is the command that would be used in the powershell to run phi3 and start the process of asking it questions and getting responses
    command = "ollama run phi3"
    
    #Run the command and pass the prompt via stdin as a string
    #Had to use chatgpt for this part, I couldn't figure out why every time I was running this script there was an error message that was caused by mismatched data types which is what the encoding utf-8 is doing.
    result = subprocess.run(command, input=prompt, shell=True, capture_output=True, text=True, encoding='utf-8')

    #Error checking  in execution
    if result.returncode != 0:
        return f"Error: {result.stderr.strip()}"
    
    return result.stdout.strip()

# Main script
def main():
    #Read the three prompts from file
    prompts = read_prompts("prompts.txt")
    #Get responses from phi3 model
    responses = []
    for prompt in prompts:
        response = get_model_response(prompt)
        responses.append(response)
    #Write the responses to output file
    write_responses("responses.txt", responses)
if __name__ == "__main__":
    main()
