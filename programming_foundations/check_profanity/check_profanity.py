import urllib.request

def read_text():
    quotes = open("C:\git\python-projects\programming_foundations\check_profanity\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)

    #remove spaces
    translator = str.maketrans('', '', " ")
    nospace = contents_of_file.translate(translator)

    #remove new lines
    translator =  str.maketrans('', '', "\n")
    nonewline = nospace.translate(translator)
    print(nonewline)
    quotes.close()
    #check_profanity(contents_of_file)
    check_profanity(nonewline)

def check_profanity(text_to_check):
    #connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) # get info from internet
    #http://www.wdylike.appspot.com/?q=shot  - will output true or false if "shot" = profanity
    #output = connection.read()
    with urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) as response:
        output = response.read()
    print(output)
    #connection.close()

read_text()

