# Weather Prediction using Bayesian Probability

# Dataset
total_days = 20
rain = 8
not_rain = 12

cloudy_rain = 7
cloudy_not_rain = 3

# Prior probabilities
p_rain = rain / total_days
p_not_rain = not_rain / total_days

# Conditional probabilities
p_cloudy_given_rain = cloudy_rain / rain
p_cloudy_given_not_rain = cloudy_not_rain / not_rain

# Probability of Cloudy
p_cloudy = (
    p_cloudy_given_rain * p_rain
    + p_cloudy_given_not_rain * p_not_rain
)

# Bayes' Theorem
p_rain_given_cloudy = (
    p_cloudy_given_rain * p_rain
) / p_cloudy

p_not_rain_given_cloudy = (
    p_cloudy_given_not_rain * p_not_rain
) / p_cloudy

# Display results
print("P(Rain) =", round(p_rain, 2))
print("P(Not Rain) =", round(p_not_rain, 2))
print("P(Cloudy | Rain) =", round(p_cloudy_given_rain, 2))
print("P(Cloudy | Not Rain) =", round(p_cloudy_given_not_rain, 2))
print("P(Rain | Cloudy) =", round(p_rain_given_cloudy, 2))
print("P(Not Rain | Cloudy) =", round(p_not_rain_given_cloudy, 2))

# Prediction
if p_rain_given_cloudy > p_not_rain_given_cloudy:
    prediction = "Rain"
else:
    prediction = "Not Rain"

print("Predicted Weather =", prediction)