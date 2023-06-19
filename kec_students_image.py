import requests
import shutil
import os

url = "https://results.kongu.edu/Photos/"
extension = ".jpg"

# CHANGE THE REGULATION AND DEPARTMENT
regulation = "19"
department = "IT"

path = ""
err_rollno = ""


def create_directory(dept):
    if not os.path.exists("./"+regulation):
        os.mkdir("./"+regulation)
        print("Path Created : " + regulation)
    else:
        print("Path Already Exists : " + regulation)

    if not os.path.exists("./" + path):
        os.mkdir("./" + path)
        print("Path Created : " + dept)
    else:
        print("Path Already Exists : " + dept)


def fetch_image(dept):
    global rollno_start
    global err_rollno
    if dept[-1] == "L":
        rollno_start = err_rollno
    while rollno_start <= rollno_end:
        id = regulation + dept + rollno_start
        response = requests.get(url + id + extension, stream=True)
        if response.status_code == 200:
            response.raw.decode_content = True
            with open(path + "/" + id + extension, "wb") as output_file:
                shutil.copyfileobj(response.raw, output_file)
                print("Image Created : " + id)
        else:
            response = requests.get(url + id + extension.upper(), stream=True)
            if response.status_code == 200:
                response.raw.decode_content = True
                with open(path + "/" + id + extension, "wb") as output_file:
                    shutil.copyfileobj(response.raw, output_file)
                    print("Image Created : " + id)
            else:
                print("Issue With Fetching Image From : " + rollno_start)
                print("No More Students In : " + dept)
                err_rollno = rollno_start
                break

        rollno_start = str(int(rollno_start) + 1).rjust(3, "0")


department_type = []
department_type.extend([department+"R", department+"L"])

rollno_start = "1".rjust(3, "0")
rollno_end = "300".rjust(3, "0")

for dept in department_type:
    path = regulation + "/" + dept
    create_directory(dept)
    fetch_image(dept)
