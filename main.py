from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    script_name = request.form['script_name']
    subprocess.call(f'python {script_name}.py')
    return 'Script executed successfully!'

if __name__ == '__main__':
    app.run(debug=True)