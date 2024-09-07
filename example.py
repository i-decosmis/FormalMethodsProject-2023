#(Da modificare solo il path dei log, il resto dovrebbe funzionare)

# GIOVANNI MAGRONE COMPUTER SCIENCE YEAR 2022/2023
import pm4py
import os
#Importing library for reachability graph
from pm4py.objects.petri_net.utils import reachability_graph
from pm4py.visualization.transition_system import visualizer as ts_visualizer
## Import the petrinet visualizer object
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
#  Import of Token-based replay
from pm4py.algo.conformance.tokenreplay import algorithm as token_based_replay

def Heuristic_mining(file_path):
    event_log = pm4py.read_xes(file_path)
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    #Here we print the number of the activities started and in witch node they finished.
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))
    # heuristics miner
    heu_net = heuristics_miner.apply_heu(event_log)
    # Visualise Process model
    gviz = hn_visualizer.apply(heu_net)
    hn_visualizer.view(gviz)
    # heuristics miner algorithm returning model, initial marking and
    # final marking
    net, im, fm = heuristics_miner.apply(event_log)
    # Petri net visualization
    gviz = pn_visualizer.apply(net, im, fm)
    pn_visualizer.view(gviz)
    #Here we analize the if the model obtained fit with the log
    print("do you want to check if the model fit with the log?")
    print("Print 1 to check, 0 to procede")
    i2=0
    i2=int(input())
    if i2==1:
        parameters_tbr = {token_based_replay.Variants.TOKEN_REPLAY.value.Parameters.DISABLE_VARIANTS: True,
                          token_based_replay.Variants.TOKEN_REPLAY.value.Parameters.ENABLE_PLTR_FITNESS: True}
        replayed_traces, place_fitness, trans_fitness, unwanted_activities = token_based_replay.apply(event_log, net,im,
                                                                                                      fm,
                                                                                                      parameters=parameters_tbr)
        print("Model fit")
        print(replayed_traces)
        print("Place fitness")
        print(place_fitness)
        print("Transactions fitness")
        print(trans_fitness)
        print("Unwanted activities")
        print(unwanted_activities)

def Inductive_mining(file_path):
    event_log = pm4py.read_xes(file_path)
    # Discovering the process tree using the inductive miner
    net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(event_log)
    tree = pm4py.discover_process_tree_inductive(event_log)
    # Petri net visualization
    gviz = pn_visualizer.apply(net, initial_marking, final_marking)
    pn_visualizer.view(gviz)
    # Discovery process tree
    pm4py.view_process_tree(tree)
    #Here we analize the if the model obtained fit with the log
    print("do you want to check if the model fit with the log?")
    print("Print 1 to check, 0 to procede")
    i2=0
    i2=int(input())
    if i2==1:
        parameters_tbr = {token_based_replay.Variants.TOKEN_REPLAY.value.Parameters.DISABLE_VARIANTS: True,
                          token_based_replay.Variants.TOKEN_REPLAY.value.Parameters.ENABLE_PLTR_FITNESS: True}
        replayed_traces, place_fitness, trans_fitness, unwanted_activities = token_based_replay.apply(event_log, net,initial_marking,
                                                                                                      final_marking,
                                                                                                      parameters=parameters_tbr)
        print("Model fit")
        print(replayed_traces)
        print("Place fitness")
        print(place_fitness)
        print("Transactions fitness")
        print(trans_fitness)
        print("Unwanted activities")
        print(unwanted_activities)

def Process_Map(file_path):
    event_log = pm4py.read_xes(file_path)
    #Obtaining the ProcessMap with DFG (Direct Following Graph)
    dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)
    pm4py.view_dfg(dfg, start_activities, end_activities)

def Input_Log():
    #SELECTING THE LOG WITH AN IF SELECTION ON ALL POSSIBILITIES
    print("Select path: 1 for detailed labour, 2 for detailed weeks, 3 for edited hh102 labour, 4 for edited hh102 weekends, 5 for edited hh104 labour, 6 for edited hh104 weekends, 7 for edited hh110 labour, 8 for edited hh110 weekends ")
    i3= int(input())
    Path=""
    if i3 == 1:
        Path= "C:/Users/176996/Desktop/progetto/activitylog_uci_detailed_labour.xes"
    elif i3 == 2:
        Path= "C:/Users/176996/Desktop/progetto/activitylog_uci_detailed_weekends.xes"
    elif i3 == 3:
        Path="C:/Users/176996/Desktop/progetto/edited_hh102_labour.xes"
    elif i3 == 4:
        Path="C:/Users/176996/Desktop/progetto/edited_hh102_weekends.xes"
    elif i3 == 5:
        Path="C:/Users/176996/Desktop/progetto/edited_hh104_labour.xes"
    elif i3 == 6:
        Path="C:/Users/176996/Desktop/progetto/edited_hh104_weekends.xes"
    elif i3 == 7:
        Path="C:/Users/176996/Desktop/progetto/edited_hh110_labour.xes"
    elif i3 == 8:
        Path = "C:/Users/176996/Desktop/progetto/edited_hh110_weekends.xes"
    else:
        Path=""

    return Path

#def Reachability_Graph(Path):


if __name__ == "__main__":
    os.environ["PATH"] += os.pathsep + 'C:/Programmi/Graphviz/bin/'
    i = 0
    Path = Input_Log()
    print("Type 1 for Heuristic miner, type 2 for Inductive miner, type 3 for Process Map , type 4 to change log,type 5 to close")
    print(Path)
    while i == 0:
        i=int(input())
        if i == 1:
            Heuristic_mining(Path)
            i = 0
        if i == 2:
            Inductive_mining(Path)
            i = 0
        if i == 3:
            Process_Map(Path)
            i = 0
        if i == 4:
            Path = Input_Log()
            i = 0
        if i == 5:
            break

   # THIS IS CODE TO GET A PROCESS MAP OF THE ACTIVITY FOLLOWING THE DFG ALGORITHM
   # dfg, start_activities, end_activities = pm4py.discover_dfg(log)
   # pm4py.view_dfg(dfg, start_activities, end_activities)