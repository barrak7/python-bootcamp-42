import time
from datetime import date

print(
    f"Seconds since January 1, 1970: {time.time():,.4f}"
    f" or {time.time():.2e} in scientific notation"
)
print(date.today().strftime("%b %d %Y"))
