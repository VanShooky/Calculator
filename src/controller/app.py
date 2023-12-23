import sys
from typing import Union, Optional

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QListView, QVBoxLayout, QWidget
from PySide6.QtGui import QFontDatabase
from PySide6.QtCore import QStringListModel

from view.design import Ui_MainWindow

from math import sqrt, log, factorial
import numpy as np
import src.controller.config as config
from src.model.operation import Operation
import os

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.op = Operation()
        self.current_index = 0
        self.history_op = ['']
        self.history_res = []
        
        self.entry = self.ui.le_entry
        self.temp = self.ui.lbl_temp
        self.entry_max_len = self.entry.maxLength()

        QFontDatabase.addApplicationFont("ui/fonts/Rubik-Regular.ttf")

        self.connect_digit_buttons()
        self.connect_math_operations()
        self.connect_other_buttons()

        self.entry.textChanged.connect(self.adjust_entry_font_size)
        self.temp.textChanged.connect(self.adjust_temp_font_size)

    def connect_digit_buttons(self) -> None:
        for btn in config.DIGIT_BUTTONS:
            getattr(self.ui, btn).clicked.connect(self.add_digit)

    def connect_math_operations(self) -> None:
        self.ui.btn_calc.clicked.connect(self.calculate)
        for btn in config.MATH_OPERATIONS:
            getattr(self.ui, btn).clicked.connect(self.math_operation)

    def connect_other_buttons(self) -> None:
        self.ui.btn_clear.clicked.connect(self.clear_all)
        self.ui.btn_ce.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)
        self.ui.btn_neg.clicked.connect(self.negate)
        self.ui.btn_backspace.clicked.connect(self.backspace)
        self.ui.btn_in2.clicked.connect(self.calculate)
        self.ui.btn_sqrt2.clicked.connect(self.calculate)
        self.ui.btn_fact.clicked.connect(self.calculate)
        self.ui.btn_mediana.clicked.connect(self.calculate)
        self.ui.btn_otkl.clicked.connect(self.calculate)
        self.ui.pushButton_C_5.clicked.connect(self.import_data_file)
        self.ui.pushButton_C_6.clicked.connect(self.export_data_file)
        self.ui.pushButton_C_8.clicked.connect(self.undo)
        self.ui.pushButton_C_12.clicked.connect(self.repeat)
        self.ui.pushButton.clicked.connect(self.show_history_window)
        
    def import_data_file(self) -> None:
        data = []
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Text files (*.txt)")

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            with open(file_path, 'r') as file:
                data = file.read()
                float_data = str([float(x) for x in data.split(',')])[1:-1].replace(' ','')
        
        self.clear_temp_if_equality()
        self.entry.setText(float_data)
    
    def export_data_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", os.path.expanduser("~"), "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'w') as file:
                data = self.op.result
                file.write(data)
                
    def update_history(self):       
        if(self.current_index == 0):
            self.history_res.append(str(self.op.data)[1:-1])     
        if self.op.value!= 0:
            self.history_op.append(self.temp.text() + self.entry.text() + ' =')
        else: self.history_op.append(self.temp.text() + ' =')
        self.history_res.append(self.op.result)
        self.get_operation()
        self.current_index += 1
                
    def undo(self):
        if self.current_index > 0:
            self.history_op.pop(self.current_index)
            self.history_res.pop(self.current_index)
            self.current_index -= 1
            
            self.temp.setText(self.history_op[self.current_index])
            self.entry.setText(str(self.history_res[self.current_index]))
            
    def repeat(self):
        self.temp.setText(self.op.result + ' ' + self.op.math_sign + ' ')
        self.entry.setText(str(self.op.value))
        self.calculate()
        
    def set_operation(self, index):
        if self.current_index > 0:
            n = self.current_index - index
            for i in range(n):
                self.history_op.pop(self.current_index)
                self.history_res.pop(self.current_index)
                self.current_index -= 1
            
            self.temp.setText(self.history_op[self.current_index])
            self.entry.setText(str(self.history_res[self.current_index]))
        
        
    def show_history_window(self):
        self.history_dialog = QDialog()
        self.history_dialog.setWindowTitle("История операций")

        history_list = QListView()
        model = QStringListModel()
        history_list.setModel(model)
        history_list.doubleClicked.connect(lambda index: self.on_item_double_clicked(model, index))

        layout = QVBoxLayout()
        layout.addWidget(history_list)

        container = QWidget()
        container.setLayout(layout)

        self.history_dialog.setLayout(layout)

        history = []  
        for i in range(self.current_index+1):
            history.append(self.history_op[i] + '\n' + self.history_res[i] + '\n')
        
        model.setStringList(history)

        self.history_dialog.exec()
        
    def on_item_double_clicked(self, model, index):
        item_number = index.row() 
        self.set_operation(item_number)
        self.history_dialog.close()        

    def add_digit(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        btn = self.sender()

        if btn.objectName() in config.DIGIT_BUTTONS:
            if self.entry.text() == '0':
                self.entry.setText(btn.text())
            else:
                self.entry.setText(self.entry.text() + btn.text())

    def add_point(self) -> None:
        self.clear_temp_if_equality()
        self.entry.setText(self.entry.text() + '.')


    def negate(self) -> None:
        self.entry.setText(self.entry.text() + ',')

    def backspace(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        entry = self.entry.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.entry.setText('0')
            else:
                self.entry.setText(entry[:-1])
        else:
            self.entry.setText('0')

    def clear_all(self) -> None:
        self.remove_error()
        self.entry.setText('0')
        self.temp.clear()

    def clear_entry(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        self.entry.setText('0')

    def clear_temp_if_equality(self) -> None:
        if self.get_math_sign() == '=':
            self.temp.clear()

    @staticmethod
    def remove_trailing_zeros(num: Union[float, int, str]) -> str:
        n = str(float(num))
        return n.replace('.0', '') if n.endswith('.0') else n

    def add_temp(self) -> None:
        btn = self.sender()
        entry = self.entry.text()

        if not self.temp.text() or self.get_math_sign() == '=':
            self.temp.setText(entry + f' {btn.text()} ')
            self.entry.setText('0')

    def get_entry_num(self):
        entry = self.entry.text().strip('.')
        return float(entry)
    
    def get_temp_num(self):
        if self.temp.text():
            input_text = self.temp.text().split(' ')[0]
            input_data = []
            for row in input_text.split(','):
                if row != '':
                    input_data.append(float(row))                 
            return input_data

    def get_math_sign(self) -> Optional[str]:
        if self.temp.text():
            return self.temp.text().strip('.').split()[-1]
        

    def get_entry_text_width(self) -> int:
        return self.entry.fontMetrics().boundingRect(self.entry.text()).width()

    def get_temp_text_width(self) -> int:
        return self.temp.fontMetrics().boundingRect(self.temp.text()).width()
    
    def get_operation(self):
        self.op.math_sign = self.get_math_sign()
        self.op.data = self.get_temp_num()
        self.op.value = self.get_entry_num()
    
    def calculate(self) -> Optional[str]:
        self.get_operation()
        result_row = []
        for element in self.op.data:
            if self.op.math_sign == '+':
                result_row.append(round(element + self.op.value, 5))
            elif self.op.math_sign == '-':
                result_row.append(round(element - self.op.value, 5))
            elif self.op.math_sign == '*':
                result_row.append(round(element * self.op.value, 5))
            elif self.op.math_sign == '/':
                result_row.append(round(element / self.op.value, 5))
            elif self.op.math_sign == "квадрат":
                result_row.append(round(element ** 2, 5))
            elif self.op.math_sign == "степень":
                result_row.append(round(element **self.op.value, 5))
            elif self.op.math_sign == "корень":
                result_row.append(round(sqrt(element), 5))
            elif self.op.math_sign == "корень⠀степени":
                result_row.append(round(element ** (1/self.op.value), 5))
            elif self.op.math_sign == "log":
                result_row.append(round(log(element, self.op.value), 5))
            elif self.op.math_sign == "факториал":
                result_row.append(factorial(int(element)))
        if self.op.math_sign == "медиана":
            result_row.append(round(np.median(self.op.data), 5))   
        elif self.op.math_sign == "отклонение":
            result_row.append(round(np.std(self.op.data), 5)) 
            
        result = str(result_row).replace(' ','')[1:-1]   
        self.op.result = result
        self.update_history()
        if self.op.value!= 0:
            self.temp.setText(self.temp.text() + self.entry.text() + ' =')
        else: self.temp.setText(self.temp.text() + ' =')
        self.entry.setText(result)
        return result

    def show_zero_division_error(self) -> None:
        if self.get_temp_num() == 0:
            self.show_error(config.ERROR_UNDEFINED)
        else:
            self.show_error(config.ERROR_ZERO_DIV)

    def math_operation(self) -> None:
        btn = self.sender()

        if not self.temp.text():
            self.add_temp()
        else:
            if self.get_math_sign() != btn.text():
                if self.get_math_sign() == '=':
                    self.add_temp()
                else:
                    self.replace_temp_sign()
            else:
                try:
                    self.temp.setText(self.calculate() + f'{btn.text()}')
                except TypeError:
                    pass

    def replace_temp_sign(self) -> None:
        btn = self.sender()
        self.temp.setText(self.temp.text()[:-2] + f'{btn.text()} ')
        self.op.math_sign = f'{btn.text()}'

    def show_error(self, text: str) -> None:
        self.entry.setMaxLength(len(text))
        self.entry.setText(text)
        self.disable_buttons(True)

    def remove_error(self) -> None:
        if self.entry.text() in (config.ERROR_UNDEFINED, config.ERROR_ZERO_DIV):
            self.entry.setMaxLength(self.entry_max_len)
            self.entry.setText('0')
            self.disable_buttons(False)

    def disable_buttons(self, disable: bool) -> None:
        for btn in config.BUTTONS_TO_DISABLE:
            getattr(self.ui, btn).setDisabled(disable)

        color = 'color: #888;' if disable else 'color: white;'
        self.change_buttons_color(color)

    def change_buttons_color(self, css_color: str) -> None:
        for btn in config.BUTTONS_TO_DISABLE:
            getattr(self.ui, btn).setStyleSheet(css_color)

    def adjust_entry_font_size(self) -> None:
        font_size = config.DEFAULT_ENTRY_FONT_SIZE
        while self.get_entry_text_width() > self.entry.width() - 15:
            font_size -= 1
            self.entry.setStyleSheet(f'font-size: {font_size}pt; border: none;')

        font_size = 1
        while self.get_entry_text_width() < self.entry.width() - 60:
            font_size += 1

            if font_size > config.DEFAULT_ENTRY_FONT_SIZE:
                break

            self.entry.setStyleSheet(f'font-size: {font_size}pt; border: none;')

    def adjust_temp_font_size(self) -> None:
        font_size = config.DEFAULT_FONT_SIZE
        while self.get_temp_text_width() > self.temp.width() - 10:
            font_size -= 1
            self.temp.setStyleSheet(f'font-size: {font_size}pt; color: #888;')

        font_size = 1
        while self.get_temp_text_width() < self.temp.width() - 60:
            font_size += 1

            if font_size > config.DEFAULT_FONT_SIZE:
                break

            self.temp.setStyleSheet(f'font-size: {font_size}pt; color: #888;')

    def resizeEvent(self, event) -> None:
        self.adjust_entry_font_size()
        self.adjust_temp_font_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
