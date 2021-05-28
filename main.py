# This Python file uses the following encoding: utf-8
import sys
import os
import random

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class GuessNumber(QWidget):
    def __init__(self):
        super(GuessNumber, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()
        self.ui.btn_guess.clicked.connect(self.guess)
        self.number=random.randint(1,30)
        self.chance=5
        self.score=0

    def guess(self):
        self.chance -= 1
        if self.chance>0:
            self.ui.lbl_guess.setText(str(self.chance) + ' guess is left')
            self.ui.lbl_score.setText( 'Score: '+str(self.score))
            user_guess=self.ui.nums.value()
            if int(user_guess)==self.number:
                self.ui.lbl_status.setText('You win...Guess new number')
                self.score +=1
                self.new()
            elif int(user_guess)<self.number:
                self.ui.lbl_status.setText('Go up...')
            elif int(user_guess)>self.number:
                self.ui.lbl_status.setText('Go down...')
        else:
            self.ui.lbl_status.setText('You lose...Guess new number')
            self.new()


    def new(self):
        self.number = random.randint(1, 30)
        self.chance = 5
        self.ui.lbl_guess.setText(str(self.chance) + ' guess is left')


if __name__ == "__main__":
    app = QApplication([])
    widget = GuessNumber()
    sys.exit(app.exec())
