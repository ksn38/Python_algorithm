def show_size(x):
    print(f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for i in x.items():
                show_size(i)
        elif not isinstance(x, str):
            for i in x:
                show_size(i)