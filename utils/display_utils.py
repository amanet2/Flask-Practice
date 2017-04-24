def show_weather_report(report: dict,desired_reportings: dict) -> dict:
    pretty_report = {}
    pretty_report['city'] = report['name']
    for field in desired_reportings:
        result = report[field]
        if field == 'weather':
            pretty_report['overall'] = result[0]["main"]
        elif field == 'main':
            pretty_report['high_low'] = f'{result["temp_max"]} / {result["temp_min"]}f'
            pretty_report['temp'] = f'{result["temp"]}f'
            pretty_report['pressure'] = f'{result["pressure"]} hPa'
            pretty_report['humidity'] = f'{result["humidity"]} %'
        elif field == 'wind':
            pretty_report['wind'] = f'{result["speed"]}mph - {result["deg"]}deg'
        elif field == 'visibility':
            pretty_report['visibility'] = f'{result}m'
        else:
            pretty_report[field] = result
    return pretty_report