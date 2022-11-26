import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator('MY3ZS8siRrGUydE6RtLCw7c5uRvFARrELVDT6ossi86Q')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
#set service url to US South Dallas
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/6550b837-7d26-43e8-b6c6-aa7345fe2741')

#English to French 
def englishToFrench(englishText):
    
    if englishText != None:
        #Call Translation Service
        translation = language_translator.translate(
        text= englishText,
        model_id='en-fr').get_result()
        #Access translated response
        frenchText = translation['translations'][0]['translation']
        return frenchText
    else:
        return None

    

#French to English
def frenchToEnglish(frenchText):
    
    if frenchText != None:
        #Call Translation Service
        translation = language_translator.translate(
        text= frenchText,
        model_id='fr-en').get_result()
        #Access translated response
        englishText = translation['translations'][0]['translation']
        return englishText
    else:
        return None

