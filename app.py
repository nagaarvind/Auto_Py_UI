from flask import Flask, render_template, request, redirect, url_for
import generate_graph

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fileuploaded', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    print(uploaded_file.filename)
    
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    generate_graph.get_filename(uploaded_file.filename)
    return 'success'

if __name__ == '__main__':
   app.run(debug = True,port=80)
