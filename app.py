#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = QLabel("Hello world!")
    main_window.show()

    app.exec()
