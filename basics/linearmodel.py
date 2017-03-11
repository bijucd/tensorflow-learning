import tensorflow as tf
W=tf.Variable([-1.0],tf.float32)
b=tf.Variable([1.0],tf.float32)
x=tf.placeholder(tf.float32)
linear_model=W*x+b
sess=tf.Session()
init=tf.global_variables_initializer()
sess.run(init)
y = tf.placeholder(tf.float32)

squared_deltas= tf.square(linear_model - y)

loss = tf.reduce_sum(squared_deltas)

print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
