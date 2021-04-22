from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient
import os

form_recognizer_client = FormRecognizerClient(endpoint="https://<>.cognitiveservices.azure.com/", credential=AzureKeyCredential("<key>"))





def recognize_content(filename):
    with open(filename, "rb") as source:
        poller = form_recognizer_client.begin_recognize_content(form=source)
    form_pages = poller.result()

    aer_selection = []
    #page = form_pages[0]
    for page in form_pages:
        for table in page.tables:
            for cell in table.cells:
                print("Cell[{}][{}] has text '{}'".format(
                    cell.row_index,
                    cell.column_index,
                    cell.text
                ))
                if cell.field_elements:
                    for element in cell.field_elements:
                        if element.kind == "selectionMark":
                            print("...Checkbox in cell is '{}' and has confidence of {}".format(
                                element.state, element.confidence
                            ))
                            if element.state == "selected" and element.confidence > 0.8:
                                aer_selection.append(cell.text)
        print("nAER Selection: {}".format(aer_selection))

filepath = "Path to Folder that contains documents"
for file in os.listdir(filepath):
    print("filename:" + file)
    recognize_content(file)



