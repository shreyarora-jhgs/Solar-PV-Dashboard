# Solar-PV-Dashboard
HTML, Python + instruction script on how to use API to link live server to viewable data of Solax

Step 1: 

Install python packages:
pip install flask requests flask-cors

flask: to run a small server
requests: to get data from Solax Cloud API
flask-cors: to allow the browser to access the server


Step 2:

Create python server provided

Step 3:

Run python server to test it and go to:
http://127.0.0.1:5000/live

You will see a javascript object notation looking like:

{
  "pv_power_kw": 0.1,
  "yield_today_kwh": 14.8,
  "consumption_kwh": 8.992,
  "imported_kwh": 0.161,
  "last_update": "2025-10-19 18:10:46"
}


Step 4:

Create the dashboard HTML provided

Step 5:

Run a local web server - 
python -m http.server 8000
in terminal

Step 6:

Open up the files app and open the HTML with google chrome 
Make sure both python and HTML file are in the same folder
