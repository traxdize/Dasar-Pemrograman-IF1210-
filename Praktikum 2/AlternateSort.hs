module AlternateSort where

-- DEFINISI DAN SPESIFIKASI
minElmt :: [Int] -> Int
delete :: Int -> [Int] -> [Int]
sorting :: [Int] -> [Int]
alternateSort :: [Int] -> [Int]
konso :: Int -> [Int] -> [Int]
{- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
   (list of integer), dengan e sebagai elemen pertama: e o li -> li' -}


-- REALISASI
konso e li = [e] ++ li

minElmt l
    | null l = 0
    | null (tail l) = head l
    | head l < last l = minElmt (init l)
    | otherwise = minElmt (tail l)

delete x l
    | null l = []
    | x == head l = tail l
    | otherwise = konso (head l) (delete x (tail l))

sorting l
    | null l = l
    | otherwise = konso (minElmt l) (sorting (delete (minElmt l) l))

alternateSort l
    | null l || null (tail l) = l
    | otherwise = konso (head (sorting l)) (konso (last (sorting l)) (alternateSort(init(tail(sorting l)))))