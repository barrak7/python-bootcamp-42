from load_image import ft_load
from pimp_image import ft_invert

array = ft_load("landscape.jpg")

ft_invert(array)

print(ft_invert.__doc__)
