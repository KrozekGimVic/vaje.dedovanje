class Human:
    """
    >>> joza = Human('Joža')
    >>> joza.hp
    4
    >>> joza.alive
    True

    Suddenly something hurts Joža!

    >>> joza._is_hurt(2)
    >>> joza.hp
    2
    >>> joza._is_hurt(2)
    >>> joza.hp
    0
    >>> joza.alive
    True
    >>> joza._is_hurt(5)
    >>> joza.hp
    -5
    >>> joza.alive
    True

    Why is he still alive? Ah, need to use the correct function (is_attacked),
    _is_hurt is meant as a helper function (mind the starting _). We could
    manually call another helper function (_die).

    >>> joza._die()
    Ghost of Joža: Oh no, I have died :(
    >>> joza.alive
    False

    But what we really want to see is a fight right? Let's create Joža again!

    >>> joza = Human('Joža')
    >>> grobijan = Human('Grobijan')
    >>> joza.alive
    True
    >>> joza.hp
    4

    Let's have a fight!

    >>> grobijan.attack(joza)
    >>> joza.hp
    3
    >>> grobijan.attack(joza)
    >>> joza.hp
    2
    >>> grobijan.attack(joza)
    >>> joza.hp
    1
    >>> grobijan.attack(joza)
    Ghost of Joža: Oh no, I have died :(
    >>> joza.hp
    0
    >>> joza.alive
    False
    >>> grobijan.attack(joza)
    Ghost of Joža: Why do you keep hitting my body???
    >>> joza.hp
    -1
    >>> joza.alive = False
    """

    def __init__(self, name):
        """Humans are fairly weak."""

        self.name = name
        self.maxhp = 4
        self.hp = self.maxhp
        self.alive = True

    def _die(self, last_words=None):
        """Called when I die :(."""

        if last_words:
            print(last_words)
        else:
            print("Ghost of {}: Oh no, I have died :(".format(self.name))
        self.alive = False

    def _check_dead(self):
        """Check if I am still alive, die if dead."""

        if self.alive and self.hp <= 0:
            self._die()

    def _is_hurt(self, n, last_words=None, words_when_hit=None):
        """Called when someone hurts me."""

        if not self.alive:
            if last_words:
                print(last_words)
            else:
                print(
                    "Ghost of {}: Why do you keep hitting my body???".format(
                        self.name)
                )
        else:
            if words_when_hit:
                print(words_when_hit)
        self.hp -= n

    def is_attacked(self, n):
        """Used when someone attacks me."""

        self._is_hurt(n)
        self._check_dead()

    def attack(self, other):
        """Use this to attack someone else. Humans are very weak ... """

        other.is_attacked(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
