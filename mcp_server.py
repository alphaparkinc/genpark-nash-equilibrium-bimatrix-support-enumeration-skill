"""
MCP Server for Bimatrix Nash Equilibrium Solver Skill
"""

import json
import sys
from client import BimatrixNashSolver

def handle_call(name: str, args: dict) -> dict:
    if name == "find_nash_equilibria":
        p1_act = args.get("p1_actions", ["C", "D"])
        p2_act = args.get("p2_actions", ["C", "D"])
        p1_u = args.get("p1_payoffs", [[3.0, 0.0], [5.0, 1.0]])
        p2_u = args.get("p2_payoffs", [[3.0, 5.0], [0.0, 1.0]])
        solver = BimatrixNashSolver(p1_act, p2_act, p1_u, p2_u)
        pure = solver.find_pure_nash_equilibria()
        mixed = solver.solve_2x2_mixed_nash()
        return {"pure_equilibria": pure, "mixed_equilibrium": mixed}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
