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
