import tkinter as tk


def bmicalculator():
    # BMI CALCULATOR
    def calbmi(w, h):
        bmi = w/((h/100)**2)
        if bmi < 18.5:
            output['text'] = "Your BMI is : {0:.2f} \n\nYou are Underweight".format(
                bmi)
        elif bmi > 18.5 and bmi < 24.9:
            output['text'] = "Your BMI is : {0:.2f} \n\nYou are having a\nnormal body weight".format(
                bmi)
        elif bmi > 25 and bmi < 29.9:
            output['text'] = "Your BMI is : {0:.2f} \n\nYou are Overweight".format(
                bmi)
        else:
            output['text'] = "Your BMI is : {0:.2f} \n\nYou are suffering \nfrom obesity".format(
                bmi)

    root = tk.Tk()

    canvas = tk.Canvas(root, height=500, width=650, bg='#99ccff')
    canvas.pack()

    compute = tk.Button(root, text="Calculate BMI", font="impact", bg='#660033',
                        fg='White', bd=2, command=lambda: calbmi(int(weight.get()), int(height.get())))
    compute.place(relx=0.3, rely=0.7, relwidth=0.2, relheight=0.12)

    mlabel = tk.Label(root, text="- Body Mass Index -",
                      font=("impact", 30), bg='#00004d', fg='White')
    mlabel.place(relx=0.2, rely=0.05, relwidth=0.60, relheight=0.1)

    wlabel = tk.Label(root, text="Enter weight (in Kgs)", bg='#99ccff')
    wlabel.place(relx=0.1, rely=0.2, relwidth=0.40, relheight=0.1)
    weight = tk.Entry(root)
    weight.place(relx=0.1, rely=0.3, relwidth=0.40, relheight=0.1)

    hlabel = tk.Label(root, text="Enter Height(in Cms)", bg='#99ccff')
    hlabel.place(relx=0.1, rely=0.4, relwidth=0.40, relheight=0.1)
    height = tk.Entry(root)
    height.place(relx=0.1, rely=0.5, relwidth=0.40, relheight=0.1)

    output = tk.Label(root, text="Check Your\nFitness",
                      bg='#002966', fg='white', font=("impact", 20))
    output.place(relx=0.55, rely=0.2, relwidth=0.40, relheight=0.62)

    credit = tk.Label(root, text="Made by :Ivanna Samydinova",
                      font=("bebas", 6), bg='#99ccff')
    credit.place(relx=0.75, rely=0.93, relwidth=0.3, relheight=0.1)

    root.mainloop()


def bmrcalculator():
    # BMR calculator
    def calbmr(w, h, a, s):
        if s == 'm' or s == 'M':
            bmr = 88.362 + (13.397 * w) + (4.799 * h) - (5.677 * a)
        else:
            bmr = 447.593 + (9.247 * w) + (3.098 * h) - (4.330 * a)

        output['text'] = "Your BMR is : {0:.2f}".format(bmr)

    boot = tk.Tk()

    canvas = tk.Canvas(boot, height=500, width=650, bg='#99ccff')
    canvas.pack()

    credit = tk.Label(boot, text="Made by :Ivanna Samydinova",
                      font=("bebas", 6), bg='#99ccff')
    credit.place(relx=0.84, rely=0.93, relwidth=0.16, relheight=0.1)

    compute = tk.Button(boot, text="Calculate BMR", font="impact", bg='#660033', fg='White', bd=2,
                        command=lambda: calbmr(int(weight.get()), int(height.get()), int(age.get()), sex.get()))
    compute.place(relx=0.65, rely=0.85, relwidth=0.2, relheight=0.12)

    mlabel = tk.Label(boot, text="- Basal Metabolic Rate -",
                      font=("impact", 30), bg='#00004d', fg='White')
    mlabel.place(relx=0.2, rely=0.05, relwidth=0.60, relheight=0.1)

    wlabel = tk.Label(boot, text="Enter weight (in Kgs)", bg='#99ccff')
    wlabel.place(relx=0.1, rely=0.2, relwidth=0.40, relheight=0.1)
    weight = tk.Entry(boot)
    weight.place(relx=0.1, rely=0.3, relwidth=0.40, relheight=0.08)

    hlabel = tk.Label(boot, text="Enter Height(in Cms)", bg='#99ccff')
    hlabel.place(relx=0.1, rely=0.4, relwidth=0.40, relheight=0.1)
    height = tk.Entry(boot)
    height.place(relx=0.1, rely=0.5, relwidth=0.40, relheight=0.08)

    alabel = tk.Label(boot, text="Enter you age ", bg='#99ccff')
    alabel.place(relx=0.1, rely=0.6, relwidth=0.40, relheight=0.1)
    age = tk.Entry(boot)
    age.place(relx=0.1, rely=0.7, relwidth=0.40, relheight=0.08)

    slabel = tk.Label(
        boot, text="Enter M for male & F for female", bg='#99ccff')
    slabel.place(relx=0.1, rely=0.8, relwidth=0.40, relheight=0.1)
    sex = tk.Entry(boot)
    sex.place(relx=0.1, rely=0.9, relwidth=0.40, relheight=0.08)

    output = tk.Label(boot, text="Check Your\nBMR",
                      bg='#002966', fg='white', font=("impact", 20))
    output.place(relx=0.55, rely=0.2, relwidth=0.40, relheight=0.62)

    boot.mainloop()


