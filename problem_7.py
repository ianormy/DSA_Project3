import unittest
from typing import List


class RouteTrieNode:
    def __init__(self, handler=None):
        """Initialize this node in the Trie"""
        self.children = {}
        self.handler = handler

    def insert(self, path, handler=None):
        """Add a child node to this node if it doesn't already exist"""
        if path not in self.children:
            self.children[path] = RouteTrieNode(handler=handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        """Initialize the trie with a root node and a handler, this is the root path or home page node"""
        self.root = RouteTrieNode(handler=root_handler)

    def insert(self, path_list, handler):
        """Similar to our previous example you will want to recursively add nodes
        Make sure you assign the handler to only the leaf (deepest) node of this path
        """
        current_node = self.root
        for path in path_list:
            current_node.insert(path)
            current_node = current_node.children[path]
        current_node.handler = handler

    def find(self, path_list):
        """Starting at the root, navigate the Trie to find a match for this path
        Return the handler for a match, or None for no match
        """
        current_node = self.root
        for path in path_list:
            if path not in current_node.children:
                return None
            current_node = current_node.children[path]
        return current_node.handler


class Router:
    def __init__(self, route_handler=None, not_found_handler=None):
        """Create a new RouteTrie for holding our routes

        You could also add a handler for 404 page not found responses as well!
        """
        self.route_trie = RouteTrie(route_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, full_path, handler):
        """Add a handler for a path

        You will need to split the path and pass the pass parts
        as a list to the RouteTrie
        """
        if full_path is None:
            raise ValueError('full_path cannot be None')
        if len(full_path) == 0:
            raise ValueError('full_path cannot be empty')
        paths = self.split_path(full_path)
        self.route_trie.insert(paths, handler=handler)

    def lookup(self, full_path):
        """lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        """
        paths = self.split_path(full_path)
        # walk down the Trie
        handler = self.route_trie.find(paths)
        return self.not_found_handler if handler is None else handler

    def split_path(self, full_path: str) -> List:
        """you need to split the path into parts for
        both the add_handler and lookup functions,
        so it should be placed in a function here
        """
        return [p for p in full_path.split('/') if len(p) > 0]


class RouterTestCase(unittest.TestCase):
    def test_split_path_1(self):
        router = Router()
        output_list = ['home', 'about', 'me']
        self.assertListEqual(output_list, router.split_path('/home/about/me'))

    def test_split_path_2(self):
        router = Router()
        output_list = ['home', 'about', 'me']
        self.assertListEqual(output_list, router.split_path('/home/about/me/'))

    def test_route_1(self):
        root_handler = 'root handler'
        not_found_handler = 'not found handler'
        router = Router(root_handler, not_found_handler)
        router.add_handler("/home/about", "about handler")
        self.assertEqual(root_handler, router.lookup("/"))

    def test_route_2(self):
        root_handler = 'root handler'
        not_found_handler = 'not found handler'
        router = Router(root_handler, not_found_handler)
        router.add_handler("/home/about", "about handler")
        self.assertEqual(not_found_handler, router.lookup("/home"))

    def test_route_3(self):
        root_handler = 'root handler'
        not_found_handler = 'not found handler'
        about_handler = 'about handler'
        router = Router(root_handler, not_found_handler)
        router.add_handler("/home/about", about_handler)
        self.assertEqual(about_handler, router.lookup("/home/about"))

    def test_route_4(self):
        root_handler = 'root handler'
        not_found_handler = 'not found handler'
        about_handler = 'about handler'
        router = Router(root_handler, not_found_handler)
        router.add_handler("/home/about", about_handler)
        self.assertEqual(about_handler, router.lookup("/home/about/"))

    def test_route_5(self):
        root_handler = 'root handler'
        not_found_handler = 'not found handler'
        about_handler = 'about handler'
        router = Router(root_handler, not_found_handler)
        router.add_handler("/home/about", about_handler)
        self.assertEqual(not_found_handler, router.lookup("/home/about/me"))

    def test_none_insert_raises_value_error(self):
        router = Router(None, None)
        with self.assertRaises(ValueError):
            router.add_handler(None, None)

    def test_empty_input_list_raises_value_error(self):
        router = Router(None, None)
        with self.assertRaises(ValueError):
            router.add_handler('', None)


if __name__ == '__main__':
    unittest.main()
