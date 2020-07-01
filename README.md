# Jindal Elective Reviews

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Contributing](#usage)

## About <a name = "about"></a>

Jindal Electives Review is a portal where students can talk about their experiences in electives taken up during their academic years at Jindal Global University. This is to provide symmetry of information and an efficient feedback system whereby students who want to take a certain elective may have easy access to knowledge and material about the elective to make an informed choice.

At its present nascent stage, it allows users to leave comments anonymously at the individual page of every elective offered. The aim is to include further features like up-voting, uploading course material/notes etc. The information is all crowd-sourced. Users will only find information if people leave comments informing them about courses.

We hope you begin with commenting on electives you have taken, so that this page is helpful for you and others in the future!

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

First fork and clone the project on your local machine. Then you can run ```python3 manage.py runserver``` to run the website on your localhost. Since there is no local database you won't see any electives or comments, but you should have the website up and running.

You can find sample electives in the resources folder if you want to migrate them locally. 

### Prerequisites

What things you need to install the software and how to install them.

```
django
postgresql
python3
heroku
```

### Installing

To run the website, follow the following steps after creating a virtual environment.

Install all python dependencies

```
pip install -r requirements.txt
```

Run the server

```
python3 manage.py runserver
```

## Contributing <a name = "usage"></a>
The website is definitely lacking features so if you want to contribute then feel free to fork the repository and add features and then open a pull request. If you find any bugs or problems then make sure to open up an issue!

