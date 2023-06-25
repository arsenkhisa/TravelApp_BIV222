import os
import subprocess
from platform import system

from file_loader import FileLoader

os_is = "Unix"


def create_conda_venv():
    os.system("conda create -n invest pip")
    run_conda()
    os.system("pip install -r requirements.txt")


def run_conda():
    path_conda = str(subprocess.check_output("conda info --base", shell=True,
                                             text=True, encoding="utf-8"))

    if os_is == "Unix":
        path_conda += "/etc/profile.d/conda.sh"
        path_conda = path_conda.replace('\n', '')
        os.system(f"source {path_conda}")
    else:
        os.system(f".{path_conda}\\bin\\activate")
    if os_is == "Unix":
        os.system("source activate invest")
    else:
        os.system("activate invest")

def create_python_venv():
    os.system("python -m venv myenv")
    run_python()
    os.system("pip install -r requirements.txt")


def run_python():
    if os_is == "Unix":
        os.system("source myenv/bin/activate")
    else:
        os.system(r".\myenv\Scripts\activate")


def create_user():
    root = input("Please, enter your MySQL root name\n")
    # password = input("Please, enter your MySQL root password")
    result = "error"
    password = ""

    while "error" in result:
        print("Required password is for root user of MySQL")
        password = input("Input your password: ")

        a = f"""mysql -u {root} -p{password} -e "CREATE USER IF NOT EXISTS 'TinkoffUser'@'localhost' 
                        IDENTIFIED BY '1nVestm$nt'; GRANT ALL PRIVILEGES ON *.* 
                         TO 'TinkoffUser'@'localhost';""".replace("\n", "")
        try:
            if os_is == "Unix":
                result = subprocess.check_output(
                    a, shell=True, text=True, encoding="utf-8"
                )
            else:
                try:
                    result = subprocess.check_output(
                        a, shell=True, text=True, encoding="utf-8"
                    )
                    print("here")
                except subprocess.CalledProcessError:
                    os.system(r"SET PATH=C:\Program Files\MySQL\MySQL Server 8.0\bin;%PATH%")
                    result = subprocess.check_output(
                        a, shell=True, text=True, encoding="utf-8"
                    )
        except subprocess.CalledProcessError as e:
            print(e)
            print("Error occurred: login or password is incorrect")
            root = input("Please, enter your MySQL root name\n")


def load_settings():
    global os_is

    if system() == "Windows":
        os_is = system()

    settings = FileLoader.get_json("info/files/.current_settings.json")
    if not ("venv" in settings):
        res = ""

        print("Hello! You need to choose conda or python.")
        while not (res in ['p', 'c']):
            res = input("Enter 'p' if you want to use python and 'c' "
                        "in case of conda\n")
        settings["venv"] = "python" if res == 'p' else "conda"
        create_user()

        create_conda_venv() if res == 'c' else create_python_venv()
        FileLoader.save_json("info/files/.current_settings.json", settings)

    if settings["venv"] == "conda":
        try:
            run_conda()
        except Exception as e:
            print("execution omg", e)
            create_conda_venv()
    else:
        try:
            run_python()
        except Exception as e:
            print(e)
            create_python_venv()
