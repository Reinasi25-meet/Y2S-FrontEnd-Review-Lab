from flask import Flask, render_ template
 import random


app = Flask(___name___)
# Route for the home page

@app. route (' /home' )

def home ():
    return render_template ( 'home.html')

# Run the Flask app

if __name__ == '__main__':

    app.run(debug=True)

    <! DOCTYPE html> 
    <html lang="en">
     <head>
          <meta charset="UTF-8"> 
          «title>Fortune Teller</title>
</head>

 <body> 

 <h1>Welcome to the Fortune Teller</h1> 

 <p>click the link below to get your fortune!</p> 

 <a href="/fortune">Tell me my fortune</a>

<br>

<a href="/indecisive">Indecisive Fortune Teller</a> 


<a href=" /magic"SMagic 8 Ball</a> 

</body> 
</html>
@app. route('/fortune')

def fortune() :

    fortunes = [
"You will have a great day!",
"A surprise is waiting for you."
"Today is your lucky day!"
"Happiness will find you."
"Be cautious today.",
"You will meet someone special.",
"An opportunity will arise."
"Expect the unexpected."
"Good news is coming your way."
"You will achieve your goals."]

chosen_fortune = random. choice (fortunes)

return render_template('fortune.html', 
    fortune=chosen_fortune)
<|DOCTYPE html>
<html lang="en">
<head>
   «meta charset="UTF-8">

   <title>Your Fortune</title>
 </head>
 <body>
   <h1>Your fortune is:</h1>
   <p>{{ fortune }}</p>
 </body>
 </html>
 <html lang="en"> 
 chead> 
 <meta charset="UTF-8">
«title>Indecisive Fortune‹/title> 
</heads 
<body> 
    <h1>I'm not sure what will happen to you, but it will be one of the following three
    <ul>
{% for fortune in fortunes %} 
<li>(f fortune }}</li> 
    {% endfor %}
    </ul> \
</body>
</html>
@app.route (' /magic' )
def magic():
   return render_ template ('magic.html')
@app.route (' /response' )
def response ( ):
  responses = [
"Yes",
"NO",
"maybe",
"only on Tuesdays",
"I think so, but one can never be sure",
"Why are you asking me?"]

chosen_response = random. choice (responses)
return render_template ('response. html', response=chosen_response)

<! DOCTYPE html>
 <html lang="en">
  <head> 
  ‹meta charset="UTF-8">
<title>Magic 8 Ball</title> 
</head> 
<body> 
<h1>Ask a yes or no question:</h1>
<form action="/response">
    <input type="text" name="question" placeholder="Type your question here"> 
    <button type="submit">Ask</button>
   </form> 
</body>
 </html>
 <! DOCTYPE html> 
 <html lang="en"> 
 <head> 
 <meta charset="UTF-8"> 
 <title>Magic 8 Ball Response</title>
</head>
 <bodv> 
 <h1>Your answer is:</h1> 
 <p>{f response }}</p>
</body> 
</html>
