#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import optparse
import csv
import datetime as dt
from collections import defaultdict

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
fontP = FontProperties()
fontP.set_size('small')

color_scheme10 = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

color_scheme20 = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a',
    '#d62728', '#ff9896', '#9467bd', '#c5b0d5', '#8c564b', '#c49c94', '#e377c2', 
    '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

line_styles = ['-', '--', '-.', ':']


class Graph(object):

    sub_categories = ['CPU', 'INTR', 'DEV', 'IFACE']

    def __init__(self, filename, output_dir, is_csv=False):
        self.input_filename = filename
        self.output_dir = output_dir
        self.is_csv = is_csv

        try:
            self.input_file = open(filename)
        except IOError as e:
            print "%s: '%s'" % (e.strerror, e.filename)
            sys.exit(3)

        try:
            os.mkdir(self.output_dir)
        except (IOError, OSError) as e:
            print "%s: '%s'" % (e.strerror, e.filename)
            sys.exit(3)


    def process(self):
        self.temp = []
        self.header = ''

        for line in self.input_file:
            if line.startswith('#'):
                self.generate()
                self.header = line[1:].strip().split(';')[2:]
                self.temp = []
            else:
                self.temp.append(line.strip().split(';')[2:])

        self.generate()


    def gen_title(self):
        if self.header:
            return '__'.join(self.header[1:]).replace('/', '-per-')
        return ''


    def generate(self):
        if not self.temp:
            return

        print "\nrows count: %d" % len(self.temp)
        print self.gen_title()

        plt.hold(True)
        fig = plt.figure()
        ax = fig.add_subplot(111)


        if self.is_csv:
            f = open(os.path.join(self.output_dir, "%s.csv" % self.gen_title()), 'wt')
            writer = csv.writer(f)
            writer.writerows([self.header] + self.temp)

        i = 0

        if self.header[1] in self.sub_categories:
            k = -1
            categories = defaultdict(list)
            for item in self.temp:
                categories[item[1]].append(item)

            for category in sorted(categories)[:4]:
                i = 0
                k += 1
                for j in range(2, len(self.header)):
                    list_date = []
                    list_value = []

                    for item in categories[category]:
                        # import pdb; pdb.set_trace()
                        list_date.append(
                        dt.datetime.strptime(item[0], '%Y-%m-%d %H:%M:%S UTC'))
                        list_value.append(item[j])    

                    if k == len(line_styles):
                        k = 0
                        i += 1

                    ax.plot_date(mpl.dates.date2num(list_date), 
                        list_value, linestyle=line_styles[k],
                        label='%s %s %s' % (self.header[1], category, 
                            self.header[j]), c=color_scheme20[i],
                        marker='.')
                    i += 1

        else:
            for j in range(1, len(self.header)):
                list_date = []
                list_value = []

                for item in self.temp:
                    list_date.append(
                        dt.datetime.strptime(item[0], '%Y-%m-%d %H:%M:%S UTC'))
                    list_value.append(item[j])

                ax.plot_date(mpl.dates.date2num(list_date), 
                        list_value, linestyle='-',
                        label=self.header[j], c=color_scheme20[i],
                        marker='.')
                i += 1

        ax.grid(True)
        minute_fmt = mpl.dates.DateFormatter('%H:%M')
        second_fmt = mpl.dates.DateFormatter('%S')
        ax.xaxis.set_major_formatter(minute_fmt)
        ax.xaxis.set_minor_formatter(second_fmt)

        second_loc = mpl.dates.SecondLocator(bysecond=range(10, 60, 10))
        minute_loc = mpl.dates.MinuteLocator()
        ax.xaxis.set_major_locator(minute_loc)
        ax.xaxis.set_minor_locator(second_loc)


        fig.autofmt_xdate()

        ax.set_title(self.gen_title())

        plt.ylabel('Value')

        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                         box.width, box.height * 0.9])

        # Put a legend below current axis
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                  fancybox=True, shadow=True, ncol=5)

        plt.savefig(os.path.join(self.output_dir, "%s.png" % self.gen_title()))



if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-i', '--input', action='store', dest='input_file', type='string')
    parser.add_option('-o', '--ouput', action='store', dest='output_dir', type='string')
    parser.add_option('--csv', action='store_true', dest='is_csv', default=False)
    parser.add_option('--height', action='store', dest='height', type='float', default=15.0)
    parser.add_option('--width', action='store', dest='width', type='float', default=60.0)

    options, remainder = parser.parse_args(sys.argv)

    mpl.rcParams['figure.figsize'] = [options.width, options.height]
    mpl.rcParams['savefig.dpi'] = 100

    if not options.input_file or not options.output_dir:
        parser.print_help()
        sys.exit(2)

    graph = Graph(options.input_file, options.output_dir, options.is_csv)
    graph.process()
