import numpy as np

def normal_pdf(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
 
# Values for the corn yield distribution
mu = 50  # mean yield (kg per hectare)
sigma = 10  # standard deviation (kg per hectare)
x_target = 60  # target yield

# Generate values for the PDF from (mu - 4*sigma) to (mu + 4*sigma)
x_values = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Calculate the PDF for these x values
pdf_values = normal_pdf(x_values, mu, sigma)

# Calculate cumulative probability for yields less than 60 kg using trapezoidal integration
cumulative_prob_less_than_60 = np.trapz(pdf_values[x_values < x_target], x_values[x_values < x_target])

# Calculate the probability for yields at least 60 kg
prob_at_least_60 = 1 - cumulative_prob_less_than_60

# PDF at the target yield
pdf_target = normal_pdf(x_target, mu, sigma)

# Output the results
print(f'PDF at {x_target} kg: {pdf_target:.4f}')
print(f'Probability of a farm producing at least {x_target} kg per hectare: {prob_at_least_60:.4f}')
