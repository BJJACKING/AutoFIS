import socket

config = {}
# config['data_path'] = '/newNAS/Datasets/path'  #add your path here
config['data_path'] = '/home/mi/mi/work/data/appStore/autoFIS/avazu/avazu/Avazu'  #add your path here

host = socket.gethostname()
config['host'] = host.lower()

# config['env'] = 'gpu'
config['env'] = 'cpu'
config['dtype'] = 'float32'
config['scale'] = 0.001
config['minval'] = - config['scale']
config['maxval'] = config['scale']
config['mean'] = 0
config['stddev'] = 0.001
config['sigma'] = config['stddev']
config['const_value'] = 0
config['rnd_type'] = 'uniform'
config['factor_type'] = 'avg'
config['magnitude'] = 3

