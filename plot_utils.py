import matplotlib.pyplot as plt 
from matplotlib.patches import Ellipse
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import seaborn as sns
from collections import Counter
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

data_folder = 'data/'
tags_names_df = pd.read_csv(data_folder + 'tags2name.csv')

def pitch():
    """
    code to plot a soccer pitch 
    """
    #create figure
    fig,ax=plt.subplots(figsize=(7,5))
    
    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,100], color="black")
    plt.plot([0,100],[100,100], color="black")
    plt.plot([100,100],[100,0], color="black")
    plt.plot([100,0],[0,0], color="black")
    plt.plot([50,50],[0,100], color="black")

    #Left Penalty Area
    plt.plot([16.5,16.5],[80,20],color="black")
    plt.plot([0,16.5],[80,80],color="black")
    plt.plot([16.5,0],[20,20],color="black")

    #Right Penalty Area
    plt.plot([83.5,100],[80,80],color="black")
    plt.plot([83.5,83.5],[80,20],color="black")
    plt.plot([83.5,100],[20,20],color="black")

    #Left 6-yard Box
    plt.plot([0,5.5],[65,65],color="black")
    plt.plot([5.5,5.5],[65,35],color="black")
    plt.plot([5.5,0.5],[35,35],color="black")

    #Right 6-yard Box
    plt.plot([100,94.5],[65,65],color="black")
    plt.plot([94.5,94.5],[65,35],color="black")
    plt.plot([94.5,100],[35,35],color="black")

    #Prepare Circles
    centreCircle = Ellipse((50, 50), width=30, height=39, edgecolor="black", facecolor="None", lw=1.8)
    centreSpot = Ellipse((50, 50), width=1, height=1.5, edgecolor="black", facecolor="black", lw=1.8)
    leftPenSpot = Ellipse((11, 50), width=1, height=1.5, edgecolor="black", facecolor="black", lw=1.8)
    rightPenSpot = Ellipse((89, 50), width=1, height=1.5, edgecolor="black", facecolor="black", lw=1.8)

    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)
    
    #limit axis
    plt.xlim(0,100)
    plt.ylim(0,100)
    
    ax.annotate("", xy=(25, 5), xytext=(5, 5),
                arrowprops=dict(arrowstyle="->", linewidth=2))
    ax.text(7,7,'Attack',fontsize=20)
    return fig,ax

