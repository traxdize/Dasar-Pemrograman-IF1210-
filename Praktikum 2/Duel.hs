module Duel where

-- DEFINISI DAN SPESIFIKASI
duel :: [String] -> [String]
{- duel adalah sebuah fungsi yang menerima list of string (l) dan mengembalikan list of string dengan kata 'desperado' diganti 'BANG' -}

-- REALISASI
duel l
    | null l = l
    | head l == "desperado" = "BANG" : duel (tail l)
    | otherwise = head l : duel (tail l)