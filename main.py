# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    kernel = 3
    stack = 3
    layer = 8
    receptive_field = 0

    for s in range(stack): # 3
        for i in range(layer): # 8
            if i == 0 and s == 0:
                receptive_field += kernel
            else:
                receptive_field += (kernel - 1) * 2 ** i

    print("Receptive field: {:3d} frames.".format(receptive_field))
