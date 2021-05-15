from flask import Flask , render_template , request 
import wolframalpha


app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/solve', methods=['GET', 'POST']) 

def solve():
    try:
        question = str(request.form['question'])
        app_id = "YOUR API KEY"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        answer = 'Answer:'+answer
        return render_template('index.html', answer=answer)
    except  Exception:
        return render_template('index.html' , answer='Please Enter The Question Properly')
if __name__ == '__main__':
    app.run(debug=True)
