import image_mat_util as imu
import transform as tf


# 4.15.4

imu.image2display(imu.file2image("py.png"))

# 4.15.5

imu.mat2display((tf.identity() * imu.file2mat("py.png")[0]), imu.file2mat("py.png")[1])

# 4.15.6

imu.mat2display((tf.translation(2,3) * imu.file2mat("py.png")[0]), imu.file2mat("py.png")[1])

# scaling test

imu.mat2display((tf.scale(2,3) * imu.file2mat("py.png")[0]), imu.file2mat("py.png")[1])

# rotation test

imu.mat2display((tf.rotation(0.523599) * imu.file2mat("py.png")[0]), imu.file2mat("py.png")[1])

