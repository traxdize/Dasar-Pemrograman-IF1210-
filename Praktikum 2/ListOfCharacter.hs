module ListOfCharacter where

-- DEFINISI DAN SPESIFIKASI
isPalindrom :: [Char] -> Bool
{- isPalindrom adalah sebuah fungsi yang mengecek apakah sebuah list of Character (l) palindrom atau tidak -}
splitAlternate :: [Char] -> ([Char],[Char])
{- splitAlternate adalah sebuah fungsi yang mengambil list dan mengoutput sebuah tuple dari hasil splitAlternateOdd dan splitAlternateEven -}
splitAlternateOdd :: Int -> [Char] -> [Char]
{- splitAlternateOdd adalah sebuah fungsi yang menerima sebuah int (n) yang merupakan panjang list of integer (ls) lalu mengoutput
sebuah list of integer yang merupakan bilangan berposisi ganjil dari list of integer tersebut. -}
splitAlternateEven :: Int -> [Char] -> [Char]
{- splitAlternateEven adalah sebuah fungsi yang menerima sebuah int (n) yang merupakan panjang list of integer (ls) lalu mengoutput
sebuah list of integer yang merupakan bilangan berposisi genap dari list of integer tersebut. -}
konkat :: [Char] -> [Char] -> [Char]
{- konkat adalah sebuah fungsi yang menerima dua buah list of character dan menggabungkannya menjadi satu buah list of character -}
pajakMakan :: [Char] -> [Int] -> [Char]
{- fungsi pajakMakan adalah fungsi yang menentukan menu apa saja yang Tuan Vin dapat pesan -}
mampuBayar :: [Char] -> [Int] -> [Char]
{- mampuBayar adalah fungsi yang membandingkan head dari sebuah list of integer dengan 182 karena 182 adalah angka terbesar yang masih
di bawah 200 setelah pajak dan kemudian menambahkan kode menu dari list of character yang bersesuaian ke sebuah list baru -}
konso :: Char -> [Char] -> [Char]
{- konso e lc menghasilkan sebuah list of character dari e (sebuah character)  
   dan lc (list of integer), dengan cc sebagai elemen pertama: e o lc -> lc' -}
konsDot :: [Char] -> Char -> [Char]
{- konsDot li e menghasilkan sebuah list of integer dari li (list of integer) dan 
   e (sebuah integer), dengan e sebagai elemen terakhir: li o e -> li' -}
{- type List of Char: [ ] atau [e o List] atau [List o e]
   Definisi type List of Char
   Basis: List of Char kosong adalah list of Char
   Rekurens: 
   List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Char di awal 
   sebuah list atau
   dibuat dengan menambahkan sebuah elemen bertype Char di akhir sebuah list -}

-- REALISASI

konso e lc = [e] ++ lc

konsDot lc e = lc ++ [e]

isPalindrom l
    | null l = True
    | null (tail l) = True
    | head l /= last l = False
    | otherwise = True


splitAlternate ls = (splitAlternateOdd n ls, splitAlternateEven n ls)
    where
        n = length ls

splitAlternateOdd n ls
    | n == 0 = []
    | null (tail ls) = [last ls]
    | n `mod` 2 /= 0 = konsDot (splitAlternateOdd (n-1) (init ls)) (last ls)
    | otherwise = splitAlternateOdd (n-1) (init ls)

splitAlternateEven n ls
    | n == 0 = []
    | null (tail ls) = []
    | n `mod` 2 == 0 = konsDot (splitAlternateEven (n-1) (init ls)) (last ls)
    | otherwise = splitAlternateEven (n-1) (init ls)

konkat l1 l2
    | null l1 = l2
    | null l2 = l1
    | null l1 && null l2 = []
    | otherwise = l1 ++ l2

pajakMakan lf lh
    | null lf && null lh = []
    | otherwise = mampuBayar lf lh

mampuBayar lf lh
    | null lf && null lh = []
    | head lh < 182 = konso (head lf) (mampuBayar (tail lf) (tail lh))
    | otherwise = mampuBayar (tail lf) (tail lh)