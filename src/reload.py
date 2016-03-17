

def load(path, name):
    partner = {}
    for line in open(path + '/' + name + '.txt'):
        (id, title) = line.split('\t')[0:2]
        partner[title] = id
    return partner


load1 = load('/Users/yupeng/Downloads/aip_partner_account_index', 'sum')
print load1
