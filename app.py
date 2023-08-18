import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import re
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Show main page"""
    counter = db.execute("SELECT COUNT(*) as counter FROM history")
    return render_template("index.html", counter=counter)



@app.route("/personality_test", methods=["GET", "POST"])
def Personality_test():
    """Personality test"""
    if request.method == "GET":
        return render_template("personality.html")
    else:
        try:
            user_id = session["user_id"]
        except:
            user_id = None
            pass
        now = datetime.now()
        Troverted = int(request.form.get("TrovertedValue")) + int(request.form.get("TrovertedValue2")) + int(request.form.get("TrovertedValue3"))
        SensorTuitive = int(request.form.get("SensorTuitive")) + int(request.form.get("SensorTuitive2")) + int(request.form.get("SensorTuitive3"))
        ThinkerFeeling = int(request.form.get("ThinkerFeeling")) + int(request.form.get("ThinkerFeeling2")) + int(request.form.get("ThinkerFeeling3"))
        JudgingPerceiving = int(request.form.get("JudgingPerceiving")) + int(request.form.get("JudgingPerceiving2")) + int(request.form.get("JudgingPerceiving3"))
        # zrobic ify i wysylaloby na /intp etc?
        # jakos przerzucic variablesy zeby zrobic wykresiki i jakies malutkie opisy

        if Troverted >= 150:
            if SensorTuitive >= 150:
                if ThinkerFeeling >= 150:
                    if JudgingPerceiving >= 150:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/enfj")

                    else:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ENFP", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/enfp")

                else:
                    if JudgingPerceiving >= 150:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ENTJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/entj")

                    else:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ENTP", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/entp")
            else:
                if ThinkerFeeling >= 150:
                    if JudgingPerceiving >= 150:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ESFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/esfj")

                    else:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ESFP", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/esfp")

                else:
                    if JudgingPerceiving >= 150:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ESTJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/estj")

                    else:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ESTP", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/estp")

        else:
            if SensorTuitive >= 150:
                if ThinkerFeeling >= 150:
                    if JudgingPerceiving >= 150:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "INFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/infj")

                    else:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "INFP", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/infp")

                else:
                    if JudgingPerceiving >= 150:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "INTJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/intj")

                    else:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "INTP", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/intp")
            else:
                if ThinkerFeeling >= 150:
                    if JudgingPerceiving >= 150:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ISFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/isfj")

                    else:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ISFP", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/isfp")

                else:
                    if JudgingPerceiving >= 150:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ISTJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/istj")

                    else:
                        if user_id != None:
                            db.execute("INSERT INTO history (user_id, MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, "ISTP", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        else:
                            db.execute("INSERT INTO history (MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date) VALUES(?, ?, ?, ?, ?, ?)", "ENFJ", Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, now)
                        return redirect("/istp")

# Analysts
@app.route("/intj")
def INTJ():
    """INTJ results"""
    return render_template("INTJ.html")

@app.route("/intp")
def INTP():
    """INTP results"""
    return render_template("INTP.html")

@app.route("/entj")
def ENTJ():
    """ENTJ results"""
    return render_template("ENTJ.html")

@app.route("/entp")
def ENTP():
    """ENTP results"""
    return render_template("ENTP.html")

# Diplomats
@app.route("/enfp")
def ENFP():
    """ENFP results"""
    return render_template("ENFP.html")

@app.route("/enfj")
def ENFJ():
    """ENFJ results"""
    return render_template("ENFJ.html")

@app.route("/infp")
def INFP():
    """INFP results"""
    return render_template("INFP.html")

@app.route("/infj")
def INFJ():
    """INFJ results"""
    return render_template("INFJ.html")

# Sentinels
@app.route("/istj")
def ISTJ():
    """ISTJ results"""
    return render_template("ISTJ.html")

@app.route("/isfj")
def ISFJ():
    """ISFJ results"""
    return render_template("ISFJ.html")

@app.route("/estj")
def ESTJ():
    """ESTJ results"""
    return render_template("ESTJ.html")

@app.route("/esfj")
def ESFJ():
    """ESFJ results"""
    return render_template("ESFJ.html")

# Explorers
@app.route("/esfp")
def ESFP():
    """ESFP results"""
    return render_template("ESFP.html")

@app.route("/estp")
def ESTP():
    """ESTP results"""
    return render_template("ESTP.html")

@app.route("/isfp")
def ISFP():
    """ISFP results"""
    return render_template("ISFP.html")

@app.route("/istp")
def ISTP():
    """ISTP results"""
    return render_template("ISTP.html")



@app.route("/history")
@login_required
def history():
    """Show history of tests"""
    user_id = session["user_id"]
    historyDB = db.execute(
        "SELECT MBTI, Troverted, SensorTuitive, ThinkerFeeling, JudgingPerceiving, date FROM history WHERE user_id = ? ORDER BY date DESC", user_id)
    history_info = []
    for row in historyDB:
        history_info.append({
            "MBTI": row["MBTI"],
            "Troverted": row["Troverted"],
            "SensorTuitive": row["SensorTuitive"],
            "ThinkerFeeling": row["ThinkerFeeling"],
            "JudgingPerceiving": row["JudgingPerceiving"],
            "date": row["date"],
        })
    return render_template("history.html", history_info=history_info)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/personality_types", methods=["GET", "POST"])
def personality_types():
    """personality types."""
    return render_template("personality_types.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("register.html")

    # User reached route via POST (as by submitting a form via POST)
    else:
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        if len(request.form.get("password")) < 8:
            return apology("Make sure your password is at least 8 letters")
        elif re.search('[0-9]', request.form.get("password")) is None:
            return apology("Make sure your password has a number in it")
        elif re.search('[A-Z]', request.form.get("password")) is None:
            return apology("Make sure your password has a capital letter in it")

        elif not request.form.get("confirmation") or request.form.get("confirmation") != request.form.get("password"):
            return apology("must provide correct confirmation")

        hash = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)

        # Query database for username
        try:
            # Remember registrant
            user = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), hash)
            session["user_id"] = user
            return redirect("/")
        except:
            return apology("Nickname already used", 400)

