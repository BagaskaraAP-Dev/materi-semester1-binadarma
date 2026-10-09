import java.util.Scanner;

public class belajar {
    public static void main(String[] args) {
        //Membuat objek untuk membaca input
        Scanner input = new Scanner(System.in);

        System.out.println("PROGRAM JAWA!!");

        System.out.print("Masukkan nilai A: ");
        double a = input.nextDouble();

        System.out.print("Masukkan nilai B: ");
        double b = input.nextDouble();

        double tambah = a + b;
        double kurang = a - b;
        double kali = a * b;
        double bagi = a / b;

        System.out.println("hasil hitung");
        System.out.println("Hasil Penambahan A + B = " + tambah);
        System.out.println("Hasil Pengurangan A - B = " + kurang);
        System.out.println("Hasil Perkalian A * B   = " + kali);
        System.out.println("Hasil Pembagian A / B   = " + bagi);

        
        input.close();
    }
}