# Optical Character Recognition (OCR) или оптическое распознавание символов
# Использовать библиотеку Tesseract.


# Импортируем библиотеки
import pytesseract
from PIL import Image

def text_filter(input_text):
    filtered_text = []  # Внутри функции создается пустой список filtered_text для хранения строк, удовлетворяющих критериям фильтрации.
    for line in input_text.split('\n'):  # Входной_текст разбивается на отдельные строки с помощью метода split('\n'). Это создаст список строк из входного текста.
                                            # Цикл for используется для итерации по каждой строке в списке строк.
        if '%' in line:  # Внутри цикла оператор if проверяет, содержит ли строка символ "%" используя условие if '%' in line.
                         # Это условие определяет, следует ли включать строку в отфильтрованный вывод.
            filtered_text.append(line)
    return '\n'.join(filtered_text)




img = Image.open("D:\Programming\Python Dev\DEV_TG_BOT_PARSER\image_check\msg-1845438530-800.jpg")  # Создаём переменную "img" и открываем файл Adom
pytesseract.pytesseract.tesseract_cmd = r"D:\Programming\Python Dev\!Programm_obj_pt\Tesseract-OCR\tesseract.exe" # Указываем для пользователя где находится приложение тессеракт


input_text = pytesseract.image_to_string(img)


filtered_output = text_filter(input_text)
print(filtered_output)
