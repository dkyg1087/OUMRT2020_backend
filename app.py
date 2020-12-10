from flask import Flask,request
from flask_pymongo import pymongo
from flask import json
from flask import jsonify
import os
CONNECTION_STRING = "mongodb+srv://cookie:E125330273@cluster0.l02pb.mongodb.net/test_project?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.flask_mongodb_atlas
user_collection = pymongo.collection.Collection(db, 'user_collection')
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb atlas!"
@app.route('/query/<string:event_id>')
def query_user(event_id):
    if event_id:
        users = db.user.find({"event_id": event_id})
        x=[]
        if users:
            for i in users:
                i.pop("_id")
                x.append(i)
            return str(x)
    else:
        return 'No user found!'
#test to insert data to the data base
@app.route("/insert")
def test():
    db.user.insert_one({"event_id": "Mary","event_name":"金瓜石特快車","status": "green","driver_id": "ABC"})
    return "Insert success"
@app.route('/delete/<string:event_id>')
def delete_docs(event_id):
    db.user.remove({"event_id":event_id})
    return "Delete success"
@app.route('/update/<string:event_id>')
def update_docs(event_id):
    doc=db.user.update(
        {"event_id" : event_id},
        {"$set":
            {"status": "red"}
        },upsert=True)
    return "Update success"
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
# if __name__ == '__main__':
#     app.run(port=8000)