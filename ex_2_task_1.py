# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail you at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

def is_valid_email_address(s):
    
# Rule 1: Must have "@" and "." but only 1 "@"


    NumAmp = s.count("@")
    if NumAmp != 1: return 1, "INVALID ADDRESS: Must have exactly one Ampersand (&)"

# Rule 2: Must have at least one period
 
    NumPeriod = s.count(".")
    if NumPeriod < 1: return 2, "INVALID ADDRESS: Must have at least one period (.)"

# Rule 3: Must have "." 4 from the right

    if s[-4] != ".": return 3, "INVALID ADDRESS: Must have a domain delimiter 3 characters from the right"

# Rule 4: 3 chars on right must be = "com" "edu" "org" or "gov"   

    if (s[-3::]) not in ["com", "edu", "org", "gov"]: return 4, "INVALID ADDRESS: Domain must be 'com', 'edu', 'org', or 'gov'"

# Rule 5: First portion of address must be between 3 and 16 characters and alphanumeric

    SpltString = s.split("@")
    PartOne, PartTwo = SpltString[0], SpltString[1] # I couldn't figure this part out, so I had to peek at the solution
    if len(PartOne) < 3 or len(PartOne) > 16: return 5, "INVALID ADDRESS: First part of address must be between 3 and 16 characters long" 
    
    if PartOne.isalnum() == False:
        return 6, "INVALID ADDRESS: First part of address must be alpha numeric."

# This is a bit of a cheat - assumes that last 4 characters are the period and extension
    PartTwoCount = len(PartTwo) - 4
    if PartTwoCount < 2 or PartTwoCount > 8: return 7, "INVALID ADDRESS: Second part of address must be between 2 nad 8 characters in long"

    



    return None, "*** NO ERRORS ***"


# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        "zug@zug.bz",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == None:
            print(e, s) # OK
        else:
            print(f"{e} - ERROR: {s}, CODE: {r}") # Error

        
