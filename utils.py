def get_consoles_by_generation(data, generation):
    result = list(filter(lambda item: item['Generation'] == generation, data))
    return result