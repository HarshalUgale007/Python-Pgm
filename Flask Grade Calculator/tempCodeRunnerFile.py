def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        maths=float(request.form["maths"])
        science=float(request.form["science"])
        history=float(request.form["history"])
        
        average_marks=(maths+science+history)/3
        
        return render_template("form.html",score=average_marks)
        
    