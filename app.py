import names
import random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Instantiate Flask
app = Flask(__name__)


@app.route('/')
def index():
	try:
		# Create data store
		ds = []

		# Generate and add entries to data store
		for i in range(0, 10):
			full_name = names.get_full_name()
			first_name = full_name.split()[0]
			last_name = full_name.split()[1]
			uid = full_name.lower().replace(" ", ".")
			employee_number = random.randint(5000, 10000)
			email = "{}@example.com".format(uid)

		# Create tuple with user elements
			user = (employee_number, uid, first_name, last_name, email)

		# Append entry elements to data store
			ds.append(user)

		# Return all data store elements
		result = (ds[0:])
		return render_template('userlist.html', result=result)
		
	except Exception as e:
		return str(e)
		
		
bootstrap = Bootstrap(app)

	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
