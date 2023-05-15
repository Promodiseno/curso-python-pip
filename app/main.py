import utils
import read_csv
import charts

def run():
    chart_population()
    #dudas()

def dudas():
    countries = ['col','mex','bol','pe']
    dict2 = { i for i in countries}
    print(dict2)


def topten_population():
    import random
    #dict2 = { i:i*2 for i in range(1,5)}
    countries = ['col','mex','bol','pe']
    population = {}
    for country in countries:
        population[country] = random.randint(1,100)
    items = list(population.items())
    print(items)
    #sortedkeys = sorted(items)
    #print(sortedkeys)
    #sorted_countries = {}
    #for key in sortedkeys:
    #    sorted_countries[key] = population[key]
    #print(sorted_countries)
    

    #print(list(range(1,5)))

def mayor_porcentaje_poblacional():
    data = read_csv.read_csv('./data.csv')
    percentages = list(map(lambda i:i['World Population Percentage'], data))
    countries = list(map(lambda i:i['Country/Territory'], data))
    charts.generate_pie_chart(countries, percentages )

def chart_population():
    data = read_csv.read_csv('./data.csv')
    country = input('Type Country =>')
    countryn = country
    result = utils.population_by_country(data,country)
    if len(result) > 0:
        country = result[0]
        print(countryn)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(countryn,labels, values)

if __name__ == '__main__': #ejecuta solo si se manda a llamar directamente en la terminal mientras no
    run()
