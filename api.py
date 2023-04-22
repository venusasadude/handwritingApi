import json
import base64
from model import HLTRModel
from flask import Flask, request
app = Flask(__name__)


charlist = open("static/model/charList.txt").read()
hltr_model = HLTRModel(charlist, testing=False)


@app.route('/api/v1/hltr-recognize', methods=['POST'])
def predict():
  image_string = request.get_json()["image"]
  image_data = base64.b64decode(image_string)
  image_path = "static/tmp.png"
  with open(image_path, "wb") as file:
        file.write(image_data)
  res  = hltr_model.recognize(image_path)
  if not res:
    return json.dumps({"failed to process"})
  recognized, corrected = res
  result = {"recognized": recognized, "corrected": corrected}
  return json.dumps(result)








if __name__ == '__main__':
    app.run()