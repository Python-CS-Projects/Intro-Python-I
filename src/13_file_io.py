"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE


def open_file(file_name):
    f = open(file_name, 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)


open_file('foo.txt')
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE


def create_file():
    f = open("bar.txt", "w+")
    f.write("-first line \n-sencon line \n-third line")
    f.close()


create_file()

open_file("bar.txt")
