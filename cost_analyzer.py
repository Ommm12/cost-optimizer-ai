def analyze_cost(data):
    insights = []

    for day in data['ResultsByTime']:
        date = day['TimePeriod']['Start']
        cost = float(day['Total']['UnblendedCost']['Amount'])

        if cost > 1:
            insights.append(f"{date}: High cost ${cost}")
        elif cost == 0:
            insights.append(f"{date}: No usage detected")

    return insights