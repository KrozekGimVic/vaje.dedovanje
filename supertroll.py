from hero import Hero


class SuperTroll(Hero):
    """
    SuperTroll fights against a hero!

    >>> supertroll = SuperTroll('SuperTroll', hp=1)
    >>> hero = Hero('Hero', hp=99999, strength=99999)
    >>> supertroll.hp
    1
    >>> hero.attack(supertroll)
    SuperTroll: lol dat tickles
    >>> hero.attack(supertroll)
    SuperTroll: lol dat tickles
    >>> hero.attack(supertroll)
    SuperTroll: lol dat tickles
    >>> hero.attack(supertroll)
    SuperTroll: lol dat tickles
    >>> supertroll.hp
    1

    Time for the SuperTroll to hit back
    >>> supertroll.attack(hero)
    SuperTroll: u wot m8? u ded now lel
    Hero: Haha, 'tis but a scratch! I, the great hero Hero will never fall from a weak attack like that!
    Ghost of Hero: Oh no, I, Hero, the great hero of the world have fallen and now darkness will surely take over the world! How can this be??
    SuperTroll: trololololo ...
    >>> hero.hp
    0
    >>> hero.alive
    False
    """

    def _die(self):
        """SuperTroll can't die!"""
        print("{0}: lol can't kill me".format(self.name))

    def _is_hurt(self, n):
        """SuperTroll can't get hurt!"""
        print("{0}: lol dat tickles".format(self.name))

    def attack(self, other):
        """SuperTroll always just kills the enemy."""

        print("{0}: u wot m8? u ded now lel".format(self.name))

        other.is_attacked(other.maxhp)

        print("{0}: trololololo ...".format(self.name))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
