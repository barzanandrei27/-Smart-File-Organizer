import os
import shutil

# Definirea categoriilor de fisiere in functie de extensie
ext_map = {
    "Images": [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Video": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".java"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

# Solicitare cale director
folder = input("Introduceti calea directorului ce urmeaza a fi organizat (ex: Downloads): ").strip()

if folder == "":
    folder = "."

# Rezolvare automata pentru directorul Downloads
if folder.lower() == "downloads":
    folder = os.path.join(os.path.expanduser("~"), "Downloads")

if not os.path.exists(folder):
    print(f"Eroare: Directorul specificat nu exista: {folder}")
    exit(1)

print(f"Se organizeaza directorul: {folder}")

fisiere_organizate = 0

for fisier in os.listdir(folder):
    cale_completa = os.path.join(folder, fisier)
    
    # Se ignora directoarele existente
    if os.path.isdir(cale_completa):
        continue

    _, extensie = os.path.splitext(fisier)
    extensie = extensie.lower()

    for categorie, extensii in ext_map.items():
        if extensie in extensii:
            director_destinatie = os.path.join(folder, categorie)
            
            if not os.path.exists(director_destinatie):
                os.mkdir(director_destinatie)
            
            shutil.move(cale_completa, os.path.join(director_destinatie, fisier))
            print(f"{fisier} -> {categorie}")
            fisiere_organizate += 1
            break

print(f"\nProces finalizat. Au fost organizate {fisiere_organizate} fisiere.")
