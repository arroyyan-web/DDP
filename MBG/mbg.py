import streamlit as st

if "nama" not in st.session_state:
    st.session_state.nama = ""
    
if "jenis_kelamin" not in st.session_state:
    st.session_state.jenis_kelamin = ""
    
if "usia" not in st.session_state:
    st.session_state.usia = ""


def tampilkan_menu_makanan(list_makanan):
    st.write("**Komposisi Menu:**")
    
    for item in list_makanan:
        nama_makanan = item[0]
        jumlah = item[1]
        st.write(f"- {nama_makanan} ({jumlah})")


def tampilkan_info_gizi(kalori, protein, lemak, karbohidrat):
    st.write("**Informasi Gizi:**")
    st.write(f"Kalori: {kalori} kal")
    st.write(f"Protein: {protein} gram")
    st.write(f"Lemak: {lemak} gram")
    st.write(f"Karbohidrat: {karbohidrat} gram")

menu_pr_sarapan_nama = "Nasi Kuning + Ikan"
menu_pr_sarapan_list = [
    ["Nasi kuning", "100 gram"],
    ["Ikan kembung goreng", "90 gram"],
    ["Tumis kacang panjang", "75 gram"],
    ["Jeruk", "1 buah"]
]
menu_pr_sarapan_kalori = 372
menu_pr_sarapan_protein = 20
menu_pr_sarapan_lemak = 13
menu_pr_sarapan_karbo = 86

menu_pr_siang_nama = "Nasi Merah + Ayam"
menu_pr_siang_list = [
    ["Nasi merah", "100 gram"],
    ["Dada ayam panggang", "100 gram"],
    ["Sayur brokoli", "50 gram"],
    ["Pisang", "75 gram"]
]
menu_pr_siang_kalori = 297
menu_pr_siang_protein = 36
menu_pr_siang_lemak = 5
menu_pr_siang_karbo = 49

menu_pr_malam_nama = "Nasi Putih + Sup"
menu_pr_malam_list = [
    ["Nasi putih", "100 gram"],
    ["Sup sayuran", "150 gram"],
    ["Tempe", "50 gram"],
    ["Yogurt", "60 gram"]
]
menu_pr_malam_kalori = 318
menu_pr_malam_protein = 18
menu_pr_malam_lemak = 10
menu_pr_malam_karbo = 57

menu_pd_sarapan_nama = "Nasi Jagung + Ikan"
menu_pd_sarapan_list = [
    ["Nasi jagung", "100 gram"],
    ["Tumis daun pepaya", "100 gram"],
    ["Ikan cakalang", "45 gram"],
    ["Pisang", "50 gram"]
]
menu_pd_sarapan_kalori = 343
menu_pd_sarapan_protein = 21
menu_pd_sarapan_lemak = 6
menu_pd_sarapan_karbo = 55

menu_pd_siang_nama = "Nasi + Telur"
menu_pd_siang_list = [
    ["Nasi putih", "100 gram"],
    ["Telur dadar", "50 gram"],
    ["Daun ubi rebus", "150 gram"],
    ["Semangka", "100 gram"]
]
menu_pd_siang_kalori = 273
menu_pd_siang_protein = 14
menu_pd_siang_lemak = 6
menu_pd_siang_karbo = 42

menu_pd_malam_nama = "Nasi + Kerang"
menu_pd_malam_list = [
    ["Nasi putih", "100 gram"],
    ["Kerang kuah asam", "150 gram"],
    ["Sayur bayam", "100 gram"],
    ["Jeruk", "100 gram"]
]
menu_pd_malam_kalori = 287
menu_pd_malam_protein = 18
menu_pd_malam_lemak = 3
menu_pd_malam_karbo = 48

menu_lr_sarapan_nama = "Gandum + Susu"
menu_lr_sarapan_list = [
    ["Gandum", "100 gram"],
    ["Susu", "200 ml"],
    ["Pisang", "50 gram"]
]
menu_lr_sarapan_kalori = 515
menu_lr_sarapan_protein = 21
menu_lr_sarapan_lemak = 10
menu_lr_sarapan_karbo = 93

menu_lr_siang_nama = "Nasi + Ayam + Brokoli"
menu_lr_siang_list = [
    ["Nasi", "100 gram"],
    ["Ayam panggang", "40 gram"],
    ["Tumis brokoli", "100 gram"]
]
menu_lr_siang_kalori = 275
menu_lr_siang_protein = 18
menu_lr_siang_lemak = 7
menu_lr_siang_karbo = 35

