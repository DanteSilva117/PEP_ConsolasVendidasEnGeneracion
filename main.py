import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')
    generation = input('Type Generation => ')
    result = utils.get_consoles_by_generation(data, generation)
    
    if len(result) > 0:
        labels = [item['Primary consoles'] for item in result]
        values = [int(item['Total Systems Sold'].replace(",", "").strip()) for item in result]
        charts.generate_bar_chart(labels, values, generation)
    else:
        print(f"No data found for {generation}")

if __name__ == '__main__':
    run()
