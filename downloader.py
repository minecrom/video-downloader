#!/usr/bin/env python3

import os
import sys
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

def setup_download_folder(folder_name='downloads'):
    # 1) Chemin absolu du dossier du script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 2) Nouveau dossier au même niveau
    download_dir = os.path.join(script_dir, folder_name)
    # 3) Création si besoin
    os.makedirs(download_dir, exist_ok=True)
    return download_dir

def download_from_url(url, download_dir, ydl_opts):
    # On force le dossier de sortie
    ydl_opts['outtmpl'] = os.path.join(download_dir, '%(title)s.%(ext)s')
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    # Configuration du dossier "downloads" à côté du script
    download_dir = setup_download_folder('downloads')

    # Récupération de l'URL
    if len(sys.argv) < 2:
        url = input("Entrez l'URL de la vidéo ou de la page : ").strip()
        if not url:
            sys.exit("Aucune URL fournie, sortie.")
    else:
        url = sys.argv[1]

    # Options de base (sans 'outtmpl')
    base_opts = {
        'nocheckcertificate': True,
        'retries': 3,
        'sleep_interval_requests': 2,
        'http_headers': {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/114.0.0.0 Safari/537.36'
            )
        }
    }

    # Télécharger
    try:
        download_from_url(url, download_dir, base_opts)
        print(f"✅ Fini ! Les fichiers sont dans :\n   {download_dir}")
    except DownloadError as e:
        sys.exit(f"❌ Erreur de téléchargement : {e}")

if __name__ == '__main__':
    main()
