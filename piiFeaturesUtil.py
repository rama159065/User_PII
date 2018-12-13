

import re
import string

output_field =['has_dot','dot_count','is_ip_pattern','has_no_alpha','is_numeric',
               'field_len','is_ip_in_range','has_at','domain_sep_count','has_dot_aft_at',
               'is_min_len','is_email_pattern','has_hyphen','has_bracket','has_curley_bracket''is_alpha_num',
               'is_hexa_decimal','is_guid_pattern','has_plus','is_num_in_range','label']

def has_curley_brackets(data):
    c = re.compile('^[{}]')
    try:
        if (bool(c.match(data))):
            return 1
        else:
            return 0
    except:
        return 0

def has_bracket(data):
    c = re.compile('^[()]')
    try:
        if (bool(c.match(data))):
            return 1
        else:
            return 0
    except:
        return 0

def is_num_in_range(data):
    nums = getOnlyDigits(data)
    if(len(nums) >=10 and len(nums)<= 15):
        return 1
    return 0

def getOnlyDigits(data):
    nums = re.sub('[^0-9]', '', data)
    return nums;

def has_plus(data):
    try:
        return 1 if data[0]=='+' else 0
    except:
        return 0

def is_guid_pattern(data):
    #c = re.compile('[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', re.I)
    c = re.compile('[0-9a-fA-F]{8}[0-9a-fA-F]{4}[0-9a-fA-F]{4}[0-9a-fA-F]{4}[0-9a-fA-F]{12}', re.I)
    res = c.match(data)
    if res:
        return 1
    return 0


def is_hexa_decimal(data):
    if (all(c in string.hexdigits for c in data)):
        return 1
    return 0


def is_alpha_num(data):
    try:
        if (data.isalnum()):
            return 1
        else:
            return 0
    except:
        return 0

def has_hyphen(data):
    if ('-' in data):
        return 1
    return 0

def is_email_pattern(data):
    c = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', re.I)
    res = c.match(data)
    if res:
        return 1
    return 0

def is_min_len(data):
    if(len(data) > 7):
        return 1
    return 0


def has_dot_aft_at(data):
    try:
        if (data.index('@') > 0):
            subset_aft_at = data[data.index('@') + 1:]
            if dot_count(subset_aft_at) > 0:
                return 1
            else:
                return 0
    except:
        return 0

def domain_sep_count(data):
    try:
        return data.count('@')
    except:
        return 0

def has_dot(data):
    if('.' in data):
        return 1
    return 0

def dot_count(data):
    try:
        return data.count('.')
    except:
        return 0

def is_ip_pattern(data):
    ippattern = '([1-2]?[0-9]?[0-9]\.){1,3}([1-2]?[0-9]?[0-9])?'
    try:
        return  1 if re.match(ippattern, data) else 0
    except:
        return 0

def has_no_alpha(data):
    if (bool(re.search('[a-zA-Z]+', data))):
        return 0
    return 1


def is_numeric(data):
    try :
        if(data.isdigit()):
            return 1
        else:
            return 0
    except:
        return 0


def get_field_length(data):
    try :
        return len(data)
    except:
        return 0

def is_ip_in_range(data):
    tokens = getTokens(data)
    fields = []
    for token in tokens:
        try:
            if(int(token) > 255):
                fields.append(token)
        except:
            return 0
    if (any(fields)):
        return 0
    return 1

def getTokens(data):
    return data.split('.')

def has_at(data):
    if('@' in data):
        return 1
    return 0