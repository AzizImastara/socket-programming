# Client - Server (Single Thread)

Untuk membuat implementasi aplikasi Client-Server Sederhana (Single Thread) pada Python, 
dapat menggunakan modul socket dan threading yang sudah disediakan oleh Python.

Pada code yang saya berikan, server akan menunggu koneksi dari client dan membaca data yang 
dikirimkan oleh client. Kemudian, server akan mengirim balasan ke client dan menutup 
koneksi. Client akan mengirimkan pesan ke server dan menunggu balasan dari server. Setelah 
menerima balasan dari server, koneksi akan ditutup. 

Program tersebut merupakan contoh sederhana dari aplikasi client-server dengan model single
threaded, di mana server hanya mampu melayani satu koneksi pada suatu waktu. Jika 
terdapat lebih dari satu koneksi yang masuk, maka koneksi tersebut akan diantre dan dilayani 
secara berurutan. 

# How to use 

1. Buka dua terminal atau command prompt untuk menjalankan server dan client secara terpisah.
2. Jalankan server pada salah satu terminal dengan menjalankan script Python server `python server.py` atau `python 2server.py` (sesuai program yang dibutuhkan) . Ini akan memulai server dan menunggu koneksi dari client.
3. Setelah server berjalan, buka terminal atau command prompt kedua untuk menjalankan client.
4. Jalankan client pada terminal kedua dengan menjalankan script Python client `python client.py` atau `python 2client.py` (sesuai program yang dibutuhkan).
5. Setelah client berjalan, Anda akan diminta untuk memasukkan pesan. Masukkan pesan sesuai keinginan dan tekan Enter.
6. Client akan mengirim pesan ke server dan menunggu respons dari server.
7. Server akan menerima pesan, menghitung jumlah karakternya, dan mengirim kembali respons ke client.
8. Client akan menerima respons dari server dan mencetaknya di terminal atau command prompt.
9. Setelah proses selesai, server dan client akan menutup koneksi mereka masing-masing.
 
