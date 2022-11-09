'''We use IBM Watson API to translato from English to French and viceversa'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    '''English to French translator'''
    try:
        french_text = language_translator.translate(text=english_text, model_id='en-fr')
        french_text = french_text.get_result()
        french_text = french_text['translation'][0]['translation']
    except IOError:
        french_text=""
        print("Error: try again")
    return french_text

def french_to_english(french_text):
    '''French to english translator'''
    try:
        english_text = language_translator.translate(text=french_text, model_id='fr-en')
        english_text = english_text.get_result()
        english_text = english_text['translation'][0]['translation']
    except IOError:
        english_text=""
        print("Error: try again")
    return english_text