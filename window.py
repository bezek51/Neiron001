from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel#ф-и для создания интерфейса
from PyQt5.QtGui import QPixmap#
from predict_text import pred_text, predict_path#
import sys
import os#библиотека операционка

window_a = 1000 #длинн окошка
window_h = 600 #высота окошка


class Window(QMainWindow):
    def __init__(self): #функция котороя будет настраивать окно !!! self - это название класса которое можно поменять??
        super().__init__() #эта функция ссылаеться на суперкласс
        self.setGeometry(100, 100, window_a, window_h) #рассположение надписи
        self.setWindowTitle('тестирование нейронной сети')#сама надпись
        self.img_name = None #изоброжение, фон??
        self.label_img = QLabel(self)#расположение изоброжения ??

        self.status_label = QLabel(self) #переменная которая типо вызов функции
        self.status_label.resize(500, 30) #размер клеточки в которой пишется текст
        self.status_label.move(150, 10) #рассположение текста
        self.status_label.setText('Загрузите изображение или каталог с изображениями для распознавания')#текст

        self.res_label = QLabel(self) #переменная которая типо вызов функции
        self.res_label.resize(500, 30) #размер клеточки в которой пишется текст
        self.res_label.move(200, 530) #рассположение текста

        # кнопка, вызывающая диалог для выбора картинки
        self.file_button = QPushButton(self) #переменная которая типо вызов функции
        self.file_button.resize(250, 50) #размер клеточки в которой пишется текст
        self.file_button.move(50, 640) #рассположение кнопки
        self.file_button.setText('Загрузить файл') #текст кнопки
        self.file_button.clicked.connect(self.choice_file) #при нажатии на кнопку вызов функции choice_file

        # кнопка, вызывающая диалог для каталога с картинками
        self.file_button = QPushButton(self) #переменная которая типо вызов функции
        self.file_button.resize(250, 50) #размер клеточки в которой пишется текст
        self.file_button.move(350, 640) #рассположение кнопки
        self.file_button.setText('Загрузить каталог') #текст кнопки
        self.file_button.clicked.connect(self.choice_dir) #при нажатии на кнопку вызов функции choice_dir

        # кнопка, по которой начинается распознавание
        self.file_button = QPushButton(self) #переменная которая типо вызов функции
        self.file_button.resize(250, 50) #размер клеточки в которой пишется текст
        self.file_button.move(200, 580) #рассположение кнопки
        self.file_button.setText('Распознать текст') #текст кнопки
        self.file_button.clicked.connect(self.predict) #при нажатии на кнопку вызов функции predict





    #функция для загрузки файла
    def choice_file(self):
        # открывается диалог с выбором картинки. Для удобства картинка отображается в окне приложения
        self.img_name = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        img = QPixmap(self.img_name) #переменная которая системного вызыва фцнкции
        wi, h = img.width(), img.height() #ширина и высота картинки
        img = img.scaled(int(0.1 * wi), int(0.1 * h)) #уменьшенее масштаба??
        self.label_img.setPixmap(img) #булевая переменная??
        self.label_img.resize(img.width(), img.height()) #размер клетки, берутся ширина и высота картинки, можно заменить на wi, h???
        self.label_img.move((window_a - img.width()) // 2, 50) #рассположение картинки
        self.status_label.setText('Изображение успешно загружено') #текстик
        self.res_label.setText('') # убирается текст




    # функция для загрузки католога(нескольких файлов)
    def choice_dir(self):
        # открывается диалог с выбором каталога
        self.img_name = QFileDialog.getExistingDirectory(self, 'Open folder', '/home')#загружает все в папку home??
        print(self.img_name)#ишет файл??
        self.label_img = QLabel(self)#переменная которая типо вызов функции
        self.status_label.setText(f'Выбранный каталог - {self.img_name}')#текст с выбранным именем католога
        self.res_label.setText('')



    # функция для запуска распознования неиронкой
    def predict(self):
        # Если изображение выбрано - запускается распознавание, иначе - надпись "изображение не выбрано"
        if self.img_name: #типо true
            if os.path.isfile(self.img_name):#открывается файл
                self.res_label.setText(f'Результат - {pred_text(self.img_name)}')#пишет результат из другого файла
            else:
                self.res_label.setText(f'Идёт распознавание...')# текстик
                predict_path(self.img_name)#отправляеться в другой файл
                self.res_label.setText(f'Результаты сохранены в файле results.txt')# текс, зачем f??
        else:
            self.status_label.setText("Изображение не выбрано")