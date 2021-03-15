# Portfolio Management Interface Project

### Status: [![Build Status](https://travis-ci.com/Housing-Valuation-Analysis/Portfolio-Management.svg?branch=main)](https://travis-ci.com/Housing-Valuation-Analysis/Portfolio-Management)


### Last Edit: 3/15/21

## Contributors: Jack Chen, William Frame, Vincent Lan, Aniruddha Dutta, Junhao Zhang, Samuel Perebikovsky

### Introduction

Welcome to the README file for our project! This goal of this project is to create a dashboard with pertinent data about stocks so that value investors can compare the attributes of multiple companies at once. We obtain our data through a scraper from Yahoo Finance and then send that information to our web interface which allows users to choose which stocks they look at and interact with our interface. Our project offers a more efficent solution to compare specific attributes of different stocks simultaneously.

### Usage

The way this project will interact with its users is as follows: A user will enter from the web interface and be greeted with an input menu. From there there are two 'use cases' that can happen based on user preference.
First is a more detailed view of a single stock. The user can type in a ticker symbol of the company they want more specific infomration on. Once a ticker is inputted, the web interface sends that ticker to our scraper which finds the data and sends it back to the web interface where it is then displayed. This format lends itself nicely for doing deep dives on one particular stock and making an informed purchase decision.
The second use case involves comparing the stocks of multiple companies at the same time. Here, as before, the user input tells the scraper which stock to retrieve information on, but this time, the information in stored in a dashboard with the most prominent features on display. This format lends itself nicely for comparisons between multiple companies and making choices to decide which company to invest in. 

### Features

We have a dashboard table that lets user see all the relevant information from multiple stocks, chosen by the user, at once, adding an aspect of customizability. We also have a view that displays even more information than the dashboard, but only for one stock. In addition, we have added user accounts so that their preferences and stock information can be saved for future logins. 

### Dependencies

This project mainly relies on a few libraries to run properly. Namely, 'requests' and 'BeautifulSoup' on the web scraper side of the project. While the web interface side relies on 'Django'. The full list of dependiencies can be found at 'requirements.txt'. Other notable dependencies include:
- urllib3
- pytest
- pathlib
- flake8

### Installation

Warning: this program may not be supported with Mac/Windows operating systems. If you are running into problems on a Mac/Windows computer try removing the `3` from the `python3` and `pip3` instances in the code below.

To install `Portfolio-Management` you will need to begin by cloning the project's git repository by using the following `git` command: 

```
git clone https://github.com/Housing-Valuation-Analysis/Portfolio-Management.git
```

Next, you will want change directories into the `Portfolio-Management` repository if you are not already there and automatically run the program by typing the following into the command line:

```
sh run_program.sh
```

If the automatic method above does not work, below are the steps to ensure it runs:

Install the file named `setup.py` using the following code:

```
python3 setup.py install
```

And to make sure all the dependencies are on your machine run:

```
pip3 install -r requirements.txt
```

Then to launch the webpage, we change directory into the `stocks` folder and run `manage.py` by using the following code:

```
cd stocks
python3 manage.py runserver
```

### Organization

This project is organized as follows:
```
Portfolio-Management/  
|- .gitignore  
|- .travis.yml  
|- README.md  
|- __init__.py  
|- requirements.txt  
|- scrapingR1.ipynb  
|- scraping/  
   |- __init__.py  
   |- clients.py  
   |- constants.py  
   |- errors.py  
   |- metrics_string_process.py  
   |- scraper.py  
   |- tests/  
      |- __init__.py  
      |- test_scraper.py  
      |- data/  
         |- ...  
|- stocks/  
   |- __init__.py  
   |- db.sqlite3  
   |- errors.py  
   |- manage.py  
   |- quotes/ 
      |- ...  
      |- templates/  
         |- ...  
   |- stocks/  
      |- ...  
```

_____________________________________________________________________________________________
_____________________________________________________________________________________________

