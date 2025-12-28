import matplotlib.pyplot as plt
import numpy as np

NUM_SIMULATIONS = 1_000_000

ANALYTICAL_PROBS = {
    2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36, 7: 6 / 36,
    8: 5 / 36, 9: 4 / 36, 10: 3 / 36, 11: 2 / 36, 12: 1 / 36
}


def monte_carlo_simulation(n: int) -> dict[int, float]:
    dice1 = np.random.randint(1, 7, n)
    dice2 = np.random.randint(1, 7, n)
    sums = dice1 + dice2
    unique, counts = np.unique(sums, return_counts=True)
    return {s: c / n for s, c in zip(unique, counts)}


def print_comparison_table(mc_probs: dict[int, float]) -> None:
    print(f"\n{'Сума':^6}|{'Монте-Карло':^14}|{'Аналітична':^14}")
    print("-" * 36)
    for s in range(2, 13):
        mc = mc_probs.get(s, 0) * 100
        an = ANALYTICAL_PROBS[s] * 100
        print(f"{s:^6}|{mc:^14.2f}%|{an:^14.2f}%")


def plot_results(mc_probs: dict[int, float]) -> None:
    sums = list(range(2, 13))
    mc_values = [mc_probs.get(s, 0) * 100 for s in sums]
    an_values = [ANALYTICAL_PROBS[s] * 100 for s in sums]

    x = np.arange(len(sums))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width / 2, mc_values, width, label='Монте-Карло', color='steelblue')
    ax.bar(x + width / 2, an_values, width, label='Аналітична', color='coral')
    ax.set_xlabel('Сума двох кубиків')
    ax.set_ylabel('Ймовірність (%)')
    ax.set_title(f'Порівняння методу Монте-Карло з аналітичним розрахунком (n={NUM_SIMULATIONS:,})')
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()
    plt.tight_layout()
    plt.savefig('monte_carlo_results.png', dpi=150)
    plt.show()


if __name__ == "__main__":
    print(f"Симуляція {NUM_SIMULATIONS:,} кидків двох кубиків...")
    mc_probs = monte_carlo_simulation(NUM_SIMULATIONS)
    print_comparison_table(mc_probs)
    plot_results(mc_probs)
