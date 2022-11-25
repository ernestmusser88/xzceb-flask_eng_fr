import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['MY3ZS8siRrGUydE6RtLCw7c5uRvFARrELVDT6ossi86Q']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/6550b837-7d26-43e8-b6c6-aa7345fe2741']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)
#set service url to US South Dallas
language_translator.set_service_url('{url}')
# disabling SSL for self signed cert
language_translator.set_disable_ssl_verification(True)

#English to French 
def englishToFrench(englishText):
    #write the code here
    frenchText = language_translator.translate(
    text= englishText,
    model_id='en-fr').get_result()

    return frenchText

#French to English
def frenchToEnglish(frenchText):
    #write the code here
    frenchText = language_translator.translate(
    text= englishText,
    model_id='en-fr').get_result()
    
    return englishText