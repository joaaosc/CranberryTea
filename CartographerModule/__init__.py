import geopandas as gpd
import plotly.express as px


class RJ_Map:
    def __init__(self, zip_file: str = r'./RJ_Municipios_2022.zip'):
        self.zip_file = zip_file

    def load_map(self):
        ''' Load map from path defined on the __init__'''
        gdf = gpd.read_file('zip://' + self.zip_file) # importa o mapa de um arquivo .zip
        return gdf

    def plot_map(self):
        ''' Plot the map. '''
        gdf = self.load_map()
        fig = px.choropleth(gdf, geojson=gdf.geometry,
                            locations=gdf.index, color="AREA_KM2",
                            projection="mercator", title="Municípios Rio de Janeiro")
        fig.update_geos(showcountries=False, showcoastlines=True, showland=True, fitbounds="locations")
        fig.show()