menu_lr_malam_nama = "Nasi + Ayam Goreng"
menu_lr_malam_list = [
    ["Nasi putih", "100 gram"],
    ["Ayam goreng", "70 gram"],
    ["Sup kimlo", "60 gram"],
    ["Pisang", "75 gram"]
]
menu_lr_malam_kalori = 594
menu_lr_malam_protein = 14
menu_lr_malam_lemak = 25
menu_lr_malam_karbo = 100


menu_ld_sarapan_nama = "Nasi + Cumi"
menu_ld_sarapan_list = [
    ["Nasi", "100 gram"],
    ["Cumi saus pedas", "50 gram"],
    ["Tumis oncom", "50 gram"]
]
menu_ld_sarapan_kalori = 372
menu_ld_sarapan_protein = 20
menu_ld_sarapan_lemak = 13
menu_ld_sarapan_karbo = 86

menu_ld_siang_nama = "Bihun Goreng + Ayam"
menu_ld_siang_list = [
    ["Bihun goreng sayur", "230 gram"],
    ["Ayam goreng", "70 gram"],
    ["Pisang", "75 gram"]
]
menu_ld_siang_kalori = 593
menu_ld_siang_protein = 12
menu_ld_siang_lemak = 19
menu_ld_siang_karbo = 93

menu_ld_malam_nama = "Nasi + Pecel"
menu_ld_malam_list = [
    ["Nasi putih", "100 gram"],
    ["Pecel sayur", "120 gram"],
    ["Telur dadar", "60 gram"],
    ["Jeruk", "110 gram"]
]
menu_ld_malam_kalori = 683
menu_ld_malam_protein = 19
menu_ld_malam_lemak = 21
menu_ld_malam_karbo = 105


st.sidebar.header("Menu Navigasi")
pilihan_halaman = st.sidebar.radio(
    "Pilih Halaman:",
    ["Data Diri", "Lihat Menu", "Total Gizi", "Aktivitas Fisik"]
)

if pilihan_halaman == "Data Diri":
    st.title("Aplikasi Gizi Harian")
    st.write("Pilih menu makanan sehat sesuai usia dan jenis kelamin")
    st.write("---")
    
    st.header("Isi Data Diri")
    st.write("Silakan isi data diri kamu di bawah ini:")
    st.write("")
    
    nama_user = st.text_input("Nama kamu:")
 
    jk_user = st.radio("Jenis Kelamin:", ["Laki-laki", "Perempuan"])

    usia_user = st.radio("Kelompok Usia:", ["Remaja (10-18 tahun)", "Dewasa (19-25 tahun)"])

    if st.button("Simpan Data"):
        st.session_state.nama = nama_user
        st.session_state.jenis_kelamin = jk_user
        st.session_state.usia = usia_user
        
        st.success("Data berhasil disimpan!")
        st.write(f"Halo {nama_user}!")
        st.write("Silakan ke tabel lihat menu untuk memilih menu.")

