This repository is the implementation on image object transfiguration with CelebA dataset of batch and one-sided label smoothing:

Following are the result for speed up(batch) and optimization(one-sided label smoothing):

First, the following is the result for batch_size V.S. loss. It looks similar with the result of our baseline which 64 works best.

![alt text](https://github.com/YanW1222/ATIDIC/blob/master/image_object_transfiguration/plot_result/batch.png)

And also for one sided-label smoothing:

![alt text](https://github.com/YanW1222/ATIDIC/blob/master/image_object_transfiguration/plot_result/smoothing.png)

The light blue line represent without smoothing and dark blue line represent with one-sided label smoothing. We can see from the plot that the line for one-sided label smoothing converged much faster, reached a lower loss and much smoother than the one without smoothing.

These are the results before(upper one) V.S. the result after smoothing(lower one):

![alt text](https://github.com/YanW1222/ATIDIC/blob/master/image_object_transfiguration/img_result/without%20smoothing.png)

![alt text](https://github.com/YanW1222/ATIDIC/blob/master/image_object_transfiguration/img_result/with%20smoothing.png)

We can see that the upper one(without smoothing) cannot swap the figure "Bangs" for the right image perfectly compared with the lower one which can transfigure the "Bangs" much better.
