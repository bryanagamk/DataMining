import os, json, band
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
from scipy import spatial

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('banding.html')

@app.route('/clusterUlang')
def cluster():
	kmeanspp = "kmeanspp"
	randomkmeans = "random"
	band.createFeature(randomkmeans,2)
	band.createFeature(randomkmeans,3)
	band.createFeature(randomkmeans,4)
	band.createFeature(randomkmeans,5)
	band.createFeature(kmeanspp,2)
	band.createFeature(kmeanspp,3)
	band.createFeature(kmeanspp,4)
	band.createFeature(kmeanspp,5)
	return render_template('banding.html')

if __name__ == '__main__':
	app.run('127.0.0.1', 9999)