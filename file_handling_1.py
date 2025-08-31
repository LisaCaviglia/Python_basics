'''
Salva numeri e rileggili
Chiedi all’utente di inserire dei numeri.
Salvali in un file (numeri.txt).
Poi riapri il file, leggi i numeri e calcola la somma/media.
'''

def write_numbers(input_numbers):
    f = open("numbers.txt", "w")
    f.write(input_numbers)
    f.close()

def read_numbers():
    f = open("numbers.txt", "r")
    numbers = f.read()
    numbers = numbers.replace(",", " ") 
    numbers = list(map(int, numbers.split())) # Converti ogni elemento in intero
    print("Numeri:", numbers)
    print("Somma:", sum(numbers))
    print("Media:", sum(numbers) / len(numbers) if numbers else 0)
    f.close()

if __name__ == '__main__':
    input_numbers = input("Give me some numbers, when you're done, just press enter.\n")
    write_numbers(input_numbers)
    read_numbers()


