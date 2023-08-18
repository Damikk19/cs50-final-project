# I4N
#### Video Demo:  <https://www.youtube.com/watch?v=_kx6c2_OEMc>
#### Description:
I4N is an awesome personality test that I managed to write as my final project for CS50.
At the top of the index page in navbar, we can see the “I4N” logo after pressing on that takes us to the index page.
Personality test option takes us to the test page where we can answer questions and submit them so we will be able to get the matched personality.
Personality types after pressing which we enter the page where every MBTI type is described, we can click on it and read about each one of them.
In the middle of the index page we can see a welcome message along with a big “Take our test” button that takes us to the test page.
Under the button, we can see a big red counter that tells us how many tests had been taken so far based on the number of results in the database.

In the personality test page we have a test that begins with “How much do you agree with the following statements” where our task is to choose if we fully disagree or fully agree with the statements using range sliders.
After we answer the questions we press the “Submit” button at the bottom of the page that will redirect us to the page with our personality type based on our answers.
If we are logged in it will save our results to the database so we can see our results anytime we want to.

In the personality types page we got 4 groups of MBTI classes which contain another 4 mini kinds of personalities.
After pressing on any of the above-mentioned options we will get redirected to the page that contains the description of the MBTI type that we pressed on.

As mentioned before we can contain our personality test results in the history page but only if we are logged in.
On the history page, as we have mentioned we got the: MBTI, 4 values based on which the test choose the personality type and date when we have submitted the test, where the results are sorted by the newest one on the top to the oldest one on the bottom of the page.

Making 16 different templates for every personality type in which we precisely described personalities, that we later redirect to enabled our test to return the most accurate results that depend on the answers that the user submitted on the test page.

The history page enables us to return info about the tests because of the usage of a list that is made in the history function based on values in the database.

Layout of the page is based on the Finance project from week 9 problem set of CS50.

Page is mostly done with html and css using flask as a framework, to make the page fully working I used some new libraries like datetime or re.
The CSS file contains 11 different classes to make the personality test better looking.

Database project.db contains 8 fields in history table to keep better track of the test history and 3 fields in users database to keep track of users.
