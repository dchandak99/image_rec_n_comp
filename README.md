# image_rec_n_comp

Images are basically matrices. Grayscale (black and white) images can be represented using 2d numpy arrays. The value at each position of the matrix denotes the light intensity at that pixel in the image. We shall work with grayscale images, but, you can easily extend it to colored images.  Usually, each element is an 8-bit integer and its value ranges from 0 (black) to 255 (white). But, you can use default 64-bit integers for this assignment.

Just FYI, color images are 3 dimensional numpy arrays, in which, third dimension is of size 3. This third dimension stores colour. You can imagine that it is a 2d array of triplets. Each element of a triplet gives the intensity of Red, Green and Blue colour respectively.

Here is some background. Images often contain noise. One such noise is salt and pepper noise. Here, some pixels get corrupted with probability , into either black (0) or white (255).

So, here is the deal: we will give you multiple (possibly overlapping) patches (along with their locations) of an image and you have to reconstruct the original image, while minimising the noise. We will also give you the overall size of image.

Understand that each patch carries pixel values of only few locations. But, for each pixel in the (to be) reconstructed image, you will get many values (likely to be distinct), from different patches. Now, the challenge is to decide which value do we put inside that pixel location.

Here is an algo that you shall follow at each pixel of (to be) reconstructed image:

Let i_1, i_2… i_m be ‘m’ values that you get for a pixel. We will scan them sequentially (this is equivalent to saying that we will see patches sequentially) and maintain 4 values. Let’s call them black_count, mid_count, white_count, mid_total. Suppose that we have scanned till i_t. At this point:

black_count is the number of times, we encountered a 0.

white_count is number of times we encountered 255.

mid_count is the number of times we encountered something between 0 and 255 (both exclusive).

mid_total is the sum of such values.

Once you have scanned all the patches, if mid_count is non-zero, the final value shall be the (mid_total / mid_count) (rounded to nearest non-negative int < 256). Otherwise, it will be 0 or 255, depending on whether black_count is > white_count (which implies, if black_count <= white_count, put 255, else, put 0).

Note: black_count <= white_count will also happen when no patch has fallen on a pixel. But, in this case, put a 0 (not 255).

You have to do this at every pixel location in an image. There might be some pixels where no patches fall! Put 0 (black) there.

You should write a function named reconstruct_from_noisy_patches and save it into a file named task 2.py.

The signature of reconstruct_from_noisy_patches should be:

def reconstruct_from_noisy_patches(input_dict, shape):

        """

input_dict:

key: 4-tuple: (topleft_row, topleft_col, bottomright_row, bottomright_col): location of the patch in the original image. topleft_row, topleft_col are inclusive but bottomright_row, bottomright_col are exclusive. i.e. if M is the reconstructed matrix. M[topleft_row:bottomright_row, topleft_col:bottomright_col] will give the patch.

value: 2d numpy array: the image patch.

shape: shape of the original matrix.

"""

# return the reconstructed image

Note: you can use loops only to iterate over different patches.


Task 3:::

We can represent colours fairly accurately as a  combination of Red, Green and Blue. In a grayscale image, we use a 2d matrix to represent the brightness of the pixel at different locations. Similarly, we can use 3 different 2d matrices to denote intensities of R, G and B colours respectively, to represent a colourful image. These 3 matrices are called colour channels, or simply, channels. These channels are stacked over each other to make a 3d array. So, basically, a colourful image can be represented as a 3d matrix, whose 3rd dimension denotes colours. In the case of a grayscale image, each pixel is a scalar intensity. But, for coloured images, each pixel is a 3d vector, whose components denote the intensities of RGB colours.

In this task, we would group colours to get 'flatter' but cool images. We would take advantage of the fact that colours are nothing but vectors.

There are various algorithms, which can be used to group vectors. We shall use KMeans++
