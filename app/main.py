import utils 
import read_csv as read_csv
import charts


def run():
    data = read_csv.read_csv('data.csv')
    

    
    data = [item for item in data if item["Continent"] == "South America"]
    
    countries = [item["Country/Territory"] for item in data]
    percentages = [item["World Population Percentage"]for item in data]
   
    charts.generate_pie_chart(countries, percentages)
    
    country = input('Escribe el pais => ').capitalize()
    
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country["Country/Territory"], labels, values)
     

if __name__ == '__main__': #* Permite ejecutar el archivo desde la terminal si se ejecuta directamente en la terminal
    run()