# Input data siswa
nilai_ujian = 80
kehadiran = 85

# Logika Matematika (AND)
apakah_lulus = (nilai_ujian >= 75) and (kehadiran >= 80)

# Menampilkan hasil
print("--- Status Kelulusan Siswa ---")
if apakah_lulus:
    print("Status: LULUS (True)")
else:
    print("Status: TIDAK LULUS (False)")