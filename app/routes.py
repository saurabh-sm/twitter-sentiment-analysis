from flask import Flask, render_template, request

from app import app

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
    if request.method == "POST":
        hash_tag = request.form['summary_report_hashtag']
        num_tweets = request.form['summary_report_tweets']
        return redirect(url_for("query_summary_report", hash_tag, num_tweets))
    else:
        return render_template("summary-report.html")


@app.route("/static-analysis/summary-report/<search_query>")
def query_summary_report(hash_tag, num_tweets):
    return render_template("query-summary-report.html")


@app.route("/static-analysis/piechart", methods=["GET", "POST"])
def static_piechart():
    if request.method == "POST":
        hash_tag = request.form['piechart_hashtag']
        num_tweets = request.form['piechart_tweets']
        return redirect(url_for("query_piechart", hash_tag, num_tweets))
    else:
        return render_template("piechart.html")


@app.route("/static-analysis/piechart/<search_query>")
def query_piechart(hash_tag, num_tweets):
    return render_template("query-piechart.html")




@app.route("/dynamic-analysis")
@app.route("/dynamic-analysis/")
def dynamic_analysis():
    return render_template("dynamic-analysis.html")




if __name__ == '__main__':
    app.run(debug=True)
