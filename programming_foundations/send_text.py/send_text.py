#from twilio.rest import Client # inside twilio is a folder called rest.
                                # Inside that rest folder is a class called Client. We will use class in our code
from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC163236635356082194924c68dfc64307"  #my account_sid
# Your Auth Token from twilio.com/console
auth_token  = "db799d17229e4c8a5ef1c47175c4a0db"    #my auth_token

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+14084396834",    #my mobile #
    from_="+18316071873", #my twilio #
    body="Hello from Python!")

print(message.sid)