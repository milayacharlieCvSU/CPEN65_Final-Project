from tkinter import *
from tkinter.ttk import Combobox
from sympy import *
from sympy.abc import x
from scipy.integrate import simpson
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)


class App(Tk):
    # -< Initialization >--------------------------------------------------------------------------------------------- #
    def __init__(self):
        super().__init__()

        # -< Window Properties >-------------------------------------------------------------------------------------- #
        win_height = 600
        win_width = int(win_height * (1 + sqrt(5)) / 2)
        self.geometry(f'{win_width}x{win_height}+25+25')
        self.title('Numerical Integration')

        for col in range(0, 6):
            self.columnconfigure(col, weight=1)

        # -----< Labels >--------------------------------------------------------------------------------------------- #
        self.title_lbl = Label(self, text="Approximation of Integral of f(x) at (a, b)", font=("Times New Roman", 14))
        self.title_lbl.grid(column=1, row=0, columnspan=4)

        self.funct_lbl = Label(self, text="Function (in x): ", font=('Times New Roman', 14))
        self.funct_lbl.grid(column=2, row=3, sticky=W)

        self.lower_lbl = Label(self, text="a: ", font=('Times New Roman', 14))
        self.lower_lbl.grid(column=2, row=4, sticky=W)

        self.upper_lbl = Label(self, text="b: ", font=('Times New Roman', 14))
        self.upper_lbl.grid(column=2, row=5, sticky=W)

        self.slice_lbl = Label(self, text="Slices: ", font=('Times New Roman', 14))
        self.slice_lbl.grid(column=2, row=6, sticky=W)

        self.method_lbl = Label(self, text="Method: ", font=('Times New Roman', 14))
        self.method_lbl.grid(column=2, row=7, sticky=W)

        self.approx_lbl = Label(self, text="Approximate Value: ", font=('Times New Roman', 14))
        self.approx_lbl.grid(column=2, row=10, sticky=W)

        self.exact_lbl = Label(self, text="Exact Value: ", font=('Times New Roman', 14))
        self.exact_lbl.grid(column=2, row=11, sticky=W)

        self.error_lbl = Label(self, text="Error: ", font=('Times New Roman', 14))
        self.error_lbl.grid(column=2, row=12, sticky=W)

        # -----< Entries/Selections >--------------------------------------------------------------------------------- #
        self.funct_data = Entry(self, font=('Times New Roman', 14))
        self.funct_data.grid(column=3, row=3, columnspan=2, sticky=E)

        self.lower_data = Entry(self, font=('Times New Roman', 14))
        self.lower_data.grid(column=3, row=4, columnspan=2, sticky=E)

        self.upper_data = Entry(self, font=('Times New Roman', 14))
        self.upper_data.grid(column=3, row=5, columnspan=2, sticky=E)

        self.n_data = Entry(self, font=('Times New Roman', 14))
        self.n_data.grid(column=3, row=6, columnspan=2, sticky=E)

        self.method_data = Combobox(self, font=('Times New Roman', 14))
        self.method_data.grid(column=3, row=7, columnspan=2, sticky=E)

        self.method_data['values'] = ['Riemann Lower Sum',
                                      'Riemann Upper Sum',
                                      'Midpoint Rule',
                                      'Trapezoidal Rule',
                                      "Simpson's Rule"]

        self.method_data['state'] = 'readonly'

        self.approx_data = Entry(self, bd=0, font=('Times New Roman', 14), state='readonly')
        self.approx_data.grid(column=3, row=10, columnspan=2, sticky=W)

        self.exact_data = Entry(self, bd=0, font=('Times New Roman', 14), state='readonly')
        self.exact_data.grid(column=3, row=11, columnspan=2, sticky=W)

        self.error_data = Entry(self, bd=0, font=('Times New Roman', 14), state='readonly')
        self.error_data.grid(column=3, row=12, columnspan=2, sticky=W)

        # -----< Button >--------------------------------------------------------------------------------------------- #
        self.calc = Button(self, text='Calculate', font=('Times New Roman', 14), command=self.calculate)
        self.calc.grid(column=2, row=9, columnspan=4)

        # -----< Plot >----------------------------------------------------------------------------------------------- #
        # ---------< Figure Environment >----------------------------------------------------------------------------- #
        self.figure = plt.Figure(figsize=(5, 5), dpi=100)

        # ---------< Placeholder Data Set >--------------------------------------------------------------------------- #
        x_plot = [-5, 5]
        y_plot = [-5, 5]

        # ---------< Plotting P. Data Set >--------------------------------------------------------------------------- #
        self.calc_plt = self.figure.subplots()
        self.calc_plt.scatter(x_plot, y_plot, color='w')

        # ---------< Adjusting Axes >--------------------------------------------------------------------------------- #
        self.calc_plt.spines['bottom'].set_position(('data', 0))
        self.calc_plt.spines['left'].set_position(('data', 0))
        self.calc_plt.axhline(y=self.calc_plt.get_ylim()[0], color='k')
        self.calc_plt.axvline(x=self.calc_plt.get_xlim()[0], color='k')
        self.figure.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
        self.calc_plt.grid()

        # ---------< Placing Figure in Window >----------------------------------------------------------------------- #
        self.calc_canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.calc_canvas.draw()
        self.calc_canvas.get_tk_widget().grid(column=1, row=1, rowspan=13)

    # -< Calculations >----------------------------------------------------------------------------------------------- #
    def calculate(self):
        # -----< Method Classes >------------------------------------------------------------------------------------- #
        class ApproxIntegral:
            def __init__(self, f, a, b, n):
                self.f = f
                self.a = a
                self.b = b
                self.n = n

        class LowerSum(ApproxIntegral):
            def approx(self):
                func = sympify(self.f)
                def_F = Integral(func, (x, self.a, self.b))
                return def_F.as_sum(self.n, 'left').evalf(15)

        class UpperSum(ApproxIntegral):
            def approx(self):
                func = sympify(self.f)
                def_F = Integral(func, (x, self.a, self.b))
                return def_F.as_sum(self.n, 'right').evalf(15)

        class Midpoint(ApproxIntegral):
            def approx(self):
                func = sympify(self.f)
                def_F = Integral(func, (x, self.a, self.b))
                return def_F.as_sum(self.n, 'midpoint').evalf(15)

        class Trapezoid(ApproxIntegral):
            def approx(self):
                func = sympify(self.f)
                def_F = Integral(func, (x, self.a, self.b))
                return def_F.as_sum(self.n, 'trapezoid').evalf(15)

        class Simpson(ApproxIntegral):
            def approx(self):
                func = sympify(self.f)
                if int(self.n) % 2 != 0:
                    self.n = int(self.n) + 1
                a, b, n = float(self.a), float(self.b), int(self.n)
                h = (b - a) / n
                x_i = linspace(a, b, n - 1)
                y_i = [func.subs(x, x_t) for x_t in x_i]
                return simpson(y_i, x_i, h)

        class ExactIntegral(ApproxIntegral):
            def exact_value(self):
                func = sympify(self.f)
                def_F = integrate(func, (x, self.a, self.b))
                return def_F.evalf(15)

        # -----< Method Usage >--------------------------------------------------------------------------------------- #
        if self.method_data.get() == "Riemann Lower Sum":
            G_approx = LowerSum(self.funct_data.get(), eval(self.lower_data.get()), eval(self.upper_data.get()),
                                self.n_data.get())
        elif self.method_data.get() == "Riemann Upper Sum":
            G_approx = UpperSum(self.funct_data.get(), eval(self.lower_data.get()), eval(self.upper_data.get()),
                                self.n_data.get())
        elif self.method_data.get() == "Midpoint Rule":
            G_approx = Midpoint(self.funct_data.get(), eval(self.lower_data.get()), eval(self.upper_data.get()),
                                self.n_data.get())
        elif self.method_data.get() == "Trapezoidal Rule":
            G_approx = Trapezoid(self.funct_data.get(), eval(self.lower_data.get()), eval(self.upper_data.get()),
                                 self.n_data.get())
        elif self.method_data.get() == "Simpson's Rule":
            G_approx = Simpson(self.funct_data.get(), eval(self.lower_data.get()), eval(self.upper_data.get()),
                               self.n_data.get())

        G_exact = ExactIntegral(self.funct_data.get(), eval(self.lower_data.get()), eval(self.upper_data.get()),
                                self.n_data.get())

        approx = G_approx.approx()
        exact = G_exact.exact_value()
        error = abs(approx - exact).evalf(3)

        self.approx_data['state'] = 'normal'
        self.approx_data.delete("0", END)
        self.approx_data.insert(END, f"{approx}")
        self.approx_data['state'] = 'readonly'

        self.exact_data['state'] = 'normal'
        self.exact_data.delete("0", END)
        self.exact_data.insert(END, f"{exact}")
        self.exact_data['state'] = 'readonly'

        self.error_data['state'] = 'normal'
        self.error_data.delete("0", END)
        self.error_data.insert(END, f"{error}")
        self.error_data['state'] = 'readonly'

        # -< Calculated Plot >---------------------------------------------------------------------------------------- #
        # -----< Figure Environment >--------------------------------------------------------------------------------- #
        self.calc_figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.calc_figure.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

        # -----< Calculating and Plotting Data Set and Visualizing Integral >----------------------------------------- #
        self.calc_plt = self.calc_figure.subplots()
        x_i = linspace(eval(self.lower_data.get()), eval(self.upper_data.get()), 250)
        try:
            y = eval(self.funct_data.get())
            F = [y for i in x_i]
            self.calc_plt.plot(x_i, F, 'b')
            self.calc_plt.fill_between(x_i, 0, F, color='blue', alpha=0.25)
        except:
            y = sympify(self.funct_data.get())
            F = lambdify(x, y, 'numpy')
            self.calc_plt.plot(x_i, F(x_i), 'b')
            self.calc_plt.fill_between(x_i, 0, F(x_i), color='blue', alpha=0.25)

        # -----< Adjusting Axes >------------------------------------------------------------------------------------- #
        x_min = self.calc_plt.get_xlim()[0]
        x_max = self.calc_plt.get_xlim()[1]
        y_min = self.calc_plt.get_ylim()[0]
        y_max = self.calc_plt.get_ylim()[1]
        if x_min < 0 < x_max:
            self.calc_plt.spines['left'].set_position(('data', 0))
            self.calc_plt.axvline(x=x_min, color='k')
        elif x_max <= 0:
            self.calc_plt.spines['right'].set_position(('data', x_min))
            self.calc_plt.spines['left'].set_position(('data', x_max))
            self.calc_plt.tick_params(axis='y', pad=-25, direction='in')
        if y_min < 0 < y_max:
            self.calc_plt.spines['bottom'].set_position(('data', 0))
            self.calc_plt.axhline(y=y_min, color='k')
        elif y_max <= 0:
            self.calc_plt.spines['top'].set_position(('data', y_min))
            self.calc_plt.spines['bottom'].set_position(('data', y_max))
            self.calc_plt.tick_params(axis='x', pad=-15, direction='in')

        # -----< Placing Figure in Window >--------------------------------------------------------------------------- #
        self.calc_plt.grid()
        self.calc_canvas = FigureCanvasTkAgg(self.calc_figure, master=self)
        self.calc_canvas.draw()
        self.calc_canvas.get_tk_widget().grid(column=1, row=1, rowspan=13)


if __name__ == "__main__":
    app = App()
    app.mainloop()
