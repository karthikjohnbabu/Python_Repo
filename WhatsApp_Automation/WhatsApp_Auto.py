from twilio.rest import Client

account_sid = 'AC068d8d0a4654ae0b47bc237653571922'
auth_token = '94ffbba67ac2676c360256de3353b786'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='This is a whatsapp automated message from twillo and pycharm by karthik Babu',
    to='whatsapp:+919'
)

print(message.sid)