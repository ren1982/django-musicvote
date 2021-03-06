from musicvote.models import Artist

artists = [
	Artist(artist_name="Blas Canto"),
	Artist(artist_name="Benny Cristo"),
	Artist(artist_name="Lake Malawi"),
	Artist(artist_name="Arilena Ara"),
	Artist(artist_name="Diodato"),
	Artist(artist_name="Montaigne"),
	Artist(artist_name="Samanta Tina"),
	Artist(artist_name="Bilal Hassani"),
	Artist(artist_name="S!sters"),
	Artist(artist_name="Poli Genova"),
	Artist(artist_name="Mans Zelmerlöw"),
	Artist(artist_name="John Lundvik"),
	Artist(artist_name="KEiiNO"),
	Artist(artist_name="Mahmood"),
	Artist(artist_name="Duncan Laurence"),
	Artist(artist_name="Tamara Todevska"),
	Artist(artist_name="Hatari"),
	Artist(artist_name="Kate Miller-Heidke"),
	Artist(artist_name="Tulia"),
	Artist(artist_name="Paenda"),
	Artist(artist_name="Conan Osiris"),
	Artist(artist_name="Sergey Lazarev"),
	Artist(artist_name="Chingiz"),
	Artist(artist_name="Leonora"),
	Artist(artist_name="Darude"),
	Artist(artist_name="Loreen"),
	Artist(artist_name="Lena"),
	Artist(artist_name="Michael Schulte"),
	Artist(artist_name="Benjamin Ingrosso"),
	Artist(artist_name="Netta"),
	Artist(artist_name="Eleni Foureira"),
	Artist(artist_name="Salvador Sobral"),
	Artist(artist_name="Jamala"),
	Artist(artist_name="Roman Lob"),
	Artist(artist_name="Cascada"),
	Artist(artist_name="Marco Mengoni"),
	Artist(artist_name="Francesco Gabbani"),
	Artist(artist_name="Kristian Kostov"),
	Artist(artist_name="Sunstroke Project"),
	Artist(artist_name="Jessica Mauboy"),
	Artist(artist_name="Dami Im"),
	Artist(artist_name="Guy Sebastian"),
	Artist(artist_name="Mikolas Josef"),
	Artist(artist_name="Rasmussen"),
	Artist(artist_name="Eugent Bushpepa"),
	Artist(artist_name="Vanja Radovanovic"),
	Artist(artist_name="Alexander Rybak"),
	Artist(artist_name="JOWST"),
	Artist(artist_name="Justs Sirmais"),
	Artist(artist_name="Zibbz"),
	Artist(artist_name="Luca Hänni"),
	Artist(artist_name="Levina"),
	Artist(artist_name="Conchita Wurst"),
	Artist(artist_name="Tamta"),
	Artist(artist_name="Michaela"),
]

def run():
	for artist in artists:
		print(artist.artist_name)
		artist.save()
		print("Saved")