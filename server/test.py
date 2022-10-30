import os

# Find your Account SID and Auth Token in Account Info
# and set the environment variables. See http://twil.io/secure
account_sid = "AC4fe03fe7e0b561f68567b0208c6e4d68"
auth_token = "55b1799faa0a1c9aa2911e18d5b5a701"
client = Client(account_sid, auth_token)


def sendMessage(message, mobNumber):
    message = client.messages.create(body=message,
                                     from_="+18316043309",
                                     to="+91" + mobNumber)

    print("message send" + str(message.sid))
