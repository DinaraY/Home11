from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def page_index():
    page_content = """ 
    <h1>Александр Юник</h1>

    """
    return page_content

if __name__ == '__main__':
    app.run()