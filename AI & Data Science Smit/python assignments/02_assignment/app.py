# Create a Right Hand Half Pyramid, both straight and reverse form.


# Ask the user to enter a number for the pyramid
user = int(input('enter your number for pyramid'))

# Loop to print pyramid going up
for i in range(1,user+1,1):
        # Print spaces and stars
    # (user - i) spaces to move stars to the right
    # i stars to make the pyramid grow
    print(' ' * (user-i)+ '*' * i )



# Ask the user to enter a number again for the inverted pyramid
user = int(input('enter your number for pyramid'))

# Loop to print pyramid going down
for i in reversed(range(1,user+1,1)):
       # Print spaces and stars
    # (user - i) spaces to move stars to the right
    # i stars to make the pyramid shrink
    print(' ' * (user-i)+ '*' * i )