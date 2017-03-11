import tensorflow as tf

node1=tf.placeholder(tf.float32)
node2=tf.placeholder(tf.float32)
sum=tf.add(node1,node2)
sess=tf.Session()
print(sess.run(sum,{node1:6,node2:8}))