elif pilihan_halaman == "Lihat Menu":
    st.header("Menu Makanan")
    
    if st.session_state.nama == "":
        st.warning("Kamu belum isi data diri!")
        st.write("Silakan isi data diri terlebih dadulu.")
    
    else:
        st.write(f"Nama: {st.session_state.nama}")
        st.write(f"Jenis Kelamin: {st.session_state.jenis_kelamin}")
        st.write(f"Usia: {st.session_state.usia}")
        st.write("---")

        waktu_makan = st.selectbox(
            "Pilih Waktu Makan:",
            ["Sarapan", "Makan Siang", "Makan Malam"]
        )
        
        if st.session_state.jenis_kelamin == "Perempuan" and "Remaja" in st.session_state.usia:
            
            if waktu_makan == "Sarapan":
                st.subheader(f"Menu {waktu_makan}: {menu_pr_sarapan_nama}")
                tampilkan_menu_makanan(menu_pr_sarapan_list)
                st.write("")
                tampilkan_info_gizi(menu_pr_sarapan_kalori, menu_pr_sarapan_protein, menu_pr_sarapan_lemak, menu_pr_sarapan_karbo)
                
            elif waktu_makan == "Makan Siang":
                st.subheader(f"Menu {waktu_makan}: {menu_pr_siang_nama}")
                tampilkan_menu_makanan(menu_pr_siang_list)
                st.write("")
                tampilkan_info_gizi(menu_pr_siang_kalori, menu_pr_siang_protein, menu_pr_siang_lemak, menu_pr_siang_karbo)
                
            else:
                st.subheader(f"Menu {waktu_makan}: {menu_pr_malam_nama}")
                tampilkan_menu_makanan(menu_pr_malam_list)
                st.write("")
                tampilkan_info_gizi(menu_pr_malam_kalori, menu_pr_malam_protein, menu_pr_malam_lemak, menu_pr_malam_karbo)
        
        elif st.session_state.jenis_kelamin == "Perempuan" and "Dewasa" in st.session_state.usia:
            
            if waktu_makan == "Sarapan":
                st.subheader(f"Menu {waktu_makan}: {menu_pd_sarapan_nama}")
                tampilkan_menu_makanan(menu_pd_sarapan_list)
                st.write("")
                tampilkan_info_gizi(menu_pd_sarapan_kalori, menu_pd_sarapan_protein, menu_pd_sarapan_lemak, menu_pd_sarapan_karbo)
                
            elif waktu_makan == "Makan Siang":
                st.subheader(f"Menu {waktu_makan}: {menu_pd_siang_nama}")
                tampilkan_menu_makanan(menu_pd_siang_list)
                st.write("")
                tampilkan_info_gizi(menu_pd_siang_kalori, menu_pd_siang_protein, menu_pd_siang_lemak, menu_pd_siang_karbo)
                
            else:
                st.subheader(f"Menu {waktu_makan}: {menu_pd_malam_nama}")
                tampilkan_menu_makanan(menu_pd_malam_list)
                st.write("")
                tampilkan_info_gizi(menu_pd_malam_kalori, menu_pd_malam_protein, menu_pd_malam_lemak, menu_pd_malam_karbo)
        
        elif st.session_state.jenis_kelamin == "Laki-laki" and "Remaja" in st.session_state.usia:
            
            if waktu_makan == "Sarapan":
                st.subheader(f"Menu {waktu_makan}: {menu_lr_sarapan_nama}")
                tampilkan_menu_makanan(menu_lr_sarapan_list)
                st.write("")
                tampilkan_info_gizi(menu_lr_sarapan_kalori, menu_lr_sarapan_protein, menu_lr_sarapan_lemak, menu_lr_sarapan_karbo)
                
            elif waktu_makan == "Makan Siang":
                st.subheader(f"Menu {waktu_makan}: {menu_lr_siang_nama}")
                tampilkan_menu_makanan(menu_lr_siang_list)
                st.write("")
                tampilkan_info_gizi(menu_lr_siang_kalori, menu_lr_siang_protein, menu_lr_siang_lemak, menu_lr_siang_karbo)
                
            else:
                st.subheader(f"Menu {waktu_makan}: {menu_lr_malam_nama}")
                tampilkan_menu_makanan(menu_lr_malam_list)
                st.write("")
                tampilkan_info_gizi(menu_lr_malam_kalori, menu_lr_malam_protein, menu_lr_malam_lemak, menu_lr_malam_karbo)
        
        else:
            
            if waktu_makan == "Sarapan":
                st.subheader(f"Menu {waktu_makan}: {menu_ld_sarapan_nama}")
                tampilkan_menu_makanan(menu_ld_sarapan_list)
                st.write("")
                tampilkan_info_gizi(menu_ld_sarapan_kalori, menu_ld_sarapan_protein, menu_ld_sarapan_lemak, menu_ld_sarapan_karbo)
                
            elif waktu_makan == "Makan Siang":
                st.subheader(f"Menu {waktu_makan}: {menu_ld_siang_nama}")
                tampilkan_menu_makanan(menu_ld_siang_list)
                st.write("")
                tampilkan_info_gizi(menu_ld_siang_kalori, menu_ld_siang_protein, menu_ld_siang_lemak, menu_ld_siang_karbo)
                
            else:
                st.subheader(f"Menu {waktu_makan}: {menu_ld_malam_nama}")
                tampilkan_menu_makanan(menu_ld_malam_list)
                st.write("")
                tampilkan_info_gizi(menu_ld_malam_kalori, menu_ld_malam_protein, menu_ld_malam_lemak, menu_ld_malam_karbo)


