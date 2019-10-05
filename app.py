import os
import sqlite3
import names
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Instantiate Flask
app = Flask(__name__)


@app.route('/')
def index():
	try:
		# Initialize sqlite3 DB
		if os.path.exists('test.db'):
			os.remove('test.db')
			
		# Set up a sqlite3 connection object
		conn = sqlite3.connect('test.db')
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS users(uid,last_name,first_name)")

		# Generate and add accounts to DB
		for i in range(0, 10):
			full_name = names.get_full_name()
			first_name = full_name.split()[0]
			last_name = full_name.split()[1]
			uid = full_name.lower().replace(" ", ".")
			c.execute("INSERT OR REPLACE INTO users (uid,last_name,first_name) VALUES(?,?,?)", (uid, last_name, first_name))
			conn.commit()

		# Select all account records
		c.execute("SELECT * FROM users")
		result = c.fetchall()

		# Clean up
		conn.close()
		
		return render_template('userlist.html', result=result)
		
	except Exception as e:
		return str(e)
		
		
bootstrap = Bootstrap(app)

	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
