# Project 1
## First (of two) course projects

Recalling that the purpose of the projects is to build things that use multiple 
concepts, in this project, you will be thinking about dimension reduction in the context 
of recommender systems. 

This project has 5 parts:   
1. Choosing a dataset for a recommender task, 
2. Designing and implementing a recommender system using a dimension reduction technique, 
3. Testing your system on specific examples, 
4. Documenting your work, and 
5. Writing a "Value-Add" Statement

### Part 1 - Choosing a dataset
A typical recommendation system takes collections of user ratings of items 
(ie. movies/books/stores) and _recommends_ the next item that a particular user 
would be interested in. 

Choose a dataset for this project that interests you. Note that you do not need to 
make "typical" recommendations (like movies, books, etc). So feel free to think about 
recommendation in a broad sense. 

In a usual recommendation system, the dataset contains **numerical ratings of items**, 
and clearly ties the ratings connect to individual users. (Hint: You may need to do 
some data transformations, but ultimately _users_ should be your observations). If 
you choose to do a less traditional recommender system (recommending characters, 
Pokemon, etc), you still need to think about the user-to-recommender set-up. 

I would recommend looking for data in one of these three places:
* [fivethirtyeight's data repository](https://github.com/fivethirtyeight/data)
* [Kaggle](https://www.kaggle.com/search?q=recommendation+in%3Adatasets)  
* The [UCI repository](http://archive.ics.uci.edu/ml/index.php) 

**Hint:** Think very carefully what 0 means in your data.

 * For example if 0 means "no rating" is that "closer" to 1 (a poor rating) or 5 (a great rating)
 * How do you want to think about "no rating"? Should you shift your recommendations so that a good rating is positive and a poor rating is negative?


### Part 2 - Designing a recommender system
In a recommender system, we want to make recommendations to users. So the output 
from our recommender system will be of a similar shape to our original data, with 
users as the observations and items as the variables. 

So far in class, we have used dimension reduction to transport our data from 
a higher dimension down to a lower one. We haven't practiced as much with pushing 
our lower dimensional approximation back to the original dimensional space. 

**One can think of a recommender system as the process of dimension reducing ratings 
data and then pushing the lower dimension approximation back to the original space.** 
Put another way, one can think about dimension reduction as a kind of currency exchange:

 * The data as in the original dimension as being in Currency A
 * The lowered dimension is something as being in Currency B. In this lower dimension we lose some information
 * Then we can push our new low dimensional representation back up to the original dimension (ie. Currency A)

The original data in Currency A and the reduced-pushed-back-up data in Currency A 
will not be exactly the same, as we saw in the image from Lab 05, that compared the 
original two-D data to the 1-d projection realized in 2-D. A comparison between the 
original data and the reduced-pushed-back-up data might be a good starting point for 
your systems.

In this part, design a recommendation system that recommends 3 items to users that 
they have not yet rated, but that your system believes that they will rate highly. 
Your system should use either PCA (from `sklearn`) or SVD (from `numpy`) as a 
central element of your recommender system. _Hint:_ use the above currency example, 
as a framing for your recommendation system; that is, lower the dimension of your 
user-item matrix, push the lower-dimension version **back** to the original dimension, 
and compare the lower-dimension (in the original dimension) to the original data. 

Your entire recommender system must be contained in a code file called `project1.py`.

You should also design two kinds of unit tests for your recommender system:  
1. The first kind of unit tests should be 'surface' level, checking the size 
   and type of your output. 
2. The second kind of unit tests should check that you are not giving 
   recommendations for items that the user has already rated. Your test file 
   should be called `test_project1.py`. 

### Part 3 - Testing your system on specific examples
For this part, you will be evaluating the quality of the system's recommendations. 
Select two users in the dataset, and note the items they have rated so far. 
Construct narratives for each of these users about what the "latent" or hidden 
preferences of these users are. 

Now look at what your system recommends. Do these results surprise you? Why or 
why not? If possible, ask a friend or two to comment on the quality of these 
recommendations. 

### Part 4 - Documenting your work
A critical part of our work is documenting what we do. To that end, the last part of 
any project will be writing a coherent report on what you did. These reports should 
**not** feel like a listing of the parts, but rather seek to tell a story of the work 
that you have done and the resulting product. 

For this project, your report should include:
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
