import arrr
from pyscript import document


def translate(text):
    # Define the Egyptian cipher mapping
    cipher_mapping = {
        'A': '𓀀', 'B': '𓁹', 'C': '𓃀', 'D': '𓃭', 'E': '𓆑',
        'F': '𓏏', 'G': '𓏭', 'H': '𓐔', 'I': '𓆑', 'J': '𓊃',
        'K': '𓊹', 'L': '𓋴', 'M': '𓎛', 'N': '𓏭', 'O': '𓏭',
        'P': '𓏌', 'Q': '𓇋', 'R': '𓅆', 'S': '𓂋', 'T': '𓍯',
        'U': '𓅃', 'V': '𓅓', 'W': '𓇓', 'X': '𓊪', 'Y': '𓎡',
        'Z': '𓃭', ' ': ' ',
    }
    
    translated_text = ''.join(cipher_mapping.get(char.upper(), char) for char in text)
    
    return translated_text



def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value

    
    output_div = document.querySelector("#output")
    # output_div.innerText = arrr.translate(english)
    output_div.innerText = translate(english)
