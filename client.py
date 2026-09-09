"""
Bimatrix Nash Equilibrium Solver Skill Client
Pure Python Standard Library implementation of bimatrix normal-form game solvers.
Identifies pure-strategy Nash equilibria via mutual best-response intersection and computes
mixed-strategy Nash equilibria for 2x2 games via indifference equations.
"""

from typing import List, Tuple, Dict, Any, Optional


class BimatrixNashSolver:
    def __init__(self, p1_actions: List[str], p2_actions: List[str], p1_payoffs: List[List[float]], p2_payoffs: List[List[float]]):
        self.p1_actions = list(p1_actions)
        self.p2_actions = list(p2_actions)
        self.A = p1_payoffs  # rows: p1, cols: p2
        self.B = p2_payoffs

    def find_pure_nash_equilibria(self) -> List[Tuple[str, str, float, float]]:
        """Find all pure strategy Nash equilibria: mutual best responses."""
        pure_ne = []
        n_rows = len(self.p1_actions)
        n_cols = len(self.p2_actions)
        for i in range(n_rows):
            for j in range(n_cols):
                p1_best = all(self.A[i][j] >= self.A[k][j] for k in range(n_rows))
                p2_best = all(self.B[i][j] >= self.B[i][l] for l in range(n_cols))
                if p1_best and p2_best:
                    pure_ne.append((self.p1_actions[i], self.p2_actions[j], self.A[i][j], self.B[i][j]))
        return pure_ne

    def solve_2x2_mixed_nash(self) -> Optional[Dict[str, Any]]:
        """Solve mixed Nash equilibrium for a 2x2 game via expected payoff indifference."""
        if len(self.p1_actions) != 2 or len(self.p2_actions) != 2:
            return None

        # Solve for q (P2's probability on col 0) making P1 indifferent between rows 0 and 1
        denom_q = (self.A[0][0] - self.A[0][1] - self.A[1][0] + self.A[1][1])
        num_q = self.A[1][1] - self.A[0][1]
        if denom_q == 0:
            return None
        q = num_q / denom_q

        # Solve for p (P1's probability on row 0) making P2 indifferent between cols 0 and 1
        denom_p = (self.B[0][0] - self.B[1][0] - self.B[0][1] + self.B[1][1])
        num_p = self.B[1][1] - self.B[1][0]
        if denom_p == 0:
            return None
        p = num_p / denom_p

        if 0.0 <= p <= 1.0 and 0.0 <= q <= 1.0:
            return {
                "p1_strategy": {self.p1_actions[0]: p, self.p1_actions[1]: 1.0 - p},
                "p2_strategy": {self.p2_actions[0]: q, self.p2_actions[1]: 1.0 - q}
            }
        return None
