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

COLORP1 = (30/255, 144/255, 255/255)
COLORP2 = (255/255, 75/255, 165/255)


def read_many_file_names(max_n):
    all_files = []
    for n_size in range(3, max_n+1):
        file_names = 'times_n' + (('0' + str(n_size)) if n_size < 10 else str(n_size)) + '_nr...txt'
        files = [f for f in os.listdir('.') if re.match(file_names, f)]
        files.insert(0, n_size)  # current n
        all_files.append(files)
    return all_files  # list of lists


def read_many_file_names_alpha_beta(max_n):
    all_files = []
    for n_size in range(3, max_n+1):
        file_names = 'times_ab_n' + (('0' + str(n_size)) if n_size < 10 else str(n_size)) + '_nr...txt'
        files = [f for f in os.listdir('.') if re.match(file_names, f)]
        files.insert(0, n_size)  # current n
        all_files.append(files)
    return all_files  # list of lists


def draw_both_algorithm_chart(files, files_ab):

    n_list, n_list_ab = [], []  # list containing n_sizes
    score_list, score_list_ab = [], []  # having [0]=n and later score of 1 player and score of second player
    time_list, time_list_ab = [], []  # having [0]=n and than in i=depth having (time, std, nr_of_operations)
    overall_time_list, overall_time_list_ab = [], []  # having [0]=n and later overall times

    for i in range(len(files)):
        many_files = files[i]
        n_size = many_files[0]
        many_files = many_files[1:]

        n_list.append(n_size)
        time_list.append([])

        if len(many_files) > 0:
            times, overall_times, score_list_i = [], [], []
            operations, depth = [], []

            for index, file_name in enumerate(many_files):
                with open(file_name) as file123:
                    f = [line.rstrip('\n') for line in file123]

                if index == 0:
                    operations = list(map(int, f[1:-3:3]))
                    depth = list(map(int, f[2:-3:3]))
                    times = [list(map(float, f[:-3:3]))]
                else:
                    times.append(list(map(float, f[:-3:3])))

                overall_times.append(float(f[-3]))
                score_list_i.append((int(f[-2]), int(f[-1])))

            times = [val for sublist in times for val in sublist]

            length = int(len(times) / len(many_files))
            for t1 in range(length):
                l = [x for x in times[t1::length]]
                time_list[i].append((np.average(l), np.std(l), operations[t1], depth[t1]))

            overall_time_list.append((np.average(overall_times), np.std(overall_times)))
            score_list.append(score_list_i)

    for i in range(len(files_ab)):
        many_files = files_ab[i]
        n_size_ab = many_files[0]
        many_files = many_files[1:]

        n_list_ab.append(n_size_ab)
        time_list_ab.append([])

        if len(many_files) > 0:
            times, overall_times, score_list_i = [], [], []
            operations, depth = [], []

            for index, file_name in enumerate(many_files):
                with open(file_name) as file123:
                    f = [line.rstrip('\n') for line in file123]

                if index == 0:
                    operations = list(map(int, f[1:-3:3]))
                    depth = list(map(int, f[2:-3:3]))
                    times = [list(map(float, f[:-3:3]))]
                else:
                    times.append(list(map(float, f[:-3:3])))

                overall_times.append(float(f[-3]))
                score_list_i.append((int(f[-2]), int(f[-1])))

            times = [val for sublist in times for val in sublist]

            length = int(len(times) / len(many_files))
            for t1 in range(length):
                l = [x for x in times[t1::length]]
                time_list_ab[i].append((np.average(l), np.std(l), operations[t1], depth[t1]))

            overall_time_list_ab.append((np.average(overall_times), np.std(overall_times)))
            score_list_ab.append(score_list_i)

    # print(overall_time_list_ab)
    # print(score_list_ab)
    # print(time_list)


    # DRAWING AVERAGE TIMES OF PLAYING
    fig, ax = plt.subplots()

    x = n_list
    y1, e1 = zip(*overall_time_list)
    y1, e1 = list(y1), list(e1)

    ax.errorbar(x, y1, e1, ecolor='r', linestyle=':', color=COLORP1, marker='.')

    plt.xlabel('size of matrix N')
    plt.ylabel('time [seconds]')
    plt.title('Average time of game play having matrix NxN')

    plt.show()
    plot_name = 'chaart_average_time_of_play.png'
    fig.savefig(plot_name)

    # LOGARITHMIC SCALE (OF X AXIS)
    fig, ax = plt.subplots()
    ax.set_yscale("log", nonposy='clip')
    ax.errorbar(x, y1, e1, ecolor='r', linestyle=':', color=COLORP1, marker='.')

    plt.xlabel('size of matrix N')
    plt.ylabel('time [seconds]')
    plt.title('Average time of game play having matrix NxN\nwith logarithmic scale of x axis')

    plt.show()
    plot_name = 'chaart_average_time_of_play_log.png'
    fig.savefig(plot_name)



    # DRAWING SCORE FOR A PLAY HAVING MATRIX NxN (N_NUMBER GIVEN)
    fig, ax = plt.subplots()
    n_number = 2

    y2a = [i[0] for i in score_list[n_number]]
    y2b = [i[1] for i in score_list[n_number]]
    size = len(y2a)
    plt.bar([(i + 0.8) for i in range(size)], y2a, width=0.4, color=COLORP1, label='random player')
    plt.bar([(i + 1.2) for i in range(size)], y2b, width=0.4, color=COLORP2, label='computer player')

    plt.xticks([(i+1) for i in range(size)])
    ax.legend(loc="upper left", shadow=True, title="Player", fancybox=True)

    plt.xlabel('number of round played')
    plt.ylabel('score')
    plt.title('Scores of random and computer player for matrix {0}x{0}'.format(n_list[n_number]))

    plt.show()
    plot_name = 'chaart_scores for matrix ' + str(n_list[n_number]) + 'x' + str(n_list[n_number]) + '.png'
    fig.savefig(plot_name)



    # DRAWING SCORES FOR ALL PLAYINGS
    fig, ax = plt.subplots()
    y3a, y3b = [], []

    for score_n in score_list:
        p1, p2 = 0, 0
        for tup in score_n:
            p1 += 1 if tup[0] > tup[1] else 0
            p2 += 1 if tup[1] > tup[0] else 0
        y3a.append(p1)
        y3b.append(p2)

    plt.bar([(i + 0.8 - 1) for i in n_list], y3a, width=0.4, color=COLORP1, label='random player')
    plt.bar([(i + 1.2 - 1) for i in n_list], y3b, width=0.4, color=COLORP2, label='computer player')

    plt.xticks(n_list)
    ax.legend(loc="upper left", shadow=True, title="Player", fancybox=True)

    plt.xlabel('matrix size n')
    plt.ylabel('number of winnings')
    plt.title('Number of winnings of random vs. computer player\nfor all matrix sizes')

    plt.show()
    plot_name = 'chaart_scores for all matrix.png'
    fig.savefig(plot_name)



    # DRAWING AVERAGE TIME OF OPERATIONS MAKING
    fig, ax = plt.subplots()
    n_number = 2

    overall_operation_times = sorted(time_list[n_number], key=lambda x: (x[2], x[3]))
    y4, e4, x4, depth = zip(*overall_operation_times)
    y4, e4, x4, depth = list(y4), list(e4), list(x4), list(depth)

    ax.errorbar(x4, y4, e4, ecolor='r', linestyle=':', color=COLORP1, marker='.')

    for label, x, y in zip(depth, x4, y4):
        plt.annotate(
            label,
            xy=(x, y), xytext=(-12, 15),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.4', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

    plt.xlabel('number of possible game states')
    plt.ylabel('time [seconds]')
    plt.title('Average time of game play having matrix {0}x{0}\ndepending on minimax depth'.format(n_list[n_number]))

    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()
    plt.xlim(x_min*2, x_max)
    plt.ylim(y_min, y_max*1.07)

    plt.show()
    plot_name = 'chaart_average_time_of_operations_for_matrix_' + str(n_list[n_number]) + 'x' + str(n_list[n_number]) + '.png'
    fig.savefig(plot_name)



    # DRAWING AVERAGE TIME OF MINIMAX COMPARING TO ALPHA-BETA
    fig, ax = plt.subplots()

    x5 = n_list
    y5, e5 = zip(*overall_time_list)
    y5, e5 = list(y5), list(e5)

    x6 = n_list_ab
    y6, e6 = zip(*overall_time_list_ab)
    y6, e6 = list(y6), list(e6)

    number_of_n = 6
    if number_of_n > 0:
        ax.errorbar(x5[:number_of_n], y5[:number_of_n], e5[:number_of_n], ecolor='b', linestyle=':', color=COLORP1, marker='.', label='minimax')
        ax.errorbar(x6[:number_of_n], y6[:number_of_n], e6[:number_of_n], ecolor='m', linestyle=':', color=COLORP2, marker='.', label='alpha-beta')
        plt.xticks(x5[:number_of_n])
    else:
        ax.errorbar(x5, y5, e5, ecolor='b', linestyle=':', color=COLORP1, marker='.', label='minimax')
        ax.errorbar(x6, y6, e6, ecolor='m', linestyle=':', color=COLORP2, marker='.', label='alpha-beta')

    ax.legend(loc="upper left", shadow=True, title="Algorithm type", fancybox=True)

    plt.xlabel('size of matrix N')
    plt.ylabel('time [seconds]')
    plt.title('Average time of game play having matrix NxN\ncomparing minimax to minimax with alpha-beta')

    plt.show()
    plot_name = 'chaart_average_time_of_play_with_alpha_beta_n' + str(number_of_n) + '.png'
    fig.savefig(plot_name)




all_files_minimax = read_many_file_names(11)
all_files_alpha_beta = read_many_file_names_alpha_beta(11)
draw_both_algorithm_chart(all_files_minimax, all_files_alpha_beta)