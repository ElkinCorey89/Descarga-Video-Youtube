import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from pytube import YouTube

video_url = input("Ingresa el link del video: ")

try:
    video = YouTube(video_url)

    print(f"\nInformación del video:")
    print(f"Título: {video.title}")
    print(f"Duración: {video.length} segundos")

    print(f"\nDescargando video en la mejor calidad...")
    stream = video.streams.get_highest_resolution()
    stream.download(output_path="./Descargas")

    print("Video descargado con éxito. Revisa la carpeta './Descargas'.")
except Exception as e:
    print(f"Ocurrió un error. Vuelve a intentarlo: {e}")
