class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


# q1-a
def siblings(t):
    """Return a list of the labels of all nodes that have siblings in t.
    
    >>> a = Tree(4, [Tree(5), Tree(6), Tree(7, [Tree(8)])])
    >>> siblings(Tree(1, [Tree(3, [a]), Tree(9, [Tree(10)])]))
    [3, 9, 5, 6, 7]
    """
    result = [branch.label for branch in t.branches] if len(t.branches) > 1 else []
    for branch in t.branches:
        result += siblings(branch)
    return result


class Sib(Tree):
    """A tree that knows how many siblings it has.
    >>> a = Sib(4, [Sib(5), Sib(6), Sib(7, [Sib(8)])])
    >>> a.label
    4
    >>> a.branches[1].label
    6
    >>> a.siblings
    0
    >>> a.branches[1].siblings
    2
    """
    def __init__(self, label, branches=[]):
        self.siblings = 0
        branch_number = len(branches)
        for branch in branches:
            branch.siblings = branch_number - 1
        Tree.__init__(self, label, branches)



# q2-a
def make_trie(words):
    """ Makes a tree where every node is a letter of a word.
    All words end as a leaf of the tree.
    words is given as a list of strings.
    """
    trie = Tree('')
    for word in words:
        add_word(trie, word)
    return trie


def add_word(trie, word):
    if not len(word):
        return None
    # Indicates whether WORD[0] exists in the branches of trie.
    # We perdicts that WORD[0] dose not exist in the branches of trie.
    is_word_root_exist = False
    # To find out where the root of WORD should be planted.
    for branch in trie.branches:
        if branch.label == word[0]:
            is_word_root_exist = True
            word_root = branch
    if not is_word_root_exist:
        word_root = Tree(word[0])
        trie.branches += [word_root]
    # We have already locate where the root of WORD should be planted.
    # Then handle the rest of the WORD.
    add_word(word_root, word[1:])


# q2-b
def get_words(trie):
    """
    >>> get_words(make_trie(['this', 'is', 'the', 'trie']))
    ['this', 'the', 'trie', 'is']
    """
    if trie.is_leaf():
        return[trie.label]
    else:
        words_to_return = []
        for branch in trie.branches:
            branch_words = get_words(branch)
            index_branch_words = 0
            while index_branch_words < len(branch_words):
                branch_words[index_branch_words] = trie.label + branch_words[index_branch_words]
                index_branch_words += 1
            words_to_return += branch_words
        return words_to_return


# q3, not completed
