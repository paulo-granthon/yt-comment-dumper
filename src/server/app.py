import os
from flask import Flask, render_template
from logic import build_comment_tree
from src.db import get_client

app = Flask(
    __name__,
    template_folder=os.path.abspath(os.path.dirname(__file__))
)

@app.route('/')
def index():
    collection = get_client()
    comments_cursor = collection.find()
    comments = list(comments_cursor)
    comment_tree = build_comment_tree(comments)
    return render_template('index.html', comments=comment_tree)

if __name__ == '__main__':
    app.run(debug=True)
