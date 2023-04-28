import fungsi_dasar as fd

commands = [['login', 'Untuk masuk menggunakan akun', ''],
            ['logout', 'Untuk keluar dari program dan kembali ke terminal', 'all'],
            ['summonjin', 'Untuk memanggil jin', 'bandung'],
            ['hapusjin', 'Untuk mengapus jin', 'bandung'],
            ['ubahjin', 'Untuk mengubah tipe jin', 'bandung'],
            ['bangun', 'Untuk membangun sebuah candi', 'pembangun'],
            ['batchbangun', 'Untuk mengerahkan semua jin pembangun', 'bandung'],
            ['kumpul', 'Untuk mengumpulkan bahan', 'pengumpul'],
            ['batchkumpul', 'Untuk mengerahkan semua jin pengumpul', 'bandung'],
            ['laporanjin', 'Untuk mengetahui kinerja dari para jin', 'bandung'],
            ['laporancandi', 'Untuk mengetahui progress pembangunan candi', 'bandung'],
            ['hancurkancandi', 'Untuk menghancurkan candi', 'roro'],
            ['ayamberkokok', 'Untuk menyelesaikan permainan', 'roro'],
            ['load', 'Untuk memuat data eksternal (HARUS ADAKAH? ATAU OTOMATIS?)', 'all'],
            ['save', 'Untuk menyimpan progress permainan', 'all'],
            ['help', 'Untuk menampilkan informasi ini', 'all'],
            ['exit', 'Untuk keluar permainan', 'all']]

def main(role):
    global commands
    unauthorized = 0

    print("========== HELP ==========")
    for i in range(fd.listLen(commands)):
        if commands[i][2] == role or commands[i][2] == 'all':
            print(f"{i+1-unauthorized}. {commands[i][0]}\n   {commands[i][1]}")
        else:
            unauthorized += 1

