########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import control, message

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, subject_control):
        for m in self._messages:
            if self.security_condition_read(m.text_control, subject_control):
                m.display_properties()
            else:
                print("\tYou are not authorized to view this message.")       

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id, subject_control, update_bool=False):
        for m in self._messages:
            if m.get_id() == id:
                if update_bool == False:
                    if self.security_condition_read(m.text_control, subject_control):
                        m.display_text()
                        return True
                else:
                    return True
        return False

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text, subject_control):
        for m in self._messages:
            if m.get_id() == id:
                if self.security_condition_write(m.text_control, subject_control):
                    m.update_text(text)
                    return
                else:
                    print("You are not authorized to update this message.")
                    return
        print("Message ID not found")

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id, subject_control):
        for m in self._messages:
            if m.get_id() == id:
                if self.security_condition_write(m.text_control, subject_control):
                    m.clear()
                    return
                else:
                    print("You are not authorized to remove this message.")
                    return
        print("Message ID not found")            

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, subject_control, text_control, text, author, date, messageLoading=False):
        if self.security_condition_write(text_control, subject_control) or messageLoading:
            m = message.Message(text_control, text, author, date)
            self._messages.append(m)
        else: 
             print("Your request has been submitted. You are not Authorized to write here.")

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    self.add(control.Control.SECRET, text_control, text.rstrip('\r\n'), author, date, True)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
            
    def security_condition_read(self, asset_control, subject_control):
        return subject_control >= asset_control
    
    def security_condition_write(self, asset_control, subject_control):
        return subject_control <= asset_control 
    