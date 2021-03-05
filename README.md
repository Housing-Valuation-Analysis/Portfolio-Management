# Portfolio Management Interface Project

### Last Edit: 3/4/21

## Contributors: Jack Chen, William Frame, Vincent Lan, Aniruddha Dutta, Junhao Zhang, Samuel Perebikovsky

### Introduction

Welcome to the readme file for our project! This goal of this project is to create a dashboard with pertinent data about stocks so that value investors can compare the attributes of multiple companies at once. We obtain our data through a scraper from Yahoo Finance and then send that information to our web interface which allows users to choose which stocks they look at and interact to an extent with our interface. Our project offers a more efficent solution to compare specific attributes of different stocks simultaneously.

### Usage

The way this project will interact with its users is as follows: A user will enter from the web interface and be greeted with an imput menu. From there the user can type in a ticker symbol of the company they want infomration on. Once a ticker is inputted, the web interface sends that ticker to our scraper which finds the data and sends it back to the web interface which is then displayed in our dashboard. 

### Features

We have a dashboard table that lets user see all the relevant information from multiple stocks at once. Our search menu allows user to find the tickers they want to observe then add them to the dashboard for nice customizability. We also would like to add user accounts so that their preferences can be saved for a future login. 

### Dependencies

This project mainly relies on a few libraries to run properly. Namely, 'requests' and 'BeautifulSoup'on the web scraper side of the project. While the web interface side relies on 'Django'. The full list of dependiencies can be found at 'requirements.txt'. Other notable dependencies include:
- urllib3
- pytest
- pathlib
- flake8


### Organization

This project is organized as follows:

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


###################################################################################
###################################################################################

