import json
import re
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# File untuk menyimpan kontak
FILE_KONTAK = os.path.join(os.path.dirname(__file__), "kontak.json")

def load_kontak():
    """Memuat kontak dari file JSON"""
    try:
        with open(FILE_KONTAK, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_kontak():
    """Menyimpan kontak ke file JSON"""
    with open(FILE_KONTAK, "w") as file:
        json.dump(daftar_kontak, file, indent=4)

def validasi_telepon(telepon):
    """Validasi nomor telepon hanya angka"""
    return telepon.isdigit()

def validasi_email(email):
    """Validasi format email sederhana"""
    pola = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pola, email)

def tambah_kontak():
    """Menambahkan kontak baru dengan validasi"""
    nama = simpledialog.askstring("Tambah Kontak", "Masukkan Nama:")
    telepon = simpledialog.askstring("Tambah Kontak", "Masukkan Nomor Telepon:")
    email = simpledialog.askstring("Tambah Kontak", "Masukkan Email:")
    
    if not nama or not telepon or not email:
        messagebox.showerror("Error", "Semua field harus diisi!")
        return
    
    if not validasi_telepon(telepon):
        messagebox.showerror("Error", "Nomor telepon harus hanya berisi angka!")
        return
    
    if not validasi_email(email):
        messagebox.showerror("Error", "Format email tidak valid!")
        return
    
    daftar_kontak.append({"nama": nama, "telepon": telepon, "email": email})
    save_kontak()
    messagebox.showinfo("Sukses", "Kontak berhasil ditambahkan!")
    tampilkan_semua_kontak()

def tampilkan_semua_kontak():
    """Menampilkan semua kontak dalam GUI"""
    listbox.delete(0, tk.END)
    for i, kontak in enumerate(daftar_kontak, 1):
        listbox.insert(tk.END, f"{i}. {kontak['nama']} - {kontak['telepon']} - {kontak['email']}")

def hapus_kontak():
    """Menghapus kontak yang dipilih"""
    try:
        index = listbox.curselection()[0]
        del daftar_kontak[index]
        save_kontak()
        messagebox.showinfo("Sukses", "Kontak berhasil dihapus!")
        tampilkan_semua_kontak()
    except IndexError:
        messagebox.showerror("Error", "Pilih kontak yang ingin dihapus!")

# Load data kontak dari file
daftar_kontak = load_kontak()

# GUI dengan Tkinter
root = tk.Tk()
root.title("Manajemen Kontak")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack()

tombol_tambah = tk.Button(root, text="Tambah Kontak", command=tambah_kontak)
tombol_tambah.pack(pady=5)

tombol_hapus = tk.Button(root, text="Hapus Kontak", command=hapus_kontak)
tombol_hapus.pack(pady=5)

tampilkan_semua_kontak()

root.mainloop()
