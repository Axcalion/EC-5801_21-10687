#from PYYAML #
from yaml import load, dump
try: 
    from yaml import Cloader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# OS IMPORT #
from pathlib import Path

#Typing Imports #
from typing import Any, Generic, TypeVar, cast

# tipo generico
generic_t = TypeVar("generic_t")

class YAML_LOADER(Generic[generic_t]):
    
    __dict: generic_t
    
    def __init__(self) -> None:
        ...
     
        
    def load_file(self, file_path: Path) -> Any:
        
        with file_path.open() as config:
            
            config_data = load(config, Loader=Loader)
            return config_data
        
# Main entrypoint for our app #
if __name__ == "__main__":
    
    yaml_loader = YAML_LOADER()
    
    load_file = yaml_loader.load_file(Path("./config.yaml"))    

    print(load_file["config"]["test"][0])