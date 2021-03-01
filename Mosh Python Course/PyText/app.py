from twilio.rest import Client

account_sid = 'ACc6906d597d4878f3561ae92363ea6833'
auth_token = '527f208d5bb43a3f7bea3d595260b5a9'

client = Client(account_sid, auth_token)

for x in range(10):
    call = client.messages.create(
        to='+447539394400',
        from_='+15632783758',
        body=f''' \n
        
        Message number {x}'''
    )
