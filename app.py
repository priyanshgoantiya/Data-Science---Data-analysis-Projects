import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters from the screenshot
n_tosses = 100  # Number of coin tosses
observed_heads = 53  # Observed number of heads
p_fair = 0.5  # Probability of heads for a fair coin (null hypothesis)

# Calculate the probability of exactly observed_heads
prob_exact = binom.pmf(observed_heads, n_tosses, p_fair)
print(f"Probability of getting exactly {observed_heads} heads in {n_tosses} tosses: {prob_exact:.4f}")

# Calculate p-value (two-tailed test)
# Sum probabilities from 0 to observed_heads and from n_tosses to observed_heads (symmetric)
p_value = binom.cdf(observed_heads, n_tosses, p_fair) + (1 - binom.cdf(n_tosses - observed_heads, n_tosses, p_fair))
if observed_heads > n_tosses / 2:
    p_value = 2 * (1 - binom.cdf(observed_heads - 1, n_tosses, p_fair))
else:
    p_value = 2 * binom.cdf(observed_heads, n_tosses, p_fair)
print(f"P-value: {p_value:.4f}")

# Decision based on p-value (assuming alpha = 0.05)
alpha = 0.05
if p_value > alpha:
    decision = "Fail to reject the null hypothesis: There is not enough evidence to conclude that the coin is not fair."
else:
    decision = "Reject the null hypothesis: There is enough evidence to conclude that the coin is not fair."
print(decision)

# Plot binomial distribution
x = np.arange(0, n_tosses + 1)
y = binom.pmf(x, n_tosses, p_fair)

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='blue', alpha=0.7, label='Binomial Distribution')
plt.bar(observed_heads, binom.pmf(observed_heads, n_tosses, p_fair), color='red', alpha=0.7, label=f'Observed: {observed_heads} heads')
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Binomial Distribution of Coin Tosses')
plt.legend()
plt.text(0.5, 0.95, f'P-value: {p_value:.4f}', transform=plt.gca().transAxes, verticalalignment='top')
plt.grid(True, alpha=0.3)
plt.show()
