import System.IO
import Control.Monad
import qualified Data.Map as Map

main :: IO ()
main = do
    -- read from input file
    let list = []
    handle <- openFile "input.txt" ReadMode
    contents <- hGetContents handle

    -- parse input
    let singlewords = words contents
        list = f singlewords

    -- put number into dictionary
    let m = Map.fromList (map (\x -> (x, 1)) list)

    -- for each elem in list, check in dictionary
    let ans = forEach list m

    print ans

    hClose handle

f :: [String] -> [Int]
f = map read

forEach :: [Int] -> Map.Map Int Int -> Int
forEach (x:xs) m = let v = 2020 - x in case (Map.lookup v m) of
    Just a -> v * x
    Nothing -> forEach xs m




--
