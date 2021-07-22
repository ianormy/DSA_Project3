# HTTPRouter using a Trie
I have implemented this using a Trie.

## Time Complexity
Assuming there are **P** paths being stored and their average length is **L**, 
then insertion and retrieval will take O(**P** * **L**) time.

## Space Complexity
Assuming we are storing paths from an alphabet of size **Z** then
space complexity is O(**P** * **L** * **Z**).
