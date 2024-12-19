from django.shortcuts import render
from django.urls import path
from collections import defaultdict

def dijkstra(graph, start):
 
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = priority_queue.pop(0)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))

    return distances

def index(request):
    return render(request, 'index.html')

def calculate(request):
    if request.method == 'POST':
        graph_input = request.POST.get('graph')
        start_node = request.POST.get('start').lower()   

       
        graph = defaultdict(dict) #parsed the graph
        try:
            for edge in graph_input.split(';'):
                if edge.strip(): #no empty string
                    node1, node2, weight = edge.split()
                    weight = int(weight)
                    node1 = node1.lower()   
                    node2 = node2.lower()   
                    graph[node1][node2] = weight
                    graph[node2][node1] = weight  

            
            result = dijkstra(graph, start_node)
            return render(request, 'result.html', {'result': result})
        except Exception as e:
            return render(request, 'error.html', {'error_message': str(e)})

