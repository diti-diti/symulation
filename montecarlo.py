import numpy as np

# Parametry bazowe
ukraina_siły = np.array([1155, 14372, 783, 658, 319])  # Czołgi, pojazdy bojowe, artyleria samobieżna, artyleria holowana, MLRS
rosja_siły = np.array([10000, 25000, 5000, 3500, 3000])  # Czołgi, pojazdy bojowe, artyleria samobieżna, artyleria holowana, MLRS
liczba_symulacji = 10000

# Zakres wsparcia
wsparcie_start = 1.2
wsparcie_stop = 1.9
wsparcie_krok = 0.01 

wyniki = []

for wsparcie in np.arange(wsparcie_start, wsparcie_stop + wsparcie_krok, wsparcie_krok):
    wsparcie_ukraina = np.random.uniform(wsparcie, wsparcie, liczba_symulacji)
    wsparcie_rosja = np.random.uniform(1.0, 1.0, liczba_symulacji)
    zmienność_ukraina = np.random.uniform(0.9, 1.7, liczba_symulacji)
    zmienność_rosja = np.random.uniform(0.9, 1.0, liczba_symulacji)
    
    wyniki_ukraina = 0
    wyniki_rosja = 0
    
    for i in range(liczba_symulacji):
        ukraina_efektywność = (ukraina_siły * wsparcie_ukraina[i] * zmienność_ukraina[i]).sum()
        rosja_efektywność = (rosja_siły * wsparcie_rosja[i] * zmienność_rosja[i]).sum()
        
        if ukraina_efektywność > rosja_efektywność:
            wyniki_ukraina += 1
        elif ukraina_efektywność < rosja_efektywność:
            wyniki_rosja += 1

    procent_zwycięstw_ukrainy = wyniki_ukraina / liczba_symulacji * 100
    procent_zwycięstw_rosji = wyniki_rosja / liczba_symulacji * 100
    
    wyniki.append((wsparcie, procent_zwycięstw_ukrainy, procent_zwycięstw_rosji))

for wsparcie, ukraina, rosja in wyniki:
    print(f"Wsparcie: {wsparcie:.1f}, Zwycięstwa Ukrainy: {ukraina:.2f}%, Zwycięstwa Rosji: {rosja:.2f}%")
