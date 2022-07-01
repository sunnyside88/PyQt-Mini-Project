import PyQt5.QtWidgets as qtw
import json
from  page_counter import PageCounter


class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Try me!")

		self.setLayout(qtw.QVBoxLayout())
		self.components = {
			"my_label": qtw.QLabel("Please select directory"),
			"button_select": qtw.QPushButton("Select folder",clicked = self.open_file),
			"button_compute": qtw.QPushButton("Compute",clicked=self.compute),
			"text_box": qtw.QLineEdit(self),
			'result_box':qtw.QMessageBox(self),
		}
		for (name,com) in self.components.items():
			self.layout().addWidget(com)
		self.show()
		self.directory = None

	def open_file(self):
		dialog = qtw.QFileDialog().getExistingDirectory(self, 'Select an awesome directory')
		self.components['text_box'].setText(dialog)
		self.directory = dialog
	
	def compute(self):
		# print('Computing from %s' % self.directory)
		filesDict = PageCounter.count_pdf(self.directory)
		if len(filesDict)>0:
			self.components['result_box'].about(self,"Result",json.dumps(filesDict))
		else:
			self.components['result_box'].about(self,"Result","No PDF files found")
app = qtw.QApplication([])
mw = MainWindow()

app.exec_()