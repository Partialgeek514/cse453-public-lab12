########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class allows one user to interact with the system
########################################################################

import messages
from control import Control

###############################################################
# USER
# User has a name and a password
###############################################################
class User:
    def __init__(self, name, password, security_level):
        self.name = name
        self.password = password
        self.security_level = security_level

userlist = [
   [ "AdmiralAbe",     "password", Control.SECRET ],  
   [ "CaptainCharlie", "password", Control.PRIVILEGED ], 
   [ "SeamanSam",      "password", Control.CONFIDENTIAL ],
   [ "SeamanSue",      "password", Control.CONFIDENTIAL ],
   [ "SeamanSly",      "password", Control.CONFIDENTIAL ]
]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [*map(lambda u: User(*u), userlist)]

ID_INVALID = -1

######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

    ##################################################
    # INTERACT CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username, password, messages):
        self.auth = self._authenticate(username, password)
        self._username = username
        self._p_messages = messages

    ##################################################
    # INTERACT :: SHOW
    # Show a single message
    ##################################################
    def show(self):
        id_ = self._prompt_for_id("display")
        if not self._p_messages.show(id_, self._subject_control_from_user(self._username)):
            print(f"ERROR! Message ID \'{id_}\' does not exist")
        print()

    ##################################################
    # INTERACT :: DISPLAY
    # Display the set of messages
    ################################################## 
    def display(self):
        print("Messages:")
        self._p_messages.display(self._subject_control_from_user(self._username))
        print()

    ##################################################
    # INTERACT :: ADD
    # Add a single message
    ################################################## 
    def add(self):
        self._p_messages.add(self._prompt_for_control(),
                             self._prompt_for_line("message"),
                             self._username,
                             self._prompt_for_line("date"),
                             self._subject_control_from_user(self._username))

    ##################################################
    # INTERACT :: UPDATE
    # Update a single message
    ################################################## 
    def update(self):
        id_ = self._prompt_for_id("update")
        if not self._p_messages.show(id_):
            print(f"ERROR! Message ID \'{id_}\' does not exist\n")
            return
        self._p_messages.update(id_, 
                                self._prompt_for_line("message"), 
                                self._subject_control_from_user(self._username))
        print()
            
    ##################################################
    # INTERACT :: REMOVE
    # Remove one message from the list
    ################################################## 
    def remove(self):
        self._p_messages.remove(self._prompt_for_id("delete"), self._subject_control_from_user(self._username))

    ##################################################
    # INTERACT :: PROMPT FOR LINE
    # Prompt for a line of input
    ################################################## 
    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    ##################################################
    # INTERACT :: PROMPT FOR ID
    # Prompt for a message ID
    ################################################## 
    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    ##################################################
    # INTERACT :: AUTHENTICATE
    # Authenticate the user: find their control level
    ################################################## 
    def _authenticate(self, username, password):
        id_ = self._id_from_user(username)
        if id_ == ID_INVALID:
            users.append(User(username, password, Control.PUBLIC))
            return True
        return ID_INVALID != id_ and password == users[id_].password

    ##################################################
    # INTERACT :: ID FROM USER
    # Find the ID of a given user
    ################################################## 
    def _id_from_user(self, username):
        for id_user in range(len(users)):
            if username == users[id_user].name:
                return id_user
        return ID_INVALID
    
    def _subject_control_from_user(self, username):
        user_id = self._id_from_user(username)
        return users[user_id].security_level
        
    def _prompt_for_control(self):
        self.display_security_options()
        text_control = input("{author}> ")
        while int(text_control) < 1 or int(text_control) > 4:
            print("Not a valid Security Level.")
            text_control = input("{author}> ")
        return Control(text_control)

#####################################################
# INTERACT :: DISPLAY USERS
# Display the set of users in the system
#####################################################
def display_users():
    for user in users:
        print(f"\t{user.name}")

