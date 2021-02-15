import struct
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import matplotlib.figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import copy
import matplotlib
import os


faces = {
    'head1.dat': [(0, 16, 18, '#613009'), (1, 15, 19, '#613009'), (15, 16, 18, 19, '#6d3c09'), (15, 10, 16, '#cfa279'),
                  (1, 10, 15, '#d7aa82'), (0, 10, 16, '#d7aa82'), (0, 11, 10, '#4d5db6'), (10, 12, 1, '#4d5db6'),
                  (0, 5, 17, 18, '#efc3a6'), (1, 2, 20, 19, '#efc3a6'), (8, 9, 10, '#ffd7be'), (1, 2, 12, '#ffcbb2'),
                  (11, 0, 5, '#ffcbb2'), (9, 10, 12, '#efc3a6'), (8, 11, 10, '#efc3a6'), (2, 7, 12, '#ffd7be'),
                  (5, 6, 11, '#ffd7be'), (7, 9, 12, '#ffcbb2'), (8, 6, 11, '#ffcbb2'), (13, 14, 9, 8, '#e7ba9a'),
                  (4, 17, 5, '#ffcbb2'), (3, 2, 20, '#ffcbb2'), (7, 3, 2, '#e7ba9a'), (4, 5, 6, '#e7ba9a'),
                  (7, 3, 21, '#dfb28e'), (6, 4, 21, '#dfb28e'), (4, 3, 21, '#f7cbb2'), (6, 21, 7, 14, 13, '#ffffff'),
                  (6, 8, 13, '#dfb28e'), (7, 14, 9, '#dfb28e')],

    'head2.dat': [(1, 21, 17, '#180971'), (0, 20, 16, '#cf2020'), (16, 17, 21, 20, '#ffffff'),
                  (1, 2, 18, 17, '#c79a6d'), (0, 5, 15, 16, '#c79a6d'), (10, 21, 20, '#aaaaaa'),
                  (0, 10, 20, '#aa0000'), (1, 10, 21, '#0000aa'), (0, 10, 11, '#6d86ff'), (1, 10, 12, '#6d86ff'),
                  (0, 5, 6, 11, '#cfa279'), (1, 2, 7, 12, '#cfa279'), (8, 9, 10, '#ffd7be'), (8, 10, 11, '#d7aa82'),
                  (9, 10, 12, '#d7aa82'), (8, 9, 14, 13, '#dfb28e'), (6, 19, 7, 14, 13, '#ffffff'),
                  (3, 4, 19, '#f7cbb2'), (3, 7, 19, '#efc3a6'), (4, 6, 19, '#efc3a6'), (5, 4, 6, '#ba8a55'),
                  (2, 3, 7, '#ba8a55'), (7, 9, 14, '#e7ba9a'), (6, 8, 13, '#e7ba9a'), (6, 8, 11, '#cfa279'),
                  (7, 9, 12, '#cfa279')],

    'head3.dat': [(10, 23, 24, '#cf6dd3'), (23, 24, 26, 25, '#ef9af3'), (10, 24, 15, '#8a590f'),
                  (10, 23, 16, '#8a590f'), (1, 19, 15, '#865109'), (1, 10, 15, '#865109'), (0, 18, 16, '#865109'),
                  (0, 10, 16, '#865109'), (15, 24, 26, 19, '#865109'), (16, 23, 25, 18, '#865109'),
                  (0, 5, 17, 18, '#7d4a09'), (1, 2, 20, 19, '#7d4a09'), (1, 10, 12, '#ffffff'), (0, 10, 11, '#ffffff'),
                  (1, 2, 12, '#824d09'), (0, 5, 11, '#824d09'), (2, 7, 12, '#92611c'), (5, 6, 11, '#92611c'),
                  (6, 13, 8, 11, '#8a590f'), (7, 14, 9, 12, '#8a590f'), (10, 8, 11, '#865109'), (10, 9, 12, '#865109'),
                  (8, 10, 21, '#92611c'), (9, 10, 21, '#8a590f'), (8, 9, 21, '#552809'), (9, 8, 13, 14, '#865109'),
                  (13, 14, 22, '#000000'), (6, 13, 22, 14, 7, 22, 6, '#ffffff'), (7, 3, 22, '#8a590f'),
                  (6, 4, 22, '#8a590f'), (3, 4, 22, '#865109'), (4, 5, 6, '#92611c'), (2, 3, 7, '#92611c')],

    'head4.dat': [(2, 12, 16, 17, '#fbae00'), (5, 13, 15, 14, '#fbae00'), (12, 13, 15, 16, '#f7ba00'),
                  (12, 13, 24, '#ffd7be'), (13, 19, 24, '#aaaaaa'), (12, 18, 24, '#aaaaaa'),
                  (22, 20, 23, 21, '#ffffff'), (3, 4, 23, 21, 22, '#e7ba9a'), (2, 6, 20, 22, '#e7ba9a'),
                  (5, 11, 20, 23, '#e7ba9a'), (2, 3, 22, '#e7ba9a'), (4, 5, 23, '#e7ba9a'), (4, 5, 14, '#efc3a6'),
                  (2, 3, 17, '#efc3a6'), (2, 6, 8, 18, '#f7cbb2'), (2, 12, 18, '#f7cbb2'), (5, 11, 10, 19, '#f7cbb2'),
                  (5, 13, 19, '#f7cbb2'), (19, 10, 8, 18, 24, '#f7cbb2'), (1, 7, 6, 8, '#c74a4d'),
                  (0, 10, 11, 9, '#c74a4d'), (0, 1, 7, 9, '#ba301c'), (0, 1, 8, 10, '#ba301c'),
                  (6, 7, 9, 11, '#962088'), (6, 11, 20, '#e7ba9a')],

    'head5.dat': [(0, 5, 17, 18, '#efc3a6'), (1, 2, 20, 19, '#efc3a6'), (2, 3, 20, '#f7cbb2'), (5, 4, 17, '#f7cbb2'),
                  (1, 15, 19, '#005500'), (15, 16, 18, 19, '#005500'), (0, 16, 18, '#005500'), (15, 10, 16, '#003500'),
                  (1, 10, 15, '#d7aa82'), (0, 10, 16, '#d7aa82'), (0, 11, 10, '#ff5555'), (1, 12, 10, '#ff5555'),
                  (0, 5, 6, 11, '#ffd7be'), (1, 2, 7, 12, '#ffd7be'), (2, 3, 7, '#e7ba9a'), (4, 5, 6, '#e7ba9a'),
                  (6, 8, 10, 11, '#f7cbb2'), (7, 9, 10, 12, '#f7cbb2'), (6, 13, 22, '#ffffff'), (7, 14, 22, '#ffffff'),
                  (13, 14, 22, '#ffffff'), (4, 6, 22, '#dfb28e'), (3, 7, 22, '#dfb28e'), (3, 4, 22, '#f7cbb2'),
                  (8, 9, 14, 13, '#e7ba9a'), (6, 8, 13, '#dfb28e'), (7, 9, 14, '#dfb28e'), (8, 9, 21, '#c39261'),
                  (8, 10, 21, '#ffd7be'),
                  (9, 10, 21, '#ffd7be')],

    'head6.dat': [(0, 24, 9, 12, 13, '#cb1c1c'), (11, 17, 18, '#ffffff'), (1, 23, 10, 15, 14, '#cb1c1c'),
                  (3, 4, 9, 12, '#dfb28e'), (2, 5, 10, 15, '#dfb28e'), (0, 1, 23, '#ba0c0c'),
                  (0, 1, 14, 13, '#ba0c0c'), (0, 23, 8, 22, 24, '#e7ba9a'), (4, 5, 18, 17, '#dfb28e'),
                  (17, 6, 7, 18, 11, '#efc3a6'), (9, 4, 17, 6, 22, '#f7cbb2'), (10, 5, 18, 7, 8, '#f7cbb2'),
                  (6, 7, 19, 16, '#a27125'), (6, 16, 20, 22, '#c79a6d'), (7, 19, 21, 8, '#c79a6d'),
                  (16, 19, 21, 20, '#ffd7be'), (20, 21, 8, 22, '#ffd7be'), (9, 22, 24, '#aaaaaa'),
                  (10, 8, 23, '#aaaaaa')],

    'head7.dat': [(4, 8, 9, '#4a4a4a'), (5, 7, 6, '#4a4a4a'), (4, 5, 7, 8, '#ffd7be'), (4, 9, 10, 16, '#ffd7be'),
                  (5, 6, 11, 17, '#ffd7be'), (5, 25, 29, '#000000'), (4, 24, 30, '#000000'), (4, 24, 25, 5, '#efc3a6'),
                  (5, 29, 25, 20, 17, '#e7ba9a'), (4, 30, 24, 21, 16, '#e7ba9a'), (16, 15, 13, 10, '#969696'),
                  (17, 14, 12, 11, '#969696'), (15, 16, 21, 19, '#b2b2b2'), (14, 17, 20, 18, '#b2b2b2'),
                  (12, 14, 18, 19, 15, 13, 26, '#7d7d7d'), (0, 13, 10, '#e3e3e3'), (3, 12, 11, '#e3e3e3'),
                  (3, 27, 28, 0, 13, 26, 12, '#e3e3e3'), (0, 1, 10, '#969696'), (3, 2, 11, '#969696'),
                  (1, 2, 3, 27, 28, 0, '#4a4a4a'), (22, 23, 24, 25, '#dfb28e'), (21, 19, 23, 24, '#dfb28e'),
                  (18, 22, 25, 20, '#dfb28e'), (18, 19, 23, 22, '#ffd7be')],

    'head8.dat': [(6, 11, 10, '#794509'), (8, 7, 9, '#794509'), (9, 12, 13, 10, '#895109'), (9, 7, 12, '#754109'),
                  (13, 6, 10, '#754109'), (8, 3, 7, '#e7ba9a'), (0, 11, 6, '#e7ba9a'), (1, 11, 0, '#dfb28e'),
                  (8, 2, 3, '#dfb28e'), (12, 7, 6, 13, '#824d09'), (7, 17, 14, 6, '#dfb28e'), (7, 18, 17, '#c39261'),
                  (14, 15, 6, '#c39261'), (3, 19, 18, 7, '#efc3a6'), (6, 15, 16, 0, '#efc3a6'), (2, 25, 3, '#b2824a'),
                  (25, 1, 0, '#b2824a'), (2, 1, 25, '#ba8a55'), (3, 25, 24, '#ffffff'), (25, 0, 24, '#ffffff'),
                  (3, 24, 23, '#c39261'), (24, 0, 23, '#c39261'), (3, 23, 20, '#dfb28e'), (23, 0, 20, '#dfb28e'),
                  (3, 20, 5, 19, '#e7ba9a'), (0, 16, 4, 20, '#e7ba9a'), (21, 23, 22, '#ffd7be'),
                  (23, 20, 22, '#efc3a6'), (21, 22, 20, '#efc3a6'), (20, 23, 21, '#efc3a6'), (5, 4, 14, 17, '#e7ba9a'),
                  (5, 20, 4, '#e7ba9a'), (19, 5, 17, 18, '#000000'), (4, 16, 15, 14, '#000000')],

    'head9.dat': [(6, 11, 10, '#ffba00'), (8, 7, 9, '#ffba00'), (9, 12, 13, 10, '#fbae00'), (9, 7, 12, '#fbae00'),
                  (13, 6, 10, '#fbae00'), (8, 3, 7, '#e7ba9a'), (0, 11, 6, '#e7ba9a'), (1, 11, 0, '#dfb28e'),
                  (8, 2, 3, '#dfb28e'), (12, 7, 6, 13, '#fbae00'), (7, 17, 14, 6, '#dfb28e'), (7, 18, 17, '#c39261'),
                  (14, 15, 6, '#c39261'), (3, 19, 18, 7, '#efc3a6'), (6, 15, 16, 0, '#efc3a6'), (2, 25, 3, '#b2824a'),
                  (25, 1, 0, '#b2824a'), (2, 1, 25, '#ba8a55'), (3, 25, 24, '#ffffff'), (25, 0, 24, '#ffffff'),
                  (3, 24, 23, '#c39261'), (24, 0, 23, '#c39261'), (3, 23, 20, '#dfb28e'), (23, 0, 20, '#dfb28e'),
                  (3, 20, 5, 19, '#e7ba9a'), (0, 16, 4, 20, '#e7ba9a'), (21, 23, 22, '#ffd7be'),
                  (23, 20, 22, '#efc3a6'), (21, 22, 20, '#efc3a6'), (20, 23, 21, '#efc3a6'), (5, 4, 14, 17, '#e7ba9a'),
                  (5, 20, 4, '#e7ba9a'), (19, 5, 17, 18, '#000000'), (4, 16, 15, 14, '#000000')],

    'head10.dat': [(1, 2, 20, 19, '#303030'), (5, 0, 18, 17, '#303030'), (0, 16, 18, '#7d4a09'),
                   (1, 19, 15, '#7d4a09'), (24, 15, 19, '#824d09'), (16, 23, 18, '#824d09'),
                   (23, 24, 19, 18, '#824d09'), (3, 20, 2, '#592c09'), (4, 5, 17, '#592c09'), (10, 24, 23, '#653509'),
                   (10, 15, 24, '#613009'), (10, 23, 16, '#613009'), (10, 16, 0, '#5d2c09'), (10, 1, 15, '#5d2c09'),
                   (0, 11, 10, '#e3e3e3'), (10, 12, 1, '#e3e3e3'), (2, 1, 12, '#693709'), (5, 11, 0, '#693709'),
                   (5, 6, 11, '#653509'), (7, 2, 12, '#653509'), (4, 6, 5, '#303030'), (3, 2, 7, '#303030'),
                   (6, 8, 11, '#613009'), (7, 9, 12, '#613009'), (8, 21, 10, '#865109'), (8, 10, 11, '#693709'),
                   (21, 9, 10, '#865109'), (9, 12, 10, '#693709'), (4, 22, 6, '#794509'), (3, 7, 22, '#794509'),
                   (4, 3, 22, '#303030'), (6, 13, 8, '#181818'), (7, 14, 9, '#181818'), (13, 14, 21, '#4a2009'),
                   (13, 21, 8, '#4a2009'), (14, 9, 21, '#4a2009'), (6, 22, 13, '#ffffff'), (22, 14, 13, '#ffffff'),
                   (22, 7, 14, '#ffffff')],

    'head11.dat': [(0, 16, 18, '#aa7941'), (1, 19, 15, '#aa7941'), (16, 15, 19, 18, '#b2824a'),
                   (5, 0, 18, 17, '#8a590f'), (2, 20, 19, 1, '#8a590f'), (3, 20, 2, '#824d09'), (4, 5, 17, '#824d09'),
                   (10, 15, 16, '#a27135'),
                   (10, 16, 0, '#9a6928'), (10, 1, 15, '#9a6928'), (4, 3, 21, '#a27135'), (4, 21, 6, '#8a590f'),
                   (3, 7, 21, '#8a590f'), (4, 6, 5, '#865109'), (3, 2, 7, '#865109'), (7, 2, 1, '#92611c'),
                   (7, 1, 12, '#92611c'), (5, 6, 11, '#92611c'), (5, 11, 0, '#92611c'), (6, 13, 8, '#865109'),
                   (7, 14, 9, '#865109'), (13, 14, 9, 8, '#8a590f'), (7, 9, 27, 12, '#92611c'),
                   (6, 8, 26, 11, '#92611c'),
                   (11, 26, 10, '#92611c'), (27, 12, 10, '#92611c'), (6, 21, 13, '#a35500'), (21, 14, 13, '#a35500'),
                   (21, 7, 14, '#a35500'), (11, 10, 0, '#000000'), (12, 1, 10, '#000000'), (26, 27, 10, '#b2824a'),
                   (22, 23, 24, 25, '#a27135'), (8, 22, 25, 26, '#aa7130'), (23, 9, 27, 24, '#aa7130'),
                   (9, 8, 22, 23, '#865109'), (24, 27, 26, 25, '#a27135')],

    'head12.dat': [(2, 18, 17, 1, '#7d7d7d'), (5, 0, 16, 15, '#7d7d7d'), (0, 14, 16, '#969696'),
                   (1, 17, 13, '#969696'), (13, 17, 16, 14, '#969696'), (10, 13, 14, '#ffd7be'),
                   (10, 14, 21, '#f7cbb2'), (10, 22, 13, '#f7cbb2'), (3, 2, 7, '#f7cbb2'), (4, 6, 5, '#f7cbb2'),
                   (0, 21, 14, '#efc3a6'), (1, 13, 22, '#efc3a6'), (4, 5, 15, '#f7cbb2'), (3, 18, 2, '#f7cbb2'),
                   (10, 2, 1, '#dfb28e'), (5, 10, 0, '#dfb28e'), (5, 8, 10, '#e7ba9a'), (10, 9, 2, '#e7ba9a'),
                   (5, 6, 8, '#efc3a6'), (7, 2, 9, '#efc3a6'), (8, 19, 10, '#ffd7be'),
                   (9, 10, 19, '#ffd7be'), (8, 9, 19, '#c39261'), (6, 11, 8, '#dfb28e'), (12, 7, 9, '#dfb28e'),
                   (8, 11, 12, 9, '#e7ba9a'), (6, 4, 27, '#e7ba9a'), (3, 7, 26, '#e7ba9a'), (6, 20, 11, '#ffffff'),
                   (20, 12, 11, '#ffffff'), (20, 7, 12, '#ffffff'), (24, 25, 23, '#f7cbb2'), (24, 23, 27, '#efc3a6'),
                   (25, 26, 23, '#efc3a6'), (27, 23, 20, 6, '#efc3a6'), (26, 7, 20, 23, '#efc3a6'),
                   (4, 24, 27, 6, '#e7ba9a'), (25, 3, 7, 6, '#e7ba9a'), (0, 10, 21, '#00f7ef'),
                   (10, 1, 22, '#00f7ef')],

    'head13.dat': [(0, 16, 15, 11, '#f7b600'), (2, 12, 14, 13, '#f7b600'), (27, 13, 26, '#fbae00'),
                   (16, 25, 24, '#fbae00'), (11, 15, 14, 12, '#f7c300'), (22, 11, 12, 23, '#f7c300'),
                   (1, 3, 2, 13, '#c79a6d'), (1, 16, 0, 4, '#c79a6d'), (19, 23, 12, '#dfb28e'),
                   (21, 11, 22, '#dfb28e'), (20, 22, 23, '#d7aa82'), (2, 19, 12, '#cfa279'),
                   (0, 11, 21, '#cfa279'), (2, 7, 20, 19, '#d7aa82'), (8, 0, 21, 20, '#d7aa82'), (7, 8, 20, '#dfb28e'),
                   (2, 3, 5, '#cfa279'), (0, 4, 6, '#cfa279'), (5, 7, 2, '#cfa279'), (6, 0, 8, '#cfa279'),
                   (3, 9, 5, '#ae5500'), (10, 4, 6, '#ae5500'), (9, 18, 5, '#cfa279'), (18, 7, 5, '#cfa279'),
                   (18, 8, 7, '#cfa279'), (18, 6, 8, '#cfa279'), (18, 10, 6, '#cfa279'), (17, 9, 3, '#962800'),
                   (17, 18, 9, '#962800'), (17, 10, 18, '#962800'), (17, 4, 10, '#962800'), (1, 17, 3, '#d7aa82'),
                   (1, 4, 17, '#d7aa82'), (20, 23, 19, '#6d86ff'), (20, 21, 22, '#6d86ff')],

    'head14.dat': [(0, 16, 15, 11, '#b20909'), (2, 12, 14, 13, '#b20909'), (27, 2, 13, 26, '#db2c2c'),
                   (24, 25, 16, 0, '#db2c2c'), (11, 15, 14, 12, '#b20909'), (22, 11, 12, 23, '#cb1c1c'),
                   (1, 3, 2, 13, '#c79a6d'), (1, 16, 0, 4, '#c79a6d'), (19, 23, 12, '#be0f0f'),
                   (21, 11, 22, '#be0f0f'), (20, 22, 23, '#d7aa82'), (2, 19, 12, '#cfa279'),
                   (0, 11, 21, '#cfa279'), (2, 7, 20, 19, '#d7aa82'), (8, 0, 21, 20, '#d7aa82'), (7, 8, 20, '#dfb28e'),
                   (2, 3, 5, '#cfa279'), (0, 4, 6, '#cfa279'), (5, 7, 2, '#cfa279'), (6, 0, 8, '#cfa279'),
                   (3, 9, 5, '#ae5500'), (10, 4, 6, '#ae5500'), (9, 18, 5, '#cfa279'), (18, 7, 5, '#cfa279'),
                   (18, 8, 7, '#cfa279'), (18, 6, 8, '#cfa279'), (18, 10, 6, '#cfa279'), (17, 9, 3, '#962800'),
                   (17, 18, 9, '#962800'), (17, 10, 18, '#962800'), (17, 4, 10, '#962800'), (1, 17, 3, '#d7aa82'),
                   (1, 4, 17, '#d7aa82'), (20, 23, 19, '#09b66d'), (20, 21, 22, '#09b66d')]}

