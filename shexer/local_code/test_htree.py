from shexer.utils.factories.h_tree import get_basic_h_tree


a = get_basic_h_tree()
print(a.root.str_value)
for a_child in a.root._children:
    print(a.root._children[a_child].str_value)
