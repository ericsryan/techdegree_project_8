import string


def get_alphabet_to_context(request):
    alphabet = string.ascii_uppercase
    return {'alphabet': alphabet}


def get_groups_to_context(request):
    GROUPS = [
    'Silicates',
    'Oxides',
    'Sulfates',
    'Sulfides',
    'Carbonates',
    'Halides',
    'Sulfosalts',
    'Phosphates',
    'Borates',
    'Organic Minerals',
    'Arsenates',
    'Native Elements',
    'Other'
    ]
    return {'groups': GROUPS}


def get_colors_to_context(request):
    COLORS = [
        'Blue',
        'Green',
        'Red',
        'Purple',
        'Yellow',
        'White',
        'Black',
        'Orange',
        'Brown',
        'Grey',
    ]
    return {'colors': COLORS}


def get_fields_to_context(request):
    FIELDS = [
        'category',
        'group',
        'formula',
        'strunz_classification',
        'crystal_system',
        'mohs_scale_hardness',
        'luster',
        'color',
        'specific_gravity',
        'cleavage',
        'diaphaneity',
        'crystal_habit',
        'streak',
        'optical_properties',
        'refractive_index',
        'unit_cell',
        'crystal_symmetry'
    ]
    return {'fields': FIELDS}
