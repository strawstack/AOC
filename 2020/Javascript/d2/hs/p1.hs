import System.IO
import Control.Monad
import qualified Text.Regex.PCRE as Re

main :: IO ()
main = do
    handle <- openFile "input.txt" ReadMode
    contents <- hGetContents handle

    let lns = lines contents

    print lns
