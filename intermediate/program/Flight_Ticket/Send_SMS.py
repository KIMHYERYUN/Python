from infobip_api_client.api_client import ApiClient, Configuration

BASE_URL = "https://yrj81j.api.infobip.com"
API_KEY = ""

SENDER = "InfoSMS"
RECIPIENT = "8210"
MESSAGE_TEXT = "This is a sample message"

from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException

"""
 * Send an sms message by using Infobip API.
 *
 * This example is already pre-populated with your account data:
 * 1. Your account Base URL
 * 2. Your account API key
 * 3. Your recipient phone number
 *
 * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!
 *
 * Send sms API reference: https://www.infobip.com/docs/api#channels/sms/send-sms-message
 * See Readme file for details.
"""

BASE_URL = "https://yrj81j.api.infobip.com"
API_KEY = ""

SENDER = "InfoSMS"
RECIPIENT = ""


client_config = Configuration(
        host= BASE_URL,
        api_key={"APIKeyHeader": API_KEY},
        api_key_prefix={"APIKeyHeader": "App"},
    )


class SendSMS:
    def __init__(self):
        self.api_client = ApiClient(client_config)

    def send_sms(self, message):
        sms_request = SmsAdvancedTextualRequest(
                messages=[
                    SmsTextualMessage(
                        destinations=[
                            SmsDestination(
                                to=RECIPIENT,
                            ),
                        ],
                        _from=SENDER,
                        text=message,
                    )
                ])

        api_instance = SendSmsApi(self.api_client)

        try:
            api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
            print(api_response)
        except ApiException as ex:
            print("Error occurred while trying to send SMS message.")
            print(ex)
