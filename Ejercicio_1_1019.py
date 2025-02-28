N = int(input())

hora = N / 3600
segundos_faltantes = N % 3600
minuto = segundos_faltantes / 60
segundo = segundos_faltantes % 60

print(f"{hora}:{minuto}:{segundo}")