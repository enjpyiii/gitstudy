# writer:enjoyiii
# 2025年05月27日10时47分49秒
# 1663472473@qq.com
RED=0
BLACK=1
class RedBlackNode:
    def __init__(self,value):
        self.value=value
        self.leftc=None
        self.right=None
        self.daddy=None
        self.color=RED
class RedBlackTree:
    def __init__(self):
        self.root=None

    def left_rotate(self,x:RedBlackNode):
        y:RedBlackNode=x.right
        x_parent:RedBlackNode=x.daddy
        if x_parent==None:
            self.root=y
        elif x_parent.leftc is x:
            x_parent.leftc=y
        else:
            x_parent.right=y
        y.daddy=x_parent
        if y.leftc:
            y.leftc.daddy=x
        x.right=y.leftc
        x.daddy=y
        y.leftc=x
    def right_rotate(self,x:RedBlackNode):
        y: RedBlackNode = x.leftc
        x_parent: RedBlackNode = x.daddy
        if x_parent==None:
            self.root=y
        elif x_parent.leftc is x:
            x_parent.leftc=y
        else:
            x_parent.right=y
        y.daddy=x_parent
        if y.right:
            y.right.daddy=x
        x.leftc=y.right
        y.right=x
        x.daddy=y
    def insert(self,value):
        node=RedBlackNode(value)
        if not self.root:
            self.root=node
        else:
            x=self.root
            while x:
                parent=x
                if node.value>x.value:
                    x=x.right
                else:
                    x=x.leftc
            if node.value>parent.value:
                parent.right=node
            else:parent.leftc=node
            node.daddy=parent
        self.insert_fixup(node)
    def insert_fixup(self,node: RedBlackNode):
        parent:RedBlackNode=node.daddy
        while parent and parent.color==RED:
            grandparent:RedBlackNode=parent.daddy
            if grandparent.leftc is parent:
                uncle: RedBlackNode = grandparent.right
                if parent.leftc is node:
                    if uncle and uncle.color==RED:#情形三
                        grandparent.color=RED
                        parent.color=BLACK
                        uncle.color=BLACK
                        node=grandparent
                        parent=node.daddy
                        continue
                    else:
                        self.right_rotate(grandparent)
                        parent.color=BLACK
                        parent=node.daddy
                        grandparent.color=RED
                        continue
                if parent.right is node:
                    self.left_rotate(parent)
                    self.right_rotate(grandparent)
                    node.color=BLACK
                    grandparent.color=RED
                    break
            else:
                uncle: RedBlackNode = grandparent.leftc
                if parent.right is node:
                    if uncle and uncle.color == RED:
                        grandparent.color = RED
                        parent.color = BLACK
                        uncle.color = BLACK
                        node = grandparent
                        parent = node.daddy
                        continue
                    else:
                        self.left_rotate(grandparent)
                        parent.color = BLACK
                        parent=node.daddy
                        grandparent.color = RED
                        continue
                if parent.leftc is node:
                    self.right_rotate(parent)
                    self.left_rotate(grandparent)
                    node.color = BLACK
                    grandparent.color = RED
                    break
        self.root.color=BLACK
    def mid_order(self,node:RedBlackNode):
        if node==None:
            return
        self.mid_order(node.leftc)
        print(node.value,end='  ')
        self.mid_order(node.right)
    def rbtree(self,node,key,direction):
        if node:
            if direction==0:
                print('%2d(B) is root' % node.value)
            else:
                print("%2d(%s) is %2d's %6s child" % (node.value,
                                                     ("B" if node.color==1 else "R"),
                                                     key,
                                                     ("right" if direction == 1 else "left")))
            self.rbtree(node.leftc,node.value,-1)
            self.rbtree(node.right,node.value,1)
if __name__ == '__main__':
    redblacktree=RedBlackTree()
    num_list=[7,4,1,8,5,2,9,6,3]#
    for number in num_list:
        redblacktree.insert(number)
    redblacktree.mid_order(redblacktree.root)
    redblacktree.rbtree(redblacktree.root,None,0) 