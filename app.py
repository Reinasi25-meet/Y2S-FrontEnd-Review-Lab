from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return('''<html><p>welcome to my photo gallery</p>
       <img height="500px" src="https://cdnb.artstation.com/p/assets/covers/images/012/971/631/large/wiktoria-stachowska-babazytnia-12.jpg">
       <img src="https://www.google.com/url?sa=i&url=h983000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNCriPjvq4cDFQAAAAAdAAAAABAd.jpeg">
       <a href="/food1">go to fav food and animals</a>
       </html>
       ''')

@app.route('/food1')    
def food1():
 	return('''
 		<html>
 		<p>food page</p>
 		 <a href=\'/home\'> go back to home </a>
 		 <br/>
 		 <a href="/food2">go to another fav food</a>"
 		 </html>''')

@app.route('/food2')    
 		<html>
 		<p>animals page</p>
 		 <a href=\'/home\'> go back to home </a>
 		 <br/>
 		 <a href="/pet2">go to another fav animal</a>"
 		 </html>''')

@app.route('/pet2')    
def pet2():
 	return('''
 		<html>
 		<p>animal page2</p>
 		 <a href=\'/home\'> go back to home </a>
 		 </html>''')

if __name__ == '__main__':
    app.run(debug=True)





























