import unittest
from typing import List


class TrieNode:
    def __init__(self):
        """Initialize this node in the Trie"""
        self.is_word = False
        self.children = {}

    def insert(self, char):
        """Add a child node to this node if it doesn't already exist"""
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix='') -> List:
        """Recursive function that collects the suffix for all complete words below this point"""
        ret = []
        if self.is_word:
            ret.append(suffix)
        for char, node in self.children.items():
            ret += self.children[char].suffixes(suffix + char)
        return ret


class Trie:
    def __init__(self):
        """Initialize this Trie (add a root node)"""
        self.root = TrieNode()

    def insert(self, word):
        """Add a word to the Trie"""
        current_node = self.root
        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        """Find the Trie node that represents this prefix

        Args:
            prefix(str): prefix to look for

        Returns:
            node(TrieNode): the TrieNode that represents the prefix, or False if not found
        """
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node


class TrieTestCase(unittest.TestCase):
    def test_valid_1(self):
        input_list, output_list = [["fun", "function", "factory"], ["un", "unction", "actory"]]
        trie = Trie()
        # add the words to the trie
        for w in input_list:
            trie.insert(w)
        # test if we can find the right suffixes
        prefix_node = trie.find("f")
        self.assertIsNotNone(prefix_node)
        self.assertListEqual(output_list, prefix_node.suffixes(""))
        print('\n'.join(prefix_node.suffixes()))


if __name__ == '__main__':
    unittest.main()
