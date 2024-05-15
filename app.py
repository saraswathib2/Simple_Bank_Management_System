from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store bank accounts
accounts = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_account", methods=["POST"])
def create_account():
    name = request.form.get("name")
    if name not in accounts:
        accounts[name] = {"balance": 0}
        return redirect(url_for("index"))
    else:
        return "Account already exists."

@app.route("/deposit", methods=["POST"])
def deposit():
    name = request.form.get("name")
    amount = float(request.form.get("amount"))
    if name in accounts:
        accounts[name]["balance"] += amount
        return f"Deposited {amount} into {name}'s account."
    else:
        return "Account not found."

@app.route("/withdraw", methods=["POST"])
def withdraw():
    name = request.form.get("name")
    amount = float(request.form.get("amount"))
    if name in accounts:
        if amount <= accounts[name]["balance"]:
            accounts[name]["balance"] -= amount
            return f"Withdrew {amount} from {name}'s account."
        else:
            return "Insufficient funds."
    else:
        return "Account not found."

@app.route("/check_balance", methods=["POST"])
def check_balance():
    name = request.form.get("name")
    if name in accounts:
        balance = accounts[name]["balance"]
        return f"{name}'s balance: {balance}"
    else:
        return "Account not found."

if __name__ == "__main__":
    app.run(debug=True)
