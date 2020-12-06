from flask import Flask, Response, redirect, url_for, render_template, request

from app import app
from app.analyzer import Analyzer
from app.streamer import Streamer


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/static-analysis")
@app.route("/static-analysis/")
def static_analysis():
    return render_template("static-analysis.html")


@app.route("/static-analysis/summary-report", methods=["GET", "POST"])
def static_summary_report():
    tweet_analyzer = Analyzer()
    if request.method == "POST":
        hash_tag = request.form['summary_report_hashtag']
        num_tweets = request.form['summary_report_tweets']
        test_summary_report_data = request.form.to_dict()    # key-value pairs in the form of field: data
        summary_report_data = tweet_analyzer.create_report(hash_tag, int(num_tweets))
        return render_template("query-summary-report.html", report_data=summary_report_data)
    else:
        return render_template("summary-report.html")


@app.route("/static-analysis/piechart", methods=["GET", "POST"])
def static_piechart():
    tweet_analyzer = Analyzer()
    if request.method == "POST":
        hash_tag = request.form['piechart_hashtag']
        num_tweets = request.form['piechart_tweets']
        piechart_data = request.form.to_dict()
        tweet_analyzer.create_chart(hash_tag, int(num_tweets))
        return render_template("query-piechart.html", name="Pie Chart", url="/static/images/piechart.png")
    else:
        return render_template("piechart.html")


@app.route("/dynamic-analysis", methods=["GET", "POST"])
@app.route("/dynamic-analysis/", methods=["GET", "POST"])
def dynamic_analysis():
    tweet_streamer = Streamer()
    if request.method == "POST":
        hash_tag = request.form['dynamic_hashtag']
        data_stream = tweet_streamer.stream_tweets(hash_tag)
        return render_template("query-dynamic-analysis.html", dynamic_data=data_stream)
    else: # request.method == "GET":
        return render_template("dynamic-analysis.html")
