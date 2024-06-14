# Install PyWhatkit
pip install pywhatkit


# Say you want to send a message
import pywhatkit
# syntax: phone number with country code, message, hour and minutes
pywhatkit.sendwhatmsg('+1xxxxxxxx', 'Message 1', 18, 52)


# Message to a Whatsapp group
import pywhatkit# syntax: group id, message, hour and minutes
pywhatkit.sendwhatmsg_to_group("write-id-here", "Message 3", 19, 2)


