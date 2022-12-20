# Recommender System
## First (of two) course projects

* An explanation of the recommender task that you are investigating and why you are 
  interested in it
* Information about your dataset and why you selected it
* An introduction to your recommender system, including how it works, whether you use 
  PCA or SVD (and why!), and how it selects three _new_ recommendations 
* A brief discussion about the quality of the recommendations for the two selected 
  users

Your report should be self-contained, meaning that all necessary figures should be 
contained within the documentation. You should also include your value add statement 
at the end of your report. The report should replace this readme.md file. You should 
make thoughtful use of [markdown formatting](https://www.markdownguide.org/basic-syntax/), 
including headings, sub-headings, paragraphs, and different kinds of font styles. 
There are no page requirements or limits; but if your report is less than 4 paragraphs 
or more than 20 paragraphs, we should check in about it. 

### Part 5 - Value Add Statement

It is common practice that programmers borrow code from each other and websites 
like stackoverflow. When you are not sure how to use a function or where to go next 
with your work, the ability to find code that suits your purpose or that can be 
extended to fit your needs is an invaluable one. Part of using others' code and 
ideas responsibly and respectfully includes 1) documenting where ideas and code came 
from (if not from you and your brain) and 2) articulating what you have done in terms 
of extending, adapting, or reshaping the code. 

For all projects in this course, I am asking that you write a **Value Add** statement. 
In this statement, you will clearly articulate:   
1. What resources you consulted,   
2. How you applied or adapted the ideas and code from those resources, and 
3. What new ideas and code you added  

In summary, the value add statement should be explicit where the ideas and code you 
consulted end and where your contributions begin. See _A few notes on grading coding_ 
_elements_ below for examples of low and high value add scenarios.

You should include the value add statement at the bottom of the readme file along with 
the citations for all consulted sources

## Submitting your Work

Your project will contain a number of files including:   
* At least one data file 
* At least one python file implementing your system  
* One python file with your tests  
* At least one data file 
* Documentation of your tests have passing both locally and on GitHub Actions. 
* A readme file with your report and value add statement  
* A `.gitignore` file

You may also include notebooks or other scratch work with your submission, but place 
these files inside a folder called `scratch`. 

## Feedback

 Topic                               | No Attempt | Partial | Complete | 
-----------------------------        |------------|---------|----------|
Build user-item matrix               |            |         |          |  
Discussion of data                   |            |         |          |  
Explaning specific recommender task  |            |         |          |
Explaining context for data and task |            |         |          |
Implementing Recommendation system   |            |         |          |   
Discussing PCA vs SVD                |            |         |          | 
Discussing three recommendations     |            |         |          |
Unit Tests                           |            |         |          |
Local tests                          |            |         |          |
GitHub Actions                       |            |         |          |


Topic                                | Have questions about| Could again without help | 
-----------------------------        |---------------------|--------------------------|
Build user-item matrix               |                     |                          |  
Discussion of data                   |                     |                          |  
Explaning specific recommender task  |                     |                          |
Explaining context for data and task |                     |                          |
Implementing Recommendation system   |                     |                          |   
Discussing PCA vs SVD                |                     |                          | 
Discussing three recommendations     |                     |                          |
Unit Tests                           |                     |                          |
Local tests                          |                     |                          |
GitHub Actions                       |                     |                          |



### A few notes on possible project "outcomes"

In any project, while a successful implementation is important, articulating your 
contributions is equally important. The feedback for this project attempts 
to codify these ideas. As such, the grading for a few extreme approaches to this 
project will be explained: 

* **Example 1: System works, but code is entirely from other sources** - In this first 
  example, the student has a working system, but clearly acknowledges that the code is from 
  a blog post with only surface level changes (like variable names) to adapt the code to the 
  student's chosen data. In this case, the project would be considered to be "half" successful
  for the working code since it functions but because most of the ideas are not the student's 
  own (or phrased another way, project has low "value add").
* **Example 2: System does not fully work, but code is entirely of the students creation**  
  **(and no sources were consulted)** - In this second example, the student used only class 
  resources (like the books and labs) to create their system that unfortunately does not 
  quite work. In this case, the project also would be considered to be "half" successful  
  non-working code since most of the ideas are the student's own (i.e. project has high "value
  add"). 

Having a successful implementation is only part of any project; explaining what your goals 
are, why they are important or interesting, and how you approached the achieving those 
goals are critical. The feedback for these projects balances the coding elements with the 
written ones. For example: 

* **Example 3: System works, but the readme file is not coherent, reading like a sequence** 
  **of events** - In this third example, we are only commenting on the grading of the 50 points 
  for the written elements. Here the project's readme follows a chronological retelling of 
  the coding; something like: "First I tried X and it didn't work. Then I tried Y and it did 
  better. Then this other thing was added and I like the results." In this project's write up, 
  there is little effort to educate the reader about the project's goals and methods, and as 
  such, the project would be considered less than "half" of a success (as the results are 
  presented in an inaccessible manner), assuming the readme file uses good 
  markdown styling and contains all the minimal elements for the report. 

## Reminders
* Don't forget to create a `.gitignore` for any notebook checkpoints that you create. 
* Any import statements should be at the top of your python files or in the first 
code block of a notebook. 

### Resources consulted 

* [Basic Syntax from Markdown Guide](https://www.markdownguide.org/basic-syntax/) 
* Value add statement based on an idea from Prof. Nick Howe (Smith College)
