"""
Demonstration of Bimatrix Nash Equilibrium Solver Skill
"""

from client import BimatrixNashSolver

def main():
    print("=== Bimatrix Normal-Form Game Nash Equilibrium Solving ===")

    # Game 1: Prisoner's Dilemma (Pure Nash Equilibrium at Defect, Defect)
    pd_game = BimatrixNashSolver(
        p1_actions=["Cooperate", "Defect"],
        p2_actions=["Cooperate", "Defect"],
        p1_payoffs=[[3.0, 0.0], [5.0, 1.0]],
        p2_payoffs=[[3.0, 5.0], [0.0, 1.0]]
    )

    pure_equilibria = pd_game.find_pure_nash_equilibria()
    print("Prisoner's Dilemma Pure Nash Equilibria:")
    for p1_act, p2_act, u1, u2 in pure_equilibria:
        print(f"  ({p1_act}, {p2_act}) with payoffs ({u1}, {u2})")

    assert len(pure_equilibria) == 1
    assert pure_equilibria[0][0] == "Defect" and pure_equilibria[0][1] == "Defect"

    # Game 2: Matching Pennies (Zero-Sum, No Pure NE, Unique Mixed NE at 50/50)
    mp_game = BimatrixNashSolver(
        p1_actions=["Heads", "Tails"],
        p2_actions=["Heads", "Tails"],
        p1_payoffs=[[1.0, -1.0], [-1.0, 1.0]],
        p2_payoffs=[[-1.0, 1.0], [1.0, -1.0]]
    )

    mp_pure = mp_game.find_pure_nash_equilibria()
    assert len(mp_pure) == 0

    mp_mixed = mp_game.solve_2x2_mixed_nash()
    print("\nMatching Pennies Mixed Strategy Nash Equilibrium:")
    print(f"  P1 Strategy: {mp_mixed['p1_strategy']}")
    print(f"  P2 Strategy: {mp_mixed['p2_strategy']}")

    assert abs(mp_mixed["p1_strategy"]["Heads"] - 0.5) < 1e-6
    assert abs(mp_mixed["p2_strategy"]["Heads"] - 0.5) < 1e-6

    print("\nBimatrix Nash Equilibrium Solver Verification PASS!")

if __name__ == "__main__":
    main()
