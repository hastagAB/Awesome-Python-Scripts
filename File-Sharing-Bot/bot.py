from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import telegram
import shutil
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#list of authorized users
#create a list of telegram usernames to authorise them, 0th username is admin.
username_list = []
# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    reply = "Welcome to World of Automation. \nI am a bot developed by a Lazy Programmer.\nSend /help command to see what i can do."
    update.message.reply_text(reply)


def help(bot, update):
    """Send a message when the command /help is issued."""
    admin = update.message.from_user.username
    if admin == username_list[0]:
        reply = '''Send /get folder_name/file_name.extension to receive a file. 
                \nSend /ls folder_name to show list of files.
                \nSend /put folder_name/file_name.extension to upload last sent file.
                \nSend /mkdir folder_name to create a Folder.
                \nSend /remove folder_name/filename.extension to delete a file.
                \nSend /adduser username to give access.
                \nSend /removeuser username to revoke access.
                \nSend /showuser to show list of users
                '''    
    else:
        reply = '''Send /get folder_name/file_name.extension to receive a file. 
                \nSend /ls folder_name to show list of files.
                \nSend /put folder_name/file_name.extension to upload last sent file.
                \nSend /mkdir folder_name to create a Folder.
                '''
    update.message.reply_text(reply)


def get(bot, update):
    """Send requested file."""
    username = update.message.from_user.username
    if(username not in username_list):
        update.message.reply_text("You are not Authorized.")
        return
    file = update.message.text.split(" ")[-1]
    if(file == "/send"):
        update.message.reply_text("Invalid File name.")
    else:
        reply = "Findind and Sending a requested file to you. Hold on..."
        update.message.reply_text(reply)
        path = os.getcwd()+'/'+file
        if (os.path.exists(path)):
            bot.send_document(chat_id=update.message.chat_id,document=open(path, 'rb'), timeout = 100)
        else:
            update.message.reply_text("File not Found.")

def ls(bot, update):
    """Show files in requested directory."""
    username = update.message.from_user.username
    if(username not in username_list):
        update.message.reply_text("You are not Authorized.")
        return
    file = update.message.text.split(" ")[-1]
    if(file == "/show"):
        update.message.reply_text("Invalid Directory name.")
    else:
        reply = "Findind and Sending a list of files to you. Hold on..."
        update.message.reply_text(reply)
        path = os.getcwd()+'/'+file
        if (os.path.exists(path)):
            update.message.reply_text(os.listdir(path))
        else:
            update.message.reply_text("Directory not Found.")

def put(bot, update):
    f = open(str(os.getcwd())+"/file", "r")
    file_id = f.read()
    f.close
    if file_id == "":
        update.message.reply_text("You didn't upload file.")
    else:
        new_file = bot.get_file(file_id)
        message = update.message.text.split(" ")
        path = message[-1]
        if len(path) < 1:
            update.message.reply_text("Enter Path correctly.")
        else:
            new_file.download(os.getcwd()+'/'+path)
            update.message.reply_text("File Stored.")


def mkdir(bot, update):
    message = update.message.text.split(" ")
    if len(message) < 1 or message[-1] == "/mkdir":
        update.message.reply_text("Invalid Syntax. Refer syntax in help section.")
        return
    path = os.getcwd() + "/" + message[-1]
    os.mkdir(path)
    update.message.reply_text("Folder Created.")


def echo(bot, update):
    """Echo the user message."""
    if update.message.document:
        file_id = update.message.document.file_id
        f = open(str(os.getcwd())+"/file", "w")
        f.write(file_id)
        f.close
        update.message.reply_text("Received.Now send file name and location to store. using /put command")
    else:
        reply = "Invalid Input."
        update.message.reply_text(reply)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def add_user(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        username = update.message.text.split(" ")[-1]
        username_list.append(username)
        update.message.reply_text("User added.")
    else:
        update.message.reply_text("You are not Authorized.")

def show_user(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        update.message.reply_text(username_list)
    else:
        update.message.reply_text("You are not Authorized.")

def remove_user(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        username = update.message.text.split(" ")[-1]
        username_list.remove(username)
        update.message.reply_text("User Removed.")
    else:
        update.message.reply_text("You are not Authorized.")

def remove(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        filename = update.message.text.split(" ")[-1]
        os.remove(os.getcwd()+ "/" + filename)
        update.message.reply_text("File Removed.")
    else:
        update.message.reply_text("You are not Authorized.")

def rmdir(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        filename = update.message.text.split(" ")[-1]
        shutil.rmtree(os.getcwd()+ "/" + filename)
        update.message.reply_text("Folder Removed.")
    else:
        update.message.reply_text("You are not Authorized.")

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    TOKEN = os.environ['TOKEN']
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("get", get))
    dp.add_handler(CommandHandler("ls", ls))
    dp.add_handler(CommandHandler("put", put))
    dp.add_handler(CommandHandler("mkdir", mkdir))

    #admin functionalities
    dp.add_handler(CommandHandler("adduser", add_user))
    dp.add_handler(CommandHandler("showuser", show_user))
    dp.add_handler(CommandHandler("removeUser", remove_user))
    dp.add_handler(CommandHandler("remove", remove))
    dp.add_handler(CommandHandler("rmdir", rmdir))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.document, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
