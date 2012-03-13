#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import optparse
import csv
import re
import datetime as dt
from random import choice
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
marker_styles = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p',
    '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_']

split_re = re.compile('[;,]')

class Graph(object):

    sub_categories = ['CPU', 'INTR', 'DEV', 'IFACE']

    def __init__(self, options):
        self.input_filename = options.input_file
        self.output_dir = options.output_dir
        self.is_csv = options.is_csv
        self.is_stat = options.is_stat
        self.is_minor = options.is_minor

        try:
            self.input_file = open(self.input_filename)
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
                try:
                    self.generate()
                except ValueError:
                    print "Error generate graph"

                self.header = split_re.split(line.strip())
                self.temp = []
            else:
                self.temp.append(split_re.split(line.strip()))

        try:
            self.generate()
        except ValueError:
            print "Error generate graph"


    def gen_title(self):
        if self.header:
            return '__'.join(self.header[3:]).replace('/', '-per-')
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
            f = open(os.path.join(self.output_dir, "%s.csv" % self.gen_title()),
                    'wt')
            writer = csv.writer(f)
            writer.writerows([self.header] + self.temp)
            f.close()

        i = 0

        if self.header[3] in self.sub_categories:
            k = -1
            categories = defaultdict(list)
            for item in self.temp:
                categories[item[3]].append(item)

            for category in sorted(categories)[:10]:
                i = 0
                k += 1
                for j in range(4, len(self.header)):
                    list_date = []
                    list_value = []

                    for item in categories[category]:
                        # import pdb; pdb.set_trace()
                        list_date.append(
                        dt.datetime.strptime(item[2], '%Y-%m-%d %H:%M:%S UTC'))
                        list_value.append(item[j])

                    if k == len(line_styles):
                        k = 0
                        i += 1

                    ax.plot_date(mpl.dates.date2num(list_date),
                        list_value, linestyle=line_styles[k],
                        label='%s %s %s' % (self.header[3], category,
                            self.header[j]), c=color_scheme20[i],
                        marker=choice(marker_styles))

                    if self.is_stat:
                        list_value = map(float, list_value)
                        f = open(os.path.join(
                            self.output_dir, "%s.txt" % self.gen_title()), 'a')
                        f.write('%s %s %s max : %s \n' % (self.header[3], 
                            category, self.header[j], max(list_value)))
                        f.write('%s %s %s min : %s \n' % (self.header[3], 
                            category, self.header[j], min(list_value)))
                        f.write('%s %s %s avg : %s \n' % (self.header[3], 
                            category, self.header[j], 
                            sum(list_value)/float(len(list_value))))
                        f.close()

                    i += 1

        else:
            for j in range(3, len(self.header)):
                list_date = []
                list_value = []

                for item in self.temp:
                    list_date.append(
                        dt.datetime.strptime(item[2], '%Y-%m-%d %H:%M:%S UTC'))
                    list_value.append(item[j])

                ax.plot_date(mpl.dates.date2num(list_date),
                        list_value, linestyle='-',
                        label=self.header[j], c=color_scheme20[i],
                        marker=choice(marker_styles))

                if self.is_stat:
                    list_value = map(float, list_value)
                    f = open(os.path.join(
                        self.output_dir, "%s.txt" % self.gen_title()), 'a')
                    f.write('%s max : %s \n' % (self.header[j], max(list_value)))
                    f.write('%s min : %s \n' % (self.header[j], min(list_value)))
                    f.write('%s avg : %s \n' % (self.header[j], 
                        sum(list_value)/float(len(list_value))))
                    f.close()

                i += 1

        ax.grid(True)
        minute_fmt = mpl.dates.DateFormatter('%H:%M')
        ax.xaxis.set_major_formatter(minute_fmt)

        minute_loc = mpl.dates.MinuteLocator()
        ax.xaxis.set_major_locator(minute_loc)

        if self.is_minor:
            second_fmt = mpl.dates.DateFormatter('%S')
            second_loc = mpl.dates.SecondLocator(bysecond=range(10, 60, 10))
            ax.xaxis.set_minor_formatter(second_fmt)
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

        #plt.show()
        plt.savefig(os.path.join(self.output_dir, "%s.png" % self.gen_title()))


def main():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--input', action='store', dest='input_file', 
        type='string')
    parser.add_option('-o', '--ouput', action='store', dest='output_dir', 
        type='string')
    parser.add_option('--csv', action='store_true', dest='is_csv',
        default=False)
    parser.add_option('--stat', action='store_true', dest='is_stat',
        default=False)
    parser.add_option('--minor', action='store_true', dest='is_minor',
        default=False)
    parser.add_option('--height', action='store', dest='height', type='float',
        default=15.0)
    parser.add_option('--width', action='store', dest='width', type='float',
        default=60.0)

    options, remainder = parser.parse_args(sys.argv)

    mpl.rcParams['figure.figsize'] = [options.width, options.height]
    mpl.rcParams['savefig.dpi'] = 100

    if not options.input_file or not options.output_dir:
        parser.print_help()
        sys.exit(2)

    graph = Graph(options)
    graph.process()


if __name__ == '__main__':
    main()

