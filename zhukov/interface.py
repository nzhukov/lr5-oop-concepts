from abc import ABC, abstractmethod

HERZEN_METEO_SERVER = 'https://meteo.herzen.spb.ru/'


class IParser(ABC):
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """

    @abstractmethod
    def get_weather_info(self, url: str, params: list[str]) -> dict:
        """
        Основной метод, который будут модифицировать декораторы.
        Должен быть реализован в конкретных компонентах.
        """
        raise NotImplementedError("Метод должен быть реализован в подклассе")
        pass


class HerzenMeteoParser(IParser):

    def __init__(self):
        self.__data = {}

    def get_weather_info(self, url: str) -> dict:
        import requests
        from bs4 import BeautifulSoup

        data = requests.get(url).text
        print(data)
        page = BeautifulSoup(data, 'html.parser')
        """<h2 id="title">27 апреля 2026 года, 12:26:38</h2>"""
        self.__data['temperature'] = float(page.find("h2", {'id': "temperature"}).get_text().split("Â")[0])
        self.__data['wind'] = str(page.find("span", {'id': 'wind'}).get_text().split(' ')[0])

        return self.__data


hmp1 = HerzenMeteoParser()
print(hmp1.get_weather_info(HERZEN_METEO_SERVER))
