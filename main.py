from flask import Flask,render_template
import random,db

app = Flask(  # Create a flask app
	__name__,
	template_folder='websitefiles',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

@app.route('/')  # What happens when the user visits the site
def base_page():
	random_num = random.randint(1, 100000)  # Sets the random number
	return render_template(
		'base.html',  # Template file path, starting from the templates folder. 
		random_number=random_num  # Sets the variable random_number in the template
	)

@app.route('/2')
def page_2():
	return render_template('site_2.html')

@app.route('/3')
def page_3():
	rand_ammnt = random.randint(10, 100)
	random_str = ''.join(random.choice(ok_chars) for a in range(rand_ammnt))
	return render_template('db.html', db=db.read())

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)

print (db.read())