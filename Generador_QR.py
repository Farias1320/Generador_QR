import sys
import argparse
from urllib.parse import urlparse

try:
	import qrcode
	from PIL import Image
except Exception:
	raise SystemExit("Faltan dependencias. Instala: pip install -r requirements.txt")


def validar_url(url: str) -> bool:
	"""Valida que la cadena sea una URL con esquema http/https."""
	if not url:
		return False
	parsed = urlparse(url)
	return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def generar_qr(url: str, output: str = "qr.png", scale: int = 10) -> str:
	"""Genera un QR para la URL y lo guarda en `output`. Devuelve la ruta del archivo guardado."""
	qr = qrcode.QRCode(
		version=None,
		error_correction=qrcode.constants.ERROR_CORRECT_M,
		box_size=scale,
		border=4,
	)
	qr.add_data(url)
	qr.make(fit=True)
	img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
	img.save(output)
	return output


def main(argv=None):
	parser = argparse.ArgumentParser(description="Generador de QR desde una URL.")
	parser.add_argument("url", help="La URL que se codificará en el QR")
	parser.add_argument("-o", "--output", default="qr.png", help="Archivo PNG de salida (default: qr.png)")
	parser.add_argument("-s", "--scale", type=int, default=10, help="Escala (box_size) del QR, entero (default: 10)")

	args = parser.parse_args(argv)

	if not validar_url(args.url):
		print("URL inválida. Usa un esquema http:// o https://")
		return 2

	try:
		salida = generar_qr(args.url, args.output, args.scale)
		print(f"QR generado y guardado en: {salida}")
		return 0
	except Exception as e:
		print(f"Error al generar QR: {e}")
		return 3


if __name__ == "__main__":
	raise SystemExit(main())
