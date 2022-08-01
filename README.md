# probable-potato

TODO - Required: 

 add a requirements.txt with the required libraries to be pip installed

 host on AWS

TODO - Bonus:

Note in app.py, the `if X in data["requested_nlp"]` is copy/pasted a lot.
Suggest a change to make the code cleaner and easier to maintain. For example, with a for loop. 
Hint: you can make a function definition the value of a dictionary and then call the dictionary
with the key to call the function.

I hard coded the translation to work from English to Italian. Can you add some logic so that source and
destination languages can be passed into the function?

I used `if request.method == 'POST':` but I opened the route to both GET and POST. Can you add some logic
to return this README when the request is sent via GET?
