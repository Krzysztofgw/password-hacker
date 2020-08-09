# password-hacker
hyperskill project

STAGE 1

Your program will receive command line arguments in this order:

  IP address
  port
  message for sending
  
The algorithm is the following:

  Create a new socket.
  Connect to a host and a port using the socket.
  Send a message from the third command line argument to the host using the socket.
  Receive the server’s response.
  Print the server’s response.
  Close the socket.
  
STAGE 2

In this stage, you should write a program that:

  Parses the command line and gets two arguments that are IP address and port.
  Tries different passwords until it finds the correct one.
  Prints the password it found.
  Note that you can connect to the server only once and then send messages many times. Don't connect to the server before sending every message.

Also, note that here and throughout the project, the password is different every time you check your code.

STAGE 3

In this stage, you should write a program that:

  Parses the command line and gets two arguments that are IP address and port.
  Finds the correct password using the list of typical passwords.
  Prints the password it found.
Note that here and throughout the project, the password is different every time you check your code.

STAGE 4

Your algorithm is the following:

Try all logins with an empty password.
When you find the login, try out every possible password of length 1.
When an exception occurs, you know that you found the first letter of the password.
Use the found login and the found letter to find the second letter of the password.
Repeat until you receive the ‘success’ message.
Finally, your program should print the combination of login and password in JSON format. 

STAGE 5

In this stage, you should write a program that uses the time vulnerability to find the password.

Use the list of logins from the previous stage.
Output the result as you did this in the previous stage.