def draw_pitch(pitch, line, orientation, view, alpha=1):
    """
    Draw a soccer pitch given the pitch, the orientation, the view and the line
    
    Parameters
    ----------
    pitch
    
    """
    orientation = orientation
    view = view
    line = line
    pitch = pitch
    
    if orientation.lower().startswith("h"):
        
        if view.lower().startswith("h"):
            fig,ax = plt.subplots(figsize=(6.8,10.4))
            plt.xlim(49,105)
            plt.ylim(-1,69)
        else:
            fig,ax = plt.subplots(figsize=(10.4,6.8))
            plt.xlim(-1,105)
            plt.ylim(-1,69)
        ax.axis('off') # this hides the x and y ticks
    
        # side and goal lines #
        ly1 = [0,0,68,68,0]
        lx1 = [0,104,104,0,0]

        plt.plot(lx1,ly1,color=line,zorder=5)


        # boxes, 6 yard box and goals

            #outer boxes#
        ly2 = [13.84,13.84,54.16,54.16] 
        lx2 = [104,87.5,87.5,104]
        plt.plot(lx2,ly2,color=line,zorder=5)

        ly3 = [13.84,13.84,54.16,54.16] 
        lx3 = [0,16.5,16.5,0]
        plt.plot(lx3,ly3,color=line,zorder=5)

            #goals#
        ly4 = [30.34,30.34,37.66,37.66]
        lx4 = [104,104.2,104.2,104]
        plt.plot(lx4,ly4,color=line,zorder=5)

        ly5 = [30.34,30.34,37.66,37.66]
        lx5 = [0,-0.2,-0.2,0]
        plt.plot(lx5,ly5,color=line,zorder=5)


           #6 yard boxes#
        ly6 = [24.84,24.84,43.16,43.16]
        lx6 = [104,99.5,99.5,104]
        plt.plot(lx6,ly6,color=line,zorder=5)

        ly7 = [24.84,24.84,43.16,43.16]
        lx7 = [0,4.5,4.5,0]
        plt.plot(lx7,ly7,color=line,zorder=5)

        #Halfway line, penalty spots, and kickoff spot
        ly8 = [0,68] 
        lx8 = [52,52]
        plt.plot(lx8,ly8,color=line,zorder=5)


        plt.scatter(93,34,color=line,zorder=5)
        plt.scatter(11,34,color=line,zorder=5)
        plt.scatter(52,34,color=line,zorder=5)

        circle1 = plt.Circle((93.5,34), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle2 = plt.Circle((10.5,34), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle3 = plt.Circle((52, 34), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=2,alpha=1)

        ## Rectangles in boxes
        rec1 = plt.Rectangle((87.5,20), 16,30,ls='-',color=pitch, zorder=1,alpha=alpha)
        rec2 = plt.Rectangle((0, 20), 16.5,30,ls='-',color=pitch, zorder=1,alpha=alpha)

        ## Pitch rectangle
        rec3 = plt.Rectangle((-1, -1), 106,70,ls='-',color=pitch, zorder=1,alpha=alpha)

        ax.add_artist(rec3)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(rec1)
        ax.add_artist(rec2)
        ax.add_artist(circle3)
        
    else:
        if view.lower().startswith("h"):
            fig,ax = plt.subplots(figsize=(10.4,6.8))
            plt.ylim(49,105)
            plt.xlim(-1,69)
        else:
            fig,ax = plt.subplots(figsize=(6.8,10.4))
            plt.ylim(-1,105)
            plt.xlim(-1,69)
        ax.axis('off') # this hides the x and y ticks

        # side and goal lines #
        lx1 = [0,0,68,68,0]
        ly1 = [0,104,104,0,0]

        plt.plot(lx1,ly1,color=line,zorder=5)


        # boxes, 6 yard box and goals

            #outer boxes#
        lx2 = [13.84,13.84,54.16,54.16] 
        ly2 = [104,87.5,87.5,104]
        plt.plot(lx2,ly2,color=line,zorder=5)

        lx3 = [13.84,13.84,54.16,54.16] 
        ly3 = [0,16.5,16.5,0]
        plt.plot(lx3,ly3,color=line,zorder=5)

            #goals#
        lx4 = [30.34,30.34,37.66,37.66]
        ly4 = [104,104.2,104.2,104]
        plt.plot(lx4,ly4,color=line,zorder=5)

        lx5 = [30.34,30.34,37.66,37.66]
        ly5 = [0,-0.2,-0.2,0]
        plt.plot(lx5,ly5,color=line,zorder=5)


           #6 yard boxes#
        lx6 = [24.84,24.84,43.16,43.16]
        ly6 = [104,99.5,99.5,104]
        plt.plot(lx6,ly6,color=line,zorder=5)

        lx7 = [24.84,24.84,43.16,43.16]
        ly7 = [0,4.5,4.5,0]
        plt.plot(lx7,ly7,color=line,zorder=5)

        #Halfway line, penalty spots, and kickoff spot
        lx8 = [0,68] 
        ly8 = [52,52]
        plt.plot(lx8,ly8,color=line,zorder=5)


        plt.scatter(34,93,color=line,zorder=5)
        plt.scatter(34,11,color=line,zorder=5)
        plt.scatter(34,52,color=line,zorder=5)

        circle1 = plt.Circle((34,93.5), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle2 = plt.Circle((34,10.5), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle3 = plt.Circle((34,52), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=2,alpha=1)


        ## Rectangles in boxes
        rec1 = plt.Rectangle((20, 87.5), 30,16.5,ls='-',color=pitch, zorder=1,alpha=alpha)
        rec2 = plt.Rectangle((20, 0), 30,16.5,ls='-',color=pitch, zorder=1,alpha=alpha)

        ## Pitch rectangle
        rec3 = plt.Rectangle((-1, -1), 70,106,ls='-',color=pitch, zorder=1,alpha=alpha)

        ax.add_artist(rec3)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(rec1)
        ax.add_artist(rec2)
        ax.add_artist(circle3)


def get_pitch_layout(title):
    lines_color = 'black'
    bg_color = 'rgb(255, 255, 255)'
    pitch_layout = dict(hovermode='closest', autosize=False,
                                        width=825,
                                        height=600,
                                        plot_bgcolor=bg_color,#'rgb(59,205,55)',
                                        xaxis={
                                            'range': [0, 100],
                                            'showgrid': False,
                                            'showticklabels': False,
                                        },
                                        yaxis={
                                            'range': [0, 100],
                                            'showgrid': False,
                                            'showticklabels': False,
                                        },
                                        title=title,
                                        shapes=[
                                            {
                                                'type': 'circle',
                                                'xref': 'x',
                                                'yref': 'y',
                                                'y0': 35,
                                                'x0': 40,
                                                'y1': 65,
                                                'x1': 60,
                                                'line': {
                                                    'color': lines_color,
                                                },

                                            },
                                         {
                                                'type': 'line',
                                                'xref': 'x',
                                                'yref': 'y',
                                                'y0': 35,
                                                'x0': 0,
                                                'y1': 35,
                                                'x1': 10,                                         
                                                'line': {
                                                    'color': lines_color,
                                                },

                                            },
                                         {
                                                'type': 'line',
                                                'xref': 'x',
                                                'yref': 'y',
                                                'y0': 35,
                                                'x0': 10,
                                                'y1': 65,
                                                'x1': 10,
                                                'line': {
                                                    'color': lines_color,
                                                }
                                         },
                                        {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 65,
                                            'x0': 10,
                                            'y1': 65,
                                            'x1': 0,
                                            'line': {
                                                'color': lines_color,
                                            }
                                          },
                                        {
                                                'type': 'line',
                                                'xref': 'x',
                                                'yref': 'y',
                                                'y0': 35,
                                                'x0': 100,
                                                'y1': 35,
                                                'x1': 90,                                         
                                                'line': {
                                                    'color': lines_color,
                                                },

                                            },
                                         {
                                                'type': 'line',
                                                'xref': 'x',
                                                'yref': 'y',
                                                'y0': 35,
                                                'x0': 90,
                                                'y1': 65,
                                                'x1': 90,
                                                'line': {
                                                    'color': lines_color,
                                                }
                                         },
                                        {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 65,
                                            'x0': 90,
                                            'y1': 65,
                                            'x1': 100,
                                            'line': {
                                                'color': lines_color,
                                            }
                                          },    
                                        {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 100,
                                            'x0': 50,
                                            'y1': 0,
                                            'x1': 50,
                                            'line': {
                                                'color': lines_color,
                                            }
                                          },
                                        {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 0,
                                            'x0': 0,
                                            'y1': 100,
                                            'x1': 0,
                                            'line': {
                                                'color': lines_color,
                                            }
                                          },
                                        {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 0,
                                            'x0': 100,
                                            'y1': 100,
                                            'x1': 100,
                                            'line': {
                                                'color': lines_color,
                                            }
                                          },
                                        {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 100,
                                            'x0': 0,
                                            'y1': 100,
                                            'x1': 100,
                                            'line': {
                                                'color': lines_color,
                                            }
                                          },
                                        {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 0,
                                            'x0': 0,
                                            'y1': 0,
                                            'x1': 100,
                                            'line': {
                                                'color': lines_color,
                                            }
                                          },
                                        ]
    )
    return pitch_layout  

def in_match_evolution(tournaments, events, event_name='Goal', event_tag=101):
    """
    """
    events_time = []
    for tournament in tournaments:
        for event in events[tournament]:
            tags = event['tags']
            for tag in tags:
                if tag['id'] == event_tag:
                    events_time.append([event['matchId'], event['matchPeriod'], 
                                    event['eventSec']])
                
    # let us convert it into a DataFrame
    event_df = pd.DataFrame(events_time, columns=['matchId','matchPeriod','eventSec'])
    
    fig, ax = plt.subplots(figsize=(8,6))
    start_bin_label = 1
    max_bin_count = 0
    
    for half, color_bar, color_last_bar in zip(['1H','2H'], 
                                               ['blue','green'], 
                                               ['skyblue','lightgreen']):
        
        df_half = event_df[event_df['matchPeriod'] == half].sort_values(['matchPeriod','eventSec'])
        bins = range(0, int(df_half['eventSec'].max())+1)[::300]
        labels = range(start_bin_label,start_bin_label+len(bins)-1)
        df_half['binned'] = pd.cut(df_half['eventSec'], bins=bins, labels=labels)
        df_half = df_half.sort_values('binned')
        barlist = plt.bar(Counter(df_half.binned.dropna()).keys(),Counter(df_half.binned.dropna()).values(),label=half,color=color_bar)
        if len(bins) == 11:
            barlist = barlist[len(bins)-2].set_color(color_last_bar)
        max_bin_half = np.max(list(Counter(df_half.binned.dropna()).values()))
        if max_bin_half > max_bin_count:
            max_bin_count = max_bin_half
        start_bin_label = 12
    
    plt.legend(loc=2, fontsize=15, frameon=True, shadow=True)
    plt.xticks(list(range(1,23)),['0-5','5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','>45','',
                                  '45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85','85-90','>90'],
              rotation=90, fontsize=18)
    plt.yticks(fontsize=18)
    plt.ylim(0,max_bin_count+(max_bin_count/100*10))
    plt.xlim(0, 22)
    plt.text(10.65, max_bin_count-(max_bin_count/100*10), 'half time', rotation=90, 
             bbox=dict(facecolor='w',edgecolor='r'),
             verticalalignment='center', horizontalalignment='left', fontsize=15, 
             color='tomato')
    plt.vlines(11, 0, max_bin_count+(max_bin_count/100*10),colors='r',alpha=0.5)
    plt.xlabel('match time (min)', fontsize=25)
    plt.ylabel('%s (n)'%event_name, fontsize=25)
    plt.grid(alpha=0.3)
    fig.tight_layout()
    plt.show()

    
def plot_invasion_and_acceleration_index(match_label, list_invasion, list_acceleration):
    sns.set_style('ticks')
    fig, ax = plt.subplots(2,1, figsize=(10,10), sharex=True)

    print ('INVASION INDEX')
    for i, c, label in zip(list(list_invasion), 
                           ['darkred','k'], ['AS Roma','ACF Fiorentina']):
        df_invasion = pd.DataFrame(list_invasion[i], columns=['time','invasion'])
        df_invasion['time'] = [x/60. for x in df_invasion.time]
        print(label, round(df_invasion['invasion'].mean(), 2), 
              round(df_invasion['invasion'].std(), 2))
        ax[0].plot(df_invasion.set_index('time').rolling(220, min_periods=1).mean(),c=c,alpha=0.7,lw=4,label=label)

    ax[0].legend(loc=1,fontsize=18,frameon=True,shadow=True)
    ax[0].grid(alpha=0.1)
    ax[0].set_ylabel('invasion index',fontsize=25)
    ax[0].yaxis.set_tick_params(labelsize=18)
    ax[0].text(45.8,0.45,'half time',rotation=90,bbox=dict(facecolor='w',edgecolor='r',lw=2),
             verticalalignment='center',horizontalalignment='left',fontsize=15,color='r')
    ax[0].vlines(47,-1,2,colors='r',lw=2)
    ax[0].text(6,0.45,'goal',rotation=90,bbox=dict(facecolor='w',edgecolor='rebeccapurple',lw=2),
             verticalalignment='center',horizontalalignment='left',fontsize=15,color='rebeccapurple')
    ax[0].vlines(7,-1,2,colors='rebeccapurple',lw=2)
    ax[0].text(38,0.45,'goal',rotation=90,bbox=dict(facecolor='w',edgecolor='rebeccapurple',lw=2),
             verticalalignment='center',horizontalalignment='left',fontsize=15,color='rebeccapurple')
    ax[0].vlines(39,-1,2,colors='rebeccapurple',lw=2)
    ax[0].text(85,0.08,'(a)',fontsize=25)
    ax[0].set_ylim(0,0.55)
    ax[0].set_title(match_label,fontsize=35)

    print ('\nACCELERATION INDEX')
    for i,c,label in zip(list(list_acceleration), 
                         ['darkred','k'], 
                         ['AS Roma','ACF Fiorentina']):
        df_acceleration = pd.DataFrame(list_acceleration[i],columns=['time','acceleration'])
        df_acceleration['time'] = [x/60. for x in df_acceleration.time]
        print (label, round(df_acceleration['acceleration'].mean(), 2), 
               round(df_acceleration['acceleration'].std(), 2))
        ax[1].plot(df_acceleration.set_index('time').rolling(220, min_periods=1).mean(),c=c,alpha=0.7,lw=4,label=label)
    ax[1].legend(fontsize=18,frameon=True,shadow=True,loc=1)
    ax[1].grid(alpha=0.1)
    ax[1].set_ylabel('acceleration index', fontsize=25)
    ax[1].xaxis.set_tick_params(labelsize=18)
    ax[1].yaxis.set_tick_params(labelsize=18)
    ax[1].text(85, 0.02,'(b)', fontsize=25)
    ax[1].vlines(47, -1, 2, colors='r', lw=2)
    plt.xlabel('time (min)', fontsize=25)
    
    ax[1].yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.xlim(0,95)
    ax[1].vlines(7,-1,2,colors='rebeccapurple',lw=2)
    ax[1].vlines(39,-1,2,colors='rebeccapurple',lw=2)
    plt.ylim(0,0.15)
    fig.tight_layout()

    plt.show()