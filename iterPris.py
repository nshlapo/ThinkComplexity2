import random as r

class Rule():
    ''' Defines a custom written rule with a step function that can play an
        iterated prisoners dilemma.

        After being initialized by the Match object, Rule.order will be assigned.

            order: 0 or 1. It represents the order of play, 0 first, 1 second,
                etc...
                It can be used to reference the proper list in history.

            Each round, the Match class provides your step function with history
                and round

                history: a list of two lists, representing the actions both
                    rules took in all previous rounds
                round: the current round of the match

         You will need to write a step function for your rule, whose inputs
            are self, history, and round. The function should return a 0 to
            defect, and a 1 to cooperate. See the examples below.
        '''
    def step(self, history, round):
        '''
        action = Your code here to determine what action your Rule will take.

        return action
        '''

#Sample Rules

class Cooperate(Rule):
    ''' Cooperate will always cooperate. '''
    def step(self, history, round):
        action = 1

        return action

class Defect(Rule):
    ''' Defect will always defect. '''
    def step(self, history, round):
        action = 0

        return action

class TitForTat(Rule):
    ''' TitForTat will replicate its opponent's last move. '''
    def step(self, history, round):
        if round == 0:
            action = 1
        else:
            action = history[(self.order+1)%2][round - 1]

        return action

class Flipper(Rule):
    ''' Flipper will alternate defections and cooperations, selecting the first
        move randomly.
    '''
    def step(self, history, round):
        if round == 0:
            self.action = r.randint(0, 1)
        else:
            self.action = (self.action+1)%2

        return self.action



class Match():
    ''' Defines a match which takes two rules and facilitates a game of iterated
        prisoner's dilemma between them.
    '''
    def __init__(self, ruleA, ruleB, length):
        ''' Init method for Match class.

            ruleA, ruleB: instances of rules
            length (int): the number of rounds to be played in this match
        '''

        order = [ruleA, ruleB]
        r.shuffle(order)

        self.rule0 = order[0]
        self.rule0.order = 0

        self.rule1 = order[1]
        self.rule1.order = 1

        self.round = 0
        self.length = length
        self.history = [[],[]]

    def run(self):
        while True:
            match.step_round()
            if match.round >= length:
                break

    def halted_run(self):
        while True:
            match.step_round()
            if match.round >= length:
                break
            print(match.history)
            print(match.score())
            input()

    def step_round(self):
        ''' Runs one round of iterated prisoners dilemma by running the step
            functions of each rule and adding them to the history, then
            advancing a round.
        '''

        action0 = self.rule0.step(self.history, self.round)
        action1 = self.rule1.step(self.history, self.round)

        if (action0 not in [0, 1]):
            raise ValueError(type(self.rule0).__name__ + 'did not provide a valid action')
        if (action1 not in [0, 1]):
            raise ValueError(type(self.rule1).__name__ + 'did not provide a valid action')

        self.history[0].append(action0)
        self.history[1].append(action1)

        self.round += 1

    def score(self):
        ''' Calculate scores for the match based on the history.

            Both cooperate (1,1): 3 points for both.
            One cooperates, one defects: 5 points for the one who defected, 0
                for the other.
            Both defect: 1 point for both.
         '''

        outcome = [[[1,1], [5,0]], [[0,5], [3,3]]]
        scoring = [0, 0]

        for i in range(len(self.history[0])):
            round_score = outcome[self.history[0][i]][self.history[1][i]]
            scoring[0] += round_score[0]
            scoring[1] += round_score[1]

        return scoring


if __name__=='__main__':

    length = 100

    ruleD = TitForTat()
    ruleE = Flipper()
    match = Match(ruleD, ruleE, length)

    match.halted_run()