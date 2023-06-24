import networkx as nx
import tweepy
import matplotlib.pyplot as plt
import os


consumer_key = "2mwk5WNYkNcWko6MhmRrivazE"
consumer_secret = "P8NEpxECYgKa5YAWr5O3F6TGFWYeJY78EBd7ZhrEX2PcUkl643"
access_token = "2403140949-iKPTtRJJlsgRT6AV2tWeMBid4lFGV7DxNADI14K"
access_token_secret = "4OZlKin7OekWX7Lx00GDNhYuHTRj9BiNwPf8sPeCNXcuO"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)



def from_name_to_user(ID):
    return(api.get_user(ID)) # result = objecte USER
    
    
def proces(actual, explored, max_followers, max_nodes_to_crawl, cases):
    explored = first_level(actual, explored, max_followers, cases)
    explored_users = [from_name_to_user(x[0]) for x in explored]
    
    for x in explored_users[1:]:
        if len(explored) < max_nodes_to_crawl:
            explored = second_level(x, explored, max_followers)  
    return(explored)


def first_level(actual, queue, max_followers, cases):
    aux = list() #aux = llista amb tots els 20 seguidors de l'actual
    for follower in actual.followers():
        if follower.followers_count < max_followers:
            aux.append((follower.screen_name, follower.followers_count))

    cont = 0
    while cont < cases[0][1]:
        if len(aux) == 0:
            queue = atencio(actual, queue, max_followers, cases, cont)
            return(queue)
        else:
            maxim = max(aux, key = lambda x: x[1])
            queue.append((maxim[0], actual.screen_name))
            aux.remove(maxim)
            cont += 1
    return(queue)


def atencio(actual, queue, max_followers, cases, cont):
    aux = list() #aux = llista amb tots els 20 seguits de l'actual
    for friend in actual.friends():
        if friend.followers_count < max_followers:
            aux.append((friend.screen_name, friend.followers_count)) 
        
    while cont < cases[0][1]:
        maxim = max(aux, key = lambda x: x[1])
        queue.append((maxim[0], actual.screen_name))
        aux.remove(maxim)
        cont += 1
    return(queue)
        

def second_level(actual, explored, max_followers):
    aux = list() #aux = llista amb tots els 20 seguidors de l'actual
    for follower in actual.followers():
        if follower.followers_count < max_followers:
            aux.append((follower.screen_name, follower.followers_count))

    maxim = max(aux, key = lambda x: x[1])
    explored.append((maxim[0], actual.screen_name))
    aux.remove(maxim)
    return(explored)
   
    
def adaptations(max_nodes_to_crawl):
    cases = list()
    aux1 = max_nodes_to_crawl - 1 
    aux2 = aux1 / 2
    
    if aux1/2 == int(aux1/2): 
        print("CAS NORMAL")
        print("Cada node de la 1a capa té un fill")
        cases.append(("CASE1", int(aux2), int(aux2)))
        
    else:
        print("CAS ESPECIAL")
        print("Cada node de la 1a capa té un fill excepte l'últim node de la 1a capa que no en té cap")
        cases.append(("CASE2", int(aux2+1), int(aux2)))

    return(cases)
    

def save(seed_node, explored, max_nodes_to_crawl):
    print("...saving...")
    f = open(str(seed_node.screen_name)+"_"+str(max_nodes_to_crawl)+".txt","w")
    for x in explored:
        f.write(x[1] + " , " + x[0] + "\n")
    print("...saved...")
    return


def crawler(nom_node, max_nodes_to_crawl, max_followers): # (ID, 40, 10000)
    explored = list()
    explored.append((nom_node, nom_node))
    seed_node = from_name_to_user(nom_node)
    cases = adaptations(max_nodes_to_crawl)
    explored = proces(seed_node, explored, max_followers, max_nodes_to_crawl, cases)
    save(seed_node, explored, max_nodes_to_crawl)
    return


def export_edges_to_graph(file_name):
    '''
    :param file_name: name of the txt file that contains the edges of the graf.
    :return: the function does not return any parameter.
    '''
    path = os.path.dirname(file_name)
    aux_arests = list()
    nodes = list()
    arests = list()
    
    with open(os.path.join(path, './' + file_name), 'r', encoding='cp1252') as f1:
        for line in f1:
            aux_arests.append(line.split())

    for line in aux_arests:
        arests.append((line[0], line[2]))
        nodes.append(line[0])
        nodes.append(line[2])
        
    nodes = list(set(nodes))

    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(arests)

    nx.draw(G, with_labels = True)
    plt.show()
    nx.write_gpickle(G, file_name[:-4]+".pickle")


def export_graph_to_gexf(g, file_name):
    '''
    :param g: A graph with the corresponding networkx format.
    :param file_name: name of the file that will be saved.
    :return: the function does not return any parameter.
    '''
    nx.gexf.write_gexf(g, file_name+".gexf")
    return


def retrieve_bidirectional_edges(g, file_name):
    '''
    :param g: A graph with the corresponding networkx format.
    :param file_name: name of the file that will be saved.
    :return: the function does not return any parameter.
    '''
    G = nx.DiGraph.to_undirected(g, reciprocal = True)
    G.remove_nodes_from(list(nx.isolates(G)))
    nx.draw(G, with_labels = True)
    plt.show()
    nx.gexf.write_gexf(G, file_name+"_undirected.pickle")


def prune_low_degree_nodes(g, min_degree, file_name):
    '''
    :param g: A graph with the corresponding networkx format.
    :param min_degree: lower bound value for the degree
    :param file_name: name of the file that will be saved.
    :return: the function does not return any parameter.
    '''
    nodes = list(g.nodes)
    for node in nodes:
        if g.degree(node) <= min_degree:
            g.remove_node(node) 
            print("-----------expulsat",node, g.degree(node))
    nx.draw(g, with_labels = True)
    plt.show() 
    nx.gexf.write_gexf(g, file_name+"_undirected_reduced.pickle")
    
    
def find_cliques(g, min_size_clique):
    '''
    :param g: A graph with the corresponding networkx format.
    :param min_size_clique: the minimum size of the clique returned
    :return:
        large_cliques: a list with the large cliques
        nodes_in_large_cliques: all different nodes apprearing on these cliques
    '''
    large_cliques =[]
    nodes_in_large_cliques = []
    
    G = nx.DiGraph.to_undirected(g, reciprocal = True)
    aux = list(nx.enumerate_all_cliques(G))
    for clique in aux:
        if len(clique) >= min_size_clique:
            large_cliques.append(clique)
            
    for clique in large_cliques:
        for node in clique:
            if node not in nodes_in_large_cliques:
                nodes_in_large_cliques.append(node)
    return [large_cliques, nodes_in_large_cliques]


def find_max_k_core(g):
    '''
    :param g: A graph with the corresponding networkx format.
    :return: The k-core with a maximum k value.
    '''
    g.remove_edges_from(nx.selfloop_edges(g))
    k_Core_max = nx.k_core(g)
    nx.draw(k_Core_max, with_labels = True)
    plt.show() 
    return k_Core_max