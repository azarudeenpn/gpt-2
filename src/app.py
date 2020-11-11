from flask import Flask, request


import subprocess


def start(executable_file):
    return subprocess.Popen(
        ["python3", executable_file],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def read(process):
    return process.stdout.readline().decode("utf-8").strip()


def write(process, message):
    process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    process.stdin.flush()


def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)


process = start("src/interactive_conditional_samples.py")

app = Flask(__name__)

@app.route('/',methods=['POST'])
def generate_data():
    request_data = request.get_json()
    textinput = request_data['input']
    print("process: ",process.pid)
    write(process,textinput)

    return read(process)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
