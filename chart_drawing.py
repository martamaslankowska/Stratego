''' times_n_nr.txt files are kept in format:
   (time, nr_of_operations, minimax_depth)
    overall_time
    player 0 score
    player 1 score
'''

import os
import re
import numpy as np
import matplotlib.pyplot as plt


def read_many_file_names(max_n):
    all_files = []
    for n_size in range(3, max_n+1):
        file_names = 'times_n' + (('0' + str(n_size)) if n_size < 10 else str(n_size)) + '_nr...txt'
        files = [f for f in os.listdir('.') if re.match(file_names, f)]
        files.insert(0, n_size)  # current n
        all_files.append(files)
    return all_files  # list of lists


def draw_both_algorithm_chart(problem_type, files):

    n_list = []  # list containing n_sizes
    score_list = []  # having [0]=n and later score of 1 player and score of second player
    time_list = []  # having [0]=n and than in i=depth having (time, std, nr_of_operations)
    overall_time_list = []  # having [0]=n and later overall times

    for i in range(len(files)):
        many_files = files[i]
        n_size = many_files[0]
        many_files = many_files[1:]

        n_list.append(n_size)
        time_list.append([(0.0, 0.0, 0)] * 7)

        if len(many_files) > 0:
            times, overall_times, score_list_i = [], [], []
            operations, depth = [], []

            for index, file_name in enumerate(many_files):
                with open(file_name) as file123:
                    f = [line.rstrip('\n') for line in file123]

                times.append(list(map(float, f[:-3:3])))
                overall_times.append(float(f[-3]))
                score_list_i.append((int(f[-2]), int(f[-1])))

                if index == 0:
                    operations = list(map(int, f[1:-3:3]))
                    depth = list(map(int, f[2:-3:3]))

            times = [val for sublist in times for val in sublist]
            length = int(len(times) / len(many_files))
            for t1 in range(length):
                l = [x for x in times[t1::length]]
                time_list[i][depth[t1]-1] = (np.average(l), np.std(l), operations[t1])

            overall_time_list.append((np.average(overall_times), np.std(overall_times)))
            score_list.append(score_list_i)

    # print(overall_time_list)
    print(score_list)


    # DRAWING AVERAGE TIMES OF PLAYING
    fig, ax = plt.subplots()

    x = n_list
    y1, e1 = zip(*overall_time_list)
    y1, e1 = list(y1), list(e1)
    print(x, y1, e1)

    ax.errorbar(x, y1, 1, ecolor='r', linestyle=':', color='b', marker='.')
    plt.xlabel('size of matrix N')
    plt.ylabel('time [seconds]')

    plt.title('Average time of game play having matrix NxN')

    # plt.xticks(x_ax)  # forces x axis to show only integers
    plt.show()
    plot_name = 'moj_wykresik.png'
    fig.savefig(plot_name)


    # DRAWING SCORE FOR A PLAY HAVING MATRIX N_xN (N_NUMBER GIVEN)
    fig, ax = plt.subplots()
    n_number = 0

    y2a = [i[0] for i in score_list[n_number]]
    y2b = [i[1] for i in score_list[n_number]]
    size = len(y2a)
    plt.bar([(i + 1.2) for i in range(size)], y2a, width=0.4, label='random player')
    plt.bar([(i + 0.8) for i in range(size)], y2b, width=0.4, label='computer player')

    plt.xticks([(i+1) for i in range(size)])
    ax.legend(loc="upper left", shadow=True, title="Player", fancybox=True)

    plt.xlabel('number of round played')
    plt.ylabel('score')
    plt.title('Scores of random and computer player for matrix {0}x{0}'.format(n_list[n_number]))

    plt.show()



all_files = read_many_file_names(11)
draw_both_algorithm_chart('', all_files)