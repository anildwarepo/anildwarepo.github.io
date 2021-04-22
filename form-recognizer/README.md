### Install Form-recognizer dependency

    $ pip install azure-ai-formrecognizer --pre

### Place Documents in a Folder location

### Update Form Recognizer API endpoint and Key

    form_recognizer_client = FormRecognizerClient(endpoint="https://<>.cognitiveservices.azure.com/", credential=AzureKeyCredential("<key>"))
        
### Update folder path variable

    filepath = "Path to Folder that contains documents"
    
### Run Recognize on Folder Path
  
    $ python recognizer-document.py

