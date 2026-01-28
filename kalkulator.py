def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("Operasi yang tersedia:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")
    
    while True:
        try:
            pilihan = input("\nPilih operasi (1-5): ")
            
            if pilihan == '5':
                print("Terima kasih telah menggunakan kalkulator!")
                break
            
            if pilihan not in ['1', '2', '3', '4']:
                print("Pilihan tidak valid!")
                continue
            
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            
            if pilihan == '1':
                hasil = angka1 + angka2
                print(f"Hasil: {angka1} + {angka2} = {hasil}")
            elif pilihan == '2':
                hasil = angka1 - angka2
                print(f"Hasil: {angka1} - {angka2} = {hasil}")
            elif pilihan == '3':
                hasil = angka1 * angka2
                print(f"Hasil: {angka1} × {angka2} = {hasil}")
            elif pilihan == '4':
                if angka2 == 0:
                    print("Error: Pembagian dengan nol!")
                else:
                    hasil = angka1 / angka2
                    print(f"Hasil: {angka1} ÷ {angka2} = {hasil}")
        
        except ValueError:
            print("Error: Masukkan angka yang valid!")
        except Exception as e:
            print(f"Terjadi error: {e}")

if __name__ == "__main__":
    kalkulator()
