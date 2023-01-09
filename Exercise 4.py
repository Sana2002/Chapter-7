def make_shirt(size="large", message="Afrah Is Dumb"):
    # Print a summary of the shirt
    print("I'm making a shirt in size " + size + " with the message '" + message + "' printed on it.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(message="Programming is fun!")
