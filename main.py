import glob
import os
from moviepy.editor import VideoFileClip

extension = 'mp4'  # здесь указываем нужное расширение

# Находим все файлы с указанным расширением в папке 'input'
files = glob.glob(f'input/*.{extension}')
files_to_delete = []  # Список файлов, которые будут удалены

# Обрабатываем каждый найденный видеофайл
for file_name in files:
    video = VideoFileClip(file_name)
    audio = video.audio  # Извлекаем аудиодорожку из видео
    audio_output_file = f"output/{os.path.splitext(os.path.basename(file_name))[0]}.mp3"  # Путь для сохранения аудиофайла
    audio.write_audiofile(audio_output_file)  # Сохраняем аудиофайл

    video.close()  # Закрываем объект VideoFileClip, освобождаем ресурсы
    files_to_delete.append(file_name)  # Добавляем текущий файл в список файлов для удаления

# Удаляем обработанные видеофайлы
for file_name in files_to_delete:
    if os.path.exists(file_name):
        os.remove(file_name)  # Удаляем файл
        print(f"Файл {file_name} успешно удален.")
    else:
        print(f"Файл {file_name} не найден.")