def mps_to_kph(mps):
    """
    Convert speed from meters per second (mps) to kilometers per hour (kph).
    """
    meters_to_km = 1000
    seconds_to_hours = 3600
    return (mps / meters_to_km) * seconds_to_hours
