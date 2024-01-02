import matplotlib.pyplot as plt       #import package
pop_hiu = 10                          #populasi hiu
pop_tuna = 25                         #populasi tuna
kl_hiu = 2                            #laju kelahiran hiu
kl_tuna = 3                           #laju kelahiran tuna
km_hiu = 0.05                         #konstanta proporsi kematian hiu
km_tuna = 0.05                        #konstanta proporsi kematian tuna
t = 0                                 #waktu
x = [pop_tuna]                        #matriks populasi tuna dari waktu ke waktu
y = [pop_hiu]                         #matriks populasi hiu dari waktu ke waktu
waktu = [t]                           #matriks waktu
dt = 1/1000                           #laju pertumbuhan populasi hiu dan tuna
num_itr = int(14/dt)                  #banyaknya iterasi pertumbuhan populasi hiu dan tuna selama 2 minggu
for i in range (num_itr+1):           #looping pertumbuhan populasi hiu dan tuna
  pop_hiu_old = pop_hiu
  pop_hiu += (kl_hiu*pop_hiu*pop_tuna - km_hiu*pop_hiu)*dt              #model lotka volterra predator
  pop_tuna += (kl_tuna*pop_tuna - km_tuna*pop_tuna*pop_hiu_old)*dt      #model lotka volterra prey
  t+=dt
  x.append(pop_tuna)                  #memasukkan hasil pertumbuhan tuna setiap iterasi kedalam matriks
  y.append(pop_hiu)                   #memasukkan hasil pertumbuhan hiu setiap iterasi kedalam matriks
  waktu.append(t)                     #memasukkan iterasi waktu kedalam matriks waktu

num_itr_nelayan = int(21/dt)          #banyaknya iterasi pertumbuhan populasi hiu dan tuna pada minggu ke-3
for i in range (num_itr, num_itr_nelayan+1):                                            #looping pertumbuhan populasi hiu dan tuna
  if i%1000 == 0:                                                                       #kondisi ketika nelayan menangkap tuna dan hiu sekali dalam sehari (asumsi nelayan berburu sekali sehari)
    pop_hiu_old = pop_hiu
    pop_hiu = (pop_hiu + (kl_hiu*pop_hiu*pop_tuna - km_hiu*pop_hiu)*dt)*0.5             #model lotka volterra ketika nelayan mengambil 50% populasi hiu dan tuna
    pop_tuna = (pop_tuna + (kl_tuna*pop_tuna - km_tuna*pop_tuna*pop_hiu_old)*dt)*0.5    #model lotka voltera ketika nelayan mengambil 50% populasi hiu dan tuna
  else :                                                                                #kondisi ketika nelayan tidak menangkap hiu dan tuna
    pop_hiu_old = pop_hiu
    pop_hiu += (kl_hiu*pop_hiu*pop_tuna - km_hiu*pop_hiu)*dt                            #model lotka volterra
    pop_tuna += (kl_tuna*pop_tuna - km_tuna*pop_tuna*pop_hiu_old)*dt                    #model lotka volterra
  t+=dt
  x.append(pop_tuna)                  #memasukkan hasil pertumbuhan tuna setiap iterasi kedalam matriks
  y.append(pop_hiu)                   #memasukkan hasil pertumbuhan hiu setiap iterasi kedalam matriks
  waktu.append(t)                     #memasukkan iterasi waktu kedalam matriks waktu

plt.figure()                          #plotting populasi hiu terhadap waktu dan populasi tuna terhadap waktu
plt.plot(waktu, x)
plt.plot(waktu, y)
plt.grid()
plt.xlabel("Waktu")
plt.ylabel("Populasi")
plt.legend(["Populasi Tuna", "Populasi Hiu"])

plt.figure()                          #plotting populasi hiu terhadap populasi tuna
plt.plot(x,y)
plt.grid()
plt.xlabel("Populasi Tuna")
plt.ylabel("Populasi Hiu")
