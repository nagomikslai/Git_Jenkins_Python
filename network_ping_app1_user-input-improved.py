import subprocess
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        lpath = details['lpath']
        ofile = details['ofile']
        names = [details[f'name{i}'] for i in range(1, 6)]

        def ping():
            output_file = f"{lpath}/{ofile}"
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
            with open(output_file, "a") as f:
                print(dt_string, file=f)
                
            print("[Date & Time =]", dt_string)
            print("Ping From Host: hostname")
            with open(output_file, "a") as f:
                print('Ping From Host: hostname', file=f)

            for name in names:
                print(f"[{name}]")
                result = subprocess.run(['ping', '-c', '1', name], capture_output=True, text=True)
                print(result.stdout)
                with open(output_file, "a") as f:
                    f.write(result.stdout)

                if "1 received" in result.stdout:
                    print(f"Ping {name} UP\n")
                else:
                    print(f"Ping {name} DOWN\n")

        ping()
                      
    return render_template('index3.html', datetime=str(datetime.now()))

if __name__ == '__main__':
    app.run(host='0.0.0.0')