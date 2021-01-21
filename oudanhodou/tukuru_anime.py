import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animator(data):
    fig = plt.figure()
    ims = []
    for add in data:
        ims.append((plt.pcolor(add),))
    im_ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=300, blit=True)
# If you want save the animation
# im_ani.save('im.mp4')