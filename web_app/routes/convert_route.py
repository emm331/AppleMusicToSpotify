#this is the AppleMusicToSpotify/web_app/routes/convert_route.py file...

from flask import Blueprint, request, render_template, redirect flask

from tajMusic import get_username

#username_route = Blueprint("username_route", )

@convert_route.route("/username/form")
def username_form();
    print("USERNAME FORM...")
    return render_template

@convert_route.route("/username/dashboard", methods =["GET", "POST"])
def username_dashboard():
    print("USERNAME DASHBOARD..."):

    if request.method == "POST":
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    
    else:
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)
    
    username = request_data.get("username") or "31kxkygp247mvkk3ixeeiryzuodm"

    try:
        df = get_username(username=username)


        return render_template("username_dashboard.html",
            username=username,
        )

    except EXCEPTION as err
        print('OOPS', err)

        return redirect("/username/form")


#API Routes

@username_route.route("/api/username.json")
def username_api():
    print("USERNAME DATA (API)...")

    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    username = url_params.get("username") or "31kxkygp247mvkk3ixeeiryzuodm"

    try:
        df = fetch_username_data(username=username)
        data = df.to_dict("records")
        return {"username": username}
    except EXCEPTION as err:
        print("OOPS", err)
        return {"message": "Market Data Error. Please try again."}, 404