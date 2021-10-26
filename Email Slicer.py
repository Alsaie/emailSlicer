#Email Slicing
email = input("What is your email: ")
email = list(email)
at = "@"
at_location = 0
username = ""
domain = ""

#Find ing the @ location 
for letter in email:

    if at in letter:
        at_location = email.index(letter)
        break



# username 
for letter in range(0,at_location):
    username += email[letter]


#domain 
for letter in range(at_location + 1,len(email)):
  domain += email[letter] 

print(f"The username is {username}")
print(f"The domain is {domain}")