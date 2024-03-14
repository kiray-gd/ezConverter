import tkinter as tk
from tkinter import filedialog

# The path can also be read from a config file, etc.
OPENSLIDE_PATH = r'C:\Users\user\AppData\Roaming\Python\Python39\site-packages\openslide\openslide-win64-20231011\bin'

import os
if hasattr(os, 'add_dll_directory'):
    # Windows
    with os.add_dll_directory(OPENSLIDE_PATH):
        import openslide
else:
    import openslide

def convert_mrxs_to_svs(mrxs_file, svs_file):
    try:
        # Открываем файл MRXS
        mrxs_slide = openslide.OpenSlide(mrxs_file)
        
        # Получаем метаданные слайда MRXS
        mrxs_properties = mrxs_slide.properties
        
        # Сохраняем файл в формате SVS
        mrxs_slide.save(svs_file, 'SVS')
        
        print("Конвертация успешно завершена!")
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")

def browse_mrxs_file():
    mrxs_file_path = filedialog.askopenfilename(filetypes=[("MRXS files", "*.mrxs")])
    mrxs_entry.delete(0, tk.END)
    mrxs_entry.insert(0, mrxs_file_path)

def browse_svs_save_location():
    svs_file_path = filedialog.asksaveasfilename(defaultextension=".svs")
    svs_entry.delete(0, tk.END)
    svs_entry.insert(0, svs_file_path)

def convert_button_clicked():
    mrxs_file_path = mrxs_entry.get()
    svs_file_path = svs_entry.get()
    convert_mrxs_to_svs(mrxs_file_path, svs_file_path)

# Создаем главное окно приложения
root = tk.Tk()
root.title("Конвертер MRXS в SVS v0.1 k_gd")

# Создаем и размещаем виджеты
mrxs_label = tk.Label(root, text="Выберите файл MRXS:")
mrxs_label.grid(row=0, column=0, padx=5, pady=5)

mrxs_entry = tk.Entry(root, width=50)
mrxs_entry.grid(row=0, column=1, padx=5, pady=5)

mrxs_button = tk.Button(root, text="Обзор", command=browse_mrxs_file)
mrxs_button.grid(row=0, column=2, padx=5, pady=5)

svs_label = tk.Label(root, text="Выберите место сохранения файла SVS:")
svs_label.grid(row=1, column=0, padx=5, pady=5)

svs_entry = tk.Entry(root, width=50)
svs_entry.grid(row=1, column=1, padx=5, pady=5)

svs_button = tk.Button(root, text="Обзор", command=browse_svs_save_location)
svs_button.grid(row=1, column=2, padx=5, pady=5)

convert_button = tk.Button(root, text="Конвертировать", command=convert_button_clicked)
convert_button.grid(row=2, column=1, padx=5, pady=5)

# Запускаем главный цикл приложения
root.mainloop()