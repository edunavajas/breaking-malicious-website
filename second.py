#!/usr/bin/env python3
import requests
import random
import time
from requests.exceptions import Timeout

def generate_dni():
    """
    Generates a valid Spanish DNI.
    """
    number = random.randint(10000000, 99999999)
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    letter = letters[number % 23]
    return f"{number}{letter}"

def generate_first_name():
    """
    Generates a random first name (two parts).
    """
    first_names = ["Maria", "Jose", "Luis", "Ana", "Carmen", "Javier", "Miguel", "Isabel", "Antonio", "Laura", "Manuel", "Rosa", "Jesus", "Dolores", "Juan", "Teresa", "Pedro", "Rocio", "Francisco", "Mercedes",
                   "Elena", "Francisca", "Carlos", "Sofia", "Raul", "Miguel", "Pablo", "Diego", "Lucia", "Sergio", "Alba", "Alejandro", "Cristina", "Andres", "Eva", "Fernando", "Celia", "Alberto", "Nuria", "David"]
    return random.choice(first_names)

def generate_surname():
    """
    Generates a random surname in uppercase.
    """
    surnames = ["Garcia", "Martinez", "Lopez", "Sanchez", "Perez", "Gonzalez", "Rodriguez", "Fernandez", "Alvarez", "Gomez", "Vazquez", "Torres", 
                "Jimenez", "Ruiz", "Diaz", "Hernandez", "Moreno", "Muñoz", "Alonso", "Romero", "Navarro", "Cano", "Marin", "Castillo", "Serrano",
                "Ortega", "Nieto", "Medina", "Vidal", "Pascual", "Carrasco", "Santos", "Crespo", "Ibañez", "Calvo", "Aguilar", "Molina", "Ramos",
                "Salas", "Soto", "Vega", "Saez", "Soler", "Vila", "Mora", "Pardo", "Roca", "Gimenez", "Ferrer", "Vicente", "Moya", "Sanz", "Rey",
                "Herrero", "Arias", "Esteban", "Bravo", "Cortes", "Garrido", "Santana", "Fuentes", "Rojas", "Vargas", "Bernal", "Santiago", "Cuesta",
                "Crespo", "Carrillo", "Gallardo", "Guerrero", "Aguirre", "Cabrera", "Cuevas", "Beltran", "Cruz", "Mendez", "Guzman", "Lara", "Pacheco",
                "Paredes", "Paz", "Pineda", "Quintero", "Ramirez", "Rendon", "Rico", "Rios", "Rivera", "Robles", "Rocha", "Rojo", "Roldan", "Romero",
                "Rosales", "Rubio", "Ruiz", "Saavedra", "Salas", "Salazar", "Salgado", "Salinas", "Salvador", "Samper", "Sanchez", "Sandoval", "Santa",
                "Santacruz", "Santamaria", "Santana", "Santander", "Santiago", "Santos", "Sarabia", "Sarmiento", "Sastre", "Segura", "Sepulveda", "Serna",
                "Serrano", "Sierra", "Silva", "Simon", "Soler", "Solis", "Solorzano", "Soria", "Sosa", "Sotelo", "Suarez", "Tamayo", "Tellez", "Tena",
                "Terrazas", "Tobon", "Toledo", "Toro", "Torres", "Tovar", "Trejo", "Trujillo", "Urbina", "Urena", "Uribe", "Urrutia", "Valdes", "Valencia",
                "Valenzuela", "Valero", "Varela", "Vargas", "Varon", "Vazquez", "Vega", "Vela", "Velasco", "Velazquez", "Velez", "Vera", "Verdugo", "Verduzco",
                "Vergara", "Vicente", "Vidal", "Viera", "Vigil", "Vila", "Villa", "Villalba", "Villalobos", "Villanueva", "Villar", "Villareal", "Villaseñor",
                "Villegas", "Yanez", "Yañez", "Ybarra", "Zambrano", "Zamora", "Zamudio", "Zaragoza", "Zarate", "Zavala", "Zayas", "Zelaya", "Zepeda", "Zuniga", "Zurita"] 
    return random.choice(surnames)

