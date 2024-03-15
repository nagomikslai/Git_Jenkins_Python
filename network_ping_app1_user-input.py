import subprocess  
#import keyword
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():

    if request.method == "POST":
        details = request.form
        lpath = details['lpath']
        ofile = details['ofile']
        name1 = details['name1']
        name2 = details['name2']
        name3 = details['name3']
        name4 = details['name4']
        name5 = details['name5']

        def ping():
            
            output_file = lpath + ofile 

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("\033[1;33;40m" '[',"Date & Time =", ']', dt_string)	
            #with open("C:/Users/lzljf/Desktop/Python/webapp/network-ping-output.txt", "a") as f:
            with open(output_file, "a") as f:
                print(dt_string, file=f)

            local_host = 'hostname'
            print("\033[1;33;40m","Ping From Host:", local_host)
            #with open("C:/Users/lzljf/Desktop/Python/webapp/network-ping-output.txt", "a") as f:
            with open(output_file, "a") as f: 
                print('Ping From Host:', local_host, file=f)

            cmd = 'ping'

            print("\033[1;32;40m" '[',name1,']')
            result = subprocess.run([cmd, name1], stdout=subprocess.PIPE)
            print("\033[1;37;40m", result.stdout.decode('utf-8').strip('\n'),'\n')
            #with open("C:/Users/lzljf/Desktop/Python/webapp/network-ping-output.txt", "a") as f:
            with open(output_file, "a") as f:
                print(result, file=f)
            
            result1 = subprocess.Popen([cmd, '-n', '1', name1], stdout = subprocess.PIPE, encoding='utf-8') 
            result2 = str(result1.communicate())
            #print(result2)

            word1 = 'data:'
            word2 = '\\n'
            word3 = 'Reply'
            word = word1+word2+word3
            #print(word)

            #for i in result2.split():
            if word in result2.split():
                print("\033[1;33;40m" 'Ping', name1, 'UP', '\n')
            else:
                print("\033[1;31;40m" 'Ping', name1, 'DOWN', '\n') 

            print("\033[1;32;40m" '[',name2,']')
            result = subprocess.run([cmd, name2], stdout=subprocess.PIPE)
            print("\033[1;37;40m", result.stdout.decode('utf-8'), '\n')
            #with open("C:/Users/lzljf/Desktop/Python/webapp/network-ping-output.txt", "a") as f:
            with open(output_file, "a") as f:
                print(result, file=f)

            result1 = subprocess.Popen([cmd, '-n', '1', name2], stdout = subprocess.PIPE, encoding='utf-8') 
            result2 = str(result1.communicate())
            #print(result2)

            word1 = 'data:'
            word2 = '\\n'
            word3 = 'Reply'
            word = word1+word2+word3
            #print(word)

            #for i in result2.split():
            if word in result2.split():
                print("\033[1;33;40m" 'Ping', name2, 'UP', '\n')
            else:
                print("\033[1;31;40m" 'Ping', name2, 'DOWN', '\n') 

            print("\033[1;32;40m" '[',name3,']')
            result = subprocess.run([cmd, name3], stdout=subprocess.PIPE)
            print("\033[1;37;40m", result.stdout.decode('utf-8'), '\n')
            #with open("C:/Users/lzljf/Desktop/Python/webapp/network-ping-output.txt", "a") as f:
            with open(output_file, "a") as f:
                print(result, file=f)

            result1 = subprocess.Popen([cmd, '-n', '1', name3], stdout = subprocess.PIPE, encoding='utf-8') 
            result2 = str(result1.communicate())
            #print(result2)

            word1 = 'data:'
            word2 = '\\n'
            word3 = 'Reply'
            word = word1+word2+word3
            #print(word)

            #for i in result2.split():
            if word in result2.split():
                print("\033[1;33;40m" 'Ping', name3, 'UP', '\n')
            else:
                print("\033[1;31;40m" 'Ping', name3, 'DOWN','\n')

            print("\033[1;32;40m" '[',name4,']')
            result = subprocess.run([cmd, name4], stdout=subprocess.PIPE)
            print("\033[1;37;40m", result.stdout.decode('utf-8'), '\n')
            #with open("C:/Users/lzljf/Desktop/Python/webapp/network-ping-output.txt", "a") as f:
            with open(output_file, "a") as f:
                print(result, file=f)

            result1 = subprocess.Popen([cmd, '-n', '1', name4], stdout = subprocess.PIPE, encoding='utf-8') 
            result2 = str(result1.communicate())
            #print(result2)

            word1 = 'data:'
            word2 = '\\n'
            word3 = 'Reply'
            word = word1+word2+word3
            #print(word)

            #for i in result2.split():
            if word in result2.split():
                print("\033[1;33;40m" 'Ping', name4, 'UP', '\n')
            else:
                print("\033[1;31;40m" 'Ping', name4, 'DOWN', '\n') 

            print("\033[1;32;40m" '[',name5,']')
            result = subprocess.run([cmd, name5], stdout=subprocess.PIPE)
            print("\033[1;37;40m", result.stdout.decode('utf-8'), '\n')
            #with open("C:/Users/lzljf/Desktop/Python/webapp/network-ping-output.txt", "a") as f:
            with open(output_file, "a") as f:
                print(result, file=f)

            result1 = subprocess.Popen([cmd, '-n', '1', name5], stdout = subprocess.PIPE, encoding='utf-8') 
            result2 = str(result1.communicate())
            #print(result2)

            word1 = 'data:'
            word2 = '\\n'
            word3 = 'Reply'
            word = word1+word2+word3
            #print(word)

            #for i in result2.split():
            if word in result2.split():
                print("\033[1;33;40m" 'Ping', name5, 'UP', '\n')
            else:
                print("\033[1;31;40m" 'Ping', name5, 'DOWN', '\n') 

        if __name__ == '__main__':
            ping()
                      
    return render_template('index3.html',datetime = str(datetime.now()))

if __name__ == '__main__':
    app.run()