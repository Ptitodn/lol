from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>POC Page</title>
</head>
<body>

<h2>Payment POC Page</h2>

{% if method == "POST" %}
    <p style="color:green;">✅ Accessed via POST</p>
    <pre>{{ data }}</pre>
{% else %}
    <p style="color:blue;">ℹ️ Accessed via GET</p>
{% endif %}

<form method="POST">
    <input name="username" placeholder="name">
    <button type="submit">Send POST</button>
</form>

</body>
</html>
"""

@app.route("/imran", methods=["GET", "POST"])
def imran():
    return render_template_string(
        HTML_PAGE,
        method=request.method,
        data=request.form.to_dict()
    )

if __name__ == "__main__":
    app.run(debug=True)
