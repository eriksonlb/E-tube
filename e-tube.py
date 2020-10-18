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
															 \033[m""")
	print("\nOpção em vermelho não está funcionando no momento!")
	print("""
Menu:

[1] - Baixar um vídeo MP4
\033[1;31m[2] - Baixar uma playlist MP4\033[m
\033[1;31m[3] - Baixar uma música MP3\033[m
[x] - Sair

		""")

	user = input("Faça sua escolha: ")

	if user.isnumeric():
		user = int(user)
		
		if user == 1:

			print("Opção de baixar apenas um vídeo está executando...")

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

			print("Opção de baixar uma playlist ainda não está disponível!")
			print("Ficará disponível em breve!")
			print("Voltando ao menu...")
			suspender(1.3)


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
