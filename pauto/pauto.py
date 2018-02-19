#!/usr/bin/env python2

import gtk.gdk
import cv2

import tempfile
import shutil
import os

class PautoProgram():
    def __init__(self, template_dir):
        self.dirpath = tempfile.mkdtemp()
        self.step_number = 1
        self.template_dir = template_dir

    def cleanup(self):
        shutil.rmtree(self.dirpath)

    def screenshot(self, step_number):
        filename = "%s/step-%0.3i.png" % (self.dirpath, step_number)

        root_window = gtk.gdk.get_default_root_window()
        root_size = root_window.get_size()

        pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, root_size[0], root_size[1])
        pb = pb.get_from_drawable(root_window, root_window.get_colormap(), 0, 0, 0, 0, root_size[0], root_size[1])
        pb.save(filename, "png")

        return filename

    def has_more_steps(self):
        return os.path.isfile("%s/%0.3i.png" % (self.template_dir, self.step_number))

    def step(self):
        filename = self.screenshot(self.step_number)
        template_filename = "%s/%0.3i.png" % (self.template_dir, self.step_number)

        method = cv2.TM_SQDIFF_NORMED

        # Read the images from the file
        template = cv2.imread(template_filename, 0)
        image = cv2.imread(filename, 0)

        width, height = template.shape[::-1]

        result = cv2.matchTemplate(image, template, method)

        # We want the minimum squared difference
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Get the size of the template. This is the same size as the match.
        trows, tcols = template.shape[:2]

        top_left = min_loc
        bottom_right = (top_left[0] + width, top_left[1] + height)

        # Draw the rectangle on image
        cv2.rectangle(image, top_left, bottom_right, 255, 2)

        cv2.imshow('output', image)
        cv2.waitKey(0)

        self.step_number += 1

        return self.step_number

    def run(self):
        while self.has_more_steps():
            self.step()
        self.cleanup()
        pass

if __name__ == '__main__':
    program = PautoProgram("./templates")
    program.run()
