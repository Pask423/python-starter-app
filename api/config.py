import os

import hydra
from hydra import compose

hydra.initialize_config_dir(config_dir=os.getenv('GREETER_CONFIG_DIR'))

api_config = compose(config_name='config')
