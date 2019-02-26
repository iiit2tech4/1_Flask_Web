
# coding: utf-8

# In[3]:


## Flask In-Prod at Openshift Basic

from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, World!"
@app.route("/Redhat")
def Redhat():
    return "Hello, Redhat !"
@app.route("/Opensource")
def Opensource():
    return "Hello, Opensource !"
if __name__ == "__main__":
    app.run(debug=True)

