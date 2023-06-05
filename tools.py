import matplotlib.pyplot as plt


class Plotter:

    def plot(self, x_data, y_data=None, _label=None, _linestyle='-', _linewidth=1):
        if y_data is None:
            plt.plot(x_data, label=_label, linestyle=_linestyle, linewidth=_linewidth)
        else:
            plt.plot(x_data, y_data, label=_label, linestyle=_linestyle, linewidth=_linewidth)

    def set_title(self, title):
        plt.title(title)

    def set_xlabel(self, name: str):

        plt.xlabel(name)

    def set_ylabel(self, name: str):

        plt.ylabel(name)

    def set_legend(self):

        plt.legend()

    def show(self):

        plt.show()

    def clear(self):

        plt.clf()


from time import perf_counter


class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start


def wrap(string):
    return f'`{string}`'


def collection_to_str(collection, symbols=" ", item_wrap=True):
    if item_wrap:
        return symbols.join([wrap(item) for item in collection])
    return symbols.join(collection)
