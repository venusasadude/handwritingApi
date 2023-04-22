import json
import base64
import requests


def test_model():
    from model import HLTRModel, DecoderType
    
    test_image = "static/self.png"
    charlist = ' "\'(),-.0189:;ABCDEFGHILMNOPRSTUWYabcdefghijklmnopqrstuvwxyz'
    hltr = HLTRModel(
        charlist, DecoderType.BestPath, mustRestore=False, testing=False
    )
    recognized, corrected = hltr.recognize(test_image)
    print("Recognized: ", recognized)
    print("Corrected: ", corrected)


def test_hltr_api():
    filepath = "static/self.png"
    with open(filepath, "rb") as img:
        string = base64.b64encode(img.read()).decode('utf-8')
    
    api_url = "http://127.0.0.1:5000/api/v1/hltr-recognize"
    response = requests.post(url= api_url, json={'image':string})
    print("API Response: ", response.json())


if __name__ == '__main__':
    test_hltr_api()

    _ = input("press enter to exit")