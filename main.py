import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QTimeEdit, QMessageBox, QDialog, QDialogButtonBox, QVBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class AlarmDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Alarm")
        self.setStyleSheet("background-color: black; color: white;")
        
        layout = QVBoxLayout()

        # Time Edit
        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat("HH:mm:ss")
        self.time_edit.setStyleSheet("font-size: 20px; color: white; background-color: black;")
        self.time_edit.setTime(QTime.currentTime())
        layout.addWidget(self.time_edit)

        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def get_time(self):
        return self.time_edit.time()

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.alarm_label = QLabel(self)
        self.timer = QTimer(self)
        self.is_paused = False
        self.is_24_hour_format = True
        self.alarm_time = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 400, 200)

        # Layouts
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px; color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;")

        self.alarm_label.setAlignment(Qt.AlignCenter)
        self.alarm_label.setStyleSheet("font-size: 20px; color: white;")
        self.alarm_label.setText("Alarm: Not Set")

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 50)
        self.time_label.setFont(my_font)

        # Buttons
        pause_button = QPushButton("Pause")
        pause_button.setStyleSheet("background-color: green; color: white;")
        pause_button.clicked.connect(self.toggle_pause)

        alarm_button = QPushButton("Set Alarm")
        alarm_button.setStyleSheet("background-color: green; color: white;")
        alarm_button.clicked.connect(self.set_alarm)

        format_button = QPushButton("AM/PM")
        format_button.setStyleSheet("background-color: green; color: white;")
        format_button.clicked.connect(self.toggle_time_format)

        # Add buttons to horizontal layout
        hbox.addWidget(pause_button)
        hbox.addWidget(alarm_button)
        hbox.addWidget(format_button)

        # Add widgets to vertical layout
        vbox.addWidget(self.alarm_label)
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        if not self.is_paused:
            time_format = "HH:mm:ss" if self.is_24_hour_format else "hh:mm:ss AP"
            current_time = QTime.currentTime().toString(time_format)
            self.time_label.setText(current_time)

            # Check for alarm
            if self.alarm_time and self.check_alarm():
                self.show_alarm_notification()

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def set_alarm(self):
        dialog = AlarmDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            alarm_time = dialog.get_time()
            self.alarm_time = alarm_time.toString("HH:mm:ss")
            self.alarm_label.setText(f"Alarm: {self.alarm_time}")

    def toggle_time_format(self):
        self.is_24_hour_format = not self.is_24_hour_format

    def check_alarm(self):
        current_time = QTime.currentTime().toString("HH:mm:ss")
        return current_time == self.alarm_time

    def show_alarm_notification(self):
        self.alarm_time = None
        self.alarm_label.setText("Alarm: Not Set")
        QMessageBox.information(self, "Alarm", "It's time!", QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

