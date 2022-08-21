import subprocess

def pushx(input, args):
    l = ['pushx']
    l.extend(args)
    process = subprocess.Popen(l,
                     stdout=subprocess.PIPE, 
                     stdin=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    process.stdin.write(input.encode())
    process.stdin.close()
    process.wait()