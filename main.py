import requests
from bs4 import BeautifulSoup
import random
import time
import logging
import gzip
import brotli

# Configuración de logs
logging.basicConfig(
    filename='script.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuración general (CENSURADO)
URL_BASE = "https://example.com"  # URL censurada
COOKIES = {
    "cf_clearance": "CENSURADO",
    "PHPSESSID": "CENSURADO"
}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/133.0.6943.120 Mobile/15E148 Safari/604.1",
    "Accept-Language": "es-ES,es;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Content-Type": "application/x-www-form-urlencoded"
}
BALANCES = [
    "Entre 1000Є y 1500Є",
    "Entre 1500Є y 4890Є",
    "Entre 4890Є y 7020Є",
    "Entre 7020Є y 9100Є",
    "Más de 9100Є"
]
DNI_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

# Descomprimir contenido según el tipo de encoding
def descomprimir_contenido(response):
    encoding = response.headers.get('Content-Encoding', '')
    contenido = response.content

    try:
        if encoding == 'gzip':
            contenido = gzip.decompress(contenido)
        elif encoding == 'br':
            contenido = brotli.decompress(contenido)
        else:
            contenido = contenido.decode('utf-8')
        return contenido
    except Exception as e:
        logging.error(f"Error al descomprimir: {e}")
        return None

# Obtener CSRF Token
def get_csrf_token(url):
    response = requests.get(url, headers=HEADERS, cookies=COOKIES)
    logging.info(f"GET {url} - Status: {response.status_code}")
    
    if response.status_code == 200:
        html_text = descomprimir_contenido(response)
        if html_text:
            soup = BeautifulSoup(html_text, 'html.parser')
            token = soup.find('input', {'name': 'csrf_token'})
            if token:
                return token['value']
    return None

# Generar DNI aleatorio
def get_dni():
    number = random.randint(10000000, 99999999)
    letter_index = number % 23
    letter = DNI_LETTERS[letter_index]
    dni = f"{number}{letter}"
    return dni

# Generar contraseña aleatoria
def get_random_pass():
    length = random.randint(4, 8)
    password = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return password

# Generar número de teléfono aleatorio
def get_random_phone():
    phone = "6" + ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return phone

# Obtener balance aleatorio
def get_random_balance():
    balance = random.choice(BALANCES)
    return balance

# Enviar datos de login
def post_login(csrf_token, user, password):
    url = f"{URL_BASE}/login"
    data = {
        "csrf_token": csrf_token,
        "step": "login",
        "user": user,
        "pass": password
    }
    
    try:
        response = requests.post(url, headers=HEADERS, cookies=COOKIES, data=data)
        logging.info(f"POST Login - Status: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Error en la solicitud POST Login: {e}")
    
    return response

# Confirmación de teléfono
def post_phone_confirmation(csrf_token, phone):
    url = f"{URL_BASE}/phone_confirmation"
    data = {
        "csrf_token": csrf_token,
        "step": "phone",
        "phone": phone
    }
    response = requests.post(url, headers=HEADERS, cookies=COOKIES, data=data)
    logging.info(f"POST Confirmación de Teléfono - Status: {response.status_code}")
    return response

# Enviar balance
def post_balance(csrf_token, balance):
    url = f"{URL_BASE}/balance"
    data = {
        "csrf_token": csrf_token,
        "step": "balance",
        "balance": balance
    }
    response = requests.post(url, headers=HEADERS, cookies=COOKIES, data=data)
    logging.info(f"POST Balance - Status: {response.status_code}")
    return response

# Ejecutar el script en bucle
def loop_script(veces):
    for i in range(veces):
        logging.info(f"--- Iteración {i+1} ---")
        
        # Obtener CSRF Token
        csrf_token = get_csrf_token(f"{URL_BASE}/login")
        if not csrf_token:
            logging.error("No se pudo obtener el CSRF Token.")
            continue
        
        # Datos de Login
        user = get_dni()
        password = get_random_pass()
        
        # POST Login
        post_login(csrf_token, user, password)
        
        # Segundo CSRF para confirmación de teléfono
        csrf_token = get_csrf_token(f"{URL_BASE}/phone_confirmation")
        if not csrf_token:
            logging.error("No se pudo obtener el CSRF Token para confirmación de teléfono.")
            continue
        
        # Confirmación de Teléfono
        phone = get_random_phone()
        post_phone_confirmation(csrf_token, phone)
        
        # Tercer CSRF para balance
        csrf_token = get_csrf_token(f"{URL_BASE}/balance")
        if not csrf_token:
            logging.error("No se pudo obtener el CSRF Token para balance.")
            continue
        
        # Enviar Balance
        balance = get_random_balance()
        post_balance(csrf_token, balance)
        
        # Pausa entre iteraciones
        time.sleep(random.randint(2, 5))

if __name__ == "__main__":
    loop_count = 100
    loop_script(loop_count)
