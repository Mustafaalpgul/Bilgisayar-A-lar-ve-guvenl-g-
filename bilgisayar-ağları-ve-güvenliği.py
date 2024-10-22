def Mustafa_(subnet_mask): # Fonksiyon oluşturduk
    # subnet mask'ın bit toplamını hesapla
    bits = subnet_mask.count('1') # 1 kaç kez tekrar ediyorsa o bits sayısıdır.
    # Host sayısını hesapla formülü
    hosts = (2 ** (32 - bits)) - 2
    return hosts # Hosts döndürdük

# Subnet maskları ve kullanılabilir host sayılarını saklamak için bir sözlük
subnet_masks = {
    "255.0.0.0": "11111111.00000000.00000000.00000000",
    "255.128.0.0": "11111111.10000000.00000000.00000000",
    "255.192.0.0": "11111111.11000000.00000000.00000000",
    "255.224.0.0": "11111111.11100000.00000000.00000000",
    "255.240.0.0": "11111111.11110000.00000000.00000000",
    "255.248.0.0": "11111111.11111000.00000000.00000000",
    "255.252.0.0": "11111111.11111100.00000000.00000000",
    "255.254.0.0": "11111111.11111110.00000000.00000000",
    "255.255.0.0": "11111111.11111111.00000000.00000000",
    "255.255.128.0": "11111111.11111111.10000000.00000000",
    "255.255.192.0": "11111111.11111111.11000000.00000000",
    "255.255.224.0": "11111111.11111111.11100000.00000000",
    "255.255.240.0": "11111111.11111111.11110000.00000000",
    "255.255.248.0": "11111111.11111111.11111000.00000000",
    "255.255.252.0": "11111111.11111111.11111100.00000000",
    "255.255.254.0": "11111111.11111111.11111110.00000000",
    "255.255.255.0": "11111111.11111111.11111111.00000000",
    "255.255.255.128": "11111111.11111111.11111111.10000000",
    "255.255.255.192": "11111111.11111111.11111111.11000000",
    "255.255.255.224": "11111111.11111111.11111111.11100000",
    "255.255.255.240": "11111111.11111111.11111111.11110000",
    "255.255.255.248": "11111111.11111111.11111111.11111000",
    "255.255.255.252": "11111111.11111111.11111111.11111100"
}

print("Subnet Mask \t Host Sayısı") # \t subnet mask ile host sayısı arasında bir boşluk bırakmak için kullanırız
# Subnet masklarını ve host sayılarını yazdır
for subnet, Mustafa in subnet_masks.items(): # subnet_masks sözlüğünün key-value değerlerini döndürüp subnet değerlerini Mikail_tali olarak aldık. onu da subnet'e attık
    hosts = Mustafa_(Mustafa) #  Mikail fonksiyonundan Mikail_tali değerlerini aldık onu da hosts sayısına attık.
    print(f"{subnet} \t {hosts}") # son olarak subnet değerlerini ve hosts sayılarını yazdırdık
