"""
Setting page for travel app
"""
from tkinter import Toplevel, Scale, HORIZONTAL, font, ttk


class SettingsPage(Toplevel):
    """
    Класс страницы настроек.
    """

    def __init__(self, app):
        """
        Инициализация страницы настроек.
        :param app: приложение, к которому привязана страница настроек.
        """
        super().__init__()
        self.title("Settings")
        self.app = app

        # Задание геометрии и параметров изменения размера окна
        self.geometry("300x200")
        self.resizable(width=False, height=False)

        # Создание и упаковка фрейма
        frame = ttk.Frame(self)
        frame.pack()

        # Создание кнопки для смены темы
        theme_button = ttk.Button(frame, text="Dark/Light theme", command=self.change_theme)
        theme_button.pack()

        # Создание слайдера для изменение размера шрифта
        self.font_size_slider = Scale(frame, from_=8, to=12, orient=HORIZONTAL,
                                      command=self.change_font_size)
        self.font_size_slider.pack()

        self.available_fonts = list(font.families())
        self.font_combobox = ttk.Combobox(self, width=12, values=self.available_fonts)
        self.font_combobox.pack()

        font_button = ttk.Button(frame, text="Change Font", command=self.change_font)
        font_button.pack()

    def change_theme(self):
        """
        Изменение темы приложения.
        """
        self.app.change_theme()

    def change_font(self):
        """
        Изменение шрифта
        """
        try:
            new_font_family = self.font_combobox.get()
            self.app.change_font(new_font_family)
        except Exception as e:
            print(f"Error occurred: {e}")

    def change_font_size(self, value):
        """
        Изменение размера шрифта
        """
        try:
            new_font_size = int(value)
            self.app.change_font_size(new_font_size)
        except Exception:
            pass
