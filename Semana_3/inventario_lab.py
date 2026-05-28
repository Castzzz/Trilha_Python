#Dados do inventário
reagentes = ['Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno', 'Acetona',
'Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno', 'Etanol', 'Acetona', 'Ácido Acético', 'Etanol', 'Benzeno', 'Ácido Sulfúrico', 'Metanol', 'Ácido Acético',
'Etanol', 'Acetona', 'Tolueno', 'Ácido Sulfúrico', 'Benzeno', 'Etanol', 'Acetona',
'Metanol', 'Ácido Sulfúrico', 'Acetona', 'Ácido Acético', 'Etanol']

lotes = ['2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01',
'2023-BEN-01', '2024-ACE-01', '2023-ETA-02', '2024-SUL-01', '2023-MET-01',
'2024-TOL-01', '2023-ETA-01', '2023-ACE-01', '2023-ACA-01', '2023-ETA-02',
'2023-BEN-01', '2023-SUL-01', '2023-MET-01', '2024-ACA-01', '2023-ETA-01',
'2023-ACE-01', '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01',
'2023-ACE-01', '2023-MET-01', '2023-SUL-01', '2024-ACE-01', '2024-ACA-01',
'2023-ETA-02']

purezas = [99.5, 92.0, 99.5, 98.0, 99.9, 98.5, 96.0, 99.0, 99.0, 98.8, 99.5, 92.0, 99.2,
96.0, 99.9, 98.0, 99.0, 95.0, 99.5, 92.0, 98.8, 99.0, 99.9, 99.5, 92.0, 99.0, 98.0, 98.5,
95.0, 96.0]

#remove as duplicações de reagentes
reagentes_unicos = set(reagentes)
print("Quantidade de reagentes únicos:", len(reagentes_unicos))

#estruturação do inventário
inventario = list(zip(reagentes, lotes, purezas))

print("\nInventario organizado:\n")

#exibe o inventário organizado
for reagente, lote, pureza in inventario:
    print(f"Reagente: {reagente} | Lote: {lote} | Pureza: {pureza}%")

