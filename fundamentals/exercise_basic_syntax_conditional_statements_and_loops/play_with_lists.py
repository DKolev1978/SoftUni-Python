import re
list_of_ints = [11, 13, 26, 90, 5, 22]
print(f"{len(list_of_ints)}")
## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)  ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print(email)