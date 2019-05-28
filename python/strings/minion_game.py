#!/usr/bin/env python3
"""The Minion Game
Kevin and Stuart want to play the 'The Minion Game'.
- Game Rules
  - Both players are given the same string, S.
  - Both players have to make substrings using the letters of the string S.
  - Stuart has to make words starting with consonants.
  - Kevin has to make words starting with vowels.
  - The game ends when both players have made all possible substrings.
- Scoring
A player gets +1 point for each occurrence of the substring in the string S.
- For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
  - For better understanding, see the image below:

            *--------*
            | BANANA |
            *--------*
     Stuart      | Kevin
    ==========================
     words score | words score
         B   1   |     A   3
         N   2   |    AN   2
        BA   1   |   ANA   2
        NA   2   |  ANAN   1
       BAN   1   | ANANA   1
       NAN   1   |
      BANA   1   |
      NANA   1   |
     BANAN   1   |
    BANANA   1   |
      total 12   |   total 9

Your task is to determine the winner of the game and their score.
- Input Format
A single line of input containing the string S.
  - Note: The string S will contain only uppercase letters: [A - Z].
- Constraints
0 < len(S <= 10^6)
- Output Format
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.
- Sample Input
    BANANA
- Sample Output
    Stuart 12
- Note: Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.
"""
class PlayerScore():
    def __init__(self, player):
        self.p = player
        self.s = 0

    def score(self, points):
        self.s += points

class ScoreBoard():
    def __init__(self, players):
        self.p1 = PlayerScore(players[0])
        self.p2 = PlayerScore(players[1])

    def print_winner(self):
        if self.p1.s == self.p2.s:
            print('Draw')
        elif self.p1.s > self.p2.s:
            print('{} {}'.format(self.p1.p, self.p1.s))
        else:
            print('{} {}'.format(self.p2.p, self.p2.s))

def minion_game(string):
    vowels = 'AEIOU'
    s_len = len(string)
    players = ['Stuart', 'Kevin']
    sb = ScoreBoard(players)
    for e in enumerate(string):
        if e[1] in vowels:
            sb.p2.score(s_len - e[0])
        else:
            sb.p1.score(s_len - e[0])
    sb.print_winner()

if __name__ == '__main__':
    s = input()
    minion_game(s)

