import abc

class Position(object, metaclass=abc.ABCMeta):
        
    def element(self):
        """Element at the given position"""
            
    def __eq__(self, other):
        """Comparision interface"""
        
    def __ne__(self, other):
        return not (self == other)


class AbstractTree(object, metaclass=abc.ABCMeta):
    
    def root(self):
        """Return root element position"""
    
    def parent(self, p):
        """Return Position representing given node parent
        or None otherwise"""
    
    def children_count(self, p):
        """Return number of children Position p has"""
    
    def children(self, p):
        """Return iterator of the given node children"""
    
    def __len__(self):
        """Total number of tree elements"""
    
    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.children_count() == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def _height(self, p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(c) for c in self.children(p))
    
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height(p)