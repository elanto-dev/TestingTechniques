# TestingTechniques
This repository contains code for the Testing Techniques course. 

## Matrix homeserver setup
For this project we use Matrix homeserver API as our System Under Test. We run homeserver locally on the computer and the process how to install Matrix homeserver is provided in the Wiki of this repository.

## Assignment 2

We use Python programming language to script the automated tests described in assignment 1. Tests were run in the Visual Studio Code IDE with two installed extensions: __python__ and __pylance__. The language version we used for the scripts is 3.9.10, but tests are highly likely to work with later versions of the language. 

Project structure:
* ___apitests.py___ contains the unit tests for 12 black-box test cases described in the first assignment;
* ___apirequests.py___ contains code that sends the requests to the Matrix homeserver and registers the responses;
* ___constants.py___ contains constant values used in this project.
