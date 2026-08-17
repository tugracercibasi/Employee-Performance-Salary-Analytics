# Çalışanlarımızın bilgilerini tutacağımız ana liste (5 Çalışan)
employees = [
    {"name": "Ahmet Yilmaz", "department": "IT", "salary": 35000, "performance": 85},

    {"name": "Ayse Demir", "department": "Sales", "salary": 30000, "performance": 90},

    {"name": "Mehmet Kaya", "department": "IT", "salary": 40000, "performance": 65},
    
    {"name": "Zeynep Celik", "department": "HR",  "salary": 28000, "performance": 75},
    
    {"name": "Canan Korkmaz", "department": "Marketing", "salary": 32000, "performance": 80}
]

print(f"Toplam çalışan sayısı: {len(employees)}")
print("Güncel çalışan listesi ve ilgili detayları aşağıdadır.")

# Her çalışanı döngü ile tek tek inceleyelim
for emp in employees:
    # Performans puanını değişkene atayalım
    perf = emp["performance"]
    
    # Koşullara göre zam oranını belirleyelim
    if perf >= 85:
        raise_rate = 0.20
    elif perf >= 70:
        raise_rate = 0.15
    else:
        raise_rate = 0.10
        
    # Yeni maaşı hesaplayalım (Mevcut maaş + (Mevcut maaş * zam oranı))
    current_salary = emp["salary"]
    new_salary = current_salary + (current_salary * raise_rate)
    
    # Sonuçları ekrana yazdıralım (int kullanarak tam sayı yapıyoruz)
    print(f"Çalışan: {emp['name']} | Eski Maaş: {current_salary} TL | Yeni Maaş: {int(new_salary)} TL")

    # Departman istatistiklerini hesaplayan fonksiyonumuz
def analyze_departments(employee_list):
    # Departmanları takip etmek için boş bir sözlük oluşturalım
    dept_stats = {}
    
    for emp in employee_list:
        dept = emp["department"]
        salary = emp["salary"]
        
        # Eğer bu departman daha önce sözlüğe eklenmediyse, sıfırdan başlatalım
        if dept not in dept_stats:
            dept_stats[dept] = {"count": 0, "total_salary": 0}
            
        # O departmanın çalışan sayısını ve toplam maaşını güncelleyelim
        dept_stats[dept]["count"] += 1
        dept_stats[dept]["total_salary"] += salary
        
    print("\n--- DEPARTMAN BAZLI ANALİZ RAPORU ---")

    # Sözlük içindeki verileri ekrana yazdıralım
    for dept, stats in dept_stats.items():
        avg_salary = stats["total_salary"] / stats["count"]
        print(f"Departman: {dept} | Çalışan Sayısı: {stats['count']} | Ortalama Maaş: {int(avg_salary)} TL")

# Yazdığımız fonksiyonu çalıştıralım ve listemizi içine gönderelim
analyze_departments(employees)

# Analiz sonuçlarını bir .txt dosyasına kaydederek raporlayan fonksiyon
def save_report_to_file(employee_list, filename="employee_report.txt"):
    # Şimdi burada Türkçe karakterlerin (ş, ç, ğ, ö, ü, ı) dosyaya yazılırken bozulmasını önlemek için utf-8 encoding kullanıyoruz

    with open(filename, "w", encoding="utf-8") as file:
        file.write("--- DETAYLI CALISAN ANALIZ VE ZAM RAPORU ---\n")

        # 50 karakter uzunluğunda görsel bir ayırıcı çizgi oluşturup alt satıra geçiyoruz
        file.write("="*50 + "\n\n")
        
        for emp in employee_list:
            perf = emp["performance"]

            # Zam oranını belirleyelim
            if perf >= 85:
                rate = 0.20
            elif perf >= 70:
                rate = 0.15
            else:
                rate = 0.10
                
            new_salary = emp["salary"] + (emp["salary"] * rate)
            
            # Şimdi tüm detayları tek bir satıra sığdıralım
            file.write(f"Isim: {emp['name']:<15} | Dept: {emp['department']:<10} | "
                       f"Perf: {perf:<3} | Eski Maas: {emp['salary']:<7} | "
                       f"Zam Orani: %{int(rate*100)} | Yeni Maas: {int(new_salary)}\n")
            
    print(f"\nRapor güncellendi ve '{filename}' dosyasına kaydedildi!")

# Dosya kaydetme fonksiyonunu çalıştıralım
save_report_to_file(employees)
print("Dosya oluşturuluyor...")
print("Dosya başarıyla oluşturuldu!")

