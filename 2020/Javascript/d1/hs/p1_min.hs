import System.IO
import Control.Monad
import qualified Data.Map as Map

main :: IO ()
main = do

    -- Read input
    handle <- openFile "input.txt" ReadMode
    contents <- hGetContents handle

    -- Parse input
    let list = f (words contents)

    -- Create Dictionary
    let m = Map.fromList (map (\x -> (x, 1)) list)

    -- For each elem in list, check in dictionary
    let ans = forEach list m

    -- Output answer
    print ans

    hClose handle

forEach :: [Int] -> Map.Map Int Int -> Int
forEach (x:xs) m = let v = 2020 - x in case (Map.lookup v m) of
    Just a -> v * x
    Nothing -> forEach xs m

f :: [String] -> [Int]
f = map read


--
