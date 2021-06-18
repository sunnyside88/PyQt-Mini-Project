import PyQt5.QtWidgets as qtw
import fnmatch
#from win32com.client import Dispatch
# PyPDF2 import PdfFileReader
import os

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Try me!")

		self.setLayout(qtw.QVBoxLayout())

		my_label = qtw.QLabel("Please select directory")
		button_select = qtw.QPushButton("Select folder",
			clicked = lambda:open_file())
		button_compute = qtw.QPushButton("Compute",
			clicked = lambda:compute())
		text_box = qtw.QLineEdit(self)

		self.layout().addWidget(my_label)
		self.layout().addWidget(text_box)
		self.layout().addWidget(button_select)
		self.layout().addWidget(button_compute)
		self.show()

		def open_file():
			dialog = qtw.QFileDialog().getExistingDirectory(self, 'Select an awesome directory')
			text_box.setText(dialog)


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()