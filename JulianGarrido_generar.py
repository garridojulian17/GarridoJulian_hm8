# se crea la funcion sample_1(N)que genera yRETORNANn ́umeros aleato-rios siguiendodistribuci ́on probabilidad exponencial con
def sample_1(N):
	a = [-10,-5,3,9]
	N_aleatorios = np.random.choice(a,N,replace = false,P=[0.1,0.4,0.2,0.3])
	return N_aleatorios
# se crea la funcion sample_2 
def sample_2(N):
	N_aleatorios = np.random.exponential(0.5,N)
	return N_aleatorios

# se crea la funcion de promedio
def get_mean(sampling_fun,N,M):
	promedios = []
	for i in range(0,M):
		promedios.append(np.mean(sampling_fun))
	return promedios

M = 1000
N = [10,100,1000]
#
for i in range(len(N))
	valor_a = get_mean(sample_1,N[i],M)
	np.savetxt("sample_1",valor_a, delimiter = ",")
	valor_b = get_mean(sample_2,N[i],M)
	np.savetxt("sample_1",valor_b, delimiter = ",")


	