def fatcalculator():
    # body fat calculator
    def bodyfatm():
        def fatm(weight, waist):
            weight = weight*2.20462
            waist = waist*0.393701

            v1 = (weight * 1.082) + 94.42
            v2 = (waist * 4.15)
            v3 = weight-(v1-v2)
            fatp = (v3/weight)*100
            output['text'] = "You are having {0:.2f}% \n of body fat".format(
                fatp)

        mroot = tk.Tk()

        canvas = tk.Canvas(mroot, height=500, width=650, bg='#99ccff')
        canvas.pack()

        compute = tk.Button(mroot, text="Calculate", font="impact", bg='#660033',
                            fg='White', bd=2, command=lambda: fatm(int(weight.get()), int(length.get())))
        compute.place(relx=0.3, rely=0.7, relwidth=0.2, relheight=0.12)

        mlabel = tk.Label(mroot, text="- Body Fat calculator -",
                          font=("impact", 30), bg='#00004d', fg='White')
        mlabel.place(relx=0.2, rely=0.05, relwidth=0.60, relheight=0.1)

        wlabel = tk.Label(mroot, text="Enter weight (in Kgs)", bg='#99ccff')
        wlabel.place(relx=0.1, rely=0.2, relwidth=0.40, relheight=0.1)
        weight = tk.Entry(mroot)
        weight.place(relx=0.1, rely=0.3, relwidth=0.40, relheight=0.1)

        llabel = tk.Label(
            mroot, text="Enter waist length(in Cms)", bg='#99ccff')
        llabel.place(relx=0.1, rely=0.4, relwidth=0.40, relheight=0.1)
        length = tk.Entry(mroot)
        length.place(relx=0.1, rely=0.5, relwidth=0.40, relheight=0.1)

        output = tk.Label(mroot, text="Check Your\nbody fat",
                          bg='#002966', fg='white', font=("impact", 20))
        output.place(relx=0.55, rely=0.2, relwidth=0.40, relheight=0.62)

        mroot.mainloop()

    def bodyfatf():
        def fatf(weight, waist, wrist, hips, forearms):
            weight = weight*2.20462
            waist = waist*0.393701
            wrist = wrist*0.393701
            hips = hips*0.393701
            forearms = forearms*0.393701

            v1 = weight * 0.732
            v2 = v1 + 8.987
            v3 = wrist/3.14
            v4 = waist*0.157
            v5 = hips*0.249
            v6 = forearms*0.434
            v7 = v2+v3
            v8 = v7-v4
            v9 = v8-v5
            v10 = weight-(v6+v9)
            fatp = (v10/weight)*100
            output['text'] = "You are having {0:.2f}% \n of body fat".format(
                fatp)

        mroot = tk.Tk()

        canvas = tk.Canvas(mroot, height=500, width=650, bg='#99ccff')
        canvas.pack()

        computex = tk.Button(mroot, text="Calculate", font="impact", bg='#660033', fg='White', bd=2, command=lambda: fatf(
            int(weight.get()), int(length.get()), int(wlength.get()), int(hlength.get()), int(flength.get())))
        computex.place(relx=0.6, rely=0.85, relwidth=0.2, relheight=0.12)

        mlabel = tk.Label(mroot, text="- Body Fat calculator -",
                          font=("impact", 30), bg='#00004d', fg='White')
        mlabel.place(relx=0.2, rely=0.05, relwidth=0.60, relheight=0.1)

        wlabel = tk.Label(mroot, text="Enter weight (in Kgs)", bg='#99ccff')
        wlabel.place(relx=0.1, rely=0.2, relwidth=0.40, relheight=0.08)
        weight = tk.Entry(mroot)
        weight.place(relx=0.1, rely=0.28, relwidth=0.40, relheight=0.08)

        llabel = tk.Label(
            mroot, text="Enter waist length(in Cms)", bg='#99ccff')
        llabel.place(relx=0.1, rely=0.36, relwidth=0.40, relheight=0.08)
        length = tk.Entry(mroot)
        length.place(relx=0.1, rely=0.44, relwidth=0.40, relheight=0.08)

        wrist = tk.Label(
            mroot, text="Enter wrist length(in Cms)", bg='#99ccff')
        wrist.place(relx=0.1, rely=0.52, relwidth=0.40, relheight=0.08)
        wlength = tk.Entry(mroot)
        wlength.place(relx=0.1, rely=0.60, relwidth=0.40, relheight=0.08)

        hips = tk.Label(mroot, text="Enter hips length(in Cms)", bg='#99ccff')
        hips.place(relx=0.1, rely=0.68, relwidth=0.40, relheight=0.08)
        hlength = tk.Entry(mroot)
        hlength.place(relx=0.1, rely=0.76, relwidth=0.40, relheight=0.08)

        four = tk.Label(
            mroot, text="Enter forearms length(in Cms)", bg='#99ccff')
        four.place(relx=0.1, rely=0.84, relwidth=0.40, relheight=0.08)
        flength = tk.Entry(mroot)
        flength.place(relx=0.1, rely=0.92, relwidth=0.40, relheight=0.07)

        output = tk.Label(mroot, text="Check Your\nbody fat",
                          bg='#002966', fg='white', font=("impact", 20))
        output.place(relx=0.55, rely=0.2, relwidth=0.40, relheight=0.62)

        mroot.mainloop()
    foot = tk.Tk()

    canvas = tk.Canvas(foot, height=500, width=650, bg='#99ccff')
    canvas.pack()

    mlabel = tk.Label(foot, text="- Body Fat Calculator -",
                      font=("impact", 30), bg='#00004d', fg='White')
    mlabel.place(relx=0.2, rely=0.05, relwidth=0.60, relheight=0.1)

    compute = tk.Button(foot, text="MALE", font=(
        "impact", 40), bg='#000066', fg='White', bd=2, command=bodyfatm)
    compute.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.3)

    compute = tk.Button(foot, text="FEMALE", font=(
        "impact", 40), bg='#b30047', fg='White', bd=2, command=bodyfatf)
    compute.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.3)

    credit = tk.Label(foot, text="Made by :Ivanna Samydinova",
                      font=("bebas", 6), bg='#99ccff')
    credit.place(relx=0.75, rely=0.93, relwidth=0.3, relheight=0.1)

    foot.mainloop()


# Main interface
mainroot = tk.Tk()

canvas = tk.Canvas(mainroot, height=500, width=650, bg='#ede059')
canvas.pack()


mlabel = tk.Label(mainroot, text="- Fitness calculator -",
                  font=("impact", 30), bg='#0c2538', fg='White')
mlabel.place(relx=0.2, rely=0.05, relwidth=0.60, relheight=0.1)

compute = tk.Button(mainroot, text="Calculate BMI", font="impact",
                    bg='#2b434f', fg='White', bd=2, command=bmicalculator)
compute.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.12)

compute = tk.Button(mainroot, text="Calculate BMR", font="impact",
                    bg='#2b434f', fg='White', bd=2, command=bmrcalculator)
compute.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.12)

compute = tk.Button(mainroot, text="Calculate Body Fat", font="impact",
                    bg='#2b434f', fg='White', bd=2, command=fatcalculator)
compute.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.12)

credits = tk.Label(
    mainroot, text="Made by:\nIvanna Samydinova\n", font=("impact", 12))
credits.place(relx=0.2, rely=0.9, relwidth=0.60, relheight=0.15)

mainroot.mainloop()
