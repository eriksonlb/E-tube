# Codigo que baixa videos do youtube
from pytube import YouTube, Playlist
from time import sleep as suspender
import sys

while True:
	print("""\033[1;32m
 _______         .___________. __    __  .______    _______ 
|   ____|        |           ||  |  |  | |   _  \  |   ____|
|  |__    ______ `---|  |----`|  |  |  | |  |_)  | |  |__   
|   __|  |______|    |  |     |  |  |  | |   _  <  |   __|  
|  |____             |  |     |  `--'  | |  |_)  | |  |____ 
|_______|            |__|      \______/  |______/  |_______|
			
				V 1.1												 \033[m""")
	print("\nOpção em vermelho não está funcionando no momento!")
	print("""
Menu:

[1] - Baixar um vídeo MP4
[2] - Baixar uma playlist MP4
\033[1;31m[3] - Baixar uma música MP3\033[m
[x] - Sair

		""")

	user = input("Faça sua escolha: ")

	if user.isnumeric():
		user = int(user)
		
		if user == 1:

			print("Opção de baixar apenas um vídeo está executando...\n")

			link = str(input("Url do vídeo: "))
			print("Buscando streams...")
			url_video = link
			yt = YouTube(url_video)

			print("\033[1;31mMostrando todas as streams disponivel para download...\n")
			print("Buscando a melhor e baixando a mesma...\033[m\n")

			for streams in yt.streams:
				print(streams)
				suspender(0.8)

			print("\033[1;32mFazendo download da stream com a melhor qualidade disponível...\033[m")
			video = yt.streams.get_highest_resolution()
			video.download()
			print("Download completo, verifique na pasta onde se encontra o script!")
			print("Voltando ao menu...")
			suspender(1.3)

		elif user == 2:
			print("Opção de baixar uma playlist está executando...\n")

			print("\033[1;31mOBS: Confira se nenhum link está quebrado para que o download ocorra corretamente!\033[m\n")
			print("\033[1;4mO que acontece se tiver um link quebrado?\033[m\n")
			print("Ele vai baixando video por vídeo, quando chegar no video")
			print("coma a url quebrada, ele para de baixar os vídeos!\n")
			input("Se entendeu dê enter para continuar\n")
			link_play = str(input("Url da playlist: "))
			PLAYLIST_URL = link_play
			playlist = Playlist(PLAYLIST_URL)
			print("\n\033[1;32mBaixando sua playlist!")
			print("Isso pode demorar um pouco...\033[m\n")
			for url in playlist:
				video = YouTube(url)
				stream = video.streams.get_highest_resolution()
				try:
					stream.download(output_path='playlist')
				except:
					pass
				else:
					pass

			print("Download Completo! Verifique na pasta!")

		elif user == 3:

			print("Opção de baixar uma música ainda não está disponível!")
			print("Ficará disponível em breve!")
			print("Voltando ao menu...")
			suspender(1.3)

		else:
			print("Opção inválida! Tente novamente.")
			suspender(0.8)

	elif user == 'X' or user == 'x':
		print("Saindo...")
		suspender(1)
		sys.exit()

	else:
		print("Opção inválida! Tente novamente.")
		suspender(0.8)
