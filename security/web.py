from flask import Flask
import allow

# 加载os被禁止
#import os

# os未被加载
#print(os.name)

print(allow.name)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

app.run()