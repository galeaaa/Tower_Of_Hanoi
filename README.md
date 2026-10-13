# Tugas 3 - Game Development: Tower of Hanoi (A* Search Algorithm)

- **Nama**: [Galea Violet]
- **NIM**: [20240801104]
- **Mata Kuliah**: Game Development

---

## Deskripsi Tugas
Membuat program (code snippet) untuk menyelesaikan permainan **Tower of Hanoi** dengan 3 cakram (piringan) dari **tiang A (Start)** menuju **tiang C (Finish)** dengan perantara **tiang B**.

Pada tugas ini, penyelesaian diimplementasikan menggunakan pendekatan **Game AI / State Space Search** dengan **Algoritma A\* (A-Star)**.

---

## Konsep & Algoritma

Dalam pengembangan game (Game Development), teka-teki Tower of Hanoi dimodelkan sebagai permasalahan **ruang keadaan (*State Space Search*)**:

1. **State (Kondisi Tiang)**:
   - Posisi cakram pada ketiga tiang direpresentasikan dalam bentuk susunan angka: `(Tiang A, Tiang B, Tiang C)`.
   - Angka 3 mewakili cakram terbesar, 2 sedang, dan 1 terkecil.
   - **Start State**: `((3, 2, 1), (), ())`
   - **Goal State**: `((), (), (3, 2, 1))`

2. **Valid Actions (Aturan Perpindahan)**:
   - Mengambil cakram teratas dari salah satu tiang.
   - Hanya boleh ditaruh di tiang kosong atau di atas cakram yang ukurannya lebih besar.

3. **Fungsi Evaluasi A\* ($f(n) = g(n) + h(n)$)**:
   - **$g(n)$ (Actual Cost)**: Jumlah langkah perpindahan yang sudah ditempuh dari titik awal.
   - **$h(n)$ (Heuristic)**: Estimasi sisa jarak ke kondisi akhir. Pada program ini dihitung dari **berapa banyak cakram yang belum berada di tiang C**. Makin banyak cakram di tiang C, nilai heuristik semakin mendekati 0.
   - **$f(n)$**: Total perkiraan biaya yang digunakan antrian prioritas (*Priority Queue*) untuk memilih langkah terbaik berikutnya.

### Hubungan A* dengan Dijkstra & Greedy:
- **Dijkstra**: Hanya memperhitungkan biaya tempuh sejauh ini ($f = g$), tanpa memperkirakan arah tujuan.
- **Greedy Best-First**: Hanya memperhitungkan perkiraan jarak ke tujuan ($f = h$), sehingga kadang tidak menemukan langkah terpendek.
- **A\***: Menggabungkan keduanya ($f = g + h$), sehingga dijamin menemukan rute perpindahan yang paling optimal (minimum langkah).

---

## Output Program

Program berhasil menemukan jalur optimal sebanyak **7 langkah**:

```
=== Penyelesaian Tower of Hanoi Menggunakan Algoritma A* ===
Start  : Tiang A = [3, 2, 1], Tiang B = [], Tiang C = []
Goal   : Tiang A = [], Tiang B = [], Tiang C = [3, 2, 1]
Rumus  : f(n) = g(n) + h(n)
------------------------------------------------------------

Langkah 1: Pindahkan cakram 1 dari tiang A ke tiang C
Langkah 2: Pindahkan cakram 2 dari tiang A ke tiang B
Langkah 3: Pindahkan cakram 1 dari tiang C ke tiang B
Langkah 4: Pindahkan cakram 3 dari tiang A ke tiang C
Langkah 5: Pindahkan cakram 1 dari tiang B ke tiang A
Langkah 6: Pindahkan cakram 2 dari tiang B ke tiang C
Langkah 7: Pindahkan cakram 1 dari tiang A ke tiang C

Selesai! Jalur optimal ditemukan dalam 7 langkah.
```