def make_shirt(size, message):
    # Print a summary of the shirt
    print("I'm making a shirt in size " + size + " with the message '" + message + "' printed on it.")

# Call the function using positional arguments
make_shirt("M", "Keep Calm and Code On")

# Call the function using keyword arguments
make_shirt(size="L", message="Python is my favorite language")
