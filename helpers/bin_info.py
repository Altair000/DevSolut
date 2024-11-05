import requests

def get_bin_info(bin_number):  # Obtiene información del BIN
    response = requests.get(f'https://lookup.binlist.net/{bin_number}')
    response.raise_for_status()  # Lanza un error si la respuesta no es 200
    bin_data = response.json()
    
    return {
        'bin': bin_number,
        'scheme': bin_data.get('scheme', 'Desconocido'),
        'type': bin_data.get('type', 'Desconocido'),
        'brand': bin_data.get('brand', 'Desconocido'),
        'bank': bin_data.get('bank', {}).get('name', 'Desconocido'),
        'country': bin_data['country']['name'],
        'alpha2': bin_data['country']['alpha2']
    }
