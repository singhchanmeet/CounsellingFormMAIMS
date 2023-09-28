## 📝 Introduction
 * This is the source code of <strong> The Admission and Counselling Portal for Maharaja Agrasen Institute of Management Studies </strong> made by me and <a href="https://github.com/exploring-solver"> Aman Sharma</a> under the guidance of CSE department, MAIT during July-August 2023..
 * If you are an Admin , please refer to the <a href="https://github.com/singhchanmeet/CounsellingFormMAIMS/blob/master/admin-docs.html"> admin-docs.html</a> file in the root directory of the project for an oversight on how to use the project.
 * If you are a developer who would like to contribute , please refer the detailed documentation below.

## ⚙️ Basic Setup
Clone the project repository :
```bash
git clone https://github.com/singhchanmeet/CounsellingFormMAIMS.git
```
Navigate to the project directory and run the command :
```bash
 pip install -r requirements.txt
```
Replace the DATABASES setting in <a href="https://github.com/singhchanmeet/CounsellingFormMAIMS/blob/master/CounsellingMAIMS/settings.py"> settings.py </a> file and then run the following commands

```bash
 python manage.py makemigrations
```
```bash
 python manage.py migrate
```
```bash
 python manage.py runserver
```
Go to http://127.0.0.1:8000/ to see the running project
