import java.util.Scanner;

public class belajar {
    public static void main(String[] args) {
        // Membuat objek Scanner untuk membaca input dari keyboard
        Scanner input = new Scanner(System.in);

        System.out.println("PROGRAM JAWA!!");

        // Meminta input nilai variabel A dan B
        System.out.print("Masukkan nilai A: ");
        double a = input.nextDouble();

        System.out.print("Masukkan nilai B: ");
        double b = input.nextDouble();

        // Operasi Aritmatika
        double tambah = a + b;
        double kurang = a - b;
        double kali = a * b;
        double bagi = a / b;

        // Menampilkan Hasil
        System.out.println("\n=== HASIL PERHITUNGAN ===");
        System.out.println("Hasil Penjumlahan A + B = " + tambah);
        System.out.println("Hasil Pengurangan A - B = " + kurang);
        System.out.println("Hasil Perkalian A * B   = " + kali);
        System.out.println("Hasil Pembagian A / B   = " + bagi);

        // Menutup scanner
        input.close();
    }
}