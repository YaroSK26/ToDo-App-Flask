from flask import Flask, render_template, request, redirect, url_for
#flask - aplikacia , render - html file  spojenie , request- post request data , redirect - to another page , url- for endpoints

app = Flask(__name__, template_folder="templates")

todos = [{"task": "Sample Todo", "done" :False}]


@app.route('/') #endpoint , stale rovnake 
def index():
    return render_template('index.html' , todos=todos) 


@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo'] # beriem input data podla name
    todos.append({"task": todo, "done" : False}) # task - uloha , done ci je hotove 
    return redirect(url_for('index')) # redirectne aj ked sa zmeni index url 

@app.route("/edit/<int:index>", methods=["POST", "GET"])
def edit(index):
    todo= todos[index]
    if request.method == 'POST':
        todo["task"] = request.form['todo']
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', todo=todo, index=index)
    
@app.route("/check/<int:index>")
def check(index):
    if index < len(todos):
        todos[index]["done"] = not todos[index]["done"]
    return redirect(url_for('index'))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)