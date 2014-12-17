from human import Human


class Hero(Human):
    """
    A normal run-of-the-mill hero is walking around

    >>> leopold = Hero('Leopold')

    When he suddenly meets a monster! (yes the monster is a Hero too, deal with
    it :) ).

    >>> monster = Hero('The Evil One', hp=500, strength=100)

    Before our hero can do anything, the evil monster slays him!

    >>> monster.attack(leopold)
    Leopold: Haha, 'tis but a scratch! I, the great hero Leopold will never fall from a weak attack like that!
    Ghost of Leopold: Oh no, I, Leopold, the great hero of the world have fallen and now darkness will surely take over the world! How can this be??
    >>> leopold.alive
    False

    But then a stronger hero comes by

    >>> martincek = Hero('Martinček', hp=1000, strength=1000)

    The monster hits him but to no avail!

    >>> monster.attack(martincek)
    Martinček: Haha, 'tis but a scratch! I, the great hero Martinček will never fall from a weak attack like that!
    >>> monster.attack(martincek)
    Martinček: Haha, 'tis but a scratch! I, the great hero Martinček will never fall from a weak attack like that!
    >>> monster.attack(martincek)
    Martinček: Haha, 'tis but a scratch! I, the great hero Martinček will never fall from a weak attack like that!

    """

    def __init__(self, name, hp=100, strength=50):
        """Heroes are a lot sturdier and stronger then normal humans!"""
        self.name = name
        self.maxhp = hp
        self.hp = self.maxhp
        self.strength = strength
        self.alive = True

    def _die(self):
        """Heroes are also much more dramatic when they die."""

        last_words = ("Ghost of {0}: Oh no, I, {0}, the great hero of the " +
                      "world have fallen and now darkness will surely take " +
                      "over the world! How can this be??")

        last_words = last_words.format(self.name)
        super()._die(last_words)

    def _is_hurt(self, n):
        """Also very dramatic when they are hurt ... """

        last_words = ("Ghost of {0}: You wretched being, must you defile " +
                      "my, the great hero {0}'s corpse so!!")

        words_when_hit = ("{0}: Haha, 'tis but a scratch! I, the great hero " +
                          "{0} will never fall from a weak attack like that!")

        last_words = last_words.format(self.name)
        words_when_hit = words_when_hit.format(self.name)

        super()._is_hurt(
            n,
            last_words=last_words,
            words_when_hit=words_when_hit,
        )

    def attack(self, other):
        """Heroes do pack quite a punch though!"""

        other.is_attacked(self.strength)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
