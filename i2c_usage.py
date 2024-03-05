import ctypes
import pylibi2c


# Open i2c device @/dev/i2c-0, addr 0x50
i2c = pylibi2c.I2CDevice('/dev/i2c-0', 0x50)

# Set i2c device @/dev/i2c-0, addr 0x50, 16bits internal address
i2c = pylibi2c.I2CDevice('/dev/i2c-0', 0x50, iaddr_bytes=2)

# Set delay
i2c.delay = 10

# Set page_bytes
i2c.page_bytes = 16

# Set flags
i2c.flags = pylibi2c.I2C_M_IGNORE_NAK

# Python3
buf = bytes(256)

# Write data to i2c, buf must be read-only type
size = i2c.write(0x0, buf)

# From i2c 0x0(internal address) read 256 bytes data, using ioctl_read.
data = i2c.ioctl_read(0x0, 256)


#
