
# Lecturo

Lecturo is a Django-based project for lecturers. This website helps with managing groups, schedules, attendance and messages.


## Tech Stack

**Client:** HTML, CSS, JavaScript (Soft UI by Creative Tim)

**Server:** Django, SQLite


## Features

- Adding/editing/deactivating Students
- Managing student groups
- Adding a list of subjects
- Adding lectures to your schedule. You can also edit or delete lectures.
- Reading messages from Students
- Option to check attendance at specific lectures
- Student preview, which automatically calculates the percentage of attendance for a given type of subject.

## Run Locally

Clone the project

```bash
  git clone https://github.com/RaiseCreed/Lecturo.git
```

Go to the project directory

```bash
  cd Lecturo
```

Create your virtual environment 

```bash
  pip install virtualenv
  virtualenv envname
```

Activate virtual environment 

```bash
  envname\scripts\activate
```

Install the requirements

```bash
  pip install -r requirements.txt
```

Run the app

```bash
  python manage.py runserver
```

> ⚠ Server will be started at http://127.0.0.1:8000/


## Screenshots

![loginPage](https://github.com/RaiseCreed/Lecturo/assets/104384996/5730aad8-b813-4fbd-8d48-f0caf9e87061)
![dashboard](https://github.com/RaiseCreed/Lecturo/assets/104384996/792cccf3-5727-402e-9998-a341e124073a)
![schedule](https://github.com/RaiseCreed/Lecturo/assets/104384996/38a96292-bc57-4279-80d0-24454f3425ea)
![profile](https://github.com/RaiseCreed/Lecturo/assets/104384996/dc26a951-f014-4fbc-a21b-6280ae0fbb82)
![group](https://github.com/RaiseCreed/Lecturo/assets/104384996/d3d2c53f-d2a8-4915-a290-af750314eb10)
![groups](https://github.com/RaiseCreed/Lecturo/assets/104384996/1df97648-d666-4d34-b2c3-547ad72dac45)
![messages](https://github.com/RaiseCreed/Lecturo/assets/104384996/389fd6df-2c84-471b-940b-9efa6e029627)
![messageDetails](https://github.com/RaiseCreed/Lecturo/assets/104384996/5ac93e64-e321-40db-8271-16eb5bb8f99c)





