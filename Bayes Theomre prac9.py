
P_cloudy = float(input("Enter P(cloudy): "))
P_rain = float(input("Enter P(rain): "))
P_cloudy_given_rain = float(input("Enter P(cloudy | rain): "))

P_rain_given_cloudy = (P_rain * P_cloudy_given_rain) / P_cloudy


print("\n∙ P (rain | cloudy) =", P_rain, "*", P_cloudy_given_rain, "/", P_cloudy)

print("\n∙ P (rain | cloudy) =", round(P_rain_given_cloudy,3))

print("\n∙ If it’s cloudy outside on a given day, the probability that it will rain that day is",
      round(P_rain_given_cloudy*100,1), "%")