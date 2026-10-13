# Tugas Game Development - Tower of Hanoi (3 Cakram)
# Metode: A* (A-Star) Search Algorithm
# Nama : [Nama Kamu]
# NIM  : [NIM Kamu]

import heapq

# Representasi tiang
NAMA_TIANG = ['A', 'B', 'C']

# State awal dan akhir sesuai gambar soal
# Tiang A punya 3 cakram (3 paling bawah, 1 paling atas)
STATE_AWAL = ((3, 2, 1), (), ())
STATE_GOAL = ((), (), (3, 2, 1))


def hitung_heuristik(state):
    """
    Fungsi heuristik h(n):
    Menghitung berapa banyak cakram yang belum berada di tiang C (tiang tujuan).
    Makin sedikit cakram di luar tiang C, nilainya makin mendekati 0 (goal).
    """
    cakram_di_tiang_c = len(state[2])
    return 3 - cakram_di_tiang_c


def cari_langkah_valid(state):
    """
    Mencari semua kemungkinan perpindahan cakram yang sah sesuai aturan:
    1. Hanya bisa memindahkan cakram paling atas.
    2. Cakram yang lebih besar tidak boleh ditaruh di atas cakram yang lebih kecil.
    """
    tetangga = []

    for i in range(3):
        # Lewati tiang jika kosong
        if not state[i]:
            continue

        # Ambil cakram teratas dari tiang asal
        cakram = state[i][-1]

        for j in range(3):
            if i != j:
                # Boleh pindah jika tiang tujuan kosong ATAU cakram teratasnya lebih besar
                if not state[j] or state[j][-1] > cakram:
                    # Buat state baru setelah cakram dipindah
                    state_baru = [list(tiang) for tiang in state]
                    state_baru[i].pop()
                    state_baru[j].append(cakram)

                    tuple_state_baru = tuple(tuple(tiang) for tiang in state_baru)
                    keterangan = f"Pindahkan cakram {cakram} dari tiang {NAMA_TIANG[i]} ke tiang {NAMA_TIANG[j]}"
                    tetangga.append((tuple_state_baru, keterangan))

    return tetangga


def a_star_hanoi():
    """
    Algoritma A* Search:
    f(n) = g(n) + h(n)
    - g(n) : biaya/jumlah langkah yang sudah ditempuh
    - h(n) : estimasi sisa jarak ke goal (heuristik)
    """
    # Priority queue menyimpan tuple: (f_score, g_score, state, path)
    h_awal = hitung_heuristik(STATE_AWAL)
    antrian = [(h_awal, 0, STATE_AWAL, [])]

    # Menyimpan biaya terbaik yang pernah dicapai untuk tiap state
    visited = {STATE_AWAL: 0}

    while antrian:
        f_score, g_score, state_sekarang, path = heapq.heappop(antrian)

        # Cek apakah sudah mencapai goal
        if state_sekarang == STATE_GOAL:
            return path

        for state_berikutnya, langkah in cari_langkah_valid(state_sekarang):
            g_baru = g_score + 1

            # Jika state ini belum pernah dikunjungi atau dapat jalur yang lebih pendek
            if state_berikutnya not in visited or g_baru < visited[state_berikutnya]:
                visited[state_berikutnya] = g_baru
                h_baru = hitung_heuristik(state_berikutnya)
                f_baru = g_baru + h_baru
                heapq.heappush(antrian, (f_baru, g_baru, state_berikutnya, path + [langkah]))

    return []


# --- Program Utama ---
if __name__ == "__main__":
    print("=== Penyelesaian Tower of Hanoi Menggunakan Algoritma A* ===")
    print("Start  : Tiang A = [3, 2, 1], Tiang B = [], Tiang C = []")
    print("Goal   : Tiang A = [], Tiang B = [], Tiang C = [3, 2, 1]")
    print("Rumus  : f(n) = g(n) + h(n)")
    print("------------------------------------------------------------\n")

    hasil_langkah = a_star_hanoi()

    for nomor, langkah in enumerate(hasil_langkah, start=1):
        print(f"Langkah {nomor}: {langkah}")

    print(f"\nSelesai! Jalur optimal ditemukan dalam {len(hasil_langkah)} langkah.")
