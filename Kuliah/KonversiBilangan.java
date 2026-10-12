/*
 * Program Konversi Bilangan (Desimal, Biner, Oktal, Heksadesimal)
 * Tugas 1 Sistem Bilangan - Soal 18
 * Nama : Bagaskara Amukti Palapa
 * NIM  : 261420008
 *
 * Mengimplementasikan algoritma soal 17 secara manual
 * (tanpa Integer.toBinaryString, Integer.parseInt(s, basis), dll).
 *
 * Kompilasi : javac KonversiBilangan.java
 * Jalankan  : java KonversiBilangan
 */
import java.util.Scanner;

public class KonversiBilangan {

    static final String SIMBOL = "0123456789ABCDEF";
    static final int DIGIT_PECAHAN = 8;   // jumlah digit maksimum di belakang koma

    // ===================================================================
    // ALGORITMA a : Desimal ke basis B (B = 2, 8, 16)
    // ===================================================================
    static String desimalKeBasis(String input, int B) {
        String[] bagian = pisah(input);
        long I = Long.parseLong(bagian[0]);   // bagian bulat
        String pecStr = bagian[1];             // bagian pecahan (teks setelah koma)

        System.out.println("  Bagian bulat " + I + " dibagi " + B + " berulang:");
        // Langkah 4: selama I > 0, simpan sisa, I = I div B
        String hasilBulat = "";
        if (I == 0) hasilBulat = "0";
        while (I > 0) {
            long hasilBagi = I / B;
            int sisa = (int) (I % B);
            System.out.printf("    %d : %d = %d  sisa %c%n", I, B, hasilBagi, SIMBOL.charAt(sisa));
            hasilBulat = SIMBOL.charAt(sisa) + hasilBulat;   // Langkah 5: dibaca dari bawah ke atas
            I = hasilBagi;
        }

        // Langkah 6: bagian pecahan dikali B berulang.
        // Pecahan disimpan sebagai pembilang/penyebut agar hasilnya tepat (tanpa error double).
        String hasilPecahan = "";
        if (!pecStr.isEmpty() && Long.parseLong(pecStr) != 0) {
            long pembilang = Long.parseLong(pecStr);
            long penyebut = (long) Math.pow(10, pecStr.length());
            System.out.println("  Bagian pecahan 0," + pecStr + " dikali " + B + " berulang:");
            for (int k = 0; k < DIGIT_PECAHAN && pembilang != 0; k++) {
                String sebelum = tulisPecahan(pembilang, penyebut);
                pembilang *= B;
                int angkaBulat = (int) (pembilang / penyebut);
                pembilang %= penyebut;
                System.out.printf("    %s x %d = %d,%s  -> %c%n", sebelum, B, angkaBulat,
                        tulisPecahan(pembilang, penyebut).substring(2), SIMBOL.charAt(angkaBulat));
                hasilPecahan += SIMBOL.charAt(angkaBulat);   // Langkah 7: dibaca dari atas ke bawah
            }
            if (pembilang != 0) System.out.println("    (dipotong sampai " + DIGIT_PECAHAN + " digit)");
        }
        return gabung(hasilBulat, hasilPecahan);
    }

    // ===================================================================
    // ALGORITMA b/c/d langkah 2 : basis B ke desimal
    // jumlah digit x B^i (bulat) + digit x B^-j (pecahan)
    // ===================================================================
    static String basisKeDesimal(String input, int B) {
        String[] bagian = pisah(input);
        String bulat = bagian[0], pecahan = bagian[1];

        long total = 0;
        StringBuilder rumus = new StringBuilder();
        int n = bulat.length();
        for (int i = 0; i < n; i++) {
            int d = SIMBOL.indexOf(bulat.charAt(i));
            int pangkat = n - 1 - i;
            total += d * (long) Math.pow(B, pangkat);
            if (i > 0) rumus.append(" + ");
            rumus.append(d).append("x").append(B).append("^").append(pangkat);
        }
        System.out.println("  Bulat  : " + rumus + " = " + total);

        String hasilPecahan = "";
        if (!pecahan.isEmpty()) {
            // pecahan = p / B^k, dihitung tepat lalu ditulis sebagai desimal
            long p = 0;
            rumus = new StringBuilder();
            for (int j = 1; j <= pecahan.length(); j++) {
                int d = SIMBOL.indexOf(pecahan.charAt(j - 1));
                p = p * B + d;
                if (j > 1) rumus.append(" + ");
                rumus.append(d).append("x").append(B).append("^-").append(j);
            }
            long q = (long) Math.pow(B, pecahan.length());
            hasilPecahan = tulisPecahan(p, q).substring(2).replaceAll("0+$", "");
            System.out.println("  Pecahan: " + rumus + " = 0," + (hasilPecahan.isEmpty() ? "0" : hasilPecahan));
        }
        return gabung(String.valueOf(total), hasilPecahan);
    }

