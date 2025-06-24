city = str(input('Digite a cidade que mais gostou de conhecer: '))

city = city.strip().split()[0].lower()

print(f'A cidade começa com Santo? {"santo" in city}')