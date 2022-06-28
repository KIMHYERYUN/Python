#send text message service
#https://console.twilio.com/

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#내 계정 설정
account_sid = os.environ[""]
auth_token = os.environ[""]
#클라이언트 설정
client = Client(account_sid, auth_token)
#메세지 설정
message = client.messages \
                .create(
                     body="It's going to rain today. You need an umbrella ☂.",
                     from_='+8210',
                     to='+18286722158'
                 )
#메세지 전송상태
#print(message.status)
#성공적으로 전송여부
print(message.sid)