face_keys = faces.keys()


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.expression_index = 0
        self.point_index = 0
        self.size = 0
        self.current_full_filename = ''
        self.current_filename = ''
        self.limits = 96

        self.x_ = []
        self.y_ = []
        self.z_ = []
        self.head_data = ()
        self.head_data_copy = ()

        self.setFixedSize(700, 600)
        self.setWindowTitle('HeadEditor')
        self.center()

        main_layout = QtWidgets.QHBoxLayout()
        layout_left = QtWidgets.QVBoxLayout()

        self.figure = matplotlib.figure.Figure()  # Plot
        self.canvas = FigureCanvas(self.figure)
        self.axes = Axes3D(self.figure)

        group_box = QtWidgets.QGroupBox("Editing:")

        self.cb = QtWidgets.QComboBox()
        self.cb.currentIndexChanged.connect(self.select_change)

        slider_lim = 128
        slider_interval = 32

        self.x_slider = QtWidgets.QSlider(Qt.Horizontal)
        self.x_slider.valueChanged.connect(self.x_slider_change)
        self.x_slider.setMinimum(-slider_lim)
        self.x_slider.setMaximum(slider_lim)
        self.x_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.x_slider.setTickInterval(slider_interval)
        self.x_slider.setEnabled(False)

        self.y_slider = QtWidgets.QSlider(Qt.Horizontal)
        self.y_slider.valueChanged.connect(self.y_slider_change)
        self.y_slider.setMinimum(-slider_lim)
        self.y_slider.setMaximum(slider_lim)
        self.y_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.y_slider.setTickInterval(slider_interval)
        self.y_slider.setEnabled(False)

        self.z_slider = QtWidgets.QSlider(Qt.Horizontal)
        self.z_slider.valueChanged.connect(self.z_slider_change)
        self.z_slider.setMinimum(-slider_lim)
        self.z_slider.setMaximum(slider_lim)
        self.z_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.z_slider.setTickInterval(slider_interval)
        self.z_slider.setEnabled(False)

        self.expression_slider = QtWidgets.QSlider(Qt.Horizontal)
        self.expression_slider.valueChanged.connect(self.expression_slider_change)
        self.expression_slider.setMinimum(0)
        self.expression_slider.setMaximum(4)
        self.expression_slider.setValue(0)
        self.expression_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.expression_slider.setTickInterval(1)
        self.expression_slider.setEnabled(False)

        self.load_button = QtWidgets.QPushButton('Load', self)
        self.load_button.clicked.connect(self.load_data)

        self.save_button = QtWidgets.QPushButton('Save', self)
        self.save_button.clicked.connect(self.save_data)

        self.x_slider_label = QtWidgets.QLabel("x : 0")
        self.y_slider_label = QtWidgets.QLabel("y : 0")
        self.z_slider_label = QtWidgets.QLabel("z : 0")
        self.exp_slider_label = QtWidgets.QLabel("Expression : 1")

        hbox = QtWidgets.QVBoxLayout()
        hbox.addWidget(self.x_slider_label)
        hbox.addWidget(self.x_slider)
        hbox.addWidget(self.y_slider_label)
        hbox.addWidget(self.y_slider)
        hbox.addWidget(self.z_slider_label)
        hbox.addWidget(self.z_slider)
        hbox.addWidget(self.exp_slider_label)
        hbox.addWidget(self.expression_slider)
        hbox.addWidget(self.load_button)
        hbox.addWidget(self.save_button)
        hbox.addStretch(1)

        allitems = QtWidgets.QVBoxLayout()
        allitems.addWidget(self.cb)
        allitems.addLayout(hbox)

        group_box.setLayout(allitems)

        layout_left.addWidget(self.canvas)

        main_layout.addLayout(layout_left)
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)

        self.axes.view_init(20, 60)
        self.plot_3d()

    def select_change(self, u):
        if u != -1:
            self.point_index = u
            self.x_slider.setValue(self.x_[u])
            self.y_slider.setValue(self.y_[u])
            self.z_slider.setValue(self.z_[u])
            self.x_slider_label.setText('x : ' + str(self.x_[u]))
            self.y_slider_label.setText('y : ' + str(self.y_[u]))
            self.z_slider_label.setText('z : ' + str(self.z_[u]))

    def x_slider_change(self):
        self.x_[self.point_index] = self.x_slider.value()
        self.x_slider_label.setText('x : ' + str(self.x_slider.value()))
        self.update_data()
        self.plot_3d()

    def y_slider_change(self):
        self.y_[self.point_index] = self.y_slider.value()
        self.y_slider_label.setText('y : ' + str(self.y_slider.value()))
        self.update_data()
        self.plot_3d()

    def z_slider_change(self):
        self.z_[self.point_index] = self.z_slider.value()
        self.z_slider_label.setText('z : ' + str(self.z_slider.value()))
        self.update_data()
        self.plot_3d()

    def expression_slider_change(self):
        self.expression_index = self.expression_slider.value()
        self.exp_slider_label.setText('Expression : ' + str(self.expression_slider.value() + 1))
        self.load_face()
        self.plot_3d()

    def load_data(self):

        points = []
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "DAT file (*.dat)")

        if filename != '':

            f = open(filename[0], 'rb')

            try:

                f.seek(0, os.SEEK_END)
                self.size = f.tell()

                head, tail = os.path.split(str(filename[0]))
                self.current_full_filename = str(filename[0])
                self.current_filename = tail

                if 660 <= self.size <= 930 and self.size % 30 == 0 and tail.lower() in face_keys:

                    f.seek(0, 0)

                    with f:
                        while 1:
                            input_stream = f.read(2)
                            if not input_stream:
                                f.close()
                                break
                            points.append(struct.unpack('<h', input_stream)[0])

            finally:
                f.close()

                points_x = []
                points_y = []
                points_z = []

                for n in range(0, int(len(points) / 3)):
                    points_x.append(points[3 * n])
                    points_y.append(points[3 * n + 1])
                    points_z.append(points[3 * n + 2])

                self.head_data = (copy.copy(points_x), copy.copy(points_y), copy.copy(points_z))
                self.head_data_copy = copy.deepcopy(self.head_data)
                self.setWindowTitle('HeadEditor - Editing: ' + self.current_filename)
                self.expression_slider.setValue(0)
                self.load_face()
                self.plot_3d()

        else:

            self.show_dialog()

    def update_data(self):

        points_per_head = int(self.size / (5 * 2 * 3))
        start = self.expression_index * points_per_head

        self.head_data[0][start + self.point_index] = self.x_slider.value()
        self.head_data[1][start + self.point_index] = self.y_slider.value()
        self.head_data[2][start + self.point_index] = self.z_slider.value()

        if self.head_data != self.head_data_copy:
            self.setWindowTitle('HeadEditor - Editing: ' + self.current_filename + ' (UNSAVED)')

    def load_face(self):

        points_per_head = int(self.size / (5 * 2 * 3))
        start = self.expression_index * points_per_head
        stop = start + points_per_head

        self.x_ = copy.copy(self.head_data[0][start:stop])
        self.y_ = copy.copy(self.head_data[1][start:stop])
        self.z_ = copy.copy(self.head_data[2][start:stop])

        self.x_slider.setEnabled(True)
        self.y_slider.setEnabled(True)
        self.z_slider.setEnabled(True)
        self.expression_slider.setEnabled(True)

        if self.cb.count() > 0:
            self.cb.clear()

        for k in range(0, int(points_per_head)):
            self.cb.addItem('Point ' + str(k))

    @staticmethod
    def show_dialog():
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Unknown file or wrong filename.")
        msg.setWindowTitle("File Loading Error")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def save_data(self):

        if self.head_data_copy != self.head_data and self.current_filename != '':
            self.setWindowTitle('HeadEditor - Editing: ' + self.current_filename + ' (SAVED)')
            output_list = []
            current_head = copy.copy(self.head_data)
            for k in range(0, len(current_head[0])):

                output_list.append(current_head[0][k])
                output_list.append(current_head[1][k])
                output_list.append(current_head[2][k])
            with open(self.current_full_filename, 'wb') as f:
                for n in range(0, len(output_list)):
                    f.write(struct.pack('<h', output_list[n]))
            f.close()

        else:
            self.setWindowTitle('HeadEditor - Editing: ' + self.current_filename)

    def plot_3d(self):

        self.axes.clear()

        lim = 96

        self.axes.set_facecolor('#2c2f33')
        self.axes.set_xlim(-lim, lim)
        self.axes.xaxis.set_ticks(np.arange(-lim, lim + 1, lim / 8))
        self.axes.set_ylim(-lim, lim)
        self.axes.yaxis.set_ticks(np.arange(-lim, lim + 1, lim / 8))
        self.axes.set_zlim(-lim, lim)
        self.axes.zaxis.set_ticks(np.arange(-lim, lim + 1, lim / 8))

        self.axes.set_xlabel('x', fontsize=6, color='white')
        self.axes.set_ylabel('z', fontsize=6, color='white')
        self.axes.set_zlabel('y', fontsize=6, color='white')

        self.axes.tick_params(axis='x', colors='white', labelsize=6)
        self.axes.tick_params(axis='z', colors='white', labelsize=6)
        self.axes.tick_params(axis='y', colors='white', labelsize=6)

        self.axes.w_xaxis.set_pane_color((1, 1, 1, 0.75))
        self.axes.w_yaxis.set_pane_color((1, 1, 1, 0.75))
        self.axes.w_zaxis.set_pane_color((1, 1, 1, 0.75))

        # MAIN ROUTINE

        if self.current_filename != '':

            current_faces = faces[self.current_filename.lower()]

            for i in range(0, len(current_faces)):
                face_x = []
                face_y = []
                face_z = []
                for n in range(0, len(current_faces[i]) - 1):
                    face_x.append(self.x_[current_faces[i][n]])
                    face_y.append(self.y_[current_faces[i][n]])
                    face_z.append(self.z_[current_faces[i][n]])
                color = current_faces[i][-1]
                vertices = [list(zip(face_x, face_z, face_y))]
                self.axes.add_collection3d(Poly3DCollection(vertices, facecolors=color + 'ff', zorder=0))

            for k in range(0, len(self.x_)):
                self.axes.text3D(self.x_[k], self.z_[k], self.y_[k], str(k), color='black', fontsize=5, alpha=0.7,
                                 zorder=50)

        self.canvas.draw_idle()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
