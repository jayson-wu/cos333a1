clx_jnwu
#----------------------------------------------------------------------------------
# readme.txt
# Authors: Connie Xu, Jayson Wu
# Assignment 1: A Registrar Application
#----------------------------------------------------------------------------------

Your name, your teammate's name, and the assignment number.
    
    Connie Xu, Jayson Wu, Assignment 1

A paragraph describing your contribution, and another paragraph describing
your teammate's contribution. Please be thorough; we're looking for two substantial 
paragraphs, not a sentence or two.

    (Connie) I did research on argparse and textwrap and figured out which 
    arguments to use, as well as how to use the libraries. I read the assignment
    specs in detail to determine which tables to use for the select statement in
    reg.py. I figured out that we should use if statements depending on which
    arguments we include, and wrote the corresponding statements and replace
    statements together with Jayson. For the testing files, I made sure to include 
    all the examples from the assignment statement. I also ran a sqlite function 
    to gather a list of all of the different departments so that we can have a more 
    full test coverage of reg.py. Finally, I ran the coverage code and did testing 
    on courselab.
    
    Jayson looked through the course handouts and retrieved some framework code.
    He also wrote the print format string, which I helped to debug. 
    We wrote the statement strings in regdetails.py together, after brainstorming 
    how to do data selection, and after some debugging, we also devised the method 
    for finding 0-many profs. For the testing files, Jayson worked on creating 
    some niche tests of our own. He also helped identify the diff between the output
    files and together we did the final stages of debugging.
    
    

    (Jayson) We both wrote the code together using VSCode Live Share. To start,
    I laid out the basic code framework using the code that we got in the course handouts. 
    I then proceeded to work with Connie to figure out how to use argparse and get
    the '-h' function working correctly. Then I wrote the original statement string
    for reg.py, but it was buggy, so Connie helped me debug it. I also wrote the format
    string for reg.py after Connie and I both figured out the format of the output together
    using ref_reg.pyc. After reg.py, regdetails.py came more easily because we didn't have
    to do much research on argparse or textwrap. I wrote the majority of the first and last
    stmt string in regdetails, while Connie did the middle two (we both debugged each other's code
    after). I wrote the boundary tests for reg.py and contibuted to the statement tests for
    reg.py and regdetails.py. In short, We coded together for the majority of the project.
    
    Connie was coding with me during the entire project. She helped me debug the argparse and 
    textwrap statements. She also helped me realize that we needed if statements to identify
    which command-line arguments are being used, so we could edit the stmt string accordingly.
    Then, she figured out how to order the output and helped me debug my format string. Connie
    wrote the majority of the middle two stmt strings in regdetails.py. She also figured out how
    to order the professors and use a list to store multiple professors/departments. Finally, she
    wrote the statement tests for both reg.py and regdetails.py as well as helping with the boundary
    tests. Connie also ran coverage in courselab and created the html file.  

A description of whatever help (if any) you received from other people
while doing the assignment, as prescribed by the course Policies web page.

    None

A description of the sources of information that you used while doing the assignment.

    Python docs
    Course website
    Course lecture slides
    Course released code
    Course handouts
    Piazza

An indication of how much time you spent doing the assignment.

    8 hours

Your assessment of the assignment: Did it help you to learn? What did it help you to learn?
Do you have any suggestions for improvement? Etc.

    (Connie) The assignment helped me solidify my knowledge of Python basics, as well as help me 
    learn how to use SQLite. I think it was a good assignment, and I don't have any suggestions for improvement.
    
    (Jayson) Assignment 1 helped me understand how to draw data from a database using SQLite, as 
    well as helping me learn new python methods. I also learned how to make a testing python file
    to automate testing as well as using coverage for statement testing. I think the assignment was 
    good except a lot of the debugging was spent on getting the style right for the output, which I 
    found to be rather tedious.


(Optionally) Any information that will help us to grade your work in the most favorable light. 
In particular you must describe all known bugs.

    None