#Code Snippets

These are pieces of code I've written that aren't part of a larger project and that are cool, elegant, fun, (by my standards) or any combination thereof. 

###FizzBuzz.py
FizzBuzz is an increasingly common technical interview question to prove you're a real hoopy frood. The premise is simple: print numbers from 1 to 100, and for multiples of 3 print "Fizz", for multiples of 5 print "Buzz"; for both print "FizzBuzz". In my implementation, I do it with two tests.

###OmniFocus.rb
This is a ruby script to be used with [Slogger](https://github.com/ttscoff/Slogger). It's a default script in the "plugins_disabled" folder, but I didn't like the way the scraped data from OmniFocus was being formatted in [DayOne](www.dayoneapp.com). My new formatting puts Project names as h3 subheadings, and adds tasks completed as unsorted bullet items beneath them. Context is captured in italics prefaced by the "@" sign at the end of the line:

ex. * Paint house *@Home*

I skipped rewriting the project name for each line by tracking a new variable called `uniqueProject`, which is initialized as `null`; and a new string called `titleString`, which is concatenated with `textString` into `output`.

A simple if statement writes the project name as a new subheading to `titleString` the first time it sees it, and sets `uniqueProject` to `project`, which causes the if statement to pass.