## Etoko - Farhan

## link: [link](farhan-dwi-etoko.pbp.cs.ui.ac.id)

### Tugas 2

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. membuat dan mengaktifkan env
2. membuat file bernama requieremnt.txt dan menginstall nya ke dalam enviroment nya
3. lalu buat project tersebut dengan perintah startproject
4. buat aplikasi bernama main dengan perintah startapp
5. Mendaftarkan aplikasi main ke dalam proyek.
6. Membuat dan Mengisi Berkas main.html agar bisa menampilkan data yang diinginkan
7. Mengubah Berkas models.py dalam Aplikasi main
8. Membuat dan Mengaplikasikan Migrasi Model dengan          makemigratons dan migrate
9. membuat logic pada views
10. merender templates html agar bisa ditampikan di browser
11. membuat superuser agar dapat mengakses dashboard admin dan membuat contoh product
12. menjalankan perintah runserver agar web dapat dilihat
13. melakukan deployment ke PWS untuk dapat diakses melalui  internet




## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Alt text](image.png)

pertama-tama user mengunjungi browser pada suatu link kemudian browser akan mengirimkan hhtp request,lalu urls pada django akan memanggil views yang berisi logika. views dapat memanggil model untuk memperoleh database.kemudian model akan mengirimkan data ke view. Lalu view akan menampilkan data dari model ke user dan menghubungkan dengan template. kemudian  template akan menampilkan tampilan antarmuka ke user yang dirender oleh views . dan terakhir views akan memberikan http respond ke browser yang berisi requested page.



 
## Jelaskan fungsi git dalam pengembangan perangkat lunak!
fungsi nya adalah sebagai sistem kontrol versi(version control system) untuk menyimpan,mengelola,dan berbagi kode
sumber secara efisien dan kolaboratif

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
karena django mudah dipahami dan memiliki alur pemrograman yang cukup mudah sehingga cocok digunakan untuk orang yang baru belajar pemrograman berbasis web

## Mengapa model pada Django disebut sebagai ORM?
Orm merupakan sebuah teknik yang digunakan dalam pemrograman untuk basis data relasional sebagai penyimpanan data yang berupa objek. Model pada django disebut sebagai ORM karena teknik pemetaan data yang memungkinkan objek dalam program berbasis objek.Model pada django adalah sebuah represntasi tabel pada database.


### Tugas 3

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?



## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?


## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?


## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

![image-xml](image-1.png)
![image-json](image-2.png)
![image-xml-id](image-3.png)
![image-json-id](image-4.png)
