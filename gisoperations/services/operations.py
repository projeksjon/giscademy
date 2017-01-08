from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import MultiPolygon

from gisoperations.services.buffers import with_metric_buffer
from layers.models import Polygon, Point, LineString


class OperationsMixin(object):

    @staticmethod
    def get_layer(json):
        ds = DataSource(json)
        return ds[0]

    @staticmethod
    def extract_properties(feature):
        fields = feature.fields
        properties = {}
        for field in fields:
            name = field.decode('UTF-8')
            properties[name] = feature.get(name)
        return properties

    @staticmethod
    def difference_features(json, layer, **kwargs):
        ds = DataSource(json)
        geoms = ds[0].get_geoms(geos=True)
        base_geom = geoms[0]
        for geom in geoms[1:]:
            base_geom = base_geom.difference(geom)
        Polygon.objects.create(geom=MultiPolygon(base_geom), layer=layer)
        return layer

    @staticmethod
    def unite_features(json, layer, **kwargs):
        ds = DataSource(json)
        geoms = ds[0].get_geoms(geos=True)
        base_geom = geoms[0]
        for geom in geoms[1:]:
            base_geom = base_geom.union(geom)
        Polygon.objects.create(geom=MultiPolygon(base_geom), layer=layer)
        return layer

    @staticmethod
    def add_all_features_to_layer(json, layer, **kwargs):
        """
        Add all the features in the json to a single layer.
        """
        lyr = OperationsMixin.get_layer(json)
        for feature in lyr:
            geom_type = feature.geom_type
            type_name = geom_type.name
            geos = feature.geom.geos
            properties = OperationsMixin.extract_properties(feature)
            if type_name == 'Point':
                Point.objects.create(geom=geos, layer=layer, properties=properties)
            elif type_name == 'LineString':
                LineString.objects.create(geom=geos, layer=layer, properties=properties)
            elif type_name == 'Polygon':
                Polygon.objects.create(geom=MultiPolygon(geos), layer=layer, properties=properties)
            elif type_name == 'MultiPolygon':
                Polygon.objects.create(geom=geos, layer=layer, properties=properties)
        return layer

    @staticmethod
    def buffer_features(json, layer, **kwargs):
        ds = DataSource(json)
        geoms = ds[0].get_geoms(geos=True)
        for geom in geoms:
            buffered = with_metric_buffer(geom, kwargs['size'])
            Polygon.objects.create(geom=MultiPolygon(buffered), layer=layer)

        return layer

    @staticmethod
    def intersect_features(json, layer, **kwargs):
        ds = DataSource(json)
        geoms = ds[0].get_geoms(geos=True)
        base_geom = geoms[0]

        for geom in geoms[1:]:
            base_geom = base_geom.intersection(geom)

        try:
            geom = MultiPolygon(base_geom)
        except:
            return None
        Polygon.objects.create(geom=geom, layer=layer)
        return layer
