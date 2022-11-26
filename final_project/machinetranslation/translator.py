"""Text conversion tool"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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
def english_to_french(english_text):
    """convert english to french"""
    if english_text is not None:
        #Call Translation Service
        translation = language_translator.translate(
        text= english_text,
        model_id='en-fr').get_result()
        #Access translated response
        french_text = translation['translations'][0]['translation']
        return french_text
    return None

#French to English
def french_to_english(french_text):
    """convert french to english"""
    if french_text is not None:
        #Call Translation Service
        translation = language_translator.translate(
        text= french_text,
        model_id='fr-en').get_result()
        #Access translated response
        english_text = translation['translations'][0]['translation']
        return english_text
    return None
