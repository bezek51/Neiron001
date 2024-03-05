from ultralytics import YOLO
from PIL import Image
import os

model_cut = YOLO('training_files/best.pt')
model_numbers = YOLO('training_files/labels.pt')



#функция для вырезания картинки
def cut_img(img):
    res = model_cut.predict(img) # что за predict??
    img = Image.open(img) #открываем картинку
    if res:
        if res[0]: #если перваый
            box = [int(float(elem)) for elem in res[0].boxes.xyxy[0]] #elem что за переменная?
            img = img.crop(box)#вырезанная картинка с координатами переносится в box
    return

#функция для определния текста на картинке
def text_definition(img):
    img_good = cut_img(img)#с помощью функции cut_img вырезаем картинку
    res = model_numbers.predict(img_good) #почему разные фаилы используются в разных функциях, нельзя один и тот же?
                                          #и как определить какой именно файл нужно брать или без разницы?
    arr = [] #результаты идут в массив (класс, х лев.верх.угл, у прав.ниж.угл)
    for i in range(sum([1 for k in res[0].boxes.xyxy])):#зачем еденица?
        arr.append((int(res[0].boxes.cls[i]), (float(res[0].boxes.xyxy[i][0]) // 75,
                                               float(res[0].boxes.xyxy[i][1]) // 75)))
        #что за cls, boxes какая то функция??, почему именно 75, параметры картинки в окне??

    return ''.join([str(elem[0]) for elem in sorted(arr, key = lambda x: (x[1][0], 0 - x[1][1]))])
    #key = lambda x: (x[1][0], 0 - x[1][1]) - кей это какая то спецю фу-я??


def reserch_img(dir_path):
    #фу-я делает ресёрч по изображениям в папке и сохраняющая результаты в текстовый файл
    f = open('result.txt', 'w')
    for file in os.listdir(dir_path):
        if os.path.isfile(f'{dir_path}/{file}'):
            f.write(file + '' + text_definition(f'{dir_path}/{file}') + '\n')
    f.close()


if __name__ == '__main__':
    # код запрашивает папку с изображениями, в выбранной папке проходит по изображениям и распознаёт их
    print('Введите папку с изображнием')
    path = input()
    reserch_img(path)
    print('\nРезультаты сохранены в файле results.txt')



