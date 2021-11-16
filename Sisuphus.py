import sys
import os
from PyQt5 import QtWidgets # For GUI Window
import GUI #file with design description
from docxtpl import DocxTemplate
import openpyxl
from datetime import datetime # To know when catalog file was modified last time


# Window with result
class DialogApp(QtWidgets.QDialog, GUI.Ui_Dialog):
    def __init__(self, result_message, res_fname, er_ocur):
        super().__init__()
        self.setupUi(self)
        self.lblResultMessage.setText(result_message)
        self.res_fname = res_fname
        # If there was an error, button will have other purpose
        if er_ocur:
            self.btnOk.setText("OK")
            self.btnOk.clicked.connect(self.hide)
        else:
            self.btnOk.clicked.connect(self.open_folder)

    # open folder with result if there weren't any errors
    def open_folder(self):
        os.startfile(self.res_fname)
        self.hide()


# Start Window
class MainApp(QtWidgets.QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Checking if there catalog file with default name and file location
        if os.path.isfile(os.path.dirname(os.getcwd()) + "\Каталог.xlsx"):
            self.cat_name = os.path.dirname(os.getcwd()) + "\Каталог.xlsx"
        # Using back up catalog file
        else:
            self.cat_name = "Каталог_default.xlsx"
        # Initial setting
        self.res_changed = False
        self.lineEditCatalog.setText(os.path.abspath(self.cat_name))  # Initial setting
        self.btnCatalog.clicked.connect(self.browse_Catalog)  # Do browse_Catolog if button is clicked
        # Checking if there template folder with default name and location
        if os.path.exists(os.path.dirname(os.getcwd()) + "\\template"):
            self.lineEditTemplate.setText(os.path.abspath(os.path.dirname(os.getcwd()) + "\\template"))
        # Using back up template folder
        else:
            self.lineEditTemplate.setText(os.path.abspath("template_default"))
        self.btnTemplate.clicked.connect(self.browse_Template)  # Do browse_Template if button is clicked
        # Finding out when selected catalog file was modified last time
        cat_mtime = datetime.fromtimestamp(os.stat(self.cat_name).st_mtime).strftime("%d.%m.%Y_%H.%M")
        # Initial setting
        self.lineEditResult.setText(os.path.abspath(os.path.dirname(os.getcwd()) + "\\result_" + cat_mtime))
        self.btnResult.clicked.connect(self.browse_Result)  # Do browse_Result if button is clicked
        self.btnStart.clicked.connect(self.process)  # Do main body of utility

    # selecting new catalog file with usage of dialog window
    def browse_Catalog(self):
        ch_file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл Каталог", self.cat_name, " *.xls *.xlsx")
        if ch_file[0]:  # checking that User selected something
            self.lineEditCatalog.setText(ch_file[0])
            # If User hasn't selected specific folder for result saving, modify future folder name
            if not self.res_changed:
                cat_mtime = datetime.fromtimestamp(os.stat(ch_file[0]).st_mtime).strftime("%d.%m.%Y_%H.%M")
                self.lineEditResult.setText(os.path.abspath(os.path.dirname(os.getcwd()) + "\\result_" + cat_mtime))

    # selecting new folder with templates with usage of dialog window
    def browse_Template(self):
        ch_fold = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Выберите папку с шаблонами",
            os.path.dirname(self.lineEditTemplate.text())
        )
        if ch_fold:  # checking that User selected something
            self.lineEditTemplate.setText(ch_fold)

    # selecting new folder for results with usage of dialog window
    def browse_Result(self):
        ch_fold = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Выберите папку, куда сохранить результаты работы",
            os.path.dirname(self.lineEditResult.text())
        )
        if ch_fold:  # checking that User selected something
            self.lineEditResult.setText(ch_fold)
            self.res_changed = True  # Stop modifying name of folder with result when new catalog file is selected

    # main body of utility
    def process(self):
        # Reset
        self.res_changed = False
        # If selected catalog file doesn't exist prepare message for User
        if os.path.isfile(self.lineEditCatalog.text()) == False:
            result_message = "Работа утилиты прервана, т.к. указанного файл-каталога не существует"
            res_fname = ""
            er_ocur = True
        # If selected folder with templates doesn't exist prepare message for User
        elif os.path.exists(self.lineEditTemplate.text()) == False:
            result_message = "Работа утилиты прервана, т.к. указанной папки с шаблонами не существует"
            er_ocur = True
            res_fname = ""
        # If selected catalog file and folder with templates do exist
        else:
            # Reset
            er_ocur = False
            # open catalog file
            cat_name = self.lineEditCatalog.text()
            wb = openpyxl.load_workbook(cat_name, data_only=True)
            # reading time of last modification of catalog file
            content = list(map(list, wb.active.iter_rows(values_only=True)))
            # first row with meanings in catalog files will be used for tags in word document
            label_tuple = tuple(map(str, content[0]))
            # creating folder with result if necessary
            res_fname = self.lineEditResult.text()
            os.makedirs(res_fname, exist_ok=True)
            # creating set for positions which templates were not found
            joker_set = set()
            # creating new word documents according to template and catalog files
            for i in range(1, len(content)):
                #   checking that there is something for template
                if content[i][1] is None or (set(str(content[i][1]))) == {" "}:
                    content[i][1] = "None"
                #   choosing template. Template name is in a second column due to the catalog structure
                tmpl_file = self.lineEditTemplate.text() + "\\" + str(content[i][1]) + ".docx"
                # If template file wasn't found, joker template will be used
                if not os.path.isfile(tmpl_file):
                    # remembering names which templates were not found
                    joker_set.add(content[i][1])
                    if os.path.isfile(self.lineEditTemplate.text() + "\\joker.docx"):
                        tmpl_file = self.lineEditTemplate.text() + "\\joker.docx"
                    # if joker template doesn't exist in selected folder with templates using joker in
                    # back up template folder
                    else:
                        tmpl_file = "template_default\\joker.docx"
                # opening proper or joker template
                doc = DocxTemplate(tmpl_file)
                #   creating dictionary for tags replacement
                context = dict(zip(label_tuple, content[i]))
                #   tags replacement
                doc.render(context, autoescape=True)
                # checking that postfix isn't empty (first column in catalog) and saving new documents
                if content[i][0] is None or (set(str(content[i][0]))) == {" "}:
                    doc.save(res_fname + "\\" + str(str(content[i][1] + ' ' + str(i) + '.docx')))
                else:
                    doc.save(res_fname + "\\" + str(str(content[i][1] + ' ' + str(content[i][0]) + '.docx')))
            # Message for User generating
            # Show the name of folder where results were saved
            result_message = "Документы сгенерированы и сохранены в папку " + res_fname
            # if joker was used show for which templates
            if len(joker_set) > 0:
                result_message +=\
                    "\n\nДля следующих наименований не были найдены шаблоны и применялась стандартная форма:"
                for i in joker_set:
                    result_message += "\n -  \"" + i + "\""
        # call for Window with result
        window = DialogApp(result_message, res_fname, er_ocur)
        window.show()
        window.exec_()

def main():
    # call for start Window
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
