import sys, requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        
        self.setStyleSheet("""
                           QLabel, QPushButton{
                               font-family: Calibri
                           }
                           QLabel#city_label {
                               font-size: 40px;
                               font-weight: bold;
                           }
                           QLineEdit#city_input {
                               font-size: 40px;
                               border: 1px solid #000;
                               border-radius: 5px;
                           }
                           QPushButton#get_weather_button {
                               font-size: 30px;
                               font-weight: bold;
                               min-height: 50px;
                           }
                           QLabel#temperature_label {
                               font-size: 75px;
                               font-weight: bold;
                           }
                           QLabel#emoji_label {
                               font-size: 100px;
                               font-family: Segoe UI emoji;
                           }
                           QLabel#description_label {
                               font-size: 50px;
                               font-weight: bold;
                               margin-top: 20px;
                           }
                           """)
        
        self.get_weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        API_KEY = "YOUR_API_KEY"
        
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        
        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()
            if data["cod"] == 200:
                self.display_weather(data)
                
        except requests.exceptions.HTTPError as http_error:
            # print(f"Status code: {res.status_code} --> Not found the city has name: {city}")
            match res.status_code:
                case 400:
                    self.display_error(f"Bad request: {res.status_code}\nPlease check your input")
                case 401:
                    self.display_error(f"Unauthorized: {res.status_code}\nInvalid API")
                case 403:
                    self.display_error(f"Forbidden: {res.status_code}\nAccess is denied")
                case 404:
                    self.display_error(f"Not found: {res.status_code}\nNot found city: {city}")
                case 500:
                    self.display_error(f"Internal server error: {res.status_code}\nPlease try again later")
                case 502:
                    self.display_error(f"Bad gateway: {res.status_code}\nInvalid response from the server")
                case 503:
                    self.display_error(f"Service unavailable: {res.status_code}\nServer is down")
                case 504:
                    self.display_error(f"Gateway timeout: {res.status_code}\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred\n{http_error}")
        except requests.exceptions.ConnectionError:
            print(f"Connection error\nPlease check your connection") 
        
        except requests.exceptions.Timeout:
            print(f"Timeout error\nPlease try again later")
        
        except requests.exceptions.TooManyRedirects:
            print(f"Too many redirects\nPlease check the URL")
            
        except requests.exceptions.RequestException as req_error:
            print(f"Request Error:\n{req_error}")
        
    
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
    
    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        kelvin_temp = data["main"]["temp"]
        celsius_temp = kelvin_temp - 273.15
        fahrenheit_temp = (kelvin_temp * 9 / 5) - 459.67
        
        weather_id = data["weather"][0]["id"]
        weather_desc = data["weather"][0]["description"]
        
        print(data)
        
        self.temperature_label.setText(f"{celsius_temp:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(f"{weather_desc}")
        
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🌨️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
