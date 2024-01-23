from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from sentence_transformers import SentenceTransformer
import json
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-2-1_6b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/stablelm-2-1_6b",
  trust_remote_code=True,
  torch_dtype="auto",
)
model.cuda()

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.post("/complete")
@cross_origin()
def main():
    print("post method")
    print(f"completing: {request.json['text']}")

    inputs = tokenizer(request.json['text'], return_tensors="pt").to(model.device)
    tokens = model.generate(
        **inputs,
        max_new_tokens=1,
        temperature=0.70,
        top_p=0.95,
        do_sample=True,
        repetition_penalty=1.1
    )

    out_token = tokenizer.decode(tokens[0, -1:], skip_special_tokens=True)
    return Response(json.dumps({'token': out_token}), content_type='Application/json')

    # return f'{"token": "Hello world"}'

