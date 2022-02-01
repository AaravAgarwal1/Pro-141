from flask import Flask, jsonify, request
import csv

all_articles = [ ]

with open('articles.csv', encoding = "utf8") as f: #if we do not provide encoding, it might give error
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:] 

liked_articles = [ ]
not_liked_articles = [ ]


app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0], 
        "status":"success" #status will be as success
    })

@app.route("/liked-article",methods =["POST"])
def liked_article():
    liked_articles.append(all_articles[2]) 
    all_articles.remove(all_articles[2]) 
    return jsonify({
        "status":"success" #status success
    }), 201 #error handling

#running the app
if __name__ == "__main__":
    app.run()