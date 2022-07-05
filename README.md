# Question generator #
### *Generator of questions from the question base - automation of effective learning.* ###

### List of contents: ###
1. About the code.
2. Manner and purpose of use.
3. About the sample data used.
4. Python modules used.

![Picture](https://th.bing.com/th/id/R.13ef639cac544d3d6b61939e019f2e9d?rik=Ve%2fHUsQlpC%2b0cQ&riu=http%3a%2f%2fwww.thebluediamondgallery.com%2fwooden-tile%2fimages%2fexam.jpg&ehk=78u6gbUFuyGXH8Mrt5bDJaTiXjOkxnlVvOM6x222AaQ%3d&risl=&pid=ImgRaw&r=0)
Source: *https://th.bing.com/th/id/R.13ef639cac544d3d6b61939e019f2e9d?rik=Ve%2fHUsQlpC%2b0cQ&riu=http%3a%2f%2fwww.thebluediamondgallery.com%2fwooden-tile%2fimages%2fexam.jpg&ehk=78u6gbUFuyGXH8Mrt5bDJaTiXjOkxnlVvOM6x222AaQ%3d&risl=&pid=ImgRaw&r=0*

### 1. About the code. ###

When studying topics for the bachelor's exam, I decided to create a simple question generator from a question bank to make learning more effective and enjoyable. The program works like flashcards.

**The program:**
- creates a question bank based on the loaded CSV file containing questions and answers;
- informs the user about the error and allows to handle it - an empty question or answer field in the loaded file;
- displays questions from the pool in random order;
- asks for permission to show the answer to the randomly selected question;
- supports the consolidation of issues (asks whether to re-add a randomly selected question to the database of randomly selected questions);
- displays the final report - how many questions have been redone or indicates that all questions have been redone.

### 2. Manner and purpose of use. ###

The program will be useful both for studying for the exam, and also as flashcards for learning a language (vocabulary or phrases).

### 3. About the sample data used. ###

The database of questions used is based on the issues for the undergraduate exam in geoinformatics at the University of Warsaw. Detailed questions and answers have been prepared for personal use.

### 4. Python modules used. ###

- csv
- dataclasses
- random
- sys
- time

*Author: Marta Solarz*
