This repository is the start-up trial of batch and one-sided label smoothing:

Following are the result for speed up(batch) and optimization(one-sided label smoothing):

First, according to the following plot, we can see that no matter what batch_size we choose, they all followed the same tendency.

![alt text](https://github.com/YanW1222/ATIDIC/blob/master/baseline/plot_result/loss_tendency.png)

Second, the following is the result for batch_size V.S. loss. So 64 works best for this task.

![alt text](https://github.com/YanW1222/ATIDIC/blob/master/baseline/plot_result/batch_size%20V.S.%20loss.png)

And also for the loss comparsion between with and w/o one sided-label smoothing:

![alt text](https://github.com/YanW1222/ATIDIC/blob/master/baseline/plot_result/smoothing.png)

These are the results before(upper one) V.S. the result after smoothing(lower one):

![alt text](https://github.com/YanW1222/ATIDIC/blob/master/baseline/image_generated/smoothing.jpg)

![alt text](https://github.com/YanW1222/ATIDIC/blob/master/baseline/image_generated/without%20smoothing.jpg)
