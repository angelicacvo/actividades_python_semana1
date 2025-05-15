def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function
