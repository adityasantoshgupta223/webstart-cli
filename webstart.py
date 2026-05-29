import sys
import os 
import subprocess as sub

def creation(proj_name):
    os.mkdir(proj_name)
    path = os.getcwd()
    folder = os.path.join(path, proj_name)
    htmlFile = os.path.join(folder, proj_name + ".html")
    cssFile = os.path.join(folder, proj_name + ".css")
    jsFile = os.path.join(folder, proj_name + ".js")

   
    with open(htmlFile, "+w") as file:
           str = getTemplate()
           str = str.replace("href", f'href="{proj_name}.css"')
           str = str.replace("src", f'src="{proj_name}.js"')
           file.write(str)
    with open(cssFile, "+w") as file:
        pass
    with open(jsFile, "+w") as file:
        msg = "Let's get started!!!"
        str = f'alert("{msg}")'
        file.write(str)

def getTemplate():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "template.txt")

    with open(file_path, "+r") as file:
        content = file.read()

    return content

def getStarted(proj_name):
    path = os.path.join(proj_name)
    cmd = f'code "{path}"'

    try:
        result = sub.run(cmd, shell=True)

        if result.returncode != 0:
            print("VS Code is not installed or 'code' command is unavailable.")
        else:
            print("Opened in VS Code Successfully")

    except Exception as e:
        print("Error:", e)

if len(sys.argv) < 2:
    print("Usage: python script.py <project_name>")
    sys.exit()

proj_name = sys.argv[1]

creation(proj_name)
print("Successfully Created!!!")
getStarted(proj_name)