elif pilihan_halaman == "Total Gizi":
    st.header("Total Gizi Harian")
    
    if st.session_state.nama == "":
        st.warning("Kamu belum isi data diri!")
        st.write("Silakan isi data diri terlebih dadulu.")
    
    else:
        st.write(f"Nama: {st.session_state.nama}")
        st.write(f"Kategori: {st.session_state.jenis_kelamin} - {st.session_state.usia}")
        st.write("---")
        
        if st.session_state.jenis_kelamin == "Perempuan" and "Remaja" in st.session_state.usia:
            total_kalori = menu_pr_sarapan_kalori + menu_pr_siang_kalori + menu_pr_malam_kalori
            total_protein = menu_pr_sarapan_protein + menu_pr_siang_protein + menu_pr_malam_protein
            total_lemak = menu_pr_sarapan_lemak + menu_pr_siang_lemak + menu_pr_malam_lemak
            total_karbo = menu_pr_sarapan_karbo + menu_pr_siang_karbo + menu_pr_malam_karbo
        
        elif st.session_state.jenis_kelamin == "Perempuan" and "Dewasa" in st.session_state.usia:
            total_kalori = menu_pd_sarapan_kalori + menu_pd_siang_kalori + menu_pd_malam_kalori
            total_protein = menu_pd_sarapan_protein + menu_pd_siang_protein + menu_pd_malam_protein
            total_lemak = menu_pd_sarapan_lemak + menu_pd_siang_lemak + menu_pd_malam_lemak
            total_karbo = menu_pd_sarapan_karbo + menu_pd_siang_karbo + menu_pd_malam_karbo
        
        elif st.session_state.jenis_kelamin == "Laki-laki" and "Remaja" in st.session_state.usia:
            total_kalori = menu_lr_sarapan_kalori + menu_lr_siang_kalori + menu_lr_malam_kalori
            total_protein = menu_lr_sarapan_protein + menu_lr_siang_protein + menu_lr_malam_protein
            total_lemak = menu_lr_sarapan_lemak + menu_lr_siang_lemak + menu_lr_malam_lemak
            total_karbo = menu_lr_sarapan_karbo + menu_lr_siang_karbo + menu_lr_malam_karbo
        
        else:
            total_kalori = menu_ld_sarapan_kalori + menu_ld_siang_kalori + menu_ld_malam_kalori
            total_protein = menu_ld_sarapan_protein + menu_ld_siang_protein + menu_ld_malam_protein
            total_lemak = menu_ld_sarapan_lemak + menu_ld_siang_lemak + menu_ld_malam_lemak
            total_karbo = menu_ld_sarapan_karbo + menu_ld_siang_karbo + menu_ld_malam_karbo
    
        st.subheader("Total Gizi dalam Sehari:")
        st.write(f"Total Kalori: {total_kalori} kal")
        st.write(f"Total Protein: {total_protein} gram")
        st.write(f"Total Lemak: {total_lemak} gram")
        st.write(f"Total Karbohidrat: {total_karbo} gram")
        
        st.write("---")
        st.success("Ini adalah total asupan gizi kamu dalam sehari!")


elif pilihan_halaman == "Aktivitas Fisik":
    st.header("Aktivitas Fisik")
    
    if st.session_state.nama == "":
        st.warning("Kamu belum isi data diri!")
        st.write("Silakan isi data diri terlebih dadulu.")
    
    else:
        st.write(f"Nama: {st.session_state.nama}")
        st.write(f"Kategori: {st.session_state.jenis_kelamin} - {st.session_state.usia}")
        st.write("---")
        
        st.subheader("Aktivitas Fisik yang Disarankan:")
        
        if st.session_state.jenis_kelamin == "Perempuan" and "Remaja" in st.session_state.usia:
            st.write("**Aktivitas Harian:**")
            
            aktivitas_list = [
                "Jalan kaki ke sekolah / bersepeda (10-15 menit)",
                "Olahraga: lari ringan / lompat tali / senam (30-40 menit)",
                "Akhir pekan: bersepeda, berenang, bermain bola (60+ menit)"
            ]
            
            for aktivitas in aktivitas_list:
                st.write(f"- {aktivitas}")
        
        elif st.session_state.jenis_kelamin == "Perempuan" and "Dewasa" in st.session_state.usia:
            st.write("**Aktivitas Harian:**")
            
            aktivitas_list = [
                "Berenang / jogging / olahraga intens (25-30 menit)",
                "Jalan santai / aktivitas ringan (20-30 menit)",
                "Naik turun tangga / pekerjaan rumah"
            ]
            
            for aktivitas in aktivitas_list:
                st.write(f"- {aktivitas}")
        
        elif st.session_state.jenis_kelamin == "Laki-laki" and "Remaja" in st.session_state.usia:
            st.write("**Aktivitas Harian:**")
            
            aktivitas_list = [
                "Jalan kaki atau naik-turun tangga ke sekolah (10-15 menit)",
                "Berenang / bermain bola (60 menit)",
                "Olahraga tim dengan teman"
            ]
            
            for aktivitas in aktivitas_list:
                st.write(f"- {aktivitas}")
        
        else:
            st.write("**Aktivitas Harian:**")
            
            aktivitas_list = [
                "Latihan kekuatan otot (30 menit)",
                "Aktivitas akademik",
                "Stretching dan relaksasi"
            ]
            
            for aktivitas in aktivitas_list:
                st.write(f"- {aktivitas}")
        
        st.write("---")
        st.success("Aktivitas fisik teratur membantu menjaga kesehatan!")

st.sidebar.write("---")