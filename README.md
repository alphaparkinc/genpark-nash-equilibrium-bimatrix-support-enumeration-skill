# GenPark Bimatrix Nash Equilibrium Solver Skill

Bimatrix normal-form game solver computing pure and mixed Nash equilibria.

Explore more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph LR
    M[Payoff Matrices A & B] --> P[Mutual Best-Response Check]
    P --> NE1[Pure Nash Equilibria]
    M --> I[Indifference Equations]
    I --> NE2[Mixed Strategy Probabilities p & q]
    style M fill:#e1f5fe
    style P fill:#fff9c4
    style NE1 fill:#c8e6c9
    style I fill:#ffcdd2
    style NE2 fill:#d1c4e9
```

## Features
- Pure strategy Nash equilibrium detection across arbitrary finite bimatrix games.
- Exact mixed strategy indifference solving for 2x2 strategic games.
- Pure Python standard library.
