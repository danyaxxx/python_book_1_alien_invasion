class Settings():
    """Класс для хранения всех настроеем игры Alien Invasion."""
    def __init__(self):
        """Инициализирукт настройки игры."""
        # Параметры экрана
        self.screen_width = 1200        # Ширина экрана
        self.screen_height = 800        # Высота экрана
        self.bg_color = (230, 230, 230) # Цвет фона

        # Настройки корабля
        self.ship_speed = 1.5
