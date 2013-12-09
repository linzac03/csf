import networkx as nx
import matplotlib

rj = nx.Graph()

rj.add_edges_from([("Friar Laurence", "Juliet"), ("Friar Laurence", "Romeo")])
rj.add_edges_from([("Juliet", "Capulet"), ("Juliet", "Romeo"), ("Juliet", "Tybalt"), ("Juliet", "Nurse")])
rj.add_edges_from([("Romeo", "Juliet"), ("Romeo", "Benvolio"), ("Romeo", "Montague"), ("Romeo", "Mercutio")])
rj.add_edges_from([("Benvolio", "Montague")])
rj.add_edges_from([("Capulet", "Tybalt"), ("Capulet", "Escalus"), ("Capulet", "Paris")])
rj.add_edges_from([("Escalus", "Montague"), ("Escalus", "Mercutio"), ("Escalus", "Paris")])
rj.add_edges_from([("Paris", "Mercutio"), ("Paris", "Capulet")])
#networkx.draw(rj)
#plt.savefig("romeonjuliet2.png")
def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    The parameter 'user' is the string name of a person in the graph.
    """
    return set(graph.neighbors(user))
    
def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given graph.
    The result does not include the given user nor any of that user's friends.
    """
    friends_of = friends(graph, user)
    f_of_f = []
    for elem in friends_of:
        if elem == user:
            pass
        else:
            f_of_f = f_of_f + list(friends(graph, elem))
    return f_of_f

p = ("yes", "no")

ls = [1,2,3,4,5,6]

