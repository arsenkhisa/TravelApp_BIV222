import os
import subprocess

os_is = "Unix"


def create_conda_venv():
    os.system("conda create -y -n myenv")
    os.system("conda install -y -n myenv pip")
    os.system(f"conda run -n myenv pip{'3' if os_is == 'Unix' else ''} "
              f"install -r requirements.txt")
    with open(".venv_made.txt", "w+") as file:
        file.write("myenv")


def create_user():
    result = "error"
    while "error" in result:
        root = input("Please, enter your MySQL root name: ")
        password = input("Input your MySQL password: ")

        a = f"""mysql -u {root} -p{password} -e "CREATE USER IF NOT EXISTS 'TravelUser'@'localhost' 
                                IDENTIFIED BY 'adv3nTur$'; GRANT ALL PRIVILEGES ON *.* 
                                 TO 'TravelUser'@'localhost';" """.replace("\n", "")
        try:
            result = subprocess.check_output(
                a, shell=True, text=True, encoding="utf-8"
            )
        except subprocess.CalledProcessError as e:
            print(e)
            print("Error occurred: login or password is incorrect")


def load_program():
    try:
        open(".venv_made.txt")
    except FileNotFoundError:
        create_conda_venv()
        create_user()
    os.system("conda run -n myenv python main.py")

load_program()
