from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def user_page():
    marks = {"maths":70,"c++":50,"java":40}
    return render_template('tmp.html',name = marks)

if __name__ =="__main__":
    app.run(debug=True)
