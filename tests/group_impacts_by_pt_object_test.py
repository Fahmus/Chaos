from nose.tools import *
from chaos import utils

class Obj(object):
    pass

def get_pt_object(uri, object_type):
    return [{'name': 'aaa'}]


def test_impacts_by_pt_object_type():
    navitia = Obj()
    navitia.get_pt_object = get_pt_object
    impacts = []
    one_impact = Obj()
    one_impact.id='1'
    one_impact.objects = []
    one_pt_object = Obj()
    one_pt_object.uri='A'
    one_pt_object.type='stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri='b'
    one_pt_object.type='stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri='c'
    one_pt_object.type='stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri='c'
    one_pt_object.type='network'
    one_impact.objects.append(one_pt_object)

    impacts.append(one_impact)

    result = utils.group_impacts_by_pt_object(impacts, 'stop_area', navitia)
    eq_(len(result), 3)

    result = utils.group_impacts_by_pt_object(impacts, 'network', navitia)
    eq_(len(result), 1)


