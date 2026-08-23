import tkinter as x
from tkinter import ttk
import math
import random
import numpy
import matplotlib.pyplot as p
from PIL import Image, ImageTk

class CalculatorApp():
    def __init__(self, root):
        self.root = root

    def styled_button(self, parent, text, command):
        return x.Button(
            parent, text=text, command=command,
            font=("Helvetica", 18, "bold"),
            bg="#B8E3E9", fg="#4F7C82",
            activebackground="#0B2E33", activeforeground="#93B1B5",
            bd=0, relief="flat", width=15, height=2, cursor="hand2"
        )

    def getHome_background(self, window):
        """Safely try to load background image. Falls back to black if missing."""
        try:
            image = Image.open("/Users/ameya/Downloads/bg.jpg")
            image = image.resize((2560, 1664))
            bg = ImageTk.PhotoImage(image)
            label = x.Label(window, image=bg)
            label.image = bg          # keep a reference
            label.place(x=0, y=0, relwidth=1, relheight=1)
            label.lower()
        except Exception:
            # File missing or any other error → just use solid black
            window.config(bg="#000000")

    def homescreen(self):
        self.HomeScreen = x.Toplevel(self.root)
        self.HomeScreen.title("Desmos (Megaman Fully Charged Version) + Extra Features")
        self.HomeScreen.geometry("900x700")
        self.HomeScreen.config(background="#000000")

        self.getHome_background(self.HomeScreen)

        title = x.Label(
            self.HomeScreen, text="Megaman Fully Charged Calculator",
            background="#000000", fg="#00FFFF",
            font=("Helvetica", 30, "bold")
        )
        title.place(relx=0.5, rely=0.2, anchor="center")

        buttonFrame = x.Frame(self.HomeScreen, bg="#999999")
        buttonFrame.place(relx=0.5, rely=0.55, anchor="center")

        buttonstyle = {
            "font": ("Helvetica", 18, "bold"),
            "bg": "#B8E3E9", "fg": "#4F7C82",
            "activebackground": "#0B2E33", "activeforeground": "#93B1B5",
            "bd": 0, "relief": "flat", "width": 20, "height": 2, "cursor": "hand2"
        }

        First = x.Button(buttonFrame, text="Basic Calculations Screen", command=self.main, **buttonstyle)
        CalculusScreenjoin = x.Button(buttonFrame, text="Calculus Calculator", command=self.newscreen, **buttonstyle)
        TrigScreenjoin = x.Button(buttonFrame, text="Trig Screen", command=self.trig_screen, **buttonstyle)
        GeometryScreenjoin = x.Button(buttonFrame, text="Geometry Screen", command=self.geometry, **buttonstyle)
        Quadratics = x.Button(buttonFrame, text="Quadratic Formula Solver", command=self.quadratics, **buttonstyle)
        FactorialPermComb = x.Button(buttonFrame, text="Combinatoric Calculator", command=self.combinatorics, **buttonstyle)
        Graph = x.Button(buttonFrame, text="Graphing", command=self.graph, **buttonstyle)

        First.grid(row=0, column=0, padx=30, pady=40)
        CalculusScreenjoin.grid(row=0, column=1, padx=30, pady=40)
        TrigScreenjoin.grid(row=0, column=2, padx=30, pady=40)
        GeometryScreenjoin.grid(row=1, column=0, padx=30, pady=40)
        Quadratics.grid(row=1, column=1, padx=30, pady=40)
        FactorialPermComb.grid(row=1, column=2, padx=30, pady=40)
        Graph.grid(row=2, column=1, padx=30, pady=40)

    def main(self):
        self.Screen = x.Toplevel(self.root)
        self.Screen.geometry("900x700")
        self.Screen.title("Standard Core Operations")

        ACCENT_COLOR = "#00FFFF"
        CalculationContainer = x.Frame(
            self.Screen, bg="#000000",
            highlightbackground=ACCENT_COLOR, highlightthickness=2
        )
        CalculationContainer.place(relwidth=1, relheight=1)
        self.getHome_background(CalculationContainer)

        x.Label(
            CalculationContainer, text="Standard Core Operations",
            font=("Helvetica", 30, "bold"), bg="#000000", fg=ACCENT_COLOR
        ).grid(row=0, column=0, columnspan=4, pady=50)

        def create_entry(row, col, label_text):
            x.Label(
                CalculationContainer, text=label_text,
                font=("Helvetica", 10, "bold"), bg="#000000", fg="#FFFFFF"
            ).grid(row=row, column=col, padx=5, pady=5)
            ent = x.Entry(
                CalculationContainer, width=45,
                bg="#202020", fg=ACCENT_COLOR,
                insertbackground="white", font=("Helvetica", 12, "bold")
            )
            ent.grid(row=row, column=col + 1, padx=5, pady=5)
            return ent

        self.entry1 = create_entry(1, 0, "Input A: ")
        self.entry2 = create_entry(1, 2, "Input B: ")
        self.entry3 = create_entry(2, 0, "SQRT TARGET: ")
        self.entry4 = create_entry(3, 0, "Random Min")
        self.entry5 = create_entry(3, 2, "Random Max")

        opsframe = x.Frame(CalculationContainer, bg="#000000")
        opsframe.grid(row=4, column=0, columnspan=4, pady=20)

        self.styled_button(opsframe, "+", self.add_numbers).grid(row=0, column=0, padx=5, pady=10)
        self.styled_button(opsframe, "-", self.subtract_numbers).grid(row=0, column=1, padx=5, pady=10)
        self.styled_button(opsframe, "*", self.product_numbers).grid(row=0, column=2, padx=5, pady=10)
        self.styled_button(opsframe, "/", self.divide_numbers).grid(row=0, column=3, padx=5, pady=10)
        self.styled_button(opsframe, "ˆ", self.power_numbers).grid(row=1, column=0, padx=5, pady=10)
        self.styled_button(opsframe, "%", self.modulo).grid(row=1, column=1, padx=5, pady=10)
        self.styled_button(opsframe, "SQRT", self.sqrt_number).grid(row=1, column=2, padx=5, pady=10)
        self.styled_button(opsframe, "RANDOM #", self.randomintgeneratorwithinrange).grid(row=1, column=3, padx=5, pady=10)

        self.label_result = x.Label(
            CalculationContainer, text="Result: ",
            font=("Helvetica", 20, "bold"), bg="#000000", fg="#00FF00"
        )
        self.label_result.grid(row=6, column=0, columnspan=4, pady=20)

    def modulo(self):
        try:
            num1 = float(self.entry1.get().strip())
            num2 = float(self.entry2.get().strip())
            result = num1 % num2
            self.label_result.config(text=f"Result: {num1} % {num2} = {result}")
        except ValueError:
            self.label_result.config(text="Syntax Error: Please enter numbers.")
        except OverflowError:
            self.label_result.config(text="The result is too large. Please enter smaller numbers.")

    def add_numbers(self):
        try:
            num1 = float(self.entry1.get().strip())
            num2 = float(self.entry2.get().strip())
            result = num1 + num2
            self.label_result.config(text=f"Result: {num1} + {num2} = {result}")
        except ValueError:
            self.label_result.config(text="Syntax Error: Please enter numbers.")
        except OverflowError:
            self.label_result.config(text="The result is too large. Please enter smaller numbers.")

    def subtract_numbers(self):
        try:
            num1 = float(self.entry1.get().strip())
            num2 = float(self.entry2.get().strip())
            result = num1 - num2
            self.label_result.config(text=f"Result: {num1} - {num2} = {result}")
        except ValueError:
            self.label_result.config(text="Syntax Error: Please enter numbers.")
        except OverflowError:
            self.label_result.config(text="The result is too large. Please enter smaller numbers.")

    def product_numbers(self):
        try:
            num1 = float(self.entry1.get().strip())
            num2 = float(self.entry2.get().strip())
            result = num1 * num2
            self.label_result.config(text=f"Result: {num1} * {num2} = {result}")
        except ValueError:
            self.label_result.config(text="Syntax Error: Please enter numbers.")
        except OverflowError:
            self.label_result.config(text="The result is too large. Please enter smaller numbers.")

    def divide_numbers(self):
        try:
            num1 = float(self.entry1.get().strip())
            num2 = float(self.entry2.get().strip())
            result = num1 / num2
            self.label_result.config(text=f"Result: {num1} / {num2} = {result}")
        except ValueError:
            self.label_result.config(text="Syntax Error: Please enter numbers.")
        except ZeroDivisionError:
            self.label_result.config(text="WARNING: CAN'T DIVIDE BY 0. Either undefined or ±infinity")
        except OverflowError:
            self.label_result.config(text="The result is too large. Please enter smaller numbers.")

    def power_numbers(self):
        try:
            num1 = float(self.entry1.get().strip())
            num2 = float(self.entry2.get().strip())
            result = num1 ** num2
            self.label_result.config(text=f"Result: {num1} ^ {num2} = {result}")
        except ValueError:
            self.label_result.config(text="Syntax Error: Please enter numbers.")
        except OverflowError:
            self.label_result.config(text="The result is too large. Please enter smaller numbers.")

    def sqrt_number(self):
        try:
            num3 = float(self.entry3.get().strip())
            if num3 < 0:
                self.label_result.config(text=f"Result: Square root of {num3} = {math.sqrt(-num3)}i")
                return
            result = math.sqrt(num3)
            self.label_result.config(text=f"Result: Square Root of {num3} = {result}")
        except ValueError:
            self.label_result.config(text="Syntax Error: Please enter numbers.")
        except OverflowError:
            self.label_result.config(text="Overflow Error: Please type smaller numbers.")

    def randomintgeneratorwithinrange(self):
        try:
            num4 = int(self.entry4.get().strip())
            num5 = int(self.entry5.get().strip())
            if num4 > num5:
                num4, num5 = num5, num4
            result = random.randint(num4, num5)
            self.label_result.config(text=f"Result: Random Integer From {num4} to {num5} = {result}")
        except ValueError:
            self.label_result.config(text="Syntax Error: Please enter whole numbers for min and max.")

    def trig_screen(self):
        self.TrigScreen = x.Toplevel(self.root)
        self.TrigScreen.geometry("900x700")
        self.TrigScreen.title("Trig Scrn")
        self.getHome_background(self.TrigScreen)

        self.trig_entry = x.Entry(
            self.TrigScreen, font=("Helvetica", 14, "bold"),
            bg="#000000", fg="#00FFFF"
        )
        self.trig_entry.pack(pady=20)

        self.unit_selection = ttk.Combobox(self.TrigScreen, values=["Degrees", "Radians"])
        self.unit_selection.set("Degrees")
        self.unit_selection.pack()

        trig_button_frame = x.Frame(self.TrigScreen, bg="#000000")
        trig_button_frame.pack(pady=30)

        style = {
            "font": ("Helvetica", 18, "bold"),
            "bg": "#B8E3E9", "fg": "#4F7C82",
            "activebackground": "#0B2E33", "activeforeground": "#93B1B5",
            "bd": 0, "relief": "flat", "width": 15, "height": 2, "cursor": "hand2"
        }

        x.Button(trig_button_frame, text="SIN", command=lambda: self.calculate_trig("sin"), **style).grid(row=0, column=0, padx=10, pady=10)
        x.Button(trig_button_frame, text="COS", command=lambda: self.calculate_trig("cos"), **style).grid(row=0, column=1, padx=10, pady=10)
        x.Button(trig_button_frame, text="TAN", command=lambda: self.calculate_trig("tan"), **style).grid(row=0, column=2, padx=10, pady=10)

        self.result_label = x.Label(
            self.TrigScreen, text="Result Will Show Here",
            font=("Helvetica", 14, "bold"), bg="#000000", fg="#00FF00"
        )
        self.result_label.place(relx=0.5, rely=0.8, anchor="center")

    def calculate_trig(self, func):
        try:
            original = float(self.trig_entry.get().strip())
            val = original
            unit = self.unit_selection.get()

            if unit == "Degrees":
                val = math.radians(val)

            if func == "sin":
                result = round(math.sin(val), 10)
            elif func == "cos":
                result = round(math.cos(val), 10)
            elif func == "tan":
                result = round(math.tan(val), 10)

            unit_symbol = "°" if unit == "Degrees" else " rad"
            self.result_label.config(text=f"Result: {func}({original}{unit_symbol}) = {result}")
        except Exception:
            self.result_label.config(text="Invalid Input...")

    def newscreen(self):
        self.CalculusScreen = x.Toplevel(self.root)
        self.CalculusScreen.geometry("1100x750")
        self.CalculusScreen.title("Graphing Calc - Calculus")
        self.getHome_background(self.CalculusScreen)

        # Coefficient labels + entries (simplified layout)
        coeffs = [
            ("x¹⁰ +", "dectic"), ("x⁹ +", "noctic"), ("x⁸ +", "octic"),
            ("x⁷ +", "septic"), ("x⁶ +", "sextic"), ("x⁵ +", "quintic"),
            ("x⁴ +", "quartic"), ("x³ +", "cubed"), ("x² +", "square"),
            ("x +", "xtotheone"), ("const", "constant")
        ]

        for i, (label, attr) in enumerate(coeffs):
            x.Label(
                self.CalculusScreen, text=label,
                font=("Helvetica", 12, "bold"), bg="#000000", fg="#00FFFF"
            ).grid(row=0, column=i*2, padx=2, pady=5, sticky="e")
            entry = x.Entry(self.CalculusScreen, font=("Helvetica", 12), width=6, bg="#000000", fg="#00FFFF")
            entry.grid(row=0, column=i*2+1, padx=2, pady=5)
            setattr(self, attr, entry)

        x.Label(
            self.CalculusScreen, text="Derivative @ x = ",
            font=("Helvetica", 14, "bold"), bg="#000000", fg="#00FFFF"
        ).grid(row=1, column=0, columnspan=2, pady=15, sticky="e")
        self.xatpoint = x.Entry(self.CalculusScreen, width=8, bg="#000000", fg="#00FFFF")
        self.xatpoint.grid(row=1, column=2, pady=15)

        self.derivativeatapoint = x.Button(
            self.CalculusScreen, text="Derivative @ a Point",
            font=("Helvetica", 14, "bold"), bg="#000000", fg="#00FFFF",
            command=self.derivativate
        )
        self.derivativeatapoint.grid(row=2, column=0, columnspan=4, pady=10)

        x.Label(self.CalculusScreen, text="Lower Bound:", font=("Helvetica", 12, "bold"),
                bg="#000000", fg="#00FFFF").grid(row=3, column=0, sticky="e")
        self.thelowerbound = x.Entry(self.CalculusScreen, width=10, bg="#000000", fg="#00FFFF")
        self.thelowerbound.grid(row=3, column=1)

        x.Label(self.CalculusScreen, text="Upper Bound:", font=("Helvetica", 12, "bold"),
                bg="#000000", fg="#00FFFF").grid(row=3, column=2, sticky="e")
        self.theupperbound = x.Entry(self.CalculusScreen, width=10, bg="#000000", fg="#00FFFF")
        self.theupperbound.grid(row=3, column=3)

        self.integralwithbounds = x.Button(
            self.CalculusScreen, text="Integral With Bounds",
            font=("Helvetica", 14, "bold"), bg="#000000", fg="#00FFFF",
            command=self.integrate
        )
        self.integralwithbounds.grid(row=4, column=0, columnspan=4, pady=10)

        self.resultlabel = x.Label(
            self.CalculusScreen, text="Result: ",
            font=("Helvetica", 16, "bold"), bg="#000000", fg="#00FF00"
        )
        self.resultlabel.grid(row=6, column=0, columnspan=8, pady=20)

    def derivativate(self):
        try:
            coeffs = [
                float(self.dectic.get() or 0),
                float(self.noctic.get() or 0),
                float(self.octic.get() or 0),
                float(self.septic.get() or 0),
                float(self.sextic.get() or 0),
                float(self.quintic.get() or 0),
                float(self.quartic.get() or 0),
                float(self.cubed.get() or 0),
                float(self.square.get() or 0),
                float(self.xtotheone.get() or 0),
                float(self.constant.get() or 0)
            ]
            x_val = float(self.xatpoint.get())

            # Power rule: derivative of a*x^n is n*a*x^(n-1)
            derivative = 0
            for power in range(10, 0, -1):
                a = coeffs[10 - power]
                derivative += power * a * (x_val ** (power - 1))

            self.resultlabel.config(text=f"Derivative = {derivative}")
        except ValueError:
            self.resultlabel.config(text="Please Enter Number Inputs")

    def integrate(self):
        try:
            coeffs = [
                float(self.dectic.get() or 0),
                float(self.noctic.get() or 0),
                float(self.octic.get() or 0),
                float(self.septic.get() or 0),
                float(self.sextic.get() or 0),
                float(self.quintic.get() or 0),
                float(self.quartic.get() or 0),
                float(self.cubed.get() or 0),
                float(self.square.get() or 0),
                float(self.xtotheone.get() or 0),
                float(self.constant.get() or 0)
            ]
            lower = float(self.thelowerbound.get())
            upper = float(self.theupperbound.get())

            integral = 0
            for power in range(10, -1, -1):
                a = coeffs[10 - power]
                integral += (a / (power + 1)) * (upper ** (power + 1) - lower ** (power + 1))

            self.resultlabel.config(text=f"Integral = {integral}")
        except ValueError:
            self.resultlabel.config(text="Please Enter Number Inputs")

    def quadratics(self):
        self.quadraticsScreen = x.Toplevel(self.root)
        self.quadraticsScreen.geometry("900x700")
        self.quadraticsScreen.title("Quadratics & Stuff")
        self.getHome_background(self.quadraticsScreen)
        self.quadraticsScreen.configure(bg="black")

        x.Label(
            self.quadraticsScreen, text="y = ax² + bx + c",
            font=("Helvetica", 16, "bold"), bg="#000000", fg="#00FFFF"
        ).grid(row=0, column=0, columnspan=2, pady=20)

        x.Label(self.quadraticsScreen, text="A = ", font=("Helvetica", 14, "bold"),
                bg="#000000", fg="#00FFFF").grid(row=1, column=0, sticky="e", padx=10)
        self.a_entry = x.Entry(self.quadraticsScreen, font=("Helvetica", 14), width=12, bg="#000000", fg="#00FFFF")
        self.a_entry.grid(row=1, column=1, pady=10)

        x.Label(self.quadraticsScreen, text="B = ", font=("Helvetica", 14, "bold"),
                bg="#000000", fg="#00FFFF").grid(row=2, column=0, sticky="e", padx=10)
        self.b_entry = x.Entry(self.quadraticsScreen, font=("Helvetica", 14), width=12, bg="#000000", fg="#00FFFF")
        self.b_entry.grid(row=2, column=1, pady=10)

        x.Label(self.quadraticsScreen, text="C = ", font=("Helvetica", 14, "bold"),
                bg="#000000", fg="#00FFFF").grid(row=3, column=0, sticky="e", padx=10)
        self.c_entry = x.Entry(self.quadraticsScreen, font=("Helvetica", 14), width=12, bg="#000000", fg="#00FFFF")
        self.c_entry.grid(row=3, column=1, pady=10)

        x.Button(
            self.quadraticsScreen, text="Quadratic Formula Solver",
            font=("Helvetica", 16, "bold"), bg="#B8E3E9", fg="#4F7C82",
            command=self.solve
        ).grid(row=4, column=0, columnspan=2, pady=30)

        self.label_result2 = x.Label(
            self.quadraticsScreen, text="Result: ",
            font=("Helvetica", 18, "bold"), bg="#000000", fg="#00FF00"
        )
        self.label_result2.grid(row=5, column=0, columnspan=2, pady=20)

    def solve(self):
        try:
            a = float(self.a_entry.get().strip())
            b = float(self.b_entry.get().strip())
            c = float(self.c_entry.get().strip())

            if a == 0:
                if b == 0:
                    self.label_result2.config(text="Not an equation (a = 0 and b = 0)")
                else:
                    # Linear equation
                    root = -c / b
                    self.label_result2.config(text=f"Linear equation → x = {root}")
                return

            disc = b**2 - 4*a*c

            if disc > 0:
                r1 = (-b + math.sqrt(disc)) / (2*a)
                r2 = (-b - math.sqrt(disc)) / (2*a)
                self.label_result2.config(text=f"Two real roots: {r1}  and  {r2}")
            elif disc == 0:
                r = -b / (2*a)
                self.label_result2.config(text=f"One real root (double): {r}")
            else:
                real = -b / (2*a)
                imag = math.sqrt(-disc) / (2*a)
                self.label_result2.config(text=f"Complex roots: {real} ± {imag}i")
        except Exception:
            self.label_result2.config(text="INVALID INPUT!")

    def combinatorics(self):
        self.CombinatoricScreen = x.Toplevel(self.root)
        self.CombinatoricScreen.title("Combinatorics Scrn")
        self.getHome_background(self.CombinatoricScreen)
        self.CombinatoricScreen.geometry("900x700")

        x.Label(self.CombinatoricScreen, text="Enter value n here:",
                font=("Helvetica", 18, "bold"), bg="#000000", fg="#00FFFF").pack(pady=15)
        self.n = x.Entry(self.CombinatoricScreen, font=("Helvetica", 14, "bold"), bg="#000000", fg="#00FFFF")
        self.n.pack(pady=10)

        x.Label(self.CombinatoricScreen, text="Enter value r here:",
                font=("Helvetica", 18, "bold"), bg="#000000", fg="#00FFFF").pack(pady=15)
        self.r = x.Entry(self.CombinatoricScreen, font=("Helvetica", 14, "bold"), bg="#000000", fg="#00FFFF")
        self.r.pack(pady=10)

        style = {
            "font": ("Helvetica", 18, "bold"),
            "bg": "#B8E3E9", "fg": "#4F7C82",
            "activebackground": "#0B2E33", "activeforeground": "#93B1B5",
            "bd": 0, "relief": "flat", "width": 15, "height": 2, "cursor": "hand2"
        }

        x.Button(self.CombinatoricScreen, text="n!", command=self.fact, **style).place(relx=0.5, rely=0.50, anchor="center")
        x.Button(self.CombinatoricScreen, text="nPr", command=self.perm, **style).place(relx=0.5, rely=0.60, anchor="center")
        x.Button(self.CombinatoricScreen, text="nCr", command=self.comb, **style).place(relx=0.5, rely=0.70, anchor="center")

        self.resultlabel = x.Label(
            self.CombinatoricScreen, text="Result: ",
            font=("Helvetica", 16, "bold"), bg="#000000", fg="#00FF00"
        )
        self.resultlabel.place(relx=0.5, rely=0.85, anchor="center")

    def fact(self):
        try:
            n = int(self.n.get().strip())
            if n < 0:
                self.resultlabel.config(text="Invalid Input! (n ≥ 0)")
                return
            result = math.factorial(n)
            self.resultlabel.config(text=f"n! = {result}")
        except ValueError:
            self.resultlabel.config(text="Invalid Input!")

    def perm(self):
        try:
            n = int(self.n.get().strip())
            r = int(self.r.get().strip())
            if n < 0 or r < 0 or r > n:
                self.resultlabel.config(text="Invalid Input!")
                return
            result = math.factorial(n) // math.factorial(n - r)
            self.resultlabel.config(text=f"nPr = {result}")
        except ValueError:
            self.resultlabel.config(text="Invalid Input!")

    def comb(self):
        try:
            n = int(self.n.get().strip())
            r = int(self.r.get().strip())
            if n < 0 or r < 0 or r > n:
                self.resultlabel.config(text="Invalid Input!")
                return
            result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
            self.resultlabel.config(text=f"nCr = {result}")
        except ValueError:
            self.resultlabel.config(text="Invalid Input!")

    def graph(self):
        self.graphing = x.Toplevel(self.root)
        self.graphing.title("Graphing Scrn")
        self.getHome_background(self.graphing)
        self.graphing.geometry("900x700")

        self.graphinginput = x.Entry(self.graphing, font=("Helvetica", 14), width=40)
        self.graphinginput.pack(pady=30)
        self.graphinginput.insert(0, "x**2")   # helpful default

        x.Button(
            self.graphing, text="Plot Graph",
            font=("Helvetica", 18, "bold"), bg="#B8E3E9", fg="#4F7C82",
            command=self.grapher
        ).pack(pady=10)

        self.resultlabel = x.Label(
            self.graphing, text="Result: ",
            font=("Helvetica", 20, "bold"), bg="#000000", fg="#00FF00"
        )
        self.resultlabel.pack(pady=20)

    def grapher(self):
        try:
            expr = self.graphinginput.get().strip()
            xval = numpy.linspace(-10, 10, 500)
            yval = []

            safe_dict = {
                "__builtins__": None,
                "x": None,
                "math": math,
                "np": numpy,
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "exp": math.exp,
                "log": math.log,
                "pi": math.pi,
                "e": math.e
            }

            for val in xval:
                safe_dict["x"] = val
                yval.append(eval(expr, safe_dict))

            p.figure()
            p.plot(xval, yval)
            p.title("Graph")
            p.xlabel("X")
            p.ylabel("Y")
            p.grid(True)
            p.show()
            self.resultlabel.config(text="✅ Graph plotted")
        except Exception:
            self.resultlabel.config(text="Invalid Function ❌")

    def geometry(self):
        self.GeometryScreen = x.Toplevel(self.root)
        self.GeometryScreen.title("Geometry Screen")
        self.getHome_background(self.GeometryScreen)
        self.GeometryScreen.geometry("900x700")

        x.Label(self.GeometryScreen, text="Enter Value 1 (length / base / radius):",
                font=("Helvetica", 14, "bold"), bg="#000000", fg="#00FFFF").pack(pady=5)
        self.geo_entry1 = x.Entry(self.GeometryScreen, font=("Helvetica", 14), bg="#000000", fg="#00FFFF")
        self.geo_entry1.pack(pady=5)

        x.Label(self.GeometryScreen, text="Enter Value 2 (width / height):",
                font=("Helvetica", 14, "bold"), bg="#000000", fg="#00FFFF").pack(pady=5)
        self.geo_entry2 = x.Entry(self.GeometryScreen, font=("Helvetica", 14), bg="#000000", fg="#00FFFF")
        self.geo_entry2.pack(pady=5)

        self.result_label = x.Label(
            self.GeometryScreen, text="Result: ",
            font=("Helvetica", 14, "bold"), bg="#000000", fg="#00FF00"
        )
        self.result_label.pack(pady=15)

        buttonFrame = x.Frame(self.GeometryScreen, bg="#999999")
        buttonFrame.place(relx=0.5, rely=0.50, anchor="center")

        buttonstyle = {
            "font": ("Helvetica", 14, "bold"),
            "bg": "#B8E3E9", "fg": "#4F7C82",
            "activebackground": "#0B2E33", "activeforeground": "#93B1B5",
            "bd": 0, "relief": "flat", "width": 22, "height": 2, "cursor": "hand2"
        }

        x.Button(buttonFrame, text="Area of Rectangle", command=self.area_rectangle, **buttonstyle).grid(row=0, column=0, padx=15, pady=15)
        x.Button(buttonFrame, text="Perimeter of Rectangle", command=self.perimeter_rectangle, **buttonstyle).grid(row=0, column=1, padx=15, pady=15)
        x.Button(buttonFrame, text="Area of Triangle", command=self.triangle_area, **buttonstyle).grid(row=0, column=2, padx=15, pady=15)
        x.Button(buttonFrame, text="Area of Circle", command=self.area_circle, **buttonstyle).grid(row=1, column=0, padx=15, pady=15)
        x.Button(buttonFrame, text="Circumference of Circle", command=self.circumference_circle, **buttonstyle).grid(row=1, column=1, padx=15, pady=15)

    def area_rectangle(self):
        try:
            a = float(self.geo_entry1.get().strip())
            b = float(self.geo_entry2.get().strip())
            self.result_label.config(text=f"Area of Rectangle: {a * b}")
        except:
            self.result_label.config(text="Invalid Input")

    def perimeter_rectangle(self):
        try:
            a = float(self.geo_entry1.get().strip())
            b = float(self.geo_entry2.get().strip())
            self.result_label.config(text=f"Perimeter of Rectangle: {2*(a + b)}")
        except:
            self.result_label.config(text="Invalid Input")

    def triangle_area(self):
        try:
            a = float(self.geo_entry1.get().strip())
            b = float(self.geo_entry2.get().strip())
            self.result_label.config(text=f"Area of Triangle: {(a * b)/2}")
        except:
            self.result_label.config(text="Invalid Input")

    def area_circle(self):
        try:
            r = float(self.geo_entry1.get().strip())
            self.result_label.config(text=f"Area of Circle: {math.pi * r**2}")
        except:
            self.result_label.config(text="Invalid Input")

    def circumference_circle(self):
        try:
            r = float(self.geo_entry1.get().strip())
            self.result_label.config(text=f"Circumference of Circle: {2 * math.pi * r}")
        except:
            self.result_label.config(text="Invalid Input")


if __name__ == "__main__":
    root = x.Tk()
    root.withdraw()
    app = CalculatorApp(root)
    app.homescreen()          # ← this was missing
    root.mainloop()