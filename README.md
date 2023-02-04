# algorithmie-SorenMesselier-Sentis
algorithmie-SorenMesselier-Sentis created by GitHub Classroom

Hey Mister Robot !
To begin, you need to retrieve the file with :

```
git clone git@github.com:IIM-Creative-Technology/algorithmie-SorenMesselier-Sentis.git
```
Then you can see the work I have done

Here is how each of the requested exercises works

# First exercise 

For the first exercise, you had to generate a valid card number between visa which starts with a 4 and mastercard which starts with a 5

As far as my generator is concerned, I managed to make a random list that generates 15 random numbers out of the 16 and the last number is another list that contains the first value (4 or 5)

* Card contains an input with 4 or 5
* Values contains the other 15 random numbers

Then I concatenate them into a single variable: all_values

But unfortunately once the first random move was done, I didn't manage to remove the values of values and restart the loop...

# Second exercise 

For this exercise, I imported each letter in lower and upper case (string.ascii_letters) and each number (string.digits)

Then I ask with an input to the user the length of the password he wants and then I take and randomize the number of characters that the user wants.

# Third exercise 

For the third exercise, I had to look in the python doc of the hashlib. 
According to the instructions, we knew that the password was encoded in md5 and that it contained 8 characters so we have to make a loop which goes from the character 0 to 99 999 999.

So I asked the user for the password to find in md5
then a brut_force loop comes to test each of the possibilities until finding on the good password.

# Fourth exercise

For this exercise we had to convert from binary to hexadecimal.
So I started by looking if there was an argument in python that allowed it and I found the hex() argument.

So I started by asking the user what binary code he wanted to convert and then I launched a function that converts my input to int and then converts it by itself with the hex() argument