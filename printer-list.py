#! ./venv3-8/bin/python3.8
import re
from flask import Flask, redirect, url_for, render_template, request
from include.printJob import PrintJob
import json

app = Flask(__name__)
test = PrintJob("jarrod_Ex1", "Jarrod", "Jarrod", 1, "T4-5",)

currentPrints = []
currentPrints.append(PrintJob("jarrod-Keychain", "Jarrod", "Jarrod", 1, "W5-6",))
currentPrints.append(PrintJob("jarrod-ex1", "Jarrod", "Jarrod", 1, "M4-5", "box 1"))


@app.route("/finished/")
def home():
	return render_template("completedPrints.html")

@app.route("/", methods=["GET", "POST"])
def test():
	
	if request.method == "POST":
		req = request.form
		fileName = 			req.get("fileName")
		personName = 		req.get("personName")
		approverName = 	req.get("approverName")
		printerID = 		req.get("printerID")
		classPeriod =		req.get("classPeriod")
		
		newJob = PrintJob(fileName, personName, approverName, printerID, classPeriod)
		currentPrints.append(newJob)
	
	return render_template("activePrints.html", printJobs=currentPrints)

@app.route("/delete/<id>/", methods=["GET", "POST"])
def delete(id):
	return render_template("deletePrint.html", toDelete=id, printJobs=currentPrints)

if __name__ == "__main__":
	app.run()