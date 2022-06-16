__version__ = '0.9.4'

from .getter import Getter
from .core import App, Security

# backward compatible
SwaggerApp = App
SwaggerSecurity = Security
SwaggerAuth = SwaggerSecurity

