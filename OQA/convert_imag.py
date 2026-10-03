import re
import base64
import mimetypes
from pathlib import Path

md = Path("OQA_T1.md")  # Se cambia esto por el nombre de cada .md
texto = md.read_text(encoding="utf-8")

def convertir(match):
    alt = match.group(1)
    ruta = match.group(2)
    archivo = (md.parent / ruta).resolve()

    if not archivo.exists():
        print(f"NO ENCONTRADA: {archivo}")
        return match.group(0)

    mime = mimetypes.guess_type(archivo)[0] or "image/png"
    datos = base64.b64encode(archivo.read_bytes()).decode("utf-8")

    print(f"Convertida: {archivo.name}")
    return f"![{alt}](data:{mime};base64,{datos})"

texto = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', convertir, texto)

salida = md.with_name(md.stem + "_base64.md")
salida.write_text(texto, encoding="utf-8")

print(f"\nArchivo creado: {salida}")