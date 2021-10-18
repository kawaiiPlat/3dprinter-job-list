#! ./venv3-8/bin/python3.8
from flask import Flask, redirect, url_for, render_template, request
from include.printJob import PrintJob
import json

app = Flask(__name__)
test = PrintJob("jarrod_Ex1", "Jarrod", "Jarrod", 1, "T4-5",)

currentPrints = []
currentPrints.append(PrintJob("jarrod-Keychain", "Jarrod", "Jarrod", 1, "W5-6",))
currentPrints.append(PrintJob("jarrod-ex1", "Jarrod", "Jarrod", 1, "M4-5", "box 1"))


@app.route("/")
def home():
	return render_template("activePrints.html")

@app.route("/finished", methods=["GET", "POST"])
def test():
	
	if request.method == "POST":
		req = request.form
		fileName = 			req.get("fileName")
		personName = 		req.get("personName")
		approverName = 	req.get("approverName")
		printerID = 		req.get("printerID")
		classPeriod =		req.get("classPeriod")

		currentPrints.append(PrintJob(fileName, personName, approverName, printerID, classPeriod))
	
	return render_template("finshedPrints.html", printJobs=currentPrints)

if __name__ == "__main__":
	app.run()