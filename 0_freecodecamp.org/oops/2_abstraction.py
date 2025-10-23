# Abstraction

# Abstraction: To reduce complexity by hiding unnecessary details
# Real world example: TV Remote - Internal circuit board is hidden

class EmailService:
    def _connect(self):
        print("Connecting to email server...")

    def _authencticate(self):
        print("Authenticating....")

    def send_email(self):
        self._connect()
        self._authencticate()
        print("Sending email....")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server")

email = EmailService()

email.send_email() # we are calling only one useful function rest all are hidden for usage. Under the hoods send_email will use rest of the functions.

# output: 
# Connecting to email server...
# Authenticating....
# Sending email....
# Disconnecting from email server

# Note if we dont follow abstraction - like handling all the functions like connect, authenticating, disconnect inside the send_email
# then we need to call them like below outside the class individually and need to make each function public. 
# email.connect()
# email.authenticate()
# email.send_email()
# email.disconnect()