def generate_email():
    """
    Generates a plausible email address based on either a first name or a surname
    with a random number appended.
    """
    domains = [
        "gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "icloud.com",
        "aol.com", "protonmail.com", "tutanota.com", "yandex.com", "zoho.com", "mail.com"
    ]
    # Decide randomly to use first name or surname
    if random.choice([True, False]):
        name_part = generate_first_name().lower()
    else:
        name_part = generate_surname().lower()
    # Append a random number between 10 and 99
    number = random.randint(10, 99)
    return f"{name_part}{number}@{random.choice(domains)}"

def generate_credit_card():
    """
    Generates a valid Visa credit card number (16 digits) using the Luhn algorithm.
    Returns the number formatted with spaces.
    """
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        total = sum(odd_digits)
        for d in even_digits:
            total += sum(digits_of(d * 2))
        return total % 10

    def calculate_check_digit(partial):
        checksum = luhn_checksum(int(partial) * 10)
        return (10 - checksum) % 10

    # Visa cards start with 4 and have 16 digits.
    partial = "4" + ''.join(random.choices("0123456789", k=14))
    check_digit = calculate_check_digit(partial)
    card_number = partial + str(check_digit)
    # Format with a space every 4 digits.
    return ' '.join(card_number[i:i+4] for i in range(0, 16, 4))

def generate_full_name():
    """
    Generates a full name with a first name and two surnames, in uppercase.
    """
    first_names = ["Maria", "Jose", "Luis", "Ana", "Carmen", "Javier", "Miguel", "Isabel", "Antonio", "Laura"]
    surnames = ["Garcia", "Martinez", "Lopez", "Sanchez", "Perez", "Gonzalez", "Rodriguez", "Fernandez", "Alvarez", "Gomez"]
    return f"{random.choice(first_names)} {random.choice(surnames)} {random.choice(surnames)}".upper()

def generate_expiry():
    """
    Generates a random expiry date in format MM/YY.
    """
    month = random.randint(1, 12)
    year = random.randint(23, 35)
    return f"{month:02d}/{year}"

def generate_cvv():
    """
    Generates a random 3-digit CVV.
    """
    return f"{random.randint(100, 999)}"

def send_post(data):
    """
    Sends a POST request with the given JSON data.
    Logs whether a 200 OK response was received.
    Returns True if the post was successful, or False if a timeout or error occurred.
    """
    url = "https://url"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es-ES,es;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://url',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://url/DGT',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Brave";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'token': '688e04660f290462c61703df747b56f690d0cd7da524b992ded9fd',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/134.0.6998.33 Mobile/15E148 Safari/604.1'
    }
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=10)
        if resp.status_code == 200:
            print(f"200 OK for key: {data['content']['key']}")
        else:
            print(f"Error {resp.status_code} for key: {data['content']['key']}")
        return True
    except Timeout:
        print(f"Timeout for key: {data['content']['key']}")
        return False
    except Exception as e:
        print(f"Error {str(e)} for key: {data['content']['key']}")
        return False

def main():
    i = 0
    while True:
        print("Cicle number: ", i)
        # Post 1: DNI (key: fullName)
        time.sleep(5)
        if not send_post({"content": {"type": "input_address", "key": "fullName", "text": generate_dni()}}):
            continue
        # Post 2: First name (key: address)
        time.sleep(5)
        if not send_post({"content": {"type": "input_address", "key": "address", "text": generate_first_name()}}):
            continue
        # Post 3: Surname (key: address2)
        time.sleep(5)
        if not send_post({"content": {"type": "input_address", "key": "address2", "text": generate_surname()}}):
            continue
        # Post 4: Email (key: email)
        time.sleep(5)
        if not send_post({"content": {"type": "input_address", "key": "email", "text": generate_email()}}):
            continue
        # Post 5: Credit card number (key: cardName)
        time.sleep(5)
        if not send_post({"content": {"type": "input_card", "key": "cardName", "text": generate_credit_card()}}):
            continue
        # Post 6: Full name (key: cardName)
        time.sleep(5)
        if not send_post({"content": {"type": "input_card", "key": "cardName", "text": generate_full_name()}}):
            continue
        # Post 7: Expiry date (key: expires)
        time.sleep(5)
        if not send_post({"content": {"type": "input_card", "key": "expires", "text": generate_expiry()}}):
            continue
        # Post 8: CVV (key: cvv)
        time.sleep(5)
        if not send_post({"content": {"type": "input_card", "key": "cvv", "text": generate_cvv()}}):
            continue
        
        i += 1
        # Wait 2 seconds before the next cycle
        time.sleep(5)

if __name__ == "__main__":
    main()
