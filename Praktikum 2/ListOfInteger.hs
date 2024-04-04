module ListOfInteger where

-- DEFINISI DAN SPESIFIKASI
isEqual :: [Int] -> [Int] -> Bool
{- isEqual adalah fungsi yang menerima dua list integer dan mengoutput sebuah Boolean True bila kedua list sama dan false 
jika berbeda -}
pecahListPosNeg :: [Int] -> ([Int],[Int])
{- pecahListPosNeg adalah fungsi yang menerima satu list integer dan memecah list tersebut menjadi dua list integer berdasarkan
bilangan positif dan bilangan negatif dengan urutan yang sama dengan list awal. -}
pecahListPos :: Int -> [Int] -> [Int]
{- pecahListPos adalah subfunction dari pecahListPosNeg yang menerima sebuah integer (n) yang merupakan panjang list dari pecahList
PosNeg dan list tersebut, pecahListPos akan mengoutput sebuah list of integer dengan bilangan positif. -}
pecahListNeg :: Int -> [Int] -> [Int]
{- pecahListPos adalah subfunction dari pecahListPosNeg yang menerima sebuah integer (n) yang merupakan panjang list dari pecahList
PosNeg dan list tersebut, pecahListPos akan mengoutput sebuah list of integer dengan bilangan negatif. -}
maxNb :: [Int] -> (Int,Int)
{- maxNb adalah sebuah fungsi yang menerima list of integer dan mengoutput sebuah tuple dengan 2 integer di mana integer yang pertama
adalah bilangan terbesar dalam list itu dan integer kedua adalah berapa kali bilangan tersebut muncul. -}
findBiggest :: [Int] -> Int
{- findBiggest adalah sebuah fungsi yang menerima list of integer dan mengoutput sebuah integer yang merupakan bilangan terbesar dari
list tersebut. -}
manyTimes :: Int -> [Int] -> Int
{- manyTimes adalah sebuah fungsi yang menerima sebuah integer dan sebuah list of integer dan mengoutput sebuah integer. -}
nbX :: Int -> [Int] -> Int
{- nbX adalah fungsi yang sama persis dengan manyTimes dan cuman dibuat karena soalnya banyak maunya. -}
quickCount :: Int -> [Int] -> [Int]
{- quickQount adalah sebuah fungsi yang mencocokkan integer (a) dengan element-element dalam list of integer (l) dan membuatnya
menjadi sebuah list of integer -}
isMember :: [Int] -> Int -> Bool
{- isMember adalah fungsi yang mengecek apakah integer tertentu adalah member dari sebuah list -}
minList :: [Int] -> Int
{- minList adalah fungsi yang menerima sebuah list of integer dan mencari angka terkecil dari list tersebut. -}
jmlMin :: [Int] -> (Int, Int)
{- maxNb adalah sebuah fungsi yang menerima list of integer dan mengoutput sebuah tuple dengan 2 integer di mana integer yang pertama
adalah bilangan terkecil dalam list itu dan integer kedua adalah berapa kali bilangan tersebut muncul. -}
konso :: Int -> [Int] -> [Int]
{- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
   (list of integer), dengan e sebagai elemen pertama: e o li -> li' -}

-- REALISASI
konso e li = [e] ++ li

isEqual l1 l2
    | null l1 && null l2 = True
    | null l1 || null l2 = False
    | head l1 == head l2 = isEqual (tail l1) (tail l2)
    | otherwise = False

pecahListPosNeg lp = (pecahListPos n lp, pecahListNeg n lp)
    where
        n = length lp

pecahListPos n lp
    | n == 0 = []
    | head lp >= 0 = konso (head lp) (pecahListPos (n-1) (tail lp))
    | otherwise = pecahListPos (n-1) (tail lp)

pecahListNeg n lp
    | n == 0 = []
    | head lp < 0 = konso (head lp) (pecahListNeg (n-1) (tail lp))
    | otherwise = pecahListNeg (n-1) (tail lp)

findBiggest l
    | null l = 0
    | null (tail l) = head l
    | head l > last l = findBiggest (init l)
    | otherwise = findBiggest (tail l)

minList l
    | null l = 0
    | null (tail l) = head l
    | head l < last l = minList (init l)
    | otherwise = minList (tail l)

manyTimes a l
    | null l = 0
    | otherwise = length (quickCount a l)

nbX a l
    | null l = 0
    | otherwise = length (quickCount a l)

quickCount a l
    | null l = []
    | a == head l = konso (head l) (quickCount a (tail l))
    | otherwise = quickCount a (tail l)

maxNb l = (max, nbmax)
    where
        max
            | null l = 0
            | otherwise = findBiggest l
        nbmax
            | null l = 0
            | otherwise = manyTimes max l

jmlMin l = (min, nbmin)
    where
        min
            | null l = 0
            | otherwise = minList l
        nbmin
            | null l = 0
            | otherwise = nbX min l

isMember l n
    | null (quickCount n l) = False
    | otherwise = True