    // ===================================================================
    // ALGORITMA b langkah 3-4 : biner ke oktal (3 bit) / heksa (4 bit)
    // ===================================================================
    static String binerKeKelompok(String input, int bit) {
        String[] bagian = pisah(input);
        String bulat = bagian[0], pecahan = bagian[1];

        // tambahkan 0 di kiri (bulat) dan di kanan (pecahan) agar kelompok penuh
        while (bulat.length() % bit != 0) bulat = "0" + bulat;
        while (!pecahan.isEmpty() && pecahan.length() % bit != 0) pecahan = pecahan + "0";

        StringBuilder tampil = new StringBuilder("  Kelompok " + bit + " bit: ");
        String hasilBulat = ubahKelompok(bulat, bit, tampil);
        String hasilPecahan = "";
        if (!pecahan.isEmpty()) {
            tampil.append(" , ");
            hasilPecahan = ubahKelompok(pecahan, bit, tampil);
        }
        System.out.println(tampil);

        hasilBulat = hasilBulat.replaceFirst("^0+(?=.)", "");   // buang nol di depan
        return gabung(hasilBulat, hasilPecahan);
    }

    static String ubahKelompok(String bits, int bit, StringBuilder tampil) {
        String hasil = "";
        for (int i = 0; i < bits.length(); i += bit) {
            String g = bits.substring(i, i + bit);
            int nilai = 0;
            for (char c : g.toCharArray()) nilai = nilai * 2 + (c - '0');
            hasil += SIMBOL.charAt(nilai);
            tampil.append(g).append("=").append(SIMBOL.charAt(nilai)).append("  ");
        }
        return hasil;
    }

    // ===================================================================
    // ALGORITMA c/d langkah 3 : oktal (3 bit) / heksa (4 bit) ke biner
    // ===================================================================
    static String kelompokKeBiner(String input, int bit) {
        String[] bagian = pisah(input);
        StringBuilder tampil = new StringBuilder("  Tiap digit jadi " + bit + " bit: ");
        String binBulat = digitKeBit(bagian[0], bit, tampil).replaceFirst("^0+(?=.)", "");
        String binPecahan = "";
        if (!bagian[1].isEmpty()) {
            tampil.append(" , ");
            binPecahan = digitKeBit(bagian[1], bit, tampil).replaceAll("0+$", "");
        }
        System.out.println(tampil);
        return gabung(binBulat, binPecahan);
    }

    static String digitKeBit(String digits, int bit, StringBuilder tampil) {
        String hasil = "";
        for (char c : digits.toCharArray()) {
            int nilai = SIMBOL.indexOf(c);
            String b = "";
            for (int k = 0; k < bit; k++) {      // bagi 2 sebanyak 'bit' kali
                b = (nilai % 2) + b;
                nilai /= 2;
            }
            hasil += b;
            tampil.append(c).append("=").append(b).append("  ");
        }
        return hasil;
    }

    // ===================================================================
    // Utilitas
    // ===================================================================
    static String[] pisah(String s) {
        s = s.trim().toUpperCase().replace('.', ',');
        int koma = s.indexOf(',');
        String bulat = koma < 0 ? s : s.substring(0, koma);
        String pecahan = koma < 0 ? "" : s.substring(koma + 1);
        if (bulat.isEmpty()) bulat = "0";
        return new String[]{bulat, pecahan};
    }

    static String gabung(String bulat, String pecahan) {
        return pecahan.isEmpty() ? bulat : bulat + "," + pecahan;
    }

    // menulis p/q sebagai "0,xxxx"
    static String tulisPecahan(long p, long q) {
        if (p == 0) return "0,0";
        StringBuilder s = new StringBuilder("0,");
        for (int i = 0; i < 12 && p != 0; i++) {
            p *= 10;
            s.append(p / q);
            p %= q;
        }
        return s.toString();
    }

