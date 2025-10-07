# Generador QR
---------

Pequeño script en Python para generar un código QR a partir de una URL.

# Requisitos
---------

- Python 3.7+
- Instalar dependencias:

```powershell

# Instalar dependencias (forma segura que evita problemas con el lanzador de pip):
& '.\.venv\Scripts\python.exe' -m pip install -r '.\requirements.txt'

# Alternativa: si `pip` funciona correctamente en tu entorno puedes usar:
pip install -r requirements.txt
```

# Uso
---

```powershell
# Generar qr.png desde una URL
python Generador_QR.py "https://example.com"

# Generar con nombre personalizado
python Generador_QR.py "https://example.com" -o ejemplo.png

# Ajustar escala (tamaño de cada caja)
python Generador_QR.py "https://example.com" -o ejemplo.png -s 8
```

El script validará que la URL tenga esquema http(s) y guardará un PNG con el QR en el directorio actual.

# Licencia
-------

Código proporcionado como ejemplo para uso personal y educativo.


