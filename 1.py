import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from Ui_main_window import Ui_MainWindow
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time

class Plot():
    def __init__(self):
        # 创建一个画布
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))

        self.canvas.mpl_connect('button_press_event', self.movePressEvent)

        # 添加一个坐标系
        self.p1 = self.canvas.figure.subplots()
        self.p1.set_ylabel('Temperature ℃')

        # 创建另一个坐标系且共享上面的X轴
        self.p2 = self.p1.twinx()
        self.p2.set_ylabel('Humidity %')

        self.p1.plot([0, 1, 2, 3], [6, 4, 3, 1], 'r')
        self.p2.plot([0, 1, 2, 3], [2, 3, 4, 5])

    def movePressEvent(self, event):
        print(event)
        pass

class window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.setupUi(self)
        self.plot = Plot()
        self.plotLayout = QtWidgets.QVBoxLayout(self.widget)

        self.plotLayout.addWidget(self.plot.canvas)


def main():
    m = window()
    m.show()
    return m


if __name__ == "__main__":
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    # matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']

    app = QtWidgets.QApplication(sys.argv)
    main_obj = main()
    sys.exit(app.exec_())
