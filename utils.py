# utils.py

def format_price(price_str):
    """
    Formate le prix extrait de la page pour le convertir en float.
    """
    return float(price_str.replace('$', '').replace(',', '').strip())