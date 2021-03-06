from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from compas.numerical import fd_numpy


__all__ = [
    'relax_boundary_openings',
    'relax_boundary_openings_proxy',
]


def relax_boundary_openings_proxy(formdata, fixed):
    from compas_tna.diagrams import FormDiagram
    form = FormDiagram.from_data(formdata)
    relax_boundary_openings(form, fixed)
    return form.to_data()


def relax_boundary_openings(form, fixed):
    """"""
    k_i = form.key_index()
    xyz = form.vertices_attributes('xyz')
    edges = [(k_i[u], k_i[v]) for u, v in form.edges()]
    fixed = [k_i[key] for key in fixed]
    q = form.edges_attribute('q')
    loads = form.vertices_attributes(('px', 'py', 'pz'))

    xyz, q, f, l, r = fd_numpy(xyz, edges, fixed, q, loads)

    for key, attr in form.vertices(True):
        index = k_i[key]
        attr['x'] = xyz[index][0]
        attr['y'] = xyz[index][1]
        attr['z'] = xyz[index][2]