    static boolean valid(String s, int basis) {
        String[] b = pisah(s);
        String boleh = SIMBOL.substring(0, basis);
        String semua = b[0] + b[1];
        if (semua.isEmpty() || b[0].length() > 15) return false;
        for (char c : semua.toCharArray()) {
            if (boleh.indexOf(c) < 0) return false;
        }
        return true;
    }

    static String namaBasis(int b) {
        switch (b) {
            case 2:  return "Biner";
            case 8:  return "Oktal";
            case 10: return "Desimal";
            default: return "Heksadesimal";
        }
    }

    static void tampilHasil(String asal, int bAsal, String hasil, int bTujuan) {
        System.out.println("  >> " + asal + " (" + bAsal + ") = " + hasil + " (" + bTujuan + ")");
        System.out.println();
    }

    // ===================================================================
    // Program utama: menu sesuai soal 17 a, b, c, d
    // ===================================================================
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] basisMenu = {10, 2, 8, 16};

        while (true) {
            System.out.println("==============================================");
            System.out.println("   PROGRAM KONVERSI BILANGAN");
            System.out.println("   Bagaskara Amukti Palapa - 261420008");
            System.out.println("==============================================");
            System.out.println("1. Desimal -> Biner, Oktal, Heksa      (17a)");
            System.out.println("2. Biner   -> Desimal, Oktal, Heksa    (17b)");
            System.out.println("3. Oktal   -> Desimal, Biner, Heksa    (17c)");
            System.out.println("4. Heksa   -> Desimal, Biner, Oktal    (17d)");
            System.out.println("0. Keluar");
            System.out.print("Pilih menu: ");
            String pilih = sc.nextLine().trim();
            if (pilih.equals("0")) {
                System.out.println("Terima kasih.");
                break;
            }
            if (!pilih.matches("[1-4]")) {
                System.out.println("Menu tidak tersedia.\n");
                continue;
            }

            int asal = basisMenu[Integer.parseInt(pilih) - 1];
            System.out.print("Masukkan bilangan " + namaBasis(asal) + " (pecahan pakai koma): ");
            String x = sc.nextLine().trim().toUpperCase();
            if (!valid(x, asal)) {
                System.out.println("Bilangan tidak valid untuk basis " + asal + ".\n");
                continue;
            }
            System.out.println();

            switch (asal) {
                case 10:   // Algoritma a
                    for (int t : new int[]{2, 8, 16}) {
                        System.out.println("[Desimal ke " + namaBasis(t) + "]");
                        tampilHasil(x, 10, desimalKeBasis(x, t), t);
                    }
                    break;

                case 2:    // Algoritma b
                    System.out.println("[Biner ke Desimal]");
                    tampilHasil(x, 2, basisKeDesimal(x, 2), 10);
                    System.out.println("[Biner ke Oktal]");
                    tampilHasil(x, 2, binerKeKelompok(x, 3), 8);
                    System.out.println("[Biner ke Heksa]");
                    tampilHasil(x, 2, binerKeKelompok(x, 4), 16);
                    break;

                case 8:    // Algoritma c
                    System.out.println("[Oktal ke Desimal]");
                    tampilHasil(x, 8, basisKeDesimal(x, 8), 10);
                    System.out.println("[Oktal ke Biner]");
                    String bin8 = kelompokKeBiner(x, 3);
                    tampilHasil(x, 8, bin8, 2);
                    System.out.println("[Oktal ke Heksa]  (lewat biner " + bin8 + ")");
                    tampilHasil(x, 8, binerKeKelompok(bin8, 4), 16);
                    break;

                case 16:   // Algoritma d
                    System.out.println("[Heksa ke Desimal]");
                    tampilHasil(x, 16, basisKeDesimal(x, 16), 10);
                    System.out.println("[Heksa ke Biner]");
                    String bin16 = kelompokKeBiner(x, 4);
                    tampilHasil(x, 16, bin16, 2);
                    System.out.println("[Heksa ke Oktal]  (lewat biner " + bin16 + ")");
                    tampilHasil(x, 16, binerKeKelompok(bin16, 3), 8);
                    break;
            }
        }
        sc.close();
    }
}
