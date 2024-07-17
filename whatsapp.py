import pywhatkit

# Using Exception Handling to avoid unprecedented errors
try:
    # Sending message to the number
    pywhatkit.sendwhatmsg("+918102157190", 
                          "massege sent hua ki nhi ", 
                          19, 19)
    print("Successfully Sent!")

except Exception as e:
    # Handling exception and printing error message
    print(f"An Unexpected Error occurred: {